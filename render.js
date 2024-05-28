const { ipcRenderer } = require('electron');

const downloadButton = document.getElementById('download-button');
const filePath = 'C:\Users\LENOVO\Desktop\Graduation project 2'; // Replace with your file URL

downloadButton.addEventListener('click', () => {
    ipcRenderer.send('download-file', filePath);
});
