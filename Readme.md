# **📦 myphantompath **
A Python wrapper for the server to server secure communication, providing easy integration for Windows and Linux.

---

## **🚀 Installation**
### **From PyPI**
```sh
pip install mpp_wrapper
```

### **From GitHub**
```sh
pip install git+https://github.com/myphantompath/mpp_wrapper.git
```

---

## **🔧 Usage**
### **Import the package**
```python
from mpp_wrapper import connect, disconnect
```

### **Connect**
```python
connect()  # Starts the connection
```

### **Disconnect**
```python
disconnect()  # Ends the connection
```

---

## **💻 Platform Compatibility**
✅ **Windows** (Uses `mpp.exe`)
✅ **Linux** (Uses `mpp` binary if available)

---

## **📁 Project Structure**
```
mpp_wrapper/      # Package directory
│── bin/              # Contains CLI binaries (mpp.exe, mpp)
│── __init__.py       # Makes this a Python package
│── cli_wrapper.py    # Python wrapper for CLI
│── setup.py          # Package metadata
│── README.md         # Documentation
│── .gitignore        # Ignore build files
│── MANIFEST.in       # Include non-Python files (like binaries)
```

---

## **⚙️ Configuration**
To use this package, ensure you have a valid `wg0.conf` file. Below is an example configuration:

```ini
[Interface]
PrivateKey = YOUR_PRIVATE_KEY
Address = 10.0.0.2/24
DNS = 1.1.1.1

[Peer]
PublicKey = SERVER_PUBLIC_KEY
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = SERVER_IP:PORT
PersistentKeepalive = 25
```

Make sure to replace `YOUR_PRIVATE_KEY`, `SERVER_PUBLIC_KEY`, and `SERVER_IP:PORT` with actual values provided by your server.


---

## **⚡ Development**
### **Clone the Repository**
```sh
git clone https://github.com/myphantompath/mpp_wrapper.git
cd mpp_wrapper
```

### **Build & Publish (For Maintainers)**
```sh
python setup.py sdist bdist_wheel
twine upload dist/*
```

---

# mpp-node

## Introduction
`mpp-node` is a Node.js package designed to establish a secure tunnel for safe communication between server to server. It includes two main functions:

- `connect()`: Establishes a tunnel.
- `disconnect()`: Deletes the tunnel.

Additionally, the package requires a file named `wg0.conf` to be present wherever `mpp-node` is imported.

This guide will help you clone the repository, set up a local version using `npm link`, and attach it to other Node.js projects.

## Cloning the Repository and Setting Up `npm link`

### Step 1: Clone the Repository
First, clone the repository from GitHub:
```sh
git clone https://github.com/myphantompath/mpp-node.git
```

### Step 2: Navigate into the Project Directory
```sh
cd mpp-node
```

### Step 3: Set up `npm link`
Run the following command to create a global symlink to the package:
```sh
npm link
```

## Using the Linked Package in Another Project

### Step 1: Navigate to Your Node.js Project
```sh
cd /path/to/your-project
```

### Step 2: Link the `mpp-node` Package
```sh
npm link mpp-node
```
This will create a symbolic link to the globally linked `mpp-node` package.

### Step 3: Ensure `wg0.conf` File is Present
Before using `mpp-node`, make sure a file named `wg0.conf` is present in the project directory.

### Step 4: Use the Package
Now, you can use `mpp-node` in your project as if it were installed from npm:
```javascript
const mpp = require('mpp-node');

// Establish a tunnel
mpp.connect();

// Disconnect the tunnel when done
mpp.disconnect();
```

## Troubleshooting
- If changes in `mpp-node` are not reflecting in the linked project, try reinstalling dependencies:
  ```sh
  npm link mpp-node
  ```
- Ensure the `wg0.conf` file is present; otherwise, `mpp-node` may not function correctly.

## **📜 License**
This project is licensed under the **MIT License**.

