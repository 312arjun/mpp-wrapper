# **📦 myphantompath python package **
A Python package for the `myphantompath` tool, providing easy integration for creating a secure encrypted tunnel between a server to server.

---

## **🚀 Installation**
### **From PyPI**
```sh
pip install mpp_cli_wrapper
```

### **From GitHub**
```sh
pip install git+https://github.com/myphantompath/mpp_cli_wrapper.git
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
✅ **Linux** (Uses `mpp` binary)

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

## **⚡ Development**
### **Clone the Repository**
```sh
git clone https://github.com/myphantompath/mpp_cli_wrapper.git
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

