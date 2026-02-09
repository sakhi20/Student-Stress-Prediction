"""
API Test Script
Test all endpoints of the Mental Health Prediction API
"""

import requests
import json

BASE_URL = 'http://localhost:5000'

def test_home():
    """Test home endpoint"""
    print("\n" + "="*60)
    print("TEST 1: Home Endpoint")
    print("="*60)
    response = requests.get(f'{BASE_URL}/')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_health():
    """Test health endpoint"""
    print("\n" + "="*60)
    print("TEST 2: Health Check")
    print("="*60)
    response = requests.get(f'{BASE_URL}/health')
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))

def test_predict():
    """Test predict endpoint"""
    print("\n" + "="*60)
    print("TEST 3: Predict Mental Health")
    print("="*60)
    
    # Test case 1: High CGPA student (low risk)
    print("\nCase 1: High CGPA Student (3.8)")
    data = {
        'age': 20,
        'gender': 1,
        'cgpa': 3.8,
        'scholarship': 1,
        'academic_year': 2
    }
    response = requests.post(f'{BASE_URL}/predict', json=data)
    print(f"Status: {response.status_code}")
    result = response.json()
    print(f"Anxiety: {result['predictions']['anxiety']['level']}")
    print(f"Stress: {result['predictions']['stress']['level']}")
    print(f"Depression: {result['predictions']['depression']['level']}")
    
    # Test case 2: Low CGPA student (high risk)
    print("\nCase 2: Low CGPA Student (2.3)")
    data['cgpa'] = 2.3
    response = requests.post(f'{BASE_URL}/predict', json=data)
    result = response.json()
    print(f"Anxiety: {result['predictions']['anxiety']['level']}")
    print(f"Stress: {result['predictions']['stress']['level']}")
    print(f"Depression: {result['predictions']['depression']['level']}")

def test_assess():
    """Test assess endpoint"""
    print("\n" + "="*60)
    print("TEST 4: Complete Assessment")
    print("="*60)
    
    data = {
        'anxiety_responses': [2, 3, 1, 2, 3, 2, 1],
        'stress_responses': [2, 2, 3, 2, 1, 3, 2, 1, 2, 3],
        'depression_responses': [1, 2, 1, 2, 3, 2, 1, 0, 0]
    }
    
    response = requests.post(f'{BASE_URL}/assess', json=data)
    print(f"Status: {response.status_code}")
    result = response.json()
    
    if 'anxiety' in result:
        print(f"\nAnxiety Score: {result['anxiety']['score']}/{result['anxiety']['max_score']}")
        print(f"Level: {result['anxiety']['level']}")
    
    if 'stress' in result:
        print(f"\nStress Score: {result['stress']['score']}/{result['stress']['max_score']}")
        print(f"Level: {result['stress']['level']}")
    
    if 'depression' in result:
        print(f"\nDepression Score: {result['depression']['score']}/{result['depression']['max_score']}")
        print(f"Level: {result['depression']['level']}")

def test_stats():
    """Test stats endpoint"""
    print("\n" + "="*60)
    print("TEST 5: Dataset Statistics")
    print("="*60)
    response = requests.get(f'{BASE_URL}/stats')
    print(f"Status: {response.status_code}")
    result = response.json()
    
    print(f"\nTotal Students: {result['total_students']}")
    print(f"Mean CGPA: {result['cgpa']['mean']:.2f}")
    print(f"\nCorrelations:")
    print(f"  CGPA vs Anxiety: {result['correlations']['cgpa_anxiety']:.3f}")
    print(f"  CGPA vs Stress: {result['correlations']['cgpa_stress']:.3f}")
    print(f"  CGPA vs Depression: {result['correlations']['cgpa_depression']:.3f}")

def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("MENTAL HEALTH PREDICTION API - TEST SUITE")
    print("="*60)
    print("\nMake sure the API is running: python api.py")
    input("Press Enter to start tests...")
    
    try:
        test_home()
        test_health()
        test_predict()
        test_assess()
        test_stats()
        
        print("\n" + "="*60)
        print("✓ ALL TESTS COMPLETED")
        print("="*60 + "\n")
        
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to API")
        print("Make sure the API is running: python api.py\n")
    except Exception as e:
        print(f"\n❌ ERROR: {e}\n")

if __name__ == '__main__':
    main()
