# 💚 LupusCare AI

### An AI-Assisted Health Tracking and Management Web Application

LupusCare AI is a healthcare-focused web application designed to help users organize symptom records, manage medication information, track doctor appointments, and prepare health summaries for medical consultations.

The application combines a Streamlit interface, Python-based text analysis, basic image processing, and JSON-based data storage.

> **Disclaimer:** LupusCare AI is an educational prototype, not a medical diagnostic tool. It cannot diagnose lupus or replace professional medical advice.

## ✨ Features

- 🏠 **Home Dashboard** — Overview of health records and activities.
- 📔 **Symptom Diary** — Record and review symptoms.
- 💊 **Medicine Tracker** — Organize medication information and logs.
- 📅 **Appointment Tracker** — Manage upcoming and completed appointments.
- 📊 **Health Insights** — Review recorded health information.
- 🩺 **Doctor Summary** — Organize information to discuss with a healthcare professional.
- 🧠 **LupusVision NLP** — Basic text-based symptom keyword analysis.
- 🖼️ **Image Processing** — Inspect image properties using Python and OpenCV.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- OpenCV
- Pillow (PIL)
- JSON
## 📸 Application Screenshots

### Home Dashboard
![Home Dashboard](screenshots/home.png)

### Symptom Diary
![Symptom Diary](screenshots/symptom-diary.png)

### Medicine Tracker
![Medicine Tracker](screenshots/medicine-tracker.png)

### Appointment Tracker
![Appointment Tracker](screenshots/appointments.png)

### Health Insights
![Health Insights](screenshots/health-insights.png)

### Doctor Summary
![Doctor Summary](screenshots/doctor-summary.png)

### LupusVision AI
![LupusVision AI](screenshots/lupusvision-ai.png)
## 🏗️ How It Works

1. The user opens the Streamlit web application.
2. The user enters symptom, medication, or appointment information.
3. The application stores supported records in local JSON files.
4. The dashboard displays available records and summaries.
5. The text-analysis module identifies configured symptom keywords.
6. The image-processing module examines basic image properties.

**Note:** Keyword analysis and image processing do not establish whether a person has lupus. No trained diagnostic model is claimed in this prototype.

## 🚀 Getting Started

### Prerequisites

- Python installed on your computer.
- Git, if you want to clone the repository.

### Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd LupusCare-AI
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 📂 Project Structure

```text
LupusCare-AI/
├── app.py
├── lupusvision_nlp.py
├── lupusvision_cv.py
├── requirements.txt
├── symptom_records.json
├── medicine_records.json
├── medicine_log.json
└── appointments.json
```

*This is an example structure. Update it to match the actual files in your repository.*

## 🎯 Project Objectives

- Make personal health-record organization easier.
- Provide a simple interface for recording symptoms and appointments.
- Demonstrate the use of Python and Streamlit in a healthcare-focused application.
- Explore basic NLP and image-processing techniques.
- Help users organize information for discussions with healthcare professionals.

## 🔮 Future Improvements

- Improve input validation and data privacy.
- Add secure user authentication and database storage.
- Evaluate text analysis using a carefully validated dataset.
- Explore machine learning only when suitable, ethically sourced data is available.
- Improve accessibility and dashboard design.

## 👩‍💻 Developer

**Sarumathi S**

B.Tech — Artificial Intelligence and Data Science

---

⭐ *An educational project exploring Python, AI-assisted features, and healthcare record management.*
