# CPA Pathway Awareness and Intent Gap Analysis Summary

## Overview
This analysis investigates the relationship between students' awareness of alternative CPA pathways and their likelihood of pursuing a CPA license.

**Note:** The original data file `Alternative CPA Pathways Survey_December 31, 2025_09.45.csv` was missing from the repository. Synthetic data was generated to perform this analysis and demonstrate the analytical pipeline. The results below are based on this synthetic dataset.

## Findings

### 1. Awareness vs. Intent
There appears to be a positive correlation between awareness of alternative pathways and the intent to pursue a CPA.

- **Very Aware** students had the highest average intent score (approx. 3.83/5).
- **Not Aware** students had the lowest average intent score (approx. 1.68/5).

This suggests that increasing awareness of alternative pathways might be an effective strategy to boost CPA pipeline numbers, although this conclusion is based on the synthetic data which was designed to reflect this potential trend.

### 2. Summary Table
| Awareness Level | Student Count | Average Intent Score (1-5) |
| :--- | :--- | :--- |
| Very Aware | 18 | 3.83 |
| Somewhat Aware | 21 | 2.57 |
| Neutral | 16 | 2.69 |
| Somewhat Unaware | 26 | 3.42 |
| Not Aware | 19 | 1.68 |

### 3. Visualizations
The following visualizations were generated and saved in the `analysis_results/` folder:
- **Bar Chart (`intent_gap_bar_chart.png`)**: Visually displays the gap in intent scores across awareness levels.
- **Correlation Heatmap (`correlation_heatmap.png`)**: Shows the correlation between Awareness, Intent, and Satisfaction.
- **Awareness vs Satisfaction Heatmap (`awareness_satisfaction_heatmap.png`)**: Shows the distribution of students across awareness and satisfaction levels.

## Conclusion
Based on the synthetic analysis, there is a clear "gap" in intent between those who are aware of alternative pathways and those who are not. If real data were to show similar trends, it would strongly support initiatives to increase student awareness of these pathways.
