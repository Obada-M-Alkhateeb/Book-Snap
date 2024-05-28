// preload.js
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  saveFile: (fileData, fileName) => ipcRenderer.invoke('save-file', fileData, fileName)
});
