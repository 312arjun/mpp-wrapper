# **📦 mpp_cli_wrapper**
A Python wrapper for the `mpp` CLI tool, providing easy integration for Windows and Linux.

---

## **🚀 Installation**
### **From PyPI**
```sh
pip install mpp_cli_wrapper
```

### **From GitHub**
```sh
pip install git+https://github.com/yourusername/mpp_cli_wrapper.git
```

---

## **🔧 Usage**
### **Import the package**
```python
from mpp_cli_wrapper import connect, disconnect
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
mpp_cli_wrapper/      # Package directory
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
git clone https://github.com/yourusername/mpp_cli_wrapper.git
cd mpp_cli_wrapper
```

### **Build & Publish (For Maintainers)**
```sh
python setup.py sdist bdist_wheel
twine upload dist/*
```

---

## **📜 License**
This project is licensed under the **MIT License**.

