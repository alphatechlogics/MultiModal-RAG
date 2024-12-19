# 🌐 Multi-RAG Portal

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.24.1-blue)](https://streamlit.io/)

## 📜 Overview

**Multi-RAG Portal** is a web-based tool designed to help you interact more intuitively with PDF resources. By harnessing **Retrieval-Augmented Generation (RAG)**, this system enables you to effortlessly upload PDF documents and pose natural language queries. It seamlessly integrates a FastAPI-powered backend with a user-friendly frontend built using Streamlit. The result is a fluid user experience where you can find information based on the contents of your uploaded files, all through simple, conversational queries.

### ✨ Key Advantages

- **Document Submission**: Easily send in your PDF documents for indexing.
- **Intelligent Q&A**: Ask questions about your PDFs and receive context-rich, human-like answers.
- **User-Friendly UI**: Enjoy a clean, intuitive interface that simplifies interaction.
- **Interactive Frontend**: Benefit from an interactive Streamlit-based frontend for enhanced user experience.

## ⚙️ Requirements

Before starting, ensure you have the following set up:

- **Python 3.10.12++**
- **pip** (Python’s package manager)
- **Node.js** and **npm** (if you need to adjust frontend components)
- **Streamlit**: For the frontend interface

### 📚 PDF Tooling

For processing PDF files, you’ll need **poppler-utils**:

- **Ubuntu/Debian**: `sudo apt-get install poppler-utils`
- **macOS**: `brew install poppler`
- **Windows**: Obtain Poppler from its official source and include its `bin` directory in your `PATH`.

## 🚀 Setup and Installation

### 1. **Clone the Repository**

```bash
git clone https://github.com/RohmaButt/MultiModal-RAG.git
cd multi-rag-portal
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install the Required Python Packages

```bash
pip install -r requirements.txt
```

### 4. Install Additional Dependencies (if needed)

- For PDF processing:

```bash
pip install pdf2image pillow
```

- On Ubuntu/Debian:

```bash
sudo apt-get install poppler-utils
```

- On macOS:

```bash
brew install poppler
```

- On Windows:

Download and install Poppler manually.
Add its bin directory to your PATH.

### 5. Set Up Environment Variables

The application requires an OpenAI API key for generating embeddings and processing queries. You can set this up using a .env file.

- a. Install python-dotenv

```bash
pip install python-dotenv
```

-b. Create a .env File

In the root directory of your project, create a file named .env and add your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key-here"
```

## Usage 🚀

#### Starting the FastAPI Backend

Activate Your Virtual Environment (if not already activated):

```bash
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

#### Start the FastAPI Server:

```bash
uvicorn api:app --reload
```

#### Backend Access:

Open a web browser and navigate to http://localhost:8000 to access the FastAPI backend (primarily used by the Streamlit frontend).

#### Using the Streamlit Frontend

Ensure the Backend is Running:

Make sure the FastAPI server is active as described above.

#### Run the Streamlit App:

In a separate terminal window, navigate to the project directory and run:

```bash
streamlit run frontend.py
```

#### Interact with the Application:

1. Use the Streamlit interface to upload PDFs and submit queries.
2. View responses directly within the Streamlit app, including any embedded images.

## API Endpoints 📡

The FastAPI backend provides the following endpoints:

- GET /: Serves the main HTML page (primarily used for backend testing; the Streamlit frontend interacts directly with the API).
- POST /upload_pdf/: Endpoint for uploading PDF files.
- POST /query/: Endpoint for submitting queries.

### Detailed Endpoint Descriptions

1. GET /

- Description: Serves the main HTML page.
- Usage: Access via http://localhost:8000/ in a web browser.
- Response: Returns the index.html file located in the static directory.

2. POST /upload_pdf/

- Description: Uploads a PDF file for processing.
- Parameters:
- file (form data): The PDF file to upload.

3. Response:

- Success (200):

```json
{
  "filename": "uploaded_file.pdf",
  "message": "File uploaded successfully"
}
```

- Error (400):

```json
{
  "detail": "Only PDF files are allowed"
}
```

3. POST /query/

- Description: Submits a natural language query related to the uploaded PDFs.
- Parameters:
  - question (JSON body): The user's query.

```json
{
  "question": "What is the main result of the paper?"
}
```

- Response:
- Success (200):

```json
{
  "response": "The main result of the paper is..."
}
```

- Error (400):

```json
Copy code
{
  "detail": "Please upload a PDF first"
}
```

## 📁 Project Structure

```bash
MultiModal-RAG/
├── api.py
├── addvectorstore.py
├── main.py
├── load_files.py
├── imgproc.py
├── ragretriever.py
├── retrieval.py
├── frontend.py
├── requirements.txt
├── .env
├── static/
│ └── index.html
├── uploads/
│ └── (uploaded PDFs and extracted images)
└── README.md
```
