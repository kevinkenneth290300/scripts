import pandas as pd

def inspect_column_names(input_file):
    # Read the Excel file
    df = pd.read_excel(input_file)
    # Print the column names
    print(df.columns)

# Example usage
input_file = 'DICV-VulnerabilityReportforthemonthofMarch24-Windows.xlsx'  # Replace with the actual path to your input file
inspect_column_names(input_file)
