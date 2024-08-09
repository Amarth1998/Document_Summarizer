# Dockerfile for FastAPI Backend
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .
# Install PyMuPDF
RUN pip install pymupdf
# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI application with uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
