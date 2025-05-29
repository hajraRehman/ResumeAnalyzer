# Resume Analyzer with NLP & GPT Feedback

A Python Streamlit web app that helps job seekers optimize their resumes by comparing them against job descriptions using Natural Language Processing (NLP) and OpenAI GPT-powered feedback.

---

## Features

- Upload PDF resumes and extract text content  
- Calculate similarity score between resume and job description using Sentence-BERT embeddings  
- Identify matched skills from a predefined skill set  
- Generate personalized improvement suggestions with OpenAI GPT-3.5 Turbo  
- User-friendly web interface built with Streamlit

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- OpenAI API key ([Get yours here](https://platform.openai.com/account/api-keys))

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/resume-analyzer.git
   cd resume-analyzer

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key:

   * Create a file named `openai_key.txt` in the project root
   * Paste your OpenAI API key into this file (no extra spaces or quotes)
   * **Make sure `openai_key.txt` is added to `.gitignore` to keep it private**

### Usage

Run the Streamlit app:

```bash
python -m streamlit run app_streamlit.py
```

* Upload your resume PDF
* Paste the job description text
* View the similarity match score, matched skills, and AI-generated feedback on how to improve your resume

---

## Technologies Used

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) for PDF text extraction
* [NLTK](https://www.nltk.org/) for text preprocessing
* [Sentence-Transformers](https://www.sbert.net/) for embeddings and similarity scoring
* [OpenAI GPT-3.5 Turbo](https://platform.openai.com/docs/models/gpt-3-5) for natural language feedback

---

## Project Structure

```
resume-analyzer/
│
├── app_streamlit.py      # Main Streamlit app script
├── requirements.txt      # Python dependencies
├── .gitignore            # Files/folders to ignore in git
├── openai_key.txt        # Your OpenAI API key (ignored by git)
└── README.md             # This documentation file
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

* Inspired by real-world recruitment needs and powered by cutting-edge NLP and AI models
* Thanks to [OpenAI](https://openai.com/) and [Streamlit](https://streamlit.io/) for their awesome tools!

---

If you have any questions or want help setting this up, feel free to contact me!

---

*Developed by Hafiza Hajrah Rehman*

```

---
