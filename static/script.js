
const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('file-input');
const fileList = document.getElementById('file-list');

// Prevent default drag behaviors
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, preventDefaults, false);
    document.body.addEventListener(eventName, preventDefaults, false);
});

// Highlight drop area when item is dragged over it
['dragenter', 'dragover'].forEach(eventName => {
    dropArea.addEventListener(eventName, highlight, false);
});

// Remove highlight when item is dragged out of drop area
['dragleave', 'drop'].forEach(eventName => {
    dropArea.addEventListener(eventName, unhighlight, false);
});

// Handle dropped files
dropArea.addEventListener('drop', handleDrop, false);

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function highlight() {
    dropArea.classList.add('highlight');
}

function unhighlight() {
    dropArea.classList.remove('highlight');
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;

    handleFiles(files);
}

function handleFiles(files) {
    if (files.length > 0) {
        fileList.innerHTML = ''; // Clear previous file list

        const file = files[0]; // Take only the first file

        const listItem = document.createElement('div');
        listItem.textContent = file.name;
        fileList.appendChild(listItem);

        // Set the file input's files property to the selected file
        fileInput.files = files;
    } else {
        fileList.innerHTML = '<p>No file selected</p>';
    }
}

function uploadFiles() {
    const form = document.getElementById('upload-form');
    const formData = new FormData(form);

    const showResult = document.querySelector(".result")
    const showCopy = document.querySelector(".hide")
    const result = document.querySelector(".transcript")
    showResult.classList.remove("result")
    showCopy.classList.remove("hide")

    fetch('/transcribe/', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then( data => {
        console.log(data);
        console.log(data.transcription);
        result.innerHTML = data.transcription
        document.getElementById("login_request").innerHTML = `<h4>Your script is not saved, login to save your transcriptions so you can get them later</h4>`

    })
    .catch(error => console.error('Error:', error));
}