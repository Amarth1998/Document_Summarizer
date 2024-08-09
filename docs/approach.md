# Project Approach and Challenges

## Approach
- **Backend:** Used FastAPI for building the backend service. Implemented endpoints for file uploads and summarization using the transformers library with the BART model.
- **Frontend:** Developed a React application for file upload and display of results. Handled different file types and provided user feedback.

## Challenges and Solutions
1. **Handling Large Documents:**
   - **Challenge:** Summarizing large documents can be resource-intensive.
   - **Solution:** Implemented text chunking to process large texts in smaller pieces.

2. **Model Loading and Efficiency:**
   - **Challenge:** Loading the model for each request can be slow.
   - **Solution:** Loaded the model once at startup to improve response times.

3. **File Type Handling:**
   - **Challenge:** Different file types require different extraction methods.
   - **Solution:** Implemented specific functions for TXT, DOCX, and PDF file types.

## Future Improvements
- **Performance Optimization:** Further optimize summarization for even larger documents.
- **User Interface:** Enhance the frontend to better handle file uploads and user interactions.
