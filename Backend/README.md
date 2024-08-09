# Backend Setup

## Requirements
- Python 3.8+
- Pip

## Setup
1. Navigate to the `backend` directory:
   cd Backend

#Create a virtual environment:
python -m venv venv
#Activate the virtual environment:
venv\Scripts\activate


Install dependencies , required packages using pip:

#FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
#pip install fastapi

#uvicorn: An ASGI server implementation to serve your FastAPI application.
Installation:pip install uvicorn

#transformers: A library from Hugging Face providing state-of-the-art Natural Language Processing models.
Installation:pip install transformers

#python-docx: A library for creating and updating Microsoft Word (.docx) files.
Installation:pip install python-docx

#PyMuPDF (fitz): A library for working with PDF files, used for extracting text from PDFs.
Installation: pip install pymupdf

#aiofiles: An asynchronous file handling library used for efficient file operations in asynchronous contexts.
Installation:pip install aiofiles

pip install -r requirements.txt
fastapi
uvicorn
transformers
python-docx
pymupdf
aiofiles

Run the FastAPI server:
uvicorn main:app --reload