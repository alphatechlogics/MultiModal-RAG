# frontend.py

import streamlit as st
import requests
import json
import base64
from PIL import Image
import io

# Define the backend API URL
API_URL = "http://localhost:8000"

# Set the title of the Streamlit app
st.title("🌐 Multi-RAG Portal")

# Sidebar for uploading PDFs and submitting queries
st.sidebar.header("Upload PDF")

# File uploader for PDF files
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type="pdf")

# Initialize a session state variable to track if a PDF has been uploaded
if 'pdf_uploaded' not in st.session_state:
    st.session_state.pdf_uploaded = False

# Function to display images from Base64 strings
def display_image_from_base64(b64_string):
    try:
        image_data = base64.b64decode(b64_string)
        image = Image.open(io.BytesIO(image_data))
        st.image(image, use_column_width=True)
    except Exception as e:
        st.error(f"Error displaying image: {e}")

# Function to handle PDF upload
def upload_pdf(file):
    files = {"file": (file.name, file, "application/pdf")}
    with st.spinner("Uploading and processing PDF..."):
        try:
            response = requests.post(f"{API_URL}/upload_pdf/", files=files)
            response.raise_for_status()
            upload_data = response.json()
            st.success(upload_data.get("message", "File uploaded successfully!"))
            st.session_state.pdf_uploaded = True
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred during PDF upload: {e}")
            st.session_state.pdf_uploaded = False

# If a file is uploaded, handle the upload
if uploaded_file is not None:
    st.sidebar.success("PDF Uploaded Successfully!")
    upload_pdf(uploaded_file)

# Sidebar for submitting queries
st.sidebar.header("Submit a Query")

# Text input for the user's question
user_query = st.sidebar.text_input("Enter your question about the PDF:")

# Button to submit the query
if st.sidebar.button("Submit Query"):
    if not st.session_state.pdf_uploaded:
        st.error("Please upload a PDF file first.")
    elif not user_query.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Processing your query..."):
            try:
                payload = {"question": user_query}
                headers = {"Content-Type": "application/json"}
                response = requests.post(f"{API_URL}/query/", headers=headers, data=json.dumps(payload))
                response.raise_for_status()
                query_response = response.json()
                st.subheader("Response:")
                response_content = query_response.get("response", "")
                
                # Check if the response contains image data
                if "data:image" in response_content:
                    # Extract Base64 string
                    try:
                        b64_str = response_content.split("base64,")[-1]
                        display_image_from_base64(b64_str)
                    except Exception as img_err:
                        st.error(f"Error processing image in response: {img_err}")
                else:
                    st.write(response_content)
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred while processing your query: {e}")

# Optional: Display uploaded file details
if st.session_state.pdf_uploaded:
    st.sidebar.write(f"**Uploaded File:** {uploaded_file.name}")
