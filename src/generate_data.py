"""
Generate synthetic student mental health survey data
Author: Sakhi Patel
"""

import pandas as pd
import numpy as np

np.random.seed(42)

def generate_synthetic_data(n_samples=500):
    """Generate realistic synthetic survey data"""
    
    data = {}
    
    # Demographics
    data['Age'] = np.random.choice(['18-20', '19', '20', '21', '22', '21-23', '23-25'], n_samples, 
                                    p=[0.15, 0.20, 0.20, 0.20, 0.15, 0.07, 0.03])
    data['Gender'] = np.random.choice(['Male', 'Female'], n_samples, p=[0.5, 0.5])
    data['University'] = np.random.choice(['NC State University', 'Duke University', 'UNC Chapel Hill', 'Wake Forest'], 
                                          n_samples, p=[0.4, 0.25, 0.25, 0.1])
    data['Department'] = np.random.choice(['Computer Science', 'Engineering', 'Business', 'Psychology', 'Biology', 'Arts'], 
                                          n_samples, p=[0.25, 0.25, 0.15, 0.15, 0.12, 0.08])
    data['Academic Year'] = np.random.choice(['1st Year', '2nd Year', '3rd Year', '4th Year'], 
                                             n_samples, p=[0.25, 0.25, 0.25, 0.25])
    
    # CGPA - some as ranges, some as exact
    cgpa_values = []
    for _ in range(n_samples):
        if np.random.random() < 0.3:
            base = np.random.uniform(2.0, 3.8)
            cgpa_values.append(f"{base:.1f}-{base+0.5:.1f}")
        else:
            cgpa_values.append(f"{np.random.uniform(2.0, 4.0):.2f}")
    data['Current CGPA'] = cgpa_values
    
    data['Did you receive a waiver or scholarship at your university?'] = np.random.choice(['Yes', 'No'], 
                                                                                           n_samples, p=[0.3, 0.7])
    
    # Convert CGPA to numeric for correlation
    cgpa_numeric = []
    for cgpa in cgpa_values:
        if '-' in cgpa:
            parts = cgpa.split('-')
            cgpa_numeric.append((float(parts[0]) + float(parts[1])) / 2)
        else:
            cgpa_numeric.append(float(cgpa))
    cgpa_numeric = np.array(cgpa_numeric)
    
    # Anxiety questions (7 questions) - correlated with CGPA (lower CGPA = higher anxiety)
    anxiety_questions = []
    for i in range(7):
        base_anxiety = 4 - (cgpa_numeric - 2) / 2 * 4  # Inverse relationship
        noise = np.random.normal(0, 0.8, n_samples)
        scores = np.clip(base_anxiety + noise, 0, 4).astype(int)
        anxiety_questions.append(scores)
    
    data['In a semester, how often you felt nervous, anxious or on edge due to academic pressure?'] = anxiety_questions[0]
    data['In a semester, how often have you been unable to stop worrying about your academic affairs?'] = anxiety_questions[1]
    data['In a semester, how often have you had trouble relaxing due to academic pressure?'] = anxiety_questions[2]
    data['In a semester, how often have you been easily annoyed or irritated because of academic pressure?'] = anxiety_questions[3]
    data['In a semester, how often have you worried too much about academic affairs?'] = anxiety_questions[4]
    data['In a semester, how often have you been so restless due to academic pressure that it is hard to sit still?'] = anxiety_questions[5]
    data['In a semester, how often have you felt afraid, as if something awful might happen?'] = anxiety_questions[6]
    
    # Anxiety Value and Label
    anxiety_values = sum(anxiety_questions)
    data['Anxiety Value'] = anxiety_values
    data['Anxiety Label'] = ['Low' if v < 18 else 'Medium' if v < 35 else 'High' for v in anxiety_values]
    
    # Stress questions (10 questions)
    stress_questions = []
    for i in range(10):
        base_stress = 4 - (cgpa_numeric - 2) / 2 * 4
        noise = np.random.normal(0, 0.9, n_samples)
        scores = np.clip(base_stress + noise, 0, 4).astype(int)
        stress_questions.append(scores)
    
    data['In a semester, how often have you felt upset due to something that happened in your academic affairs?'] = stress_questions[0]
    data['In a semester, how often you felt as if you were unable to control important things in your academic affairs?'] = stress_questions[1]
    data['In a semester, how often you felt nervous and stressed because of academic pressure?'] = stress_questions[2]
    data['In a semester, how often you felt as if you could not cope with all the mandatory academic activities?'] = stress_questions[3]
    data['In a semester, how often you felt confident about your ability to handle your academic problems?'] = 4 - stress_questions[4]  # Reverse
    data['In a semester, how often you felt as if things in your academic life are going your way?'] = 4 - stress_questions[5]  # Reverse
    data['In a semester, how often are you able to control irritations in your academic affairs?'] = 4 - stress_questions[6]  # Reverse
    data['In a semester, how often you felt as if your academic performance was on top?'] = 4 - stress_questions[7]  # Reverse
    data['In a semester, how often you got angered due to bad performance or low grades that are beyond your control?'] = stress_questions[8]
    data['In a semester, how often you felt as if academic difficulties are piling up so high that you could not overcome them?'] = stress_questions[9]
    
    stress_values = sum(stress_questions)
    data['Stress Value'] = stress_values
    data['Stress Label'] = ['Low' if v < 18 else 'Medium' if v < 35 else 'High' for v in stress_values]
    
    # Depression questions (9 questions)
    depression_questions = []
    for i in range(9):
        base_depression = 4 - (cgpa_numeric - 2) / 2 * 4
        noise = np.random.normal(0, 1.0, n_samples)
        scores = np.clip(base_depression + noise, 0, 4).astype(int)
        depression_questions.append(scores)
    
    data['In a semester, how often have you had little interest or pleasure in doing things?'] = depression_questions[0]
    data['In a semester, how often have you been feeling down, depressed or hopeless?'] = depression_questions[1]
    data['In a semester, how often have you had trouble falling or staying asleep, or sleeping too much?'] = depression_questions[2]
    data['In a semester, how often have you been feeling tired or having little energy?'] = depression_questions[3]
    data['In a semester, how often have you had poor appetite or overeating?'] = depression_questions[4]
    data['In a semester, how often have you been feeling bad about yourself - or that you are a failure or have let yourself or your family down?'] = depression_questions[5]
    data['In a semester, how often have you been having trouble concentrating on things, such as reading books or watching television?'] = depression_questions[6]
    data['In a semester, how often have you moved or spoke too slowly for other people to notice?'] = depression_questions[7]
    data['In a semester, how often have you had thoughts that you would be better off dead, or of hurting yourself?'] = depression_questions[8]
    
    depression_values = sum(depression_questions)
    data['Depression Value'] = depression_values
    data['Depression Label'] = ['Low' if v < 18 else 'Medium' if v < 35 else 'High' for v in depression_values]
    
    df = pd.DataFrame(data)
    return df


if __name__ == '__main__':
    print("Generating synthetic student mental health survey data...")
    df = generate_synthetic_data(500)
    df.to_csv('data/student_mental_health_survey.csv', index=False)
    print(f"✓ Generated {len(df)} survey responses")
    print(f"✓ Saved to: data/student_mental_health_survey.csv")
    print(f"\nDataset shape: {df.shape}")
    print(f"Columns: {len(df.columns)}")
