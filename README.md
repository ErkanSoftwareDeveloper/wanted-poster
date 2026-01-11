# 🎯 WANTED Poster Generator

A fun and simple **desktop application** to create WANTED posters from images, built with **Python** and **Tkinter**.
Add “WANTED” and “REWARD” banners, then save your poster as a PDF.

---

## ✨ Features

* Upload any image
* Add top banner **“WANTED”**
* Add bottom banner **“REWARD $5000”**
* Preview poster in GUI
* Save poster as PDF
* Simple and intuitive interface

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI framework
* **Pillow (PIL)** – image processing and PDF generation
* **ImageFont** – custom font support for poster text

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/ErkanSoftwareDeveloper/wanted-poster.git
cd wanted-poster
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure the **Font/LibreBodoni-Medium.ttf** file is present, or the app will fallback to the default font.

---

## ▶️ Usage

Run the application:

```bash
python wantedposter.py
```

1. Click **UPLOAD IMAGE** to select a photo
2. Click **GENERATE WANTED** to add banners
3. Click **SAVE AS PDF** to export your poster
4. Preview is shown in the GUI before saving

---

## 📁 Project Structure

```text
wanted-poster/
├─ wantedposter.py      # Main application file
├─ Font/LibreBodoni-Medium.ttf  # Optional custom font
├─ .gitignore           # Git ignored files
├─ README.md            # Project documentation
└─ requirements.txt     # Project dependencies
```

---

## 📸 Video

![2026-01-1116-12-42-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/02a4daf4-5f15-46e4-adc6-00d1f4ba98c7)

---

## 🚀 Possible Improvements

* Custom text for top and bottom banners
* Custom reward amount
* Save as image formats (PNG/JPG)
* Dark / light theme support
* Packaging as executable (.exe)

---

## 📄 License

This project is intended for **educational and personal use**.
