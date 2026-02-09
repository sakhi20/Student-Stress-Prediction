# REST API Quick Start

## ✅ API Successfully Created!

Your Mental Health Prediction system now has a **REST API** that can be integrated into web apps, mobile apps, or other services.

---

## 🚀 Start the API

### Terminal 1: Start Server
```bash
cd "/Users/sakhipatel/Desktop/masters/own/Stress Prediction"
python api.py
```

You'll see:
```
Student Mental Health Prediction API
====================================
API Endpoints:
  GET  /           - API information
  GET  /health     - Health check
  POST /predict    - Predict mental health levels
  POST /assess     - Complete assessment
  GET  /stats      - Dataset statistics

Starting server on http://localhost:5000
```

---

## 🧪 Test the API

### Terminal 2: Run Tests
```bash
python test_api.py
```

This will test all 5 endpoints automatically.

---

## 📡 API Endpoints

### 1. **GET /** - API Info
```bash
curl http://localhost:5000/
```

### 2. **GET /health** - Health Check
```bash
curl http://localhost:5000/health
```

### 3. **POST /predict** - Predict Mental Health
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 20,
    "gender": 1,
    "cgpa": 3.5,
    "scholarship": 1,
    "academic_year": 2
  }'
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

### 4. **POST /assess** - Complete Assessment
```bash
curl -X POST http://localhost:5000/assess \
  -H "Content-Type: application/json" \
  -d '{
    "anxiety_responses": [2, 3, 1, 2, 3, 2, 1],
    "stress_responses": [2, 2, 3, 2, 1, 3, 2, 1, 2, 3],
    "depression_responses": [1, 2, 1, 2, 3, 2, 1, 0, 0]
  }'
```

### 5. **GET /stats** - Dataset Statistics
```bash
curl http://localhost:5000/stats
```

---

## 🐍 Python Example

```python
import requests

# Predict mental health
response = requests.post('http://localhost:5000/predict', json={
    'age': 20,
    'gender': 1,
    'cgpa': 3.2,
    'scholarship': 0,
    'academic_year': 2
})

result = response.json()
print(f"Anxiety: {result['predictions']['anxiety']['level']}")
print(f"Stress: {result['predictions']['stress']['level']}")
print(f"Depression: {result['predictions']['depression']['level']}")
```

---

## 🌐 JavaScript Example

```javascript
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
.then(data => {
  console.log('Anxiety:', data.predictions.anxiety.level);
  console.log('Stress:', data.predictions.stress.level);
  console.log('Depression:', data.predictions.depression.level);
});
```

---

## 📊 What the API Does

### Predict Endpoint
- Takes student data (age, gender, CGPA, etc.)
- Uses trained Random Forest models (88-92% accuracy)
- Returns predictions for anxiety, stress, and depression
- Provides confidence scores and recommendations

### Assess Endpoint
- Takes questionnaire responses (0-4 scale)
- Calculates total scores
- Classifies into Low/Medium/High
- Provides interpretations and recommendations
- Includes crisis resources if needed

### Stats Endpoint
- Returns dataset statistics
- Shows correlations
- Provides mental health distributions
- Useful for dashboards and reports

---

## 🔧 Integration Examples

### Web Application
```html
<form id="predictForm">
  <input name="age" type="number" placeholder="Age">
  <input name="cgpa" type="number" step="0.01" placeholder="CGPA">
  <button type="submit">Predict</button>
</form>

<script>
document.getElementById('predictForm').onsubmit = async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData);
  
  const response = await fetch('http://localhost:5000/predict', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data)
  });
  
  const result = await response.json();
  console.log(result);
};
</script>
```

### Mobile App (React Native)
```javascript
const predictMentalHealth = async (studentData) => {
  try {
    const response = await fetch('http://localhost:5000/predict', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(studentData)
    });
    return await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
};
```

---

## 📝 API Features

✅ **5 RESTful Endpoints**  
✅ **JSON Request/Response**  
✅ **CORS Enabled** (works with web apps)  
✅ **Error Handling**  
✅ **Input Validation**  
✅ **Crisis Detection** (for high-risk assessments)  
✅ **Confidence Scores**  
✅ **Recommendations**  

---

## 🎯 Use Cases

1. **University Portal Integration**
   - Add mental health screening to student portals
   - Automated risk assessment during registration

2. **Mobile Health App**
   - Self-assessment feature
   - Track mental health over time

3. **Counseling Dashboard**
   - Visualize at-risk students
   - Prioritize interventions

4. **Research Platform**
   - Collect and analyze data
   - Generate reports

---

## 📚 Documentation

- **Full API Docs:** `API_DOCUMENTATION.md`
- **Test Suite:** `test_api.py`
- **Source Code:** `api.py`

---

## 🚀 Deployment Options

### Local Development
```bash
python api.py
```

### Production (Gunicorn)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 api:app
```

### Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "api.py"]
```

### Cloud Platforms
- **Heroku:** `git push heroku main`
- **AWS Lambda:** Use Zappa or Serverless
- **Google Cloud Run:** Deploy container
- **Azure App Service:** Deploy Python app

---

## ✅ What's Included

- ✓ Complete REST API (`api.py`)
- ✓ API Documentation (`API_DOCUMENTATION.md`)
- ✓ Test Suite (`test_api.py`)
- ✓ CORS enabled for web apps
- ✓ Error handling and validation
- ✓ Crisis resource detection
- ✓ Updated README with API section
- ✓ Pushed to GitHub

---

## 🎉 Your API is Ready!

**GitHub:** https://github.com/sakhi20/Student-Stress-Prediction  
**Local:** http://localhost:5000

Start the server and test it now! 🚀
