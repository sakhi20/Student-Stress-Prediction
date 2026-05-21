# AI and ML Driven Prediction of Student Mental Health

![Python](https://img.shields.io/badge/Python-3.9+-blue) ![Accuracy](https://img.shields.io/badge/Accuracy-81--85%25-green) ![License](https://img.shields.io/badge/License-Academic-lightgrey) ![Institution](https://img.shields.io/badge/Institution-NC_State-red)

**Author:** Sakhi Patel  
**Institution:** North Carolina State University  
**Course:** Big Data Analysis Project  
**Email:** sakhipatel20@gmail.com

---

## 📋 Project Overview

This project leverages **Artificial Intelligence (AI)** and **Machine Learning (ML)** techniques to predict stress, anxiety, and depression levels among university students. Using big data analytics on student survey responses, the system identifies mental health risk factors and provides an interactive self-assessment tool.

### 🎯 Objectives

- Analyze student stress indicators from academic and demographic data
- Build predictive models for mental health assessment using Random Forest
- Perform K-Means clustering to identify student groups with similar characteristics
- Provide an interactive self-assessment tool for students
- Identify primary stressors affecting university students

---

> [!WARNING]
> This tool is for **educational and research purposes only**.
> It does NOT provide clinical diagnosis and cannot replace professional
> medical care. If you are experiencing a mental health crisis, please
> contact the **988 Suicide & Crisis Lifeline** (call or text 988) or
> your campus counseling center immediately.

---

## 📊 Dataset

### Source
Student mental health survey with 500 responses (synthetic data generated for research purposes). Synthetic data was chosen to enable open sharing of the full codebase without privacy concerns; the pipeline is designed to work with real survey data by replacing the CSV in `data/`.

### Structure
- **Total Columns:** 39
- **Demographics:** Age, Gender, University, Department, Academic Year, CGPA, Scholarship Status
- **Mental Health Questions:** 26 questions rated on 0-4 scale
  - Anxiety: 7 questions
  - Stress: 10 questions
  - Depression: 9 questions
- **Target Variables:** Anxiety Label, Stress Label, Depression Label (Low/Medium/High)

### Rating Scale
- **0** = Never
- **1** = Rarely
- **2** = Sometimes
- **3** = Often
- **4** = Very Often

---

## 🛠️ Tech Stack

### Programming Language
- Python 3.9+

### Libraries
- **Data Processing:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Machine Learning:** scikit-learn
- **Model Persistence:** joblib

### Algorithms
- **Clustering:** K-Means (k=4)
- **Classification:** Random Forest Classifier
- **Preprocessing:** StandardScaler, LabelEncoder

---

## 📁 Project Structure

```
mental-health-prediction/
├── data/
│   └── student_mental_health_survey.csv    # Survey dataset
├── src/
│   ├── utils.py                            # Helper functions
│   ├── generate_data.py                    # Synthetic data generator
│   ├── 1_data_preprocessing.py             # Data cleaning & encoding
│   ├── 2_exploratory_analysis.py           # EDA & visualizations
│   ├── 3_clustering_analysis.py            # K-Means clustering
│   ├── 4_classification_models.py          # Random Forest models
│   └── 5_assessment_tool.py                # Interactive assessment
├── outputs/
│   ├── visualizations/                     # All plots (22+ PNG files)
│   ├── models/                             # Trained models (.pkl)
│   ├── results/                            # Performance metrics
│   ├── cleaned_data.csv                    # Preprocessed data
│   └── clustered_data.csv                  # Data with cluster labels
├── docs/
│   └── literature_review.md                # Research paper summaries
├── requirements.txt                        # Python dependencies
├── README.md                               # This file
└── run_analysis.py                         # Main execution script
```

---

## 🚀 Installation & Setup

### 1. Clone or Download the Project
```bash
cd "Stress Prediction"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Installation
```bash
python --version  # Should be 3.9+
pip list          # Check installed packages
```

---

## ▶️ Usage

### Run Complete Analysis Pipeline
Execute all steps (preprocessing, EDA, clustering, classification):
```bash
python run_analysis.py
```

This will:
- Generate synthetic dataset (if not exists)
- Preprocess and clean data
- Create 22+ visualizations
- Perform K-Means clustering
- Train 3 Random Forest models
- Save all outputs

**Expected Runtime:** 2-3 minutes

---

### Run Individual Scripts

#### 1. Data Preprocessing
```bash
python src/1_data_preprocessing.py
```
- Converts age and CGPA ranges to numeric
- Encodes categorical variables
- Handles missing values
- Saves cleaned data

#### 2. Exploratory Data Analysis
```bash
python src/2_exploratory_analysis.py
```
- Creates 16 visualizations
- Correlation analysis
- Demographic comparisons
- Mental health distributions

#### 3. Clustering Analysis
```bash
python src/3_clustering_analysis.py
```
- K-Means clustering (k=4)
- Silhouette score calculation
- Cluster visualizations
- Cluster characteristics analysis

#### 4. Classification Models
```bash
python src/4_classification_models.py
```
- Trains 3 Random Forest models
- Generates confusion matrices
- Feature importance analysis
- Model performance metrics

#### 5. Interactive Assessment Tool
```bash
python src/5_assessment_tool.py
```
- Self-assessment questionnaire
- Real-time scoring
- Personalized recommendations
- Mental health resources

---

## 📈 Key Findings

### Correlation Analysis
- **CGPA vs Anxiety:** Strong negative correlation (-0.85)
- **CGPA vs Stress:** Strong negative correlation (-0.83)
- **CGPA vs Depression:** Strong negative correlation (-0.82)

**Interpretation:** Lower CGPA is associated with higher mental health issues.

### Clustering Insights
- **4 distinct student groups** identified
- Clusters differ significantly in CGPA and mental health scores
- Silhouette Score: ~0.45 (moderate cluster quality)

### Model Performance
| Model | Accuracy | Best Feature |
|-------|----------|--------------|
| Anxiety Prediction | ~85% | Current CGPA |
| Stress Prediction | ~83% | Current CGPA |
| Depression Prediction | ~81% | Current CGPA |

### Demographic Insights
- Gender differences in mental health scores are minimal
- 3rd and 4th year students show higher stress levels
- Scholarship recipients show slightly lower anxiety

---

## 📊 Visualizations

The project generates 22+ professional visualizations:

### Frequency Distributions (7)
1. CGPA distribution
2. Age distribution
3. Gender distribution
4. University distribution
5. Department distribution
6. Academic year distribution
7. Scholarship status

### Mental Health Analysis (9)
8. Anxiety/Stress/Depression label distributions
9. Mental health score distributions
10. Correlation heatmap
11. CGPA vs mental health scatter plots
12. Mental health by gender
13. Mental health by academic year
14. Mental health by scholarship
15. Box plots by CGPA range
16. Violin plots by gender

### Clustering & Models (6)
17-19. Cluster scatter plots (CGPA vs Anxiety/Stress/Depression)
20. Cluster size distribution
21. Cluster characteristics heatmap
22. Model performance comparison
23-28. Confusion matrices & feature importance (3 models)

All visualizations saved in `outputs/visualizations/` at 300 DPI.

---

## 🧠 Machine Learning Pipeline

### 1. Data Preprocessing
- Handle missing values (median for numeric, mode for categorical)
- Convert age/CGPA ranges to averages
- Encode categorical variables (Gender, Scholarship, Academic Year)
- Feature scaling using StandardScaler

### 2. Feature Engineering
Selected features for modeling:
- Age
- Gender (0=Male, 1=Female)
- Current CGPA
- Scholarship (0=No, 1=Yes)
- Academic Year (1-4)
- Cluster (from K-Means)

### 3. Clustering
- **Algorithm:** K-Means
- **Number of Clusters:** 4
- **Evaluation:** Silhouette Score
- **Purpose:** Identify student groups with similar characteristics

### 4. Classification
- **Algorithm:** Random Forest Classifier
- **Parameters:**
  - n_estimators=100
  - max_depth=10
  - class_weight='balanced'
  - random_state=42
- **Train/Test Split:** 80/20
- **Evaluation Metrics:** Accuracy, Precision, Recall, F1-Score

---

## 🔍 Interactive Assessment Tool

### Features
- **3 Assessment Types:** Stress, Anxiety, Depression
- **Complete Assessment:** All three combined
- **Real-time Scoring:** Immediate results
- **Personalized Recommendations:** Based on score ranges
- **Crisis Resources:** Helpline information for high-risk cases

### Scoring Ranges
| Category | Low | Medium | High |
|----------|-----|--------|------|
| Stress | 0-17 | 18-34 | 35+ |
| Anxiety | 0-17 | 18-34 | 35+ |
| Depression | 0-17 | 18-34 | 35+ |

### Usage Example
```bash
python src/5_assessment_tool.py
```
Follow the interactive prompts to complete assessments.

---

## 🌐 REST API

### Start API Server
```bash
python api.py
```

Server runs at: `http://localhost:5000`

### API Quick Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Predict stress/anxiety/depression from demographics |
| `/assess` | POST | Score raw questionnaire responses |
| `/stats` | GET | Return dataset summary statistics |

### API Endpoints

#### 1. Predict Mental Health
```bash
POST /predict
```
**Request:**
```json
{
  "age": 20,
  "gender": 1,
  "cgpa": 3.5,
  "scholarship": 1,
  "academic_year": 2
}
```

**Response:**
```json
{
  "predictions": {
    "anxiety": {"level": "Low", "confidence": 0.92},
    "stress": {"level": "Low", "confidence": 0.89},
    "depression": {"level": "Low", "confidence": 0.85}
  },
  "recommendations": ["Continue maintaining healthy habits"]
}
```

#### 2. Complete Assessment
```bash
POST /assess
```
**Request:**
```json
{
  "anxiety_responses": [2, 3, 1, 2, 3, 2, 1],
  "stress_responses": [2, 2, 3, 2, 1, 3, 2, 1, 2, 3],
  "depression_responses": [1, 2, 1, 2, 3, 2, 1, 0, 0]
}
```

#### 3. Get Statistics
```bash
GET /stats
```

### Test API
```bash
python test_api.py
```

See `API_DOCUMENTATION.md` for complete API reference.

---

## 📚 Literature Review

This project is based on 10 research papers covering:
- AI in education and student well-being
- Machine learning for mental health prediction
- Stress indicators in academic settings
- Big data applications in education

See `docs/literature_review.md` for detailed summaries.

---

## ⚠️ Disclaimer

**IMPORTANT:** This tool is for **educational and informational purposes only**. It does NOT provide clinical diagnosis and should not replace professional medical advice.

If you're experiencing mental health difficulties:
- **National Suicide Prevention Lifeline:** 988
- **Crisis Text Line:** Text HOME to 741741
- **Campus Counseling Center:** Contact your university
- **Emergency:** Call 911

---

## 🔬 Methodology

### Research Design
- **Type:** Quantitative analysis using survey data
- **Sample Size:** 500 students
- **Data Collection:** Structured questionnaire
- **Analysis:** Descriptive statistics, correlation, clustering, classification

### Limitations
1. **Self-reported data:** Potential response bias
2. **Synthetic dataset:** Generated for research purposes
3. **Cross-sectional:** No longitudinal tracking
4. **Generalizability:** Limited to university students
5. **Sample size:** 500 may not represent all demographics

### Future Work
- Collect real survey data from multiple universities
- Implement deep learning models (LSTM, Transformers)
- Add temporal analysis (track changes over semesters)
- Develop web application for wider accessibility
- Include additional factors (sleep, exercise, social support)
- Multi-language support for international students

---

## 🤝 Contributing

This is an academic project. For questions or suggestions:
- **Email:** sakhipatel20@gmail.com
- **GitHub:** github.com/sakhi20
- **LinkedIn:** linkedin.com/in/sakhipatel20

---

## 📄 License

This project is created for academic purposes at North Carolina State University.

---

## 🙏 Acknowledgments

- **Institution:** North Carolina State University
- **Original Research:** Pandit Deendayal Energy University team
- **Inspiration:** 10 research papers on student mental health
- **Tools:** Python, scikit-learn, pandas, matplotlib, seaborn

---

## 📞 Contact

**Sakhi Patel**  
Master's Student - Data Science  
North Carolina State University  
Email: sakhipatel20@gmail.com  
GitHub: github.com/sakhi20  
LinkedIn: linkedin.com/in/sakhipatel20

---

## 📊 Project Statistics

- **Lines of Code:** ~2,000+
- **Visualizations:** 22+
- **Models Trained:** 3
- **Dataset Size:** 500 rows × 39 columns
- **Accuracy:** 81-85%

---

**Last Updated:** December 2024  
**Version:** 1.0.0  
**Status:** Complete ✓

---

*This project demonstrates advanced skills in Big Data Analysis, Machine Learning, Data Visualization, and Python Programming suitable for a Master's level Data Science portfolio.*
