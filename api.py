"""
REST API for Student Mental Health Prediction
Author: Sakhi Patel
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load models
MODELS = {
    'anxiety': joblib.load('outputs/models/anxiety_prediction_model.pkl'),
    'stress': joblib.load('outputs/models/stress_prediction_model.pkl'),
    'depression': joblib.load('outputs/models/depression_prediction_model.pkl')
}

# Load data for statistics
df = pd.read_csv('outputs/clustered_data.csv')


@app.route('/')
def home():
    """API home endpoint"""
    return jsonify({
        'message': 'Student Mental Health Prediction API',
        'version': '1.0.0',
        'author': 'Sakhi Patel',
        'endpoints': {
            '/predict': 'POST - Predict mental health levels',
            '/assess': 'POST - Complete assessment with scores',
            '/stats': 'GET - Get dataset statistics',
            '/health': 'GET - API health check'
        }
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'models_loaded': len(MODELS)})


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict mental health levels
    
    Request body:
    {
        "age": 20,
        "gender": 0,  # 0=Male, 1=Female
        "cgpa": 3.5,
        "scholarship": 1,  # 0=No, 1=Yes
        "academic_year": 2,  # 1-4
        "cluster": 1  # Optional, will be estimated if not provided
    }
    """
    try:
        data = request.json
        
        # Validate input
        required = ['age', 'gender', 'cgpa', 'scholarship', 'academic_year']
        if not all(k in data for k in required):
            return jsonify({'error': f'Missing required fields: {required}'}), 400
        
        # Estimate cluster if not provided
        if 'cluster' not in data:
            data['cluster'] = estimate_cluster(data['cgpa'])
        
        # Prepare features
        features = pd.DataFrame([{
            'Age': data['age'],
            'Gender': data['gender'],
            'Current CGPA': data['cgpa'],
            'Scholarship': data['scholarship'],
            'Academic Year': data['academic_year'],
            'Cluster': data['cluster']
        }])
        
        # Make predictions
        predictions = {}
        for name, model in MODELS.items():
            pred = model.predict(features)[0]
            proba = model.predict_proba(features)[0]
            
            label_map = {0: 'Low', 1: 'Medium', 2: 'High'}
            predictions[name] = {
                'level': label_map.get(pred, 'Low'),
                'confidence': float(max(proba)),
                'probabilities': {
                    'Low': float(proba[0]) if len(proba) > 0 else 0,
                    'Medium': float(proba[1]) if len(proba) > 1 else 0,
                    'High': float(proba[2]) if len(proba) > 2 else 0
                }
            }
        
        # Generate recommendations
        recommendations = generate_recommendations(predictions)
        
        return jsonify({
            'predictions': predictions,
            'recommendations': recommendations,
            'input': data
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/assess', methods=['POST'])
def assess():
    """
    Complete mental health assessment from questionnaire responses
    
    Request body:
    {
        "anxiety_responses": [2, 3, 1, 2, 3, 2, 1],  # 7 questions, 0-4 scale
        "stress_responses": [2, 2, 3, 2, 1, 3, 2, 1, 2, 3],  # 10 questions
        "depression_responses": [1, 2, 1, 2, 3, 2, 1, 0, 0]  # 9 questions
    }
    """
    try:
        data = request.json
        
        results = {}
        
        # Anxiety assessment
        if 'anxiety_responses' in data:
            anxiety_score = sum(data['anxiety_responses'])
            results['anxiety'] = {
                'score': anxiety_score,
                'max_score': 28,
                'level': get_level(anxiety_score, 18, 35),
                'interpretation': get_interpretation('anxiety', anxiety_score)
            }
        
        # Stress assessment
        if 'stress_responses' in data:
            stress_score = sum(data['stress_responses'])
            results['stress'] = {
                'score': stress_score,
                'max_score': 40,
                'level': get_level(stress_score, 18, 35),
                'interpretation': get_interpretation('stress', stress_score)
            }
        
        # Depression assessment
        if 'depression_responses' in data:
            depression_score = sum(data['depression_responses'])
            results['depression'] = {
                'score': depression_score,
                'max_score': 36,
                'level': get_level(depression_score, 18, 35),
                'interpretation': get_interpretation('depression', depression_score)
            }
            
            # Check for suicidal thoughts
            if len(data['depression_responses']) >= 9 and data['depression_responses'][8] >= 2:
                results['crisis_alert'] = True
                results['crisis_resources'] = get_crisis_resources()
        
        # Overall recommendations
        results['recommendations'] = generate_assessment_recommendations(results)
        
        return jsonify(results)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/stats')
def stats():
    """Get dataset statistics"""
    try:
        statistics = {
            'total_students': len(df),
            'cgpa': {
                'mean': float(df['Current CGPA'].mean()),
                'std': float(df['Current CGPA'].std()),
                'min': float(df['Current CGPA'].min()),
                'max': float(df['Current CGPA'].max())
            },
            'mental_health': {
                'anxiety': {
                    'mean': float(df['Anxiety Value'].mean()),
                    'distribution': df['Anxiety Label'].value_counts().to_dict()
                },
                'stress': {
                    'mean': float(df['Stress Value'].mean()),
                    'distribution': df['Stress Label'].value_counts().to_dict()
                },
                'depression': {
                    'mean': float(df['Depression Value'].mean()),
                    'distribution': df['Depression Label'].value_counts().to_dict()
                }
            },
            'correlations': {
                'cgpa_anxiety': float(df[['Current CGPA', 'Anxiety Value']].corr().iloc[0, 1]),
                'cgpa_stress': float(df[['Current CGPA', 'Stress Value']].corr().iloc[0, 1]),
                'cgpa_depression': float(df[['Current CGPA', 'Depression Value']].corr().iloc[0, 1])
            },
            'clusters': df['Cluster'].value_counts().to_dict()
        }
        
        return jsonify(statistics)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Helper functions
def estimate_cluster(cgpa):
    """Estimate cluster based on CGPA"""
    if cgpa < 2.7:
        return 0  # High risk
    elif cgpa >= 3.3:
        return 1  # Low risk
    else:
        return 2  # Medium risk


def get_level(score, medium_threshold, high_threshold):
    """Determine level based on score"""
    if score < medium_threshold:
        return 'Low'
    elif score < high_threshold:
        return 'Medium'
    else:
        return 'High'


def get_interpretation(category, score):
    """Get interpretation for score"""
    level = get_level(score, 18, 35)
    
    interpretations = {
        'anxiety': {
            'Low': 'You appear to have minimal anxiety related to academics.',
            'Medium': 'You are experiencing moderate levels of academic anxiety.',
            'High': 'You are experiencing high levels of academic anxiety.'
        },
        'stress': {
            'Low': 'You appear to be managing academic stress well.',
            'Medium': 'You are experiencing moderate levels of academic stress.',
            'High': 'You are experiencing high levels of academic stress.'
        },
        'depression': {
            'Low': 'You appear to have minimal depressive symptoms.',
            'Medium': 'You are experiencing moderate depressive symptoms.',
            'High': 'You are experiencing significant depressive symptoms.'
        }
    }
    
    return interpretations.get(category, {}).get(level, '')


def generate_recommendations(predictions):
    """Generate recommendations based on predictions"""
    recommendations = []
    
    for category, pred in predictions.items():
        if pred['level'] == 'High':
            recommendations.append(f"Seek professional help for {category}")
        elif pred['level'] == 'Medium':
            recommendations.append(f"Consider stress management techniques for {category}")
    
    if not recommendations:
        recommendations.append("Continue maintaining healthy habits")
    
    return recommendations


def generate_assessment_recommendations(results):
    """Generate recommendations from assessment"""
    recommendations = []
    
    for category in ['anxiety', 'stress', 'depression']:
        if category in results:
            level = results[category]['level']
            if level == 'High':
                recommendations.append(f"Seek professional counseling for {category}")
            elif level == 'Medium':
                recommendations.append(f"Practice self-care and stress management for {category}")
    
    if not recommendations:
        recommendations.append("Keep up the good work maintaining your mental health")
    
    return recommendations


def get_crisis_resources():
    """Get crisis resources"""
    return {
        'suicide_prevention_lifeline': '988',
        'crisis_text_line': 'Text HOME to 741741',
        'emergency': '911',
        'message': 'Please reach out for help immediately'
    }


if __name__ == '__main__':
    print("\n" + "="*60)
    print("Student Mental Health Prediction API")
    print("="*60)
    print("\nAPI Endpoints:")
    print("  GET  /           - API information")
    print("  GET  /health     - Health check")
    print("  POST /predict    - Predict mental health levels")
    print("  POST /assess     - Complete assessment")
    print("  GET  /stats      - Dataset statistics")
    print("\nStarting server on http://localhost:5000")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
