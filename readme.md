# 🎙️ Voice Emotion Analysis Dashboard

## 📌 Project Overview
The **Voice Emotion Analysis Dashboard** is a web-based application that analyzes human emotions from voice recordings and visualizes how emotions change over time.  
The system processes audio input, converts speech into text, evaluates sentiment polarity, maps it to emotions, and displays the results in an interactive dashboard.

This project is developed using **Python 3.13**, **Streamlit**, and **NLP-based sentiment analysis**, making it lightweight, stable, and easy to deploy.

---

## 🎯 Objectives
- Accept voice/audio input from the user
- Convert speech to text
- Analyze sentiment and emotions from speech
- Detect **emotion changes at specific timestamps (seconds)**
- Visualize emotion transitions using charts
- Deploy the application on a cloud platform

---

## 🧠 Key Features
- 🎧 Audio file upload (WAV / MP3)
- ⏱️ Chunk-wise emotion detection (every 10 seconds)
- 😀 Emotion mapping (Happy, Calm, Neutral, Sad, Angry)
- 📊 Interactive emotion timeline visualization
- 📋 Detailed emotion log with timestamps
- ☁️ Cloud-deployable using Streamlit

---

## 🏗️ System Architecture
User Audio Input

↓

Audio Chunking (10 seconds)

↓

Speech-to-Text Conversion

↓

Sentiment Polarity Analysis

↓

Emotion Mapping

↓

Streamlit Dashboard Visualization


---

## 🛠️ Technology Stack

| Component | Technology |
|--------|------------|
| Programming Language | Python 3.13 |
| Web Framework | Streamlit |
| Speech Recognition | SpeechRecognition (Google API) |
| Audio Processing | Pydub |
| Sentiment Analysis | TextBlob |
| Visualization | Plotly |
| Deployment | Streamlit Cloud |

---

## 📁 Project Structure

Voice-Analysis/
│

├── app.py # Main Streamlit application

├── requirements.txt # Project dependencies

├── .gitignore # Ignored files

└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Rahulcheedella/Voice-Analysis.git
cd Voice-Analysis
```

### 2️⃣ Create Virtual environment
```bash
python -m venv venv
venv/Scripts/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Running the streamlit application
```bash
streamlit run app.py
```

### The app will be open in your browser
```bash
http://localhost:8501
```

## In this way you can run the streamlit application for to check the sentiment based on the voice
