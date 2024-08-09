import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from transformers import pipeline
from docx import Document
import fitz  # PyMuPDF
import io
from typing import Optional
import asyncio

# Disable oneDNN optimizations for consistent results
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load summarizer once at startup
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def extract_text_from_docx(file_content: bytes) -> str:
    doc = Document(io.BytesIO(file_content))
    return "\n".join(paragraph.text for paragraph in doc.paragraphs)

def extract_text_from_pdf(file_content: bytes) -> str:
    text = ""
    pdf_document = fitz.open(stream=file_content, filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

async def summarize_text(text: str) -> str:
    # Chunking for large text
    chunk_size = 1024 * 1024  # 1MB
    summaries = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        summary = summarizer(chunk)
        summaries.append(summary[0]['summary_text'])
    return " ".join(summaries)

@app.post("/summarize/")
async def summarize_document(file: UploadFile = File(...), chunk_size: Optional[int] = 1024 * 1024):
    try:
        file_content = await file.read()
        file_extension = file.filename.split('.')[-1].lower()

        if file_extension == 'txt':
            text = file_content.decode('utf-8')
        elif file_extension == 'docx':
            text = extract_text_from_docx(file_content)
        elif file_extension == 'pdf':
            text = extract_text_from_pdf(file_content)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type. Please upload a .txt, .docx, or .pdf file.")

        if not text.strip():
            raise HTTPException(status_code=400, detail="The file is empty or does not contain readable text.")

        summary = await summarize_text(text)
        return {"content": text, "summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")




# Submission Requirements
# 1.A GitHub Monorepo repository containing:
# The backend code.
# The frontend code.
# Instructions for setting up and running the application locally.
# A suitable Docker Compose file for local deployment will be a plus.
# 2.A brief document explaining the approach, challenges faced, and how they were overcome, part of the above repo, in markdown.
# 3.A Bibliography of all relevant sources ( FOSS ) forked / referred to.



