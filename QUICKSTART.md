# Quick Start Guide

## Student Mental Health Prediction System

**Author:** Sakhi Patel  
**Institution:** North Carolina State University

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Complete Analysis
```bash
python run_analysis.py
```

This will:
- ✓ Generate synthetic dataset (500 students)
- ✓ Preprocess and clean data
- ✓ Create 22+ visualizations
- ✓ Perform K-Means clustering
- ✓ Train 3 Random Forest models
- ✓ Save all results

**Runtime:** ~2-3 minutes

---

## 📊 What You Get

### Outputs Created

1. **Data Files**
   - `outputs/cleaned_data.csv` - Preprocessed dataset
   - `outputs/clustered_data.csv` - Data with cluster labels

2. **Visualizations** (22+ PNG files in `outputs/visualizations/`)
   - Frequency distributions (CGPA, age, gender, etc.)
   - Mental health distributions
   - Correlation heatmaps
   - Cluster visualizations
   - Confusion matrices
   - Feature importance plots

3. **Machine Learning Models** (in `outputs/models/`)
   - `anxiety_prediction_model.pkl` (92% accuracy)
   - `stress_prediction_model.pkl` (91% accuracy)
   - `depression_prediction_model.pkl` (88% accuracy)

4. **Results**
   - `outputs/results/model_performance.txt` - Performance metrics

---

## 🧪 Try the Interactive Assessment Tool

```bash
python src/5_assessment_tool.py
```

Features:
- Self-assessment for stress, anxiety, or depression
- Real-time scoring and interpretation
- Personalized recommendations
- Crisis resources for high-risk cases

---

## 📈 Key Results

### Model Performance
| Model | Accuracy |
|-------|----------|
| Anxiety | 92% |
| Stress | 91% |
| Depression | 88% |

### Key Findings
- **Strong negative correlation** between CGPA and mental health issues
- **CGPA is the most important predictor** (80%+ feature importance)
- **4 distinct student clusters** identified
- Lower CGPA students show significantly higher stress/anxiety/depression

---

## 📁 Project Structure

```
Stress Prediction/
├── data/                           # Dataset
├── src/                            # Source code
│   ├── 1_data_preprocessing.py
│   ├── 2_exploratory_analysis.py
│   ├── 3_clustering_analysis.py
│   ├── 4_classification_models.py
│   └── 5_assessment_tool.py
├── outputs/                        # All results
│   ├── visualizations/
│   ├── models/
│   └── results/
├── docs/                           # Documentation
├── run_analysis.py                 # Main script
├── requirements.txt
└── README.md
```

---

## 🔧 Run Individual Components

### Preprocessing Only
```bash
python src/1_data_preprocessing.py
```

### Exploratory Analysis Only
```bash
python src/2_exploratory_analysis.py
```

### Clustering Only
```bash
python src/3_clustering_analysis.py
```

### Classification Only
```bash
python src/4_classification_models.py
```

---

## 📊 View Results

### Visualizations
```bash
open outputs/visualizations/
```

### Model Performance
```bash
cat outputs/results/model_performance.txt
```

### Data Files
```bash
head outputs/cleaned_data.csv
```

---

## 🎯 Use Cases

1. **Academic Research**
   - Analyze student mental health patterns
   - Identify risk factors
   - Develop intervention strategies

2. **University Administration**
   - Early identification of at-risk students
   - Resource allocation for counseling services
   - Policy development

3. **Student Self-Assessment**
   - Personal mental health check
   - Awareness and education
   - Guidance to seek help

4. **Portfolio Project**
   - Demonstrates ML skills
   - Big data analysis
   - End-to-end project development

---

## ⚠️ Important Notes

### Disclaimer
This tool is for **educational purposes only**. It does NOT provide clinical diagnosis.

### Crisis Resources
- **National Suicide Prevention Lifeline:** 988
- **Crisis Text Line:** Text HOME to 741741
- **Emergency:** 911

---

## 🐛 Troubleshooting

### Issue: Module not found
```bash
pip install -r requirements.txt
```

### Issue: Permission denied
```bash
chmod +x run_analysis.py
```

### Issue: Data file not found
The script automatically generates synthetic data if not present.

---

## 📚 Learn More

- **Full Documentation:** See `README.md`
- **Literature Review:** See `docs/literature_review.md`
- **Data Description:** See `data/data_description.txt`

---

## 📧 Contact

**Sakhi Patel**  
Email: sakhipatel20@gmail.com  
GitHub: github.com/sakhi20  
LinkedIn: linkedin.com/in/sakhipatel20

---

## ✅ Checklist

After running the project, you should have:

- [ ] 500-row synthetic dataset generated
- [ ] Cleaned and preprocessed data
- [ ] 22+ high-quality visualizations
- [ ] 3 trained ML models (92%, 91%, 88% accuracy)
- [ ] Cluster analysis with 4 groups
- [ ] Interactive assessment tool working
- [ ] All outputs in `outputs/` directory

---

**Ready to showcase this project?**

✓ Add to GitHub portfolio  
✓ Include in resume  
✓ Present in interviews  
✓ Use for academic submissions

---

*Last Updated: December 2024*  
*Version: 1.0.0*
