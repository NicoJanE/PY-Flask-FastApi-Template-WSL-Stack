# What
This is a Python project application template using Flask and FastAPI in a **WSL container**


## Requirements
- Windows 10 or 11
- WSL 2.6.1.0
- Powershell 5.1 or 7.3

This is a Python Flask application (template) that requires the following libraries (installed with pip via the requirements file):
1. Flask: A web framework for Python.
2. Redis: An in-memory data structure store, used as a database.
3. Jinja2: A modern and designer-friendly templating language for Python.
4. PDB: Python Debugger, used for debugging the Flask application.

The template includes a basic structure for a web application using FastAPI and Flask, with support for Redis as a database and Jinja2 for templating. PDB is provided for debugging purposes during development.

<small> Note: There is also a Docker version of this project template available. However, due to remote debugging issues in the Docker container, it is recommended to use this non-Docker version. The Docker container can be found [here](https://github.com/NicoJanE/PY-Flask-FastApi-Template-Stack) <small>

---

# About WSLFile

This WSL is generated with the `WSLFile` script utility which can be found [here](https://github.com/NicoJanE/Powershell-Utilities/blob/master/WSLFile/).
This file functions similarly to a Dockerfile and can:
- Download and install the **Debian Trixie** OS into  your new  WSL distribution
- Create/Run under a specific Debian user
- Install packages into to the WSL
- Copy files from the host to the WSL distribution
- Set Environment variables in the WSL

---

# Setup

This will install and configure the WSl distribution

1. Open the `WSFile` and optional customize settings, recommend settings to customize include:
  - `DISTRO` Indicates the WSL distribution to use, if it's a new distribution make sure to uncomment: `DISTRO_DEBIAN_NEW` 
  - `USER` Indicates the user under which the Debian packages are installed and to which user directory the  files are copied 
  - `DISTRO_DEBIAN_NEW` When Enabled will generate a new WSL under the name defined in `DISTRO`
  - `DESCRIPTION` Set a description for the WSL 
2. Run the WSLFile with:  
`powershell.exe -ExecutionPolicy Bypass -File .\wsl-parser.ps1`
3. Ensure that this is the only WSL distribution running.
4. Check available WSL distributions and their states with: `wsl -l -v
5. Set the new WSL as default with: `wsl --set-default <DistroName>`.
6. Restart the WSL with: `wsl --shutdown` followed by `wsl`. 
7. You will enter the new WSL distribution. Exit the WSL using `exit`. The WSL will continue running (`wsl -l -v`).
8. The WSL is now installed with the required packages, and the template project files are copied into the WSL in the user's home folder.

---

# VSC (Visual Studio Code)

To use VS Code in combination with WSL (development stack):

### First Time Setup

1. Install VS Code on the host and the Remote WSL extension (Name: `WSL`, Id: `ms-vscode-remote.remote-wsl`).
2. Ensure only one WSL distribution is running to prevent issues.
3. Connect to your WSL from VS Code by either:
   - Pressing F1 and selecting 'WSL: Connect to WSL'.
   - Activating the VS Code tab: `Remote Explorer`, right-clicking on your container name, and choosing one of the options:
     - `Connect in New Window`
     - `Connect in Current Window`
4. Open the `/app` directory from the user's `home` directory using `File -> Open Folder`.
5. Ensure the following extensions are installed in the opened WSL container:
   - Python: `ms-python.vscode-pylance` (required), `ms-python.python` (required)
   - Ruff: `charliermarsh.ruff`
   - REST Client: `humao.rest-client`
   - Database Client: `cweijan.vscode-database-client2`

### Debug and Run
Debugging and running of the application happen in the WSL container. The `pdb` (Python Debugger) is used to debug the application. Some code is required to enable the `pdb` process, but this code is already provided in the sample.

To debug and run:
- Select the `Run and Debug` tab in VS Code.
- From the combo box, select `Debug Flask App`. VS Code will display your link for the website; click on it.