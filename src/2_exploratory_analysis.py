"""
Exploratory Data Analysis with Visualizations
Author: Sakhi Patel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import save_plot

# Set style
sns.set_style('whitegrid')
sns.set_palette('Set2')


def run():
    """Execute exploratory data analysis"""
    
    print("\n" + "="*60)
    print("STEP 2: EXPLORATORY DATA ANALYSIS")
    print("="*60)
    
    # Load cleaned data
    print("\n[2.1] Loading cleaned data...")
    df = pd.read_csv('outputs/cleaned_data.csv')
    print(f"  ✓ Loaded {len(df)} records")
    
    os.makedirs('outputs/visualizations', exist_ok=True)
    
    # 1. CGPA Distribution
    print("\n[2.2] Creating frequency distributions...")
    plt.figure(figsize=(12, 6))
    plt.hist(df['Current CGPA'], bins=30, edgecolor='black', alpha=0.7)
    plt.title('Distribution of Student CGPA', fontsize=16, fontweight='bold')
    plt.xlabel('CGPA', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.axvline(df['Current CGPA'].mean(), color='red', linestyle='--', label=f'Mean: {df["Current CGPA"].mean():.2f}')
    plt.legend()
    plt.tight_layout()
    save_plot('01_cgpa_distribution.png')
    
    # 2. Age Distribution
    plt.figure(figsize=(12, 6))
    plt.hist(df['Age'], bins=15, edgecolor='black', alpha=0.7, color='skyblue')
    plt.title('Distribution of Student Age', fontsize=16, fontweight='bold')
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.tight_layout()
    save_plot('02_age_distribution.png')
    
    # 3. Gender Distribution
    plt.figure(figsize=(10, 6))
    gender_counts = df['Gender'].value_counts()
    gender_labels = ['Male', 'Female']
    plt.bar(gender_labels, gender_counts.values, edgecolor='black', alpha=0.8)
    plt.title('Gender Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Gender', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    for i, v in enumerate(gender_counts.values):
        plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    save_plot('03_gender_distribution.png')
    
    # 4. University Distribution
    plt.figure(figsize=(12, 6))
    univ_counts = df['University'].value_counts()
    plt.barh(univ_counts.index, univ_counts.values, edgecolor='black', alpha=0.8)
    plt.title('University Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('University', fontsize=12)
    plt.tight_layout()
    save_plot('04_university_distribution.png')
    
    # 5. Department Distribution
    plt.figure(figsize=(12, 6))
    dept_counts = df['Department'].value_counts()
    plt.barh(dept_counts.index, dept_counts.values, edgecolor='black', alpha=0.8, color='coral')
    plt.title('Department Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Department', fontsize=12)
    plt.tight_layout()
    save_plot('05_department_distribution.png')
    
    # 6. Academic Year Distribution
    plt.figure(figsize=(10, 6))
    year_counts = df['Academic Year'].value_counts().sort_index()
    year_labels = ['1st Year', '2nd Year', '3rd Year', '4th Year']
    plt.bar(year_labels, year_counts.values, edgecolor='black', alpha=0.8, color='lightgreen')
    plt.title('Academic Year Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Academic Year', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.tight_layout()
    save_plot('06_academic_year_distribution.png')
    
    # 7. Scholarship Status
    plt.figure(figsize=(8, 8))
    scholarship_counts = df['Scholarship'].value_counts()
    labels = ['No Scholarship', 'Scholarship']
    colors = ['#ff9999', '#66b3ff']
    plt.pie(scholarship_counts.values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Scholarship Status Distribution', fontsize=16, fontweight='bold')
    plt.tight_layout()
    save_plot('07_scholarship_distribution.png')
    
    # 8-10. Mental Health Label Distributions
    print("\n[2.3] Creating mental health distributions...")
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Anxiety
    anxiety_counts = df['Anxiety Label'].value_counts()
    axes[0].bar(anxiety_counts.index, anxiety_counts.values, edgecolor='black', alpha=0.8, color=['green', 'orange', 'red'])
    axes[0].set_title('Anxiety Label Distribution', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('Count', fontsize=12)
    
    # Stress
    stress_counts = df['Stress Label'].value_counts()
    axes[1].bar(stress_counts.index, stress_counts.values, edgecolor='black', alpha=0.8, color=['green', 'orange', 'red'])
    axes[1].set_title('Stress Label Distribution', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('Count', fontsize=12)
    
    # Depression
    depression_counts = df['Depression Label'].value_counts()
    axes[2].bar(depression_counts.index, depression_counts.values, edgecolor='black', alpha=0.8, color=['green', 'orange', 'red'])
    axes[2].set_title('Depression Label Distribution', fontsize=14, fontweight='bold')
    axes[2].set_ylabel('Count', fontsize=12)
    
    plt.tight_layout()
    save_plot('08_mental_health_labels.png')
    
    # 11. Mental Health Scores Distribution
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    axes[0].hist(df['Anxiety Value'], bins=30, edgecolor='black', alpha=0.7, color='salmon')
    axes[0].set_title('Anxiety Score Distribution', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Anxiety Value', fontsize=12)
    axes[0].set_ylabel('Frequency', fontsize=12)
    axes[0].axvline(df['Anxiety Value'].mean(), color='red', linestyle='--', label=f'Mean: {df["Anxiety Value"].mean():.1f}')
    axes[0].legend()
    
    axes[1].hist(df['Stress Value'], bins=30, edgecolor='black', alpha=0.7, color='lightcoral')
    axes[1].set_title('Stress Score Distribution', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Stress Value', fontsize=12)
    axes[1].set_ylabel('Frequency', fontsize=12)
    axes[1].axvline(df['Stress Value'].mean(), color='red', linestyle='--', label=f'Mean: {df["Stress Value"].mean():.1f}')
    axes[1].legend()
    
    axes[2].hist(df['Depression Value'], bins=30, edgecolor='black', alpha=0.7, color='plum')
    axes[2].set_title('Depression Score Distribution', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Depression Value', fontsize=12)
    axes[2].set_ylabel('Frequency', fontsize=12)
    axes[2].axvline(df['Depression Value'].mean(), color='red', linestyle='--', label=f'Mean: {df["Depression Value"].mean():.1f}')
    axes[2].legend()
    
    plt.tight_layout()
    save_plot('09_mental_health_scores.png')
    
    # 12. Correlation Heatmap
    print("\n[2.4] Creating correlation analysis...")
    plt.figure(figsize=(10, 8))
    corr_features = ['Current CGPA', 'Anxiety Value', 'Stress Value', 'Depression Value']
    corr_matrix = df[corr_features].corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', center=0, 
                square=True, linewidths=1, cbar_kws={"shrink": 0.8})
    plt.title('Correlation Matrix: CGPA vs Mental Health', fontsize=16, fontweight='bold')
    plt.tight_layout()
    save_plot('10_correlation_heatmap.png')
    
    print("\n  Correlation Insights:")
    print(f"    CGPA vs Anxiety:    {corr_matrix.loc['Current CGPA', 'Anxiety Value']:.3f}")
    print(f"    CGPA vs Stress:     {corr_matrix.loc['Current CGPA', 'Stress Value']:.3f}")
    print(f"    CGPA vs Depression: {corr_matrix.loc['Current CGPA', 'Depression Value']:.3f}")
    
    # 13-15. Scatter plots
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    axes[0].scatter(df['Current CGPA'], df['Anxiety Value'], alpha=0.5, c='red', edgecolors='black')
    axes[0].set_title('CGPA vs Anxiety', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('CGPA', fontsize=12)
    axes[0].set_ylabel('Anxiety Value', fontsize=12)
    axes[0].grid(True, alpha=0.3)
    
    axes[1].scatter(df['Current CGPA'], df['Stress Value'], alpha=0.5, c='orange', edgecolors='black')
    axes[1].set_title('CGPA vs Stress', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('CGPA', fontsize=12)
    axes[1].set_ylabel('Stress Value', fontsize=12)
    axes[1].grid(True, alpha=0.3)
    
    axes[2].scatter(df['Current CGPA'], df['Depression Value'], alpha=0.5, c='purple', edgecolors='black')
    axes[2].set_title('CGPA vs Depression', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('CGPA', fontsize=12)
    axes[2].set_ylabel('Depression Value', fontsize=12)
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_plot('11_cgpa_vs_mental_health.png')
    
    # 16. Mental Health by Gender
    print("\n[2.5] Creating demographic comparisons...")
    gender_mental = df.groupby('Gender')[['Anxiety Value', 'Stress Value', 'Depression Value']].mean()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(3)
    width = 0.35
    
    ax.bar(x - width/2, gender_mental.iloc[0], width, label='Male', alpha=0.8, edgecolor='black')
    ax.bar(x + width/2, gender_mental.iloc[1], width, label='Female', alpha=0.8, edgecolor='black')
    
    ax.set_title('Mean Mental Health Scores by Gender', fontsize=16, fontweight='bold')
    ax.set_ylabel('Mean Score', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(['Anxiety', 'Stress', 'Depression'])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    save_plot('12_mental_health_by_gender.png')
    
    # 17. Mental Health by Academic Year
    year_mental = df.groupby('Academic Year')[['Anxiety Value', 'Stress Value', 'Depression Value']].mean()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(len(year_mental))
    width = 0.25
    
    ax.bar(x - width, year_mental['Anxiety Value'], width, label='Anxiety', alpha=0.8, edgecolor='black')
    ax.bar(x, year_mental['Stress Value'], width, label='Stress', alpha=0.8, edgecolor='black')
    ax.bar(x + width, year_mental['Depression Value'], width, label='Depression', alpha=0.8, edgecolor='black')
    
    ax.set_title('Mean Mental Health Scores by Academic Year', fontsize=16, fontweight='bold')
    ax.set_ylabel('Mean Score', fontsize=12)
    ax.set_xlabel('Academic Year', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(['1st Year', '2nd Year', '3rd Year', '4th Year'])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    save_plot('13_mental_health_by_year.png')
    
    # 18. Mental Health by Scholarship
    scholarship_mental = df.groupby('Scholarship')[['Anxiety Value', 'Stress Value', 'Depression Value']].mean()
    
    fig, ax = plt.subplots(figsize=(12, 6))
    x = np.arange(3)
    width = 0.35
    
    ax.bar(x - width/2, scholarship_mental.iloc[0], width, label='No Scholarship', alpha=0.8, edgecolor='black')
    ax.bar(x + width/2, scholarship_mental.iloc[1], width, label='Scholarship', alpha=0.8, edgecolor='black')
    
    ax.set_title('Mean Mental Health Scores by Scholarship Status', fontsize=16, fontweight='bold')
    ax.set_ylabel('Mean Score', fontsize=12)
    ax.set_xticks(x)
    ax.set_xticklabels(['Anxiety', 'Stress', 'Depression'])
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    save_plot('14_mental_health_by_scholarship.png')
    
    # 19. Box plots by CGPA ranges
    df['CGPA_Range'] = pd.cut(df['Current CGPA'], bins=[0, 2.5, 3.0, 3.5, 4.0], 
                               labels=['<2.5', '2.5-3.0', '3.0-3.5', '3.5-4.0'])
    
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    df.boxplot(column='Anxiety Value', by='CGPA_Range', ax=axes[0])
    axes[0].set_title('Anxiety by CGPA Range', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('CGPA Range', fontsize=12)
    axes[0].set_ylabel('Anxiety Value', fontsize=12)
    
    df.boxplot(column='Stress Value', by='CGPA_Range', ax=axes[1])
    axes[1].set_title('Stress by CGPA Range', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('CGPA Range', fontsize=12)
    axes[1].set_ylabel('Stress Value', fontsize=12)
    
    df.boxplot(column='Depression Value', by='CGPA_Range', ax=axes[2])
    axes[2].set_title('Depression by CGPA Range', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('CGPA Range', fontsize=12)
    axes[2].set_ylabel('Depression Value', fontsize=12)
    
    plt.suptitle('')
    plt.tight_layout()
    save_plot('15_boxplots_by_cgpa.png')
    
    # 20. Violin plots
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    gender_labels = {0: 'Male', 1: 'Female'}
    df['Gender_Label'] = df['Gender'].map(gender_labels)
    
    sns.violinplot(data=df, x='Gender_Label', y='Anxiety Value', ax=axes[0], palette='Set2')
    axes[0].set_title('Anxiety Distribution by Gender', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Gender', fontsize=12)
    
    sns.violinplot(data=df, x='Gender_Label', y='Stress Value', ax=axes[1], palette='Set2')
    axes[1].set_title('Stress Distribution by Gender', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Gender', fontsize=12)
    
    sns.violinplot(data=df, x='Gender_Label', y='Depression Value', ax=axes[2], palette='Set2')
    axes[2].set_title('Depression Distribution by Gender', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Gender', fontsize=12)
    
    plt.tight_layout()
    save_plot('16_violin_plots_by_gender.png')
    
    print("\n" + "="*60)
    print("✓ EXPLORATORY ANALYSIS COMPLETE")
    print(f"✓ Created 16 visualizations in outputs/visualizations/")
    print("="*60)


if __name__ == '__main__':
    run()
