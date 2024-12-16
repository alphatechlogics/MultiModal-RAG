let isFileUploaded = false;

async function uploadPDF() {
  const fileInput = document.getElementById("pdfFile");
  const file = fileInput.files[0];
  const messageArea = document.getElementById("uploadMessage");
  const querySection = document.getElementById("querySection");

  if (!file) {
    alert("Please select a file");
    return;
  }

  // Show loading message
  messageArea.textContent = "Uploading file...";
  messageArea.className = "message info";

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("http://localhost:8000/upload_pdf/", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();

    messageArea.textContent = "File uploaded successfully!";
    messageArea.className = "message success";

    // Show result
    document.getElementById("result").innerText = JSON.stringify(
      result,
      null,
      2
    );

    isFileUploaded = true;
    enableQuerySection();
  } catch (error) {
    console.error("Error:", error);
    messageArea.textContent = "Error uploading file.";
    messageArea.className = "message error";

    document.getElementById("result").innerText =
      "Error uploading file: " + error.message;
    isFileUploaded = false;
    disableQuerySection();
  }
}

function enableQuerySection() {
  const queryInput = document.getElementById("queryInput");
  const submitButton = document.querySelector(".query-section button");
  queryInput.disabled = false;
  submitButton.disabled = false;
}

function disableQuerySection() {
  const queryInput = document.getElementById("queryInput");
  const submitButton = document.querySelector(".query-section button");
  queryInput.disabled = true;
  submitButton.disabled = true;
}

async function submitQuery() {
  if (!isFileUploaded) {
    alert("Please upload a file before submitting a query.");
    return;
  }

  const query = document.getElementById("queryInput").value;
  if (!query) {
    alert("Please enter a query");
    return;
  }

  // Show loading spinner or message
  document.getElementById("result").innerText = "Processing your query...";

  try {
    const response = await fetch("http://localhost:8000/query/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question: query }),
    });

    const result = await response.json();
    document.getElementById("result").innerText = JSON.stringify(
      result,
      null,
      2
    );
  } catch (error) {
    console.error("Error:", error);
    document.getElementById("result").innerText =
      "Error submitting query: " + error.message;
  }
}

function clearResults() {
  document.getElementById("result").innerText = "";
  document.getElementById("queryInput").value = "";
  document.getElementById("uploadMessage").textContent = "";
  isFileUploaded = false;
  disableQuerySection();
}

// Initially disable the query section
disableQuerySection();
