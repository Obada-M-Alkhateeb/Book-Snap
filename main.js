// main.js
const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const path = require('path');
const fs = require('fs');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'), // Enable contextBridge in the renderer process
      nodeIntegration: false,
      contextIsolation: true
    }
  });

  mainWindow.loadFile('index.html');
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});

// Listen for file save requests
ipcMain.handle('save-file', async (event, fileData, fileName) => {
  const { canceled, filePath } = await dialog.showSaveDialog({
    defaultPath: fileName
  });

  if (!canceled && filePath) {
    fs.writeFileSync(filePath, fileData);
    return true;
  } else {
    return false;
  }
});

