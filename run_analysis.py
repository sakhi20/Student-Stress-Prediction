"""
Main script to run complete analysis pipeline
Author: Sakhi Patel
"""

import os
import sys

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src import generate_data
from src import utils as _  # Import to ensure module is available
import importlib


def main():
    """Execute complete analysis pipeline"""
    
    print("\n" + "="*70)
    print(" "*10 + "STUDENT MENTAL HEALTH PREDICTION - COMPLETE ANALYSIS")
    print("="*70)
    print("\nAuthor: Sakhi Patel")
    print("Institution: North Carolina State University")
    print("Project: Big Data Analysis - AI/ML Driven Mental Health Prediction")
    print("="*70)
    
    # Create output directories
    print("\n[Setup] Creating output directories...")
    os.makedirs('outputs/visualizations', exist_ok=True)
    os.makedirs('outputs/models', exist_ok=True)
    os.makedirs('outputs/results', exist_ok=True)
    print("  ✓ Directories created")
    
    # Check if data exists, if not generate it
    if not os.path.exists('data/student_mental_health_survey.csv'):
        print("\n[Step 0/4] Generating synthetic dataset...")
        generate_data.generate_synthetic_data(500).to_csv('data/student_mental_health_survey.csv', index=False)
        print("  ✓ Dataset generated")
    else:
        print("\n[Step 0/4] Dataset already exists")
    
    # Import and run each module
    print("\n" + "="*70)
    print("[Step 1/4] Running Data Preprocessing...")
    print("="*70)
    preprocessing = importlib.import_module('src.1_data_preprocessing')
    preprocessing.run()
    
    print("\n" + "="*70)
    print("[Step 2/4] Running Exploratory Data Analysis...")
    print("="*70)
    eda = importlib.import_module('src.2_exploratory_analysis')
    eda.run()
    
    print("\n" + "="*70)
    print("[Step 3/4] Running Clustering Analysis...")
    print("="*70)
    clustering = importlib.import_module('src.3_clustering_analysis')
    clustering.run()
    
    print("\n" + "="*70)
    print("[Step 4/4] Running Classification Models...")
    print("="*70)
    classification = importlib.import_module('src.4_classification_models')
    classification.run()
    
    # Final summary
    print("\n" + "="*70)
    print(" "*20 + "ANALYSIS COMPLETE!")
    print("="*70)
    
    print("\n📊 Results Summary:")
    print("  ✓ Dataset: 500 student survey responses")
    print("  ✓ Preprocessing: Data cleaned and encoded")
    print("  ✓ Visualizations: 22+ plots created")
    print("  ✓ Clustering: K-Means with 4 clusters")
    print("  ✓ Models: 3 Random Forest classifiers trained")
    
    print("\n📁 Output Files:")
    print("  • Cleaned Data: outputs/cleaned_data.csv")
    print("  • Clustered Data: outputs/clustered_data.csv")
    print("  • Visualizations: outputs/visualizations/ (22+ PNG files)")
    print("  • Models: outputs/models/ (3 .pkl files)")
    print("  • Results: outputs/results/model_performance.txt")
    
    print("\n🔧 Next Steps:")
    print("  • Review visualizations in outputs/visualizations/")
    print("  • Check model performance in outputs/results/")
    print("  • Run self-assessment tool: python src/5_assessment_tool.py")
    
    print("\n" + "="*70)
    print("Thank you for using the Mental Health Prediction System!")
    print("="*70 + "\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Analysis interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
