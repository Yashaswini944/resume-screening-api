import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

job_description = """
Looking for a Python developer with experience in machine learning, data analysis, and web development.
Familiarity with Django, pandas, and scikit-learn is preferred. Strong problem-solving and communication skills are essential.
"""

resumes = [
    "Experienced Python developer with strong background in Django and web APIs. Built scalable applications.",
    "Data scientist skilled in Python, pandas, and machine learning. Worked on several classification problems.",
    "Frontend developer with React and JavaScript expertise. Limited experience with backend systems.",
    "Software engineer familiar with Java and Spring Boot. Looking to switch to data science roles.",
    "Machine learning enthusiast with academic projects in scikit-learn and deep learning using PyTorch."
]

documents = [job_description] + resumes

vectorizer = TfidfVectorizer(stop_words='english')
vectorizer.fit(documents)

with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("model/resumes.pkl", "wb") as f:
    pickle.dump(resumes, f)
