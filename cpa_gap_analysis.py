import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory
output_dir = "analysis_results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load data
file_path = "Alternative CPA Pathways Survey_December 31, 2025_09.45.csv"
try:
    df = pd.read_csv(file_path)
    print(f"Loaded {file_path}")
except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
    exit(1)

# Mappings
awareness_map = {
    "Very Aware": 5,
    "Somewhat Aware": 4,
    "Neutral": 3,
    "Somewhat Unaware": 2,
    "Not Aware": 1
}

likelihood_map = {
    "Very Likely": 5,
    "Somewhat Likely": 4,
    "Neutral": 3,
    "Somewhat Unlikely": 2,
    "Very Unlikely": 1
}

satisfaction_map = {
    "Very Satisfied": 5,
    "Satisfied": 4,
    "Neutral": 3,
    "Dissatisfied": 2,
    "Very Dissatisfied": 1
}

# Apply mappings
df["Awareness Score"] = df["Awareness of Alternative Pathways"].map(awareness_map)
df["Intent Score"] = df["Likelihood of Pursuing CPA"].map(likelihood_map)
df["Satisfaction Score"] = df["Graduate Program Satisfaction"].map(satisfaction_map)

# Check for unmapped values
if df["Awareness Score"].isnull().any():
    print("Warning: Some Awareness values could not be mapped.")
    print(df[df["Awareness Score"].isnull()]["Awareness of Alternative Pathways"].unique())

if df["Intent Score"].isnull().any():
    print("Warning: Some Intent values could not be mapped.")
    print(df[df["Intent Score"].isnull()]["Likelihood of Pursuing CPA"].unique())

if df["Satisfaction Score"].isnull().any():
    print("Warning: Some Satisfaction values could not be mapped.")
    print(df[df["Satisfaction Score"].isnull()]["Graduate Program Satisfaction"].unique())

# Drop rows with missing mapped values for analysis
df_clean = df.dropna(subset=["Awareness Score", "Intent Score", "Satisfaction Score"])

# Analysis 1: Summary Table
summary_table = df_clean.groupby("Awareness of Alternative Pathways").agg(
    Count=("Intent Score", "count"),
    Average_Intent_Score=("Intent Score", "mean")
).reset_index()

# Sort by awareness level logic
summary_table["Awareness_Sort_Order"] = summary_table["Awareness of Alternative Pathways"].map(awareness_map)
summary_table = summary_table.sort_values("Awareness_Sort_Order", ascending=False).drop(columns=["Awareness_Sort_Order"])

print("\nSummary Table:")
print(summary_table)

summary_table.to_csv(f"{output_dir}/summary_table.csv", index=False)

# Analysis 2: Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Awareness of Alternative Pathways", y="Intent Score", data=df_clean, order=list(awareness_map.keys()))
plt.title("Average CPA Intent Score by Awareness of Alternative Pathways")
plt.xlabel("Awareness Level")
plt.ylabel("Average Intent Score (1-5)")
plt.ylim(1, 5)
plt.savefig(f"{output_dir}/intent_gap_bar_chart.png")
plt.close()

# Analysis 3: Heatmap / Correlation
# Correlation Matrix
correlation_matrix = df_clean[["Awareness Score", "Intent Score", "Satisfaction Score"]].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Matrix: Awareness, Intent, and Satisfaction")
plt.savefig(f"{output_dir}/correlation_heatmap.png")
plt.close()

# Additional Heatmap: Awareness vs Satisfaction counts
# Create a crosstab
ct = pd.crosstab(df_clean["Awareness of Alternative Pathways"], df_clean["Graduate Program Satisfaction"])
# Reorder index and columns
ct = ct.reindex(index=list(awareness_map.keys()), columns=list(satisfaction_map.keys()))

plt.figure(figsize=(10, 8))
sns.heatmap(ct, annot=True, fmt="d", cmap="YlGnBu")
plt.title("Heatmap of Student Counts: Awareness vs Satisfaction")
plt.xlabel("Graduate Program Satisfaction")
plt.ylabel("Awareness of Alternative Pathways")
plt.savefig(f"{output_dir}/awareness_satisfaction_heatmap.png")
plt.close()

print(f"\nAnalysis complete. Results saved to {output_dir}/")
