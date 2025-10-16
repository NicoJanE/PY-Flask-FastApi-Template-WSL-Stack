---
layout: default_c
RefPages:

--- 

<br>

# Setup Page

This is the setup page of the ***Python Flask/FAst-Api template project***
<br>



## 1. About WSLFile

This WSL is generated with the `WSLFile` script utility which is included but also can be found [here](https://github.com/NicoJanE/Powershell-Utilities/blob/master/WSLFile/).
This file script functions similarly to a `Dockerfile` and can:

- Download and install the **Debian Trixie** OS into  your new  WSL distribution
- Create/Setup your WSL environment, for example Create specific Debian user.
- Install packages into to the WSL
- Copy files from the host to the WSL distribution
- Set Environment variables in the WSL

---

## 2. Setup Instructions

This will install and configure the WSl distribution

1. Open and edit the `WSFile` to customize the settings, recommend settings to customize include:
    - `DISTRO` Indicates the WSL distribution to use, if it's a new distribution make sure to uncomment: `DISTRO_DEBIAN_NEW` 
    - `USER` Indicates the user under which the Debian packages are installed and to which user directory the  files are copied 
    - `DISTRO_DEBIAN_NEW` When Enabled will generate a new WSL under the name defined in `DISTRO`
   - `DESCRIPTION` Set a description for the WSL 

2. Run the WSLFile with:  
`powershell.exe -ExecutionPolicy Bypass -File .\wsl-parser.ps1`  
After this The WSL is now installed with the required packages, and the template project files are copied into the WSL in the user's home folder.
3. Check available WSL distributions and their states with: `wsl -l -v`
   - Optional Set the new WSL as default with: `wsl --set-default <DistroName>`.
4. Run the WSL distribution: `wsl -d <name> -u <username>`
   - Check Python extension are installed (requirements.txt): `cd /home/nico/`
   - `source venv/bin/activate`
   - `pip list` # Should display list with also: Flask, fastapi, Werkzeug, and others
5. Start VS code by typing: ` code .` (see next paragrap)

---

## 3. Visual Studio Code in the WSL

### 3.1  First-Time Setup

Make sure the VS Code is installed on your **host** with the **WSL** extension

- [Download from](https://code.visualstudio.com) and install it on the host
- Add the Remote WSL extension (Name: `WSL`, Id: `ms-vscode-remote.remote-wsl`).

### 3.2. Start VS Code from WSL (Recommended Method)

This is the easiest way to do it:

1. Make sure the 'First Time Setup' is done.
2. In Powershell start your WSL distribution: (`wsl -d <distro-name> -u <username>`)
3. Navigate to your project folder, e.g.: `cd ~/app`
4. Type: `code .`  
This launches a VS Code instance on the Windows host, connects it to your WSL environment, and automatically installs the VS Code Server inside WSL.
From there, you can **instal**l the required **extensions** in your WSL container (see 3.4)
5. Open the `/app` directory from the user's `home` directory using `File -> Open Folder`.

><details>  
>  <summary class="clickable-summary">
>  <span  class="summary-icon"></span> <!-- Square Symbol -->
>  <b>Help: `code .` command does not work the first time!</b>
>  </summary> <!-- On same line is failure -->
>
> This can happen if VS Code on the host has never been connected to a WSL environment before. In that case, start VS Code once using the **Alternative Method** below (via *WSL: Connect to WSL*). This will initialize the integration and make the code command available inside WSL.

</details>

### 3.3. Start VS Code Connected to WSL (Alternative Method)

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

### 3.4. Required WSL VS Code extensions

Ensure the following extensions are installed inside your WSL environment (VS Code will prompt you if any are missing):

- Python Debugpy `ms-python.debugpy` (required)
- Python: `ms-python.vscode-pylance` (required), `ms-python.python` (required)
- Ruff: `charliermarsh.ruff`
- REST Client: `humao.rest-client`
- Database Client: `cweijan.vscode-database-client2`


---

### 3.5 Debug and Run

Debugging and running the application take place **inside the WSL environment**. The project uses the built-in **Python Debugger** (pdb) for debugging, and the necessary setup code is already included in the sample.

To debug and run:

- Open the Run and Debug tab in VS Code.
- From the configuration dropdown, select **Debug Flask App**.
- When VS Code starts the server, it will display a link to the running web app — click the link to open it in your browser.

> **Python Interpreter Selection:** On first run, VS Code may prompt you to select a Python interpreter. Choose the one in the virtual environment: `~/venv/bin/python`. 
> 
> *Note: Unfortunately, VS Code sometimes ignores the `python.defaultInterpreterPath` setting in `settings.json`, requiring manual selection.*

<br><br>
<div align="center"> ─── ✦ ───
</div>
