import pickle
from sklearn.metrics.pairwise import cosine_similarity

def load_vectorizer():
    with open("model/vectorizer.pkl", "rb") as f:
        return pickle.load(f)

def load_resumes():
    with open("model/resumes.pkl", "rb") as f:
        return pickle.load(f)

def compute_similarity(job_description, resumes, vectorizer):
    job_vec = vectorizer.transform([job_description])
    resume_vecs = vectorizer.transform(resumes)
    similarities = cosine_similarity(job_vec, resume_vecs)[0]
    return similarities

import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

