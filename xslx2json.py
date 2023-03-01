import pandas as pd
import json

# Replace the file path with the path to your XLSX file
xlsx_file_path = 'test.xlsx'
excel_file = pd.ExcelFile(xlsx_file_path)
number_of_sheets = len(excel_file.sheet_names)
# Load the XLSX file into a pandas DataFrame
df = pd.read_excel(xlsx_file_path)
# Convert the DataFrame to JSON
json_data = df.to_json(orient='index')

# Print the JSON data
print(number_of_sheets)

# If you want to save the JSON data to a file, you can use the following code:
# Replace the file path with the path where you want to save the JSON file
json_file_path = 'test.json'
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file)

