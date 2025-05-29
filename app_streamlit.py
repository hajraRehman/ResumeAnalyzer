import streamlit as st
import fitz
import re
import nltk
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer, util

# Read OpenAI API key securely
def read_api_key(file_path="openai_APIkey.txt"):
    try:
        with open(file_path, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

api_key = read_api_key()
if api_key is None:
    st.error("OpenAI API key file not found. Please create 'openai_key.txt' with your key.")
else:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

st.set_page_config(page_title="Resume Analyzer with GPT Feedback", page_icon="📄", layout="centered")

def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = re.sub(r'\W+', ' ', text)
    tokens = text.lower().split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

SKILLS = {
    "python", "javascript", "machine learning", "deep learning", "pytorch", "sql",
    "tensorflow", "data science", "nlp", "computer vision", "docker", "aws",
    "react", "nodejs", "c++", "c#", "html", "css"
}

def extract_skills(text):
    found = set()
    for skill in SKILLS:
        if skill in text:
            found.add(skill)
    return found

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

model = load_model()

def generate_feedback(resume, job_desc):
    prompt = f"""
You are a helpful assistant that compares a candidate's resume with a job description.
Provide specific suggestions to improve the resume to better match the job description.

Resume:
{resume}

Job Description:
{job_desc}

Suggestions:
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user", "content": prompt}],
            max_tokens=300,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating feedback: {e}"

st.title("📄 Resume Analyzer with GPT Feedback")
st.markdown("## Upload your resume and paste the job description")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description here")

if uploaded_file and job_description and api_key is not None:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        clean_resume = clean_text(resume_text)
        clean_job_desc = clean_text(job_description)

        embeddings = model.encode([clean_resume, clean_job_desc])
        similarity_score = util.cos_sim(embeddings[0], embeddings[1]).item()
        match_percent = round(similarity_score * 100, 2)

        resume_skills = extract_skills(clean_resume)
        job_skills = extract_skills(clean_job_desc)
        matched_skills = resume_skills.intersection(job_skills)

        st.markdown("---")
        st.subheader(f"Match Score: {match_percent}%")

        st.subheader("✅ Matched Skills")
        if matched_skills:
            for skill in sorted(matched_skills):
                st.write(f"- {skill}")
        else:
            st.write("No matched skills found.")

        st.subheader("📝 GPT-based Suggestions to Improve Resume")
        feedback = generate_feedback(resume_text, job_description)
        st.write(feedback)

# Footer
st.markdown("---")
st.markdown("<small>Developed by Hafiza Hajrah Rehman | Resume Analyzer Project</small>", unsafe_allow_html=True)
