import pandas as pd
import numpy as np
import random

def generate_mock_data(num_rows=100):
    # Set seed for reproducibility
    np.random.seed(42)
    random.seed(42)

    awareness_levels = [
        "Very Aware",
        "Somewhat Aware",
        "Neutral",
        "Somewhat Unaware",
        "Not Aware"
    ]

    likelihood_levels = [
        "Very Likely",
        "Somewhat Likely",
        "Neutral",
        "Somewhat Unlikely",
        "Very Unlikely"
    ]

    satisfaction_levels = [
        "Very Satisfied",
        "Satisfied",
        "Neutral",
        "Dissatisfied",
        "Very Dissatisfied"
    ]

    # Generate random data
    data = {
        "Awareness of Alternative Pathways": np.random.choice(awareness_levels, num_rows),
        "Likelihood of Pursuing CPA": np.random.choice(likelihood_levels, num_rows),
        "Graduate Program Satisfaction": np.random.choice(satisfaction_levels, num_rows)
    }

    df = pd.DataFrame(data)

    # Introduce some correlation for demonstration purposes
    # If "Very Aware", more likely to be "Very Likely"
    for idx, row in df.iterrows():
        if row["Awareness of Alternative Pathways"] == "Very Aware":
            if random.random() < 0.6:
                df.at[idx, "Likelihood of Pursuing CPA"] = "Very Likely"
        elif row["Awareness of Alternative Pathways"] == "Not Aware":
             if random.random() < 0.6:
                df.at[idx, "Likelihood of Pursuing CPA"] = "Very Unlikely"

    output_file = "Alternative CPA Pathways Survey_December 31, 2025_09.45.csv"
    df.to_csv(output_file, index=False)
    print(f"Generated {output_file} with {num_rows} rows.")

if __name__ == "__main__":
    generate_mock_data()
