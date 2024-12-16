# 🌐 Multi-RAG Portal

[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.6-green)](https://fastapi.tiangolo.com/)

## 📜 Overview

**Multi-RAG Portal** is a web-based tool designed to help you interact more intuitively with PDF resources. By harnessing **Retrieval-Augmented Generation (RAG)**, this system enables you to effortlessly upload PDF documents and pose natural language queries. It seamlessly integrates a FastAPI-powered backend with a straightforward frontend comprised of HTML, CSS, and JavaScript. The result is a fluid user experience where you can find information based on the contents of your uploaded files, all through simple, conversational queries.

### ✨ Key Advantages

- **Document Submission**: Easily send in your PDF documents for indexing.
- **Intelligent Q&A**: Ask questions about your PDFs and receive context-rich, human-like answers.
- **User-Friendly UI**: Enjoy a clean, intuitive interface that simplifies interaction.

## ⚙️ Requirements

Before starting, ensure you have the following set up:

- **Python 3.12+**
- **pip** (Python’s package manager)
- **Node.js** and **npm** (if you need to adjust frontend components)

### 📚 PDF Tooling

For processing PDF files, you’ll need **poppler-utils**:

- **Ubuntu/Debian**: `sudo apt-get install poppler-utils`
- **macOS**: `brew install poppler`
- **Windows**: Obtain Poppler from its official source and include its `bin` directory in your `PATH`.

## 🚀 Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/RohmaButt/MultiModal-RAG.git
   cd multi-rag-portal

   ```

1. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

1. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

1. Install additional dependencies (if needed):
   - For PDF processing: `pip install pdf2image pillow`
   - On Ubuntu/Debian: `sudo apt-get install poppler-utils`
   - On macOS: `brew install poppler`
   - On Windows: Download and install poppler manually, then add its bin directory to your PATH.

## Usage 🚀

1. Start the FastAPI server:

   ```
   uvicorn api:app --reload
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. Use the interface to upload a PDF file and submit queries.

## API Endpoints 📡

- `GET /`: Serves the main HTML page
- `POST /upload_pdf/`: Endpoint for uploading PDF files
- `POST /query/`: Endpoint for submitting queries
