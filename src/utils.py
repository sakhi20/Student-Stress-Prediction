"""
Utility functions for data preprocessing and analysis
Author: Sakhi Patel
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt


def convert_age(age_str):
    """Convert age string to numeric value"""
    if pd.isna(age_str):
        return np.nan
    age_str = str(age_str).strip()
    if '-' in age_str:
        parts = age_str.split('-')
        return (float(parts[0]) + float(parts[1])) / 2
    return float(age_str)


def convert_cgpa(cgpa_str):
    """Convert CGPA string to numeric value"""
    if pd.isna(cgpa_str):
        return np.nan
    cgpa_str = str(cgpa_str).strip()
    if '-' in cgpa_str:
        parts = cgpa_str.split('-')
        return (float(parts[0]) + float(parts[1])) / 2
    return float(cgpa_str)


def encode_categorical_variables(df):
    """Encode categorical variables to numeric"""
    df_encoded = df.copy()
    
    # Gender encoding
    if 'Gender' in df_encoded.columns:
        df_encoded['Gender'] = df_encoded['Gender'].map({'Male': 0, 'Female': 1})
    
    # Scholarship encoding
    scholarship_col = 'Did you receive a waiver or scholarship at your university?'
    if scholarship_col in df_encoded.columns:
        df_encoded['Scholarship'] = df_encoded[scholarship_col].map({'Yes': 1, 'No': 0})
    
    # Academic Year encoding
    if 'Academic Year' in df_encoded.columns:
        year_map = {'1st Year': 1, '2nd Year': 2, '3rd Year': 3, '4th Year': 4}
        df_encoded['Academic Year'] = df_encoded['Academic Year'].map(year_map)
    
    return df_encoded


def handle_missing_values(df):
    """Impute missing values"""
    df_clean = df.copy()
    
    # Numeric columns: fill with median
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df_clean[col].isna().any():
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
    
    # Categorical columns: fill with mode
    categorical_cols = df_clean.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df_clean[col].isna().any():
            df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)
    
    return df_clean


def save_plot(filename, output_dir='outputs/visualizations'):
    """Save matplotlib figure to file"""
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"  ✓ Saved: {filename}")
