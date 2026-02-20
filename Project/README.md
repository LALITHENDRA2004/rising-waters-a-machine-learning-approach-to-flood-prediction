# 🌊 Rising Waters: A Machine Learning Approach to Flood Prediction

## 📌 Project Overview

Flood Prediction using Machine Learning is an Artificial Intelligence application designed to forecast flood occurrences based on environmental and historical weather data.

This system analyzes key climatic and rainfall-related parameters to predict the possibility of severe floods. The goal is to assist in early warning, disaster response planning, and infrastructure resilience by providing timely predictions.

---

## 🎯 Objectives

- Predict flood occurrence using machine learning classification algorithms.
- Analyze environmental features such as rainfall, temperature, and humidity.
- Build a web-based application using Flask.
- Provide real-time prediction interface through a user-friendly UI.

---

## 🛠 Tech Stack

- Programming Language: Python
- Data Analysis: Pandas, NumPy
- Visualization: Matplotlib, Seaborn
- Machine Learning: Scikit-learn, XGBoost
- Web Framework: Flask
- Frontend: HTML, CSS
- Version Control: Git & GitHub

---

## 📊 Dataset Features Used

The model is trained using the following environmental features:

- Temperature (Temp)
- Humidity
- Cloud Cover
- Annual Rainfall (ANNUAL)
- Jan–Feb Rainfall
- Mar–May Rainfall
- Jun–Sep Rainfall
- Oct–Dec Rainfall
- Average June Rainfall (avgjune)
- Sub Parameter

Target Variable:
- Flood (0 = No Flood, 1 = Flood)

---

## 🔎 Machine Learning Workflow

1. Data Loading and Exploration (EDA)
2. Data Preprocessing
   - Feature & Target Separation
   - Train-Test Split
   - Standardization using StandardScaler
3. Model Training
   - Decision Tree
   - Random Forest
   - KNN
   - XGBoost (Final Model)
4. Model Evaluation
   - Accuracy
   - Precision
   - Recall
   - Confusion Matrix
5. Model Saving using Joblib
6. Flask Deployment

---

## 📈 Model Performance

- Accuracy: ~96%
- Precision: 1.0
- Recall: 0.66

Confusion Matrix Example:

[[26, 0],
 [ 1, 2]]

The model correctly identifies most flood cases while minimizing false alarms.

---

## 🌐 Web Application Structure

```

Flask/
│
├── app.py
├── floods.save
├── transform.save
│
├── static/
│   └── css/
│       └── styles.css
│
└── templates/
├── home.html
├── index.html
├── chance.html
└── noChance.html

```

---

## 🚀 How to Run the Project Locally

1. Clone the repository:

   - git clone https://github.com/YOUR_USERNAME/rising-waters-a-machine-learning-approach-to-flood-prediction.git

2. Navigate to the project folder:

   - cd flood_prediction_system

3. Install dependencies:

   - pip install -r requirements.txt

4. Run Flask app:

   - python app.py

5. Open in browser:

   - http://127.0.0.1:5000

---

## 📌 Use Cases

1. Early Warning Systems  
Authorities can use predictions to issue alerts to residents in flood-prone areas.

2. Disaster Response Planning  
Emergency services can allocate resources effectively based on predicted flood risks.

3. Infrastructure Resilience  
Urban planners can use risk assessments for designing flood-resistant infrastructure.

---

## 🔮 Future Improvements

- Integration with real-time weather APIs
- Use of larger datasets
- Deployment on cloud platforms (IBM Cloud)
- Advanced model tuning and cross-validation

---
