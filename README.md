# Smart File Organizer

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)]()
[![Automation](https://img.shields.io/badge/Automation-Ready-success.svg)]()

---

### Overview
**Smart File Organizer** is a lightweight Python utility designed to automatically categorize and sort files based on their **content type** and **access/modification date**.  
Unlike traditional file organizers that rely on file extensions, this tool uses the [`python-magic`](https://pypi.org/project/python-magic/) library to detect the *actual* file type by analyzing its internal signature.  

The script creates a clean, structured directory system — organized by **file category** (Images, Documents, Audio, Archives, etc.) and further sorted into **date-based subfolders** (e.g., `2025-10-27`).

---

## Features

-  **Content-Aware Detection** – Identifies file types accurately using `python-magic`.  
-  **Automatic Folder Structuring** – Files are sorted into logical categories.  
-  **Date-Based Organization** – Subfolders created by access or modification date.  
-  **Automated File Relocation** – Moves files to their correct destinations.  
-  **Highly Customizable** – Categories, date format, and directory paths are easy to modify.  
-  **Cross-Platform** – Works on Windows, Linux, and macOS. 
