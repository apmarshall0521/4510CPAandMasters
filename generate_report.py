import pandas as pd
import os

def generate_html_report():
    # Load summary table
    summary_file = "analysis_results/summary_table.csv"
    try:
        df = pd.read_csv(summary_file)
    except FileNotFoundError:
        print(f"Error: {summary_file} not found.")
        return

    # Convert DataFrame to HTML table
    table_html = df.to_html(classes="table table-striped", index=False)

    # Image paths
    images = [
        "analysis_results/intent_gap_bar_chart.png",
        "analysis_results/correlation_heatmap.png",
        "analysis_results/awareness_satisfaction_heatmap.png"
    ]

    # HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CPA Pathway Analysis Results</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            h2 {{ color: #666; margin-top: 30px; }}
            table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #f2f2f2; }}
            img {{ max-width: 100%; height: auto; margin-bottom: 20px; border: 1px solid #ccc; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>CPA Pathway Analysis Results</h1>

            <h2>Summary Table</h2>
            {table_html}

            <h2>Visualizations</h2>
    """

    for img_path in images:
        if os.path.exists(img_path):
            img_name = os.path.basename(img_path).replace("_", " ").replace(".png", "").title()
            html_content += f"""
            <h3>{img_name}</h3>
            <img src="{img_path}" alt="{img_name}">
            """
        else:
            print(f"Warning: Image {img_path} not found.")

    html_content += """
        </div>
    </body>
    </html>
    """

    # Write to file
    with open("index.html", "w") as f:
        f.write(html_content)

    print("Report generated successfully: index.html")

if __name__ == "__main__":
    generate_html_report()
