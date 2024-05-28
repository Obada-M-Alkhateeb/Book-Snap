const { ipcRenderer } = require('electron');
const axios = require('axios');
const FormData = require('form-data');

document.getElementById('upload-button').addEventListener('click', async () => {
  const fileInput = document.getElementById('file');
  if (fileInput.files.length === 0) {
    alert('Please select a file.');
    return;
  }

  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      },
      responseType: 'blob'
    });

    const url = window.URL.createObjectURL(new Blob([response.data]));
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', 'presentation.pptx');
    document.body.appendChild(link);
    link.click();
    link.remove();
  } catch (error) {
    console.error('Error uploading file:', error);
    alert('Failed to upload file.');
  }
});
