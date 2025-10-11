# What

This is a Python project application template using Flask and FastAPI in a **WSL container**

<br>

## 1. Requirements

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

## 2. About WSLFile

This WSL is generated with the `WSLFile` script utility which can be found [here](https://github.com/NicoJanE/Powershell-Utilities/blob/master/WSLFile/).
This file functions similarly to a Dockerfile and can:

- Download and install the **Debian Trixie** OS into  your new  WSL distribution
- Create/Setup your WSL environment, for example Create specific Debian user.
- Install packages into to the WSL
- Copy files from the host to the WSL distribution
- Set Environment variables in the WSL

---

## 3. Setup

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

## 4. Visual Studio Code in the WSL

### 4.1  First-Time Setup

Make sure the VS Code is installed on your **host** with the **WSL** extension

- [Download from](https://code.visualstudio.com) and install it on the host
- Add the Remote WSL extension (Name: `WSL`, Id: `ms-vscode-remote.remote-wsl`).

### 4.2. Start VS Code from WSL (Recommended Method)

This is the easiest way to do it:

1. Make sure the 'First Time Setup' is done.
2. In Powershell start your WSL distribution: (`wsl -d <distro-name> -u <username>`)
3. Navigate to your project folder, e.g.: `cd ~/app`
4. Type: `code .`  
This launches a VS Code instance on the Windows host, connects it to your WSL environment, and automatically installs the VS Code Server inside WSL.
From there, you can install the required extensions and open your project folder.

><details>  
>  <summary class="clickable-summary">
>  <span  class="summary-icon"></span> <!-- Square Symbol -->
>  <b>Help: `code .` command does not work the first time!</b>
>  </summary> <!-- On same line is failure -->
>  
> This can happen if VS Code on the host has never been connected to a WSL environment before. In that case, start VS Code once using the **Alternative Method** below (via *WSL: Connect to WSL*). This will initialize the integration and make the code command available inside WSL.
>
</details>

### 4.3. Start VS Code Connected to WSL (Alternative Method)

To start the VS Code WSL from the Windows host VS Code

1. Make sure the *First Time Setup* is done.
2. Ensure only one WSL distribution is running to prevent issues.
3. Connect to your WSL from VS Code by either:
   - Pressing F1 and selecting 'WSL: Connect to WSL'.
   - Activating the VS Code tab: `Remote Explorer`, right-clicking on your container name, and choosing one of the options:
     - `Connect in New Window`
     - `Connect in Current Window`
4. Open the `/app` directory from the user's `home` directory using `File -> Open Folder`.

---

### 4.4. Required WSL VS Code extensions

Ensure the following extensions are installed inside your WSL environment (VS Code will prompt you if any are missing):

- Python Debugpy `ms-python.debugpy` (required)
- Python: `ms-python.vscode-pylance` (required), `ms-python.python` (required)
- Ruff: `charliermarsh.ruff`
- REST Client: `humao.rest-client`
- Database Client: `cweijan.vscode-database-client2`


---

### 4.5 Debug and Run

Debugging and running the application take place **inside the WSL environment**. The project uses the built-in **Python Debugger** (pdb) for debugging, and the necessary setup code is already included in the sample.

To debug and run:

- Open the Run and Debug tab in VS Code.
- From the configuration dropdown, select **Debug Flask App**.
- When VS Code starts the server, it will display a link to the running web app — click the link to open it in your browser.