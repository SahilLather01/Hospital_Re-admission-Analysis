# 🏥 Hospital Readmission Analysis

An end-to-end analytics and modeling solution designed to assess patient readmission risk across specialties and treatment patterns. This project analyzes **25,000+ patient records** to empower hospitals with predictive insights, operational dashboards, and data-driven care strategies.

---

##  GitHub Repository  
🔗 [click to view Hospital-Readmission-Analysis](https://github.com/aneshraj-d96/Hospital-Readmission-Analysis)

---

## 🧠 Project Overview

Hospital readmissions are a key metric for care quality and operational efficiency. This project delivers a full-stack solution that enables:

- 🔍 Risk profiling of patients based on visit history and diagnosis  
- 📊 Specialty-level readmission trend analysis  
- 🧠 Predictive modeling for care optimization  
- 📈 Dashboard-driven insights for hospital decision-making  

### 🎯 Key Objectives

- Clean and preprocess patient-level hospital data  
- Engineer features for readmission prediction and dashboarding  
- Build classification models to assess readmission risk  
- Deploy interactive dashboards for real-time clinical insights  

---

## 📁 Project Structure

| File Name                              | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| `hospital_readmission.sql`            | SQL queries for data extraction and transformation                         |
| `hospital readmission.ipynb`          | Jupyter notebook with full analysis workflow                               |
| `sqlconnect.py`                       | Python script for SQL database connection                                  |
| `app.py`                              | Streamlit app for interactive model deployment                             |
| `readmission_model.pkl`               | Trained classification model for readmission prediction                    |
| `feature_names.pkl`                   | Serialized feature list used in model training                             |
| `cleaned_hospital_readmission.csv`    | Preprocessed dataset used for modeling                                     |
| `hospital_readmissions_cleaned.csv`   | Alternate cleaned dataset version                                          |
| `Hospital Readmission Analytics.docx` | Project documentation and summary report                                   |

---

## 📊 Dataset Summary

- **Total Records**: 25,000  
- **Key Columns**:  
  `age`, `time_in_hospital`, `n_lab_procedures`, `n_procedures`, `n_medications`, `n_outpatient`, `n_inpatient`, `n_emergency`, `medical_specialty`, `diag_1`, `diag_2`, `diag_3`, `glucose_test`, `A1Ctest`, `change`, `diabetes_med`, `readmitted`, `total_visits`  
- **Target Variable**: `readmitted`  
- **Feature Set**: Visit counts, diagnosis codes, medication history, specialty, and encoded categorical variables  

---

## 🧹 Data Preprocessing

- Converted date fields and calculated total visits  
- Normalized treatment metrics and encoded categorical features  
- Removed outliers and handled missing values  
- Engineered features for diagnosis grouping and specialty impact  

---

## 📈 Exploratory Data Analysis

- 📊 Readmission trends by specialty and diagnosis  
- 🏥 Visit patterns across inpatient, outpatient, and emergency channels  
- 💊 Medication change and diabetes treatment impact  
- 📅 Hospital stay duration and seasonal readmission patterns  

---

## 🤖 Modeling Approach

- **Target Variable**: `readmitted`  
- **Algorithms Used**: Logistic Regression, Random Forest, XGBoost  
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1 Score, ROC-AUC  
- **Top Features**: `n_inpatient`, `change`, `medical_specialty`, `diag_1`, `n_medications`  

---

## 📊 Dashboard Overview

### 🔷 Power BI Dashboard  
Visualizes hospital-level readmission metrics:

- 🧑‍⚕️ Specialty-wise readmission breakdown  
- 📈 KPI cards for hospital stay, medication count, and readmission rate  
- 📅 Diagnosis trends and treatment intensity  

![Power BI Preview](https://image2url.com/images/1755689108294-04c8b2aa-7705-4922-bd8f-ea39d5c351f2.png)

---

### 🟢 Streamlit App  
Interactive dashboard for real-time patient risk prediction:

- 🧍 Patient-level readmission summary  
- 🔮 Risk prediction tool based on visit and diagnosis history  
- 📊 Feature importance visualization  
- 📍 Filters by specialty, diagnosis, and treatment type  

![Streamlit Preview](https://image2url.com/images/1755871866936-eccca89e-deec-4677-b261-d9faf1b35db4.png)  
![Streamlit Preview](https://image2url.com/images/1755871895569-76e3f3ac-3c4b-462a-bb10-ad9b164ecc65.png)  
![Streamlit Preview](https://image2url.com/images/1755871927124-061aa7b4-7f70-4e7c-901e-668b6f1536b3.png)

---

## 🚀 Deployment

- Model serialized with `joblib` as `readmission_model.pkl`  
- Dashboard deployed via **Streamlit Cloud**  
- SQL integration for dynamic data updates  
- Git LFS used for large file management  

---

## 🧠 Business Impact

- Flags high-risk patients for proactive care  
- Improves hospital resource allocation and discharge planning  
- Enables real-time readmission monitoring  
- Supports data-driven clinical strategy and quality improvement  

---

## 🛠️ Tech Stack

- **Python**: Pandas, NumPy, Scikit-learn, Streamlit  
- **SQL**: Data extraction and transformation  
- **Visualization**: Power BI, Matplotlib, Seaborn  
- **Deployment**: Streamlit Cloud, GitHub, Git LFS  

---

## 📌 Future Enhancements

- Integrate real-time EHR feeds via APIs  
- Add explainability via SHAP or LIME  
- Enable user-uploaded patient records for prediction  
- Expand dashboard to include treatment outcome forecasting  

---

## 👤 Author

**Sahil Lather**  

🔗 [GitHub Profile](https://github.com/SahilLather01)
