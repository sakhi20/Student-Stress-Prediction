"""
Random Forest Classification Models
Author: Sakhi Patel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import save_plot

sns.set_style('whitegrid')


def train_model(df, target_col, model_name):
    """Train Random Forest model for a specific mental health category"""
    
    print(f"\n{'='*60}")
    print(f"Training {model_name} Model")
    print('='*60)
    
    # Prepare features
    feature_cols = ['Age', 'Gender', 'Current CGPA', 'Scholarship', 'Academic Year', 'Cluster']
    X = df[feature_cols]
    
    # Encode target
    le = LabelEncoder()
    y = le.fit_transform(df[target_col])
    
    print(f"\n[1] Dataset prepared:")
    print(f"  Features: {feature_cols}")
    print(f"  Target: {target_col}")
    print(f"  Classes: {le.classes_}")
    print(f"  Class distribution: {pd.Series(y).value_counts().to_dict()}")
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    print(f"\n[2] Train-test split:")
    print(f"  Training samples: {len(X_train)}")
    print(f"  Testing samples: {len(X_test)}")
    
    # Train Random Forest
    print(f"\n[3] Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, max_depth=10, 
                                class_weight='balanced', random_state=42)
    rf.fit(X_train, y_train)
    print("  ✓ Model trained")
    
    # Predictions
    y_pred = rf.predict(X_test)
    
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n[4] Model Performance:")
    print(f"  Accuracy: {accuracy:.4f}")
    
    print(f"\n[5] Classification Report:")
    print(classification_report(y_test, y_pred, target_names=le.classes_))
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=le.classes_, yticklabels=le.classes_,
                cbar_kws={'label': 'Count'})
    plt.title(f'{model_name} - Confusion Matrix', fontsize=16, fontweight='bold')
    plt.xlabel('Predicted Label', fontsize=12)
    plt.ylabel('True Label', fontsize=12)
    plt.tight_layout()
    save_plot(f'{model_name.lower().replace(" ", "_")}_confusion_matrix.png')
    
    # Feature Importance
    feature_importance = pd.DataFrame({
        'Feature': feature_cols,
        'Importance': rf.feature_importances_
    }).sort_values('Importance', ascending=False)
    
    print(f"\n[6] Feature Importance:")
    print(feature_importance.to_string(index=False))
    
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance['Feature'], feature_importance['Importance'], 
             edgecolor='black', alpha=0.8)
    plt.title(f'{model_name} - Feature Importance', fontsize=16, fontweight='bold')
    plt.xlabel('Importance', fontsize=12)
    plt.ylabel('Feature', fontsize=12)
    plt.gca().invert_yaxis()
    plt.tight_layout()
    save_plot(f'{model_name.lower().replace(" ", "_")}_feature_importance.png')
    
    # Save model
    os.makedirs('outputs/models', exist_ok=True)
    model_path = f'outputs/models/{model_name.lower().replace(" ", "_")}_model.pkl'
    joblib.dump(rf, model_path)
    print(f"\n[7] Model saved to: {model_path}")
    
    return accuracy, cm, feature_importance


def run():
    """Execute classification pipeline for all mental health categories"""
    
    print("\n" + "="*60)
    print("STEP 4: CLASSIFICATION MODELS")
    print("="*60)
    
    # Load clustered data
    print("\n[4.1] Loading clustered data...")
    df = pd.read_csv('outputs/clustered_data.csv')
    print(f"  ✓ Loaded {len(df)} records")
    
    # Train models for each mental health category
    results = {}
    
    # 1. Anxiety Model
    print("\n" + "="*60)
    print("MODEL 1: ANXIETY PREDICTION")
    print("="*60)
    acc_anxiety, cm_anxiety, fi_anxiety = train_model(df, 'Anxiety Label', 'Anxiety Prediction')
    results['Anxiety'] = {'accuracy': acc_anxiety, 'confusion_matrix': cm_anxiety}
    
    # 2. Stress Model
    print("\n" + "="*60)
    print("MODEL 2: STRESS PREDICTION")
    print("="*60)
    acc_stress, cm_stress, fi_stress = train_model(df, 'Stress Label', 'Stress Prediction')
    results['Stress'] = {'accuracy': acc_stress, 'confusion_matrix': cm_stress}
    
    # 3. Depression Model
    print("\n" + "="*60)
    print("MODEL 3: DEPRESSION PREDICTION")
    print("="*60)
    acc_depression, cm_depression, fi_depression = train_model(df, 'Depression Label', 'Depression Prediction')
    results['Depression'] = {'accuracy': acc_depression, 'confusion_matrix': cm_depression}
    
    # Summary
    print("\n" + "="*60)
    print("MODEL PERFORMANCE SUMMARY")
    print("="*60)
    print(f"\nAnxiety Model Accuracy:    {acc_anxiety:.4f}")
    print(f"Stress Model Accuracy:     {acc_stress:.4f}")
    print(f"Depression Model Accuracy: {acc_depression:.4f}")
    
    # Save results
    os.makedirs('outputs/results', exist_ok=True)
    with open('outputs/results/model_performance.txt', 'w') as f:
        f.write("="*60 + "\n")
        f.write("MENTAL HEALTH PREDICTION - MODEL PERFORMANCE\n")
        f.write("="*60 + "\n\n")
        f.write(f"Anxiety Model Accuracy:    {acc_anxiety:.4f}\n")
        f.write(f"Stress Model Accuracy:     {acc_stress:.4f}\n")
        f.write(f"Depression Model Accuracy: {acc_depression:.4f}\n")
        f.write("\n" + "="*60 + "\n")
    
    print("\n✓ Results saved to: outputs/results/model_performance.txt")
    
    # Comparison plot
    plt.figure(figsize=(10, 6))
    models = ['Anxiety', 'Stress', 'Depression']
    accuracies = [acc_anxiety, acc_stress, acc_depression]
    colors = ['#ff6b6b', '#feca57', '#48dbfb']
    
    bars = plt.bar(models, accuracies, edgecolor='black', alpha=0.8, color=colors)
    plt.title('Model Performance Comparison', fontsize=16, fontweight='bold')
    plt.ylabel('Accuracy', fontsize=12)
    plt.ylim(0, 1.0)
    plt.grid(True, alpha=0.3, axis='y')
    
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.02,
                f'{acc:.3f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    save_plot('22_model_comparison.png')
    
    print("\n" + "="*60)
    print("✓ CLASSIFICATION COMPLETE")
    print(f"✓ Trained 3 Random Forest models")
    print(f"✓ Created 7 visualizations")
    print("="*60)


if __name__ == '__main__':
    run()
