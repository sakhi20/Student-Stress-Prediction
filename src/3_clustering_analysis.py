"""
K-Means Clustering Analysis
Author: Sakhi Patel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.utils import save_plot

sns.set_style('whitegrid')


def run():
    """Execute clustering analysis"""
    
    print("\n" + "="*60)
    print("STEP 3: CLUSTERING ANALYSIS")
    print("="*60)
    
    # Load cleaned data
    print("\n[3.1] Loading cleaned data...")
    df = pd.read_csv('outputs/cleaned_data.csv')
    print(f"  ✓ Loaded {len(df)} records")
    
    # Select features for clustering
    print("\n[3.2] Selecting features for clustering...")
    features = ['Age', 'Gender', 'Current CGPA', 'Scholarship', 'Academic Year']
    X = df[features].copy()
    print(f"  ✓ Selected features: {features}")
    
    # Standardize features
    print("\n[3.3] Standardizing features...")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print("  ✓ Features standardized using StandardScaler")
    
    # Perform K-Means clustering
    print("\n[3.4] Performing K-Means clustering (k=4)...")
    kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
    df['Cluster'] = kmeans.fit_predict(X_scaled)
    print("  ✓ Clustering complete")
    
    # Calculate Silhouette Score
    silhouette = silhouette_score(X_scaled, df['Cluster'])
    print(f"\n[3.5] Cluster Quality:")
    print(f"  Silhouette Score: {silhouette:.4f}")
    
    # Save clustered data
    print("\n[3.6] Saving clustered data...")
    df.to_csv('outputs/clustered_data.csv', index=False)
    print("  ✓ Saved to: outputs/clustered_data.csv")
    
    # Cluster statistics
    print("\n[3.7] Cluster Statistics:")
    print("="*60)
    for cluster in range(4):
        cluster_data = df[df['Cluster'] == cluster]
        print(f"\nCluster {cluster} (n={len(cluster_data)}):")
        print(f"  Mean Age: {cluster_data['Age'].mean():.2f}")
        print(f"  Mean CGPA: {cluster_data['Current CGPA'].mean():.2f}")
        print(f"  Gender (Male%): {(cluster_data['Gender']==0).sum()/len(cluster_data)*100:.1f}%")
        print(f"  Scholarship%: {cluster_data['Scholarship'].mean()*100:.1f}%")
        print(f"  Mean Anxiety: {cluster_data['Anxiety Value'].mean():.2f}")
        print(f"  Mean Stress: {cluster_data['Stress Value'].mean():.2f}")
        print(f"  Mean Depression: {cluster_data['Depression Value'].mean():.2f}")
    
    # Visualizations
    print("\n[3.8] Creating cluster visualizations...")
    
    # 1. Cluster scatter: CGPA vs Anxiety
    plt.figure(figsize=(12, 6))
    scatter = plt.scatter(df['Current CGPA'], df['Anxiety Value'], 
                         c=df['Cluster'], cmap='viridis', 
                         alpha=0.6, edgecolors='black', s=50)
    plt.colorbar(scatter, label='Cluster')
    plt.title('K-Means Clusters: CGPA vs Anxiety Value', fontsize=16, fontweight='bold')
    plt.xlabel('Current CGPA', fontsize=12)
    plt.ylabel('Anxiety Value', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    save_plot('17_clusters_cgpa_anxiety.png')
    
    # 2. Cluster scatter: CGPA vs Stress
    plt.figure(figsize=(12, 6))
    scatter = plt.scatter(df['Current CGPA'], df['Stress Value'], 
                         c=df['Cluster'], cmap='viridis', 
                         alpha=0.6, edgecolors='black', s=50)
    plt.colorbar(scatter, label='Cluster')
    plt.title('K-Means Clusters: CGPA vs Stress Value', fontsize=16, fontweight='bold')
    plt.xlabel('Current CGPA', fontsize=12)
    plt.ylabel('Stress Value', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    save_plot('18_clusters_cgpa_stress.png')
    
    # 3. Cluster scatter: CGPA vs Depression
    plt.figure(figsize=(12, 6))
    scatter = plt.scatter(df['Current CGPA'], df['Depression Value'], 
                         c=df['Cluster'], cmap='viridis', 
                         alpha=0.6, edgecolors='black', s=50)
    plt.colorbar(scatter, label='Cluster')
    plt.title('K-Means Clusters: CGPA vs Depression Value', fontsize=16, fontweight='bold')
    plt.xlabel('Current CGPA', fontsize=12)
    plt.ylabel('Depression Value', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    save_plot('19_clusters_cgpa_depression.png')
    
    # 4. Cluster size distribution
    plt.figure(figsize=(10, 6))
    cluster_counts = df['Cluster'].value_counts().sort_index()
    plt.bar(cluster_counts.index, cluster_counts.values, 
            edgecolor='black', alpha=0.8, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    plt.title('Cluster Size Distribution', fontsize=16, fontweight='bold')
    plt.xlabel('Cluster', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    for i, v in enumerate(cluster_counts.values):
        plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
    plt.tight_layout()
    save_plot('20_cluster_sizes.png')
    
    # 5. Cluster characteristics heatmap
    cluster_features = df.groupby('Cluster')[['Age', 'Current CGPA', 'Anxiety Value', 
                                               'Stress Value', 'Depression Value']].mean()
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(cluster_features.T, annot=True, fmt='.2f', cmap='YlOrRd', 
                cbar_kws={'label': 'Mean Value'}, linewidths=1)
    plt.title('Cluster Characteristics Heatmap', fontsize=16, fontweight='bold')
    plt.xlabel('Cluster', fontsize=12)
    plt.ylabel('Feature', fontsize=12)
    plt.tight_layout()
    save_plot('21_cluster_characteristics.png')
    
    # Mental health distribution by cluster
    print("\n[3.9] Mental Health Distribution by Cluster:")
    print("="*60)
    for cluster in range(4):
        cluster_data = df[df['Cluster'] == cluster]
        print(f"\nCluster {cluster}:")
        print(f"  Anxiety:    {cluster_data['Anxiety Label'].value_counts().to_dict()}")
        print(f"  Stress:     {cluster_data['Stress Label'].value_counts().to_dict()}")
        print(f"  Depression: {cluster_data['Depression Label'].value_counts().to_dict()}")
    
    print("\n" + "="*60)
    print("✓ CLUSTERING ANALYSIS COMPLETE")
    print(f"✓ Created 5 cluster visualizations")
    print("="*60)


if __name__ == '__main__':
    run()
