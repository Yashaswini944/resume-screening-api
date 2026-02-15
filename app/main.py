from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from .utils import load_vectorizer, load_resumes, compute_similarity, extract_text_from_pdf

app = FastAPI(title="Resume Screening API")

vectorizer = load_vectorizer()
resumes = load_resumes()

class JobDescription(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Resume Screening API is running"}

# -------------------------------
# 1. UPLOAD RESUME ENDPOINT
# -------------------------------
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    try:
        extracted_text = extract_text_from_pdf(file.file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting PDF text: {str(e)}")

    return {"extracted_text": extracted_text}

# -------------------------------
# 2. PREDICT ENDPOINT
# -------------------------------
@app.post("/predict")
def predict(data: JobDescription):
    job_desc = data.text
    similarities = compute_similarity(job_desc, resumes, vectorizer)

    ranked = sorted(
        list(enumerate(similarities)),
        key=lambda x: x[1],
        reverse=True
    )

    results = [
        {
            "resume_id": idx + 1,
            "similarity_score": round(score, 2),
            "resume_text": resumes[idx]
        }
        for idx, score in ranked
    ]

    return {"ranked_resumes": results}
