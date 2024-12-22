import pandas as pd

def inspect_file(input_file):
    # Read the first few rows of the Excel file
    df = pd.read_excel(input_file, nrows=5)
    print(df.head())

# Example usage
input_file = 'DICV-VulnerabilityReportforthemonthofMarch24-Windows.xlsx'  # Replace with the actual path to your input file
inspect_file(input_file)