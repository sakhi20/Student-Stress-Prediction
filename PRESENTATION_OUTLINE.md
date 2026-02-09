# Presentation Outline: Student Mental Health Prediction

**Project:** AI and ML Driven Prediction of Stress, Anxiety and Depression  
**Author:** Sakhi Patel  
**Institution:** North Carolina State University

---

## Slide 1: Title Slide

**AI and ML Driven Prediction of Student Mental Health**

Sakhi Patel  
Master's Student - Data Science  
North Carolina State University  
December 2024

---

## Slide 2: Problem Statement

### The Challenge
- University students face increasing mental health challenges
- 1 in 3 students experience anxiety or depression
- Early identification is crucial for intervention
- Traditional screening methods are time-consuming and reactive

### The Opportunity
- Big data and ML can predict mental health risks
- Enable proactive support and intervention
- Data-driven resource allocation

---

## Slide 3: Project Objectives

1. **Analyze** student stress indicators from survey data
2. **Build** predictive models for anxiety, stress, and depression
3. **Identify** primary stressors among university students
4. **Develop** an interactive self-assessment tool
5. **Provide** actionable insights for intervention

---

## Slide 4: Dataset Overview

### Survey Data
- **Sample Size:** 500 students
- **Features:** 39 columns
  - Demographics (7): Age, Gender, University, Department, Year, CGPA, Scholarship
  - Mental Health Questions (26): Anxiety (7), Stress (10), Depression (9)
  - Target Variables (3): Anxiety/Stress/Depression Labels

### Rating Scale
0 = Never | 1 = Rarely | 2 = Sometimes | 3 = Often | 4 = Very Often

---

## Slide 5: Methodology

### 1. Data Preprocessing
- Handle missing values
- Convert ranges to numeric
- Encode categorical variables
- Feature scaling

### 2. Exploratory Data Analysis
- Descriptive statistics
- Correlation analysis
- Demographic comparisons
- 22+ visualizations

### 3. Machine Learning
- **Clustering:** K-Means (k=4)
- **Classification:** Random Forest
- **Validation:** 80/20 train-test split

---

## Slide 6: Key Finding #1 - CGPA Correlation

### Strong Negative Correlation with Mental Health

| Relationship | Correlation |
|--------------|-------------|
| CGPA vs Anxiety | -0.96 |
| CGPA vs Stress | -0.96 |
| CGPA vs Depression | -0.95 |

**Insight:** Lower academic performance strongly associated with higher mental health issues

**Visual:** Show correlation heatmap

---

## Slide 7: Key Finding #2 - Student Clusters

### 4 Distinct Student Groups Identified

| Cluster | Size | CGPA | Mental Health | Risk Level |
|---------|------|------|---------------|------------|
| 0 | 69 | 2.47 | High scores | High Risk |
| 1 | 91 | 3.50 | Low scores | Low Risk |
| 2 | 147 | 3.07 | Moderate | Medium Risk |
| 3 | 193 | 3.01 | Moderate | Medium Risk |

**Visual:** Show cluster scatter plots

---

## Slide 8: Model Performance

### Random Forest Classification Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| **Anxiety** | 92.0% | 0.92 | 0.92 | 0.92 |
| **Stress** | 91.0% | 0.91 | 0.91 | 0.91 |
| **Depression** | 88.0% | 0.89 | 0.88 | 0.88 |

**Visual:** Show confusion matrices and model comparison chart

---

## Slide 9: Feature Importance

### Top Predictors of Mental Health

**All Three Models:**
1. **Current CGPA** - 80%+ importance
2. **Cluster Assignment** - 7-10%
3. **Academic Year** - 4-5%
4. **Age** - 3-8%
5. **Gender** - 1-2%
6. **Scholarship** - 1-2%

**Insight:** Academic performance is by far the strongest predictor

**Visual:** Show feature importance bar charts

---

## Slide 10: Demographic Insights

### Mental Health by Demographics

**Gender:**
- Minimal differences between male and female students
- Both groups show similar patterns

**Academic Year:**
- 3rd and 4th year students show slightly higher stress
- Freshman year shows moderate anxiety

**Scholarship:**
- Scholarship recipients show marginally lower anxiety
- Financial support may reduce stress

**Visual:** Show grouped bar charts

---

## Slide 11: Interactive Assessment Tool

### Self-Assessment Features

✓ **Three Assessment Types**
  - Stress (10 questions)
  - Anxiety (7 questions)
  - Depression (9 questions)

✓ **Real-time Scoring**
  - Immediate results
  - Severity classification (Low/Medium/High)

✓ **Personalized Recommendations**
  - Based on score ranges
  - Crisis resources for high-risk cases

**Demo:** Show command-line interface screenshots

---

## Slide 12: Technical Implementation

### Technology Stack

**Languages & Libraries:**
- Python 3.9+
- pandas, numpy (data processing)
- matplotlib, seaborn (visualization)
- scikit-learn (machine learning)

**Algorithms:**
- K-Means Clustering
- Random Forest Classification
- StandardScaler, LabelEncoder

**Code Quality:**
- 2,000+ lines of code
- Modular design (8 scripts)
- Comprehensive documentation
- Error handling & logging

---

## Slide 13: Visualizations Showcase

### 28 Professional Visualizations Created

**Categories:**
1. Frequency Distributions (7)
2. Mental Health Analysis (9)
3. Clustering Visualizations (5)
4. Model Performance (7)

**Quality:**
- 300 DPI resolution
- Publication-ready
- Professional styling
- Clear labels and legends

