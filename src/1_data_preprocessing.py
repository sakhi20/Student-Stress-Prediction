"""
Data Preprocessing Pipeline
Author: Sakhi Patel
"""

import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import convert_age, convert_cgpa, encode_categorical_variables, handle_missing_values


def run():
    """Execute data preprocessing pipeline"""
    
    print("\n" + "="*60)
    print("STEP 1: DATA PREPROCESSING")
    print("="*60)
    
    # Load data
    print("\n[1.1] Loading dataset...")
    df = pd.read_csv('data/student_mental_health_survey.csv')
    print(f"  ✓ Loaded {len(df)} records with {len(df.columns)} columns")
    
    # Display basic info
    print("\n[1.2] Dataset Information:")
    print(f"  Shape: {df.shape}")
    print(f"  Missing values: {df.isna().sum().sum()}")
    print(f"\n  Data types:\n{df.dtypes.value_counts()}")
    
    # Convert Age
    print("\n[1.3] Converting Age column...")
    df['Age'] = df['Age'].apply(convert_age)
    print(f"  ✓ Age range: {df['Age'].min():.1f} - {df['Age'].max():.1f}")
    
    # Convert CGPA
    print("\n[1.4] Converting CGPA column...")
    df['Current CGPA'] = df['Current CGPA'].apply(convert_cgpa)
    print(f"  ✓ CGPA range: {df['Current CGPA'].min():.2f} - {df['Current CGPA'].max():.2f}")
    
    # Encode categorical variables
    print("\n[1.5] Encoding categorical variables...")
    df = encode_categorical_variables(df)
    print("  ✓ Encoded: Gender, Scholarship, Academic Year")
    
    # Handle missing values
    print("\n[1.6] Handling missing values...")
    missing_before = df.isna().sum().sum()
    df = handle_missing_values(df)
    missing_after = df.isna().sum().sum()
    print(f"  ✓ Missing values: {missing_before} → {missing_after}")
    
    # Save cleaned data
    print("\n[1.7] Saving cleaned data...")
    os.makedirs('outputs', exist_ok=True)
    df.to_csv('outputs/cleaned_data.csv', index=False)
    print("  ✓ Saved to: outputs/cleaned_data.csv")
    
    # Summary statistics
    print("\n[1.8] Summary Statistics:")
    print("\n" + "="*60)
    print("NUMERIC FEATURES")
    print("="*60)
    numeric_cols = ['Age', 'Current CGPA', 'Anxiety Value', 'Stress Value', 'Depression Value']
    print(df[numeric_cols].describe().round(2))
    
    print("\n" + "="*60)
    print("CATEGORICAL DISTRIBUTIONS")
    print("="*60)
    print(f"\nGender: {df['Gender'].value_counts().to_dict()}")
    print(f"Academic Year: {df['Academic Year'].value_counts().sort_index().to_dict()}")
    print(f"Scholarship: {df['Scholarship'].value_counts().to_dict()}")
    print(f"\nAnxiety Labels: {df['Anxiety Label'].value_counts().to_dict()}")
    print(f"Stress Labels: {df['Stress Label'].value_counts().to_dict()}")
    print(f"Depression Labels: {df['Depression Label'].value_counts().to_dict()}")
    
    print("\n[1.9] First 10 rows of cleaned data:")
    print(df[['Age', 'Gender', 'Current CGPA', 'Scholarship', 'Academic Year', 
              'Anxiety Value', 'Stress Value', 'Depression Value']].head(10))
    
    print("\n" + "="*60)
    print("✓ PREPROCESSING COMPLETE")
    print("="*60)
    
    return df


if __name__ == '__main__':
    run()
