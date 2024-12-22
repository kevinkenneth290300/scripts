import pandas as pd

# Load the data from the Excel file
file_path = 'DTAG_DICV Report_23.10.2024.xlsx'  # Update with your actual file path
df = pd.read_excel(file_path, header=None)

# Create a dictionary to hold the final result
result = {}

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    id_value = row[0]
    name_info = row[2]
    
    # Extract the name
    # if ',' in name_info:
    #     surname, given_name = name_info.split(', ')
    #     full_name = f"{given_name} {surname}"
    # else:
    #     full_name = name_info
    
    # Add the ID to the corresponding name in the dictionary
    if name_info not in result:
        result[name_info] = []
    result[name_info].append(id_value)

# Print the result dictionary
for name, ids in result.items():
    print(f"'{name}': {ids},")
