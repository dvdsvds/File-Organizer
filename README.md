# 📂 File Organizer
> An automatic file organization tool built with a **C++ backend** and a **Python GUI (CustomTkinter)**.

---

## 🚀 Features
- ⚡ High-speed file classification powered by **C++17 + pybind11**
- 🪟 Modern and clean **CustomTkinter GUI**
- 📁 Automatically sorts files by extension (Images, Documents, Media, Archives, etc.)

---

## 🧩 Project Structure (Explained)

This project consists of two main parts:

- **core/**  
  Contains the C++ backend using **pybind11**, responsible for scanning and organizing files.  
  - `fileorganizer.cpp` – The main logic for file sorting  
  - `CMakeLists.txt` – CMake build configuration

- **gui.py** – A **CustomTkinter** frontend providing a simple and elegant interface for users.  
  You can select a folder and organize files with one click.

- **requirements.txt** – Lists Python dependencies used during development.

---

## 💾 Installation

You don’t need to build anything manually.

1. Go to the **[Releases page](https://github.com/dvdsvds/File-Organizer/releases)**  
2. Download the latest version of `FileOrganizer.exe`  
3. Run it on your Windows PC 🎯  

That’s it — the GUI will launch and you can start organizing your files immediately!

---

## 🖱️ How It Works
1. Click **“Select Folder”** to choose your target directory  
2. Press **“Start Organizing”**  
3. Files are automatically categorized into subfolders like:  
   - `Images/`  
   - `Documents/`  
   - `Media/`  
   - `Archives/`

---

## 📜 License
This project is licensed under the **MIT License** – see the [LICENSE](./LICENSE) file for details.
