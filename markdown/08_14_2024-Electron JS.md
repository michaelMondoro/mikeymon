# Electron JS

In the evolving landscape of software development, creating desktop applications that are both powerful and accessible across multiple platforms can be challenging. This is where Electron.js comes into play. Electron.js has gained significant traction as a framework for building cross-platform desktop applications using familiar web technologies. Let’s dive into what makes Electron.js a popular choice for developers and how it leverages the power of modern web development.

#### What is Electron.js?

Electron.js, developed by GitHub, is an open-source framework that allows developers to build desktop applications using web technologies such as HTML, CSS, and JavaScript. Launched in 2013, Electron combines the Chromium rendering engine and the Node.js runtime to provide a robust platform for creating desktop apps. This means that developers can use a single codebase to target Windows, macOS, and Linux. `print("this is awesome")`


**example**

```
npm init
npm install electron --save-dev
```

```
const { app, BrowserWindow } = require('electron');
const path = require('path');
function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js')
    }
  });

  mainWindow.loadFile('index.html');
}
app.whenReady().then(() => {
  createWindow();
  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});
```
