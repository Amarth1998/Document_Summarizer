import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [file, setFile] = useState(null);
    const [summary, setSummary] = useState("");
    const [uploadedContent, setUploadedContent] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);

    // Handle file selection
    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        if (selectedFile) {
            setFile(selectedFile);
            setError(""); // Clear any previous errors

            const reader = new FileReader();
            if (selectedFile.type.startsWith('text/')) {
                reader.onload = (event) => {
                    setUploadedContent(event.target.result);
                };
                reader.readAsText(selectedFile);
            } else if (selectedFile.type === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' || selectedFile.type === 'application/pdf') {
                setUploadedContent(`${selectedFile.name} will be processed.`);
            } else {
                setError("Please upload a valid text, DOCX, or PDF file.");
                setFile(null); // Clear the file state
            }
        }
    };

    // Handle form submission
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) {
            setError("Please select a file to upload.");
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            setLoading(true);
            const response = await axios.post("http://localhost:8000/summarize/", formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setUploadedContent(response.data.content);  // Display extracted content
            setSummary(response.data.summary);          // Display summary
            setError(""); // Clear any previous errors
        } catch (error) {
            setError("There was an error: " + error.response?.data?.detail || error.message);
            setSummary(""); // Clear the summary in case of error
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            
         <div><h1>Document Summarizer</h1>
         <h1>Upload a file and get a summary</h1> </div>
        

            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit" disabled={loading}>Summarize</button>
            </form>


            {loading && <p>Processing...</p>}
            {uploadedContent && (
                <div>
                    <h2>Uploaded Content:</h2>
                    <pre>{uploadedContent}</pre>
                </div>
            )}
            {summary && (
                <div>
                    <h2>Summary:</h2>
                    <p>{summary}</p>
                </div>
            )}
            {error && (
                <div style={{ color: 'red' }}>
                    <h2>Error:</h2>
                    <p>{error}</p>
                </div>
            )}
        </div>
    );
}

export default App;