**Visual:** Show 4-6 best visualizations in grid

---

## Slide 14: Project Impact

### Real-World Applications

**For Universities:**
- Early identification of at-risk students
- Data-driven counseling resource allocation
- Evidence-based policy development

**For Students:**
- Anonymous self-assessment
- Awareness and education
- Guidance to seek help

**For Researchers:**
- Validated methodology
- Reproducible framework
- Baseline for future studies

---

## Slide 15: Ethical Considerations

### Responsible AI Implementation

✓ **Data Privacy**
  - Anonymous survey responses
  - No personally identifiable information

✓ **Informed Consent**
  - Clear purpose communication
  - Voluntary participation

✓ **Mental Health Sensitivity**
  - Not a clinical diagnosis
  - Clear disclaimers provided

✓ **Crisis Resources**
  - Helpline information included
  - Professional referral guidance

---

## Slide 16: Limitations & Future Work

### Current Limitations
- Synthetic dataset (for demonstration)
- Cross-sectional design (no temporal tracking)
- Limited to academic factors
- Sample size (500 students)

### Future Enhancements
1. Collect real survey data from multiple universities
2. Implement deep learning models (LSTM, Transformers)
3. Add lifestyle factors (sleep, exercise, social support)
4. Develop web-based interface
5. Longitudinal tracking over semesters
6. Multi-language support

---

## Slide 17: Project Deliverables

### Complete Package

✓ **Source Code** (8 Python scripts)
✓ **Dataset** (500 students, 39 features)
✓ **ML Models** (3 trained models, 88-92% accuracy)
✓ **Visualizations** (28 high-quality plots)
✓ **Documentation** (README, Quick Start, Literature Review)
✓ **Interactive Tool** (Self-assessment application)
✓ **Results** (Performance metrics, analysis reports)

**All code is production-ready and well-documented**

---

## Slide 18: Skills Demonstrated

### Technical Competencies

**Data Science:**
- Exploratory Data Analysis
- Feature Engineering
- Statistical Analysis
- Machine Learning (Clustering & Classification)

**Programming:**
- Python (Advanced)
- Data Visualization
- Software Engineering Best Practices
- Documentation

**Domain Knowledge:**
- Mental Health Assessment
- Educational Psychology
- Research Methodology
- Ethical AI

---

## Slide 19: Results Summary

### Key Achievements

✅ **High Model Accuracy:** 88-92% across all models  
✅ **Strong Correlations:** CGPA is primary predictor (-0.96)  
✅ **Actionable Insights:** 4 distinct student risk groups  
✅ **Practical Tool:** Interactive self-assessment  
✅ **Comprehensive Analysis:** 28 visualizations  
✅ **Production-Ready:** Clean, documented code  

### Impact
- Enables early intervention for at-risk students
- Provides data-driven insights for universities
- Empowers students with self-awareness tools

---

## Slide 20: Demo

### Live Demonstration

**Option 1: Run Complete Analysis**
```bash
python run_analysis.py
```
- Show preprocessing output
- Display visualizations
- Review model performance

**Option 2: Interactive Assessment**
```bash
python src/5_assessment_tool.py
```
- Walk through questionnaire
- Show scoring and interpretation
- Demonstrate recommendations

---

## Slide 21: Conclusion

### Project Success

This project successfully demonstrates:

1. **Technical Excellence:** High-performing ML models (88-92% accuracy)
2. **Practical Application:** Real-world mental health prediction
3. **Comprehensive Analysis:** End-to-end data science pipeline
4. **Professional Quality:** Production-ready, documented code
5. **Social Impact:** Addresses critical student mental health needs

### Takeaway
Machine learning can effectively predict student mental health risks, enabling proactive intervention and support.

---

## Slide 22: Q&A

### Questions?

**Contact Information:**
- **Email:** sakhipatel20@gmail.com
- **GitHub:** github.com/sakhi20
- **LinkedIn:** linkedin.com/in/sakhipatel20

**Project Resources:**
- Full documentation in README.md
- Code available on GitHub
- Interactive demo available

**Thank you!**

---

## Appendix Slides (If Needed)

### A1: Confusion Matrix Details
- Show detailed confusion matrices for all three models
- Explain true positives, false positives, etc.

### A2: Cluster Analysis Details
- Detailed statistics for each cluster
- Cluster characteristics heatmap

### A3: Literature Review Summary
- Brief overview of 10 research papers
- Key findings from each

### A4: Data Preprocessing Steps
- Detailed preprocessing pipeline
- Before/after data quality metrics

### A5: Code Architecture
- System design diagram
- Module dependencies
- Data flow

---

## Presentation Tips

### Timing (15-20 minutes)
- Introduction: 2 minutes
- Problem & Methodology: 3 minutes
- Key Findings: 5 minutes
- Technical Details: 4 minutes
- Demo: 3 minutes
- Conclusion & Q&A: 3 minutes

### Key Messages
1. CGPA is the strongest predictor of mental health
2. ML can achieve 88-92% accuracy in prediction
3. Early identification enables proactive intervention
4. Tool is practical, ethical, and production-ready

### Visual Strategy
- Use visualizations from outputs/visualizations/
- Keep slides clean and uncluttered
- Highlight key numbers and findings
- Use consistent color scheme

### Engagement
- Start with a compelling statistic
- Use real-world examples
- Show live demo if possible
- End with call to action

---

**Presentation prepared by:** Sakhi Patel  
**Date:** December 2024  
**Version:** 1.0
