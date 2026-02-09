# Mental Health Prediction API Documentation

## Overview
REST API for predicting student mental health levels (anxiety, stress, depression) using trained ML models.

**Base URL:** `http://localhost:5000`

---

## Endpoints

### 1. GET `/`
**Description:** API information and available endpoints

**Response:**
```json
{
  "message": "Student Mental Health Prediction API",
  "version": "1.0.0",
  "endpoints": {...}
}
```

---

### 2. GET `/health`
**Description:** Health check

**Response:**
```json
{
  "status": "healthy",
  "models_loaded": 3
}
```

---

### 3. POST `/predict`
**Description:** Predict mental health levels from student data

**Request Body:**
```json
{
  "age": 20,
  "gender": 0,
  "cgpa": 3.5,
  "scholarship": 1,
  "academic_year": 2,
  "cluster": 1
}
```

**Parameters:**
- `age` (number): Student age (18-25)
- `gender` (number): 0=Male, 1=Female
- `cgpa` (number): Current CGPA (2.0-4.0)
- `scholarship` (number): 0=No, 1=Yes
- `academic_year` (number): 1-4
- `cluster` (number, optional): Cluster assignment (0-3)

**Response:**
```json
{
  "predictions": {
    "anxiety": {
      "level": "Low",
      "confidence": 0.92,
      "probabilities": {
        "Low": 0.92,
        "Medium": 0.08,
        "High": 0.00
      }
    },
    "stress": {...},
    "depression": {...}
  },
  "recommendations": [
    "Continue maintaining healthy habits"
  ],
  "input": {...}
}
```

---

### 4. POST `/assess`
**Description:** Complete mental health assessment from questionnaire

**Request Body:**
```json
{
  "anxiety_responses": [2, 3, 1, 2, 3, 2, 1],
  "stress_responses": [2, 2, 3, 2, 1, 3, 2, 1, 2, 3],
  "depression_responses": [1, 2, 1, 2, 3, 2, 1, 0, 0]
}
```

**Parameters:**
- `anxiety_responses` (array): 7 responses (0-4 scale)
- `stress_responses` (array): 10 responses (0-4 scale)
- `depression_responses` (array): 9 responses (0-4 scale)

**Response:**
```json
{
  "anxiety": {
    "score": 14,
    "max_score": 28,
    "level": "Low",
    "interpretation": "You appear to have minimal anxiety..."
  },
  "stress": {...},
  "depression": {...},
  "recommendations": [...]
}
```

---

### 5. GET `/stats`
**Description:** Get dataset statistics

**Response:**
```json
{
  "total_students": 500,
  "cgpa": {
    "mean": 3.04,
    "std": 0.57,
    "min": 2.01,
    "max": 4.05
  },
  "mental_health": {...},
  "correlations": {
    "cgpa_anxiety": -0.96,
    "cgpa_stress": -0.96,
    "cgpa_depression": -0.95
  }
}
```

---

## Usage Examples

### Python
```python
import requests

# Predict
response = requests.post('http://localhost:5000/predict', json={
    'age': 20,
    'gender': 1,
    'cgpa': 3.2,
    'scholarship': 0,
    'academic_year': 2
})
print(response.json())

# Assess
response = requests.post('http://localhost:5000/assess', json={
    'anxiety_responses': [2, 3, 1, 2, 3, 2, 1],
    'stress_responses': [2, 2, 3, 2, 1, 3, 2, 1, 2, 3],
    'depression_responses': [1, 2, 1, 2, 3, 2, 1, 0, 0]
})
print(response.json())
```

### cURL
```bash
# Predict
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"age":20,"gender":1,"cgpa":3.2,"scholarship":0,"academic_year":2}'

# Stats
curl http://localhost:5000/stats
```

### JavaScript
```javascript
// Predict
fetch('http://localhost:5000/predict', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    age: 20,
    gender: 1,
    cgpa: 3.2,
    scholarship: 0,
    academic_year: 2
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## Error Responses

**400 Bad Request:**
```json
{
  "error": "Missing required fields: ['age', 'gender', 'cgpa']"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Error message"
}
```

---

## Installation

```bash
pip install flask flask-cors
```

## Run API

```bash
python api.py
```

Server starts at: `http://localhost:5000`

---

## Notes

- All predictions use trained Random Forest models (88-92% accuracy)
- CGPA is the strongest predictor (80%+ feature importance)
- Crisis resources provided for high-risk assessments
- CORS enabled for web applications
