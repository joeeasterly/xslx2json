import pandas as pd
import json

# Replace the file path with the path to your XLSX file
xlsx_file_path = 'test.xlsx'

# Load the XLSX file into a pandas DataFrame
df = pd.read_excel(xlsx_file_path)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records')

# Print the JSON data
print(json_data)

# If you want to save the JSON data to a file, you can use the following code:
# Replace the file path with the path where you want to save the JSON file
json_file_path = 'path/to/your/file.json'
with open(json_file_path, 'w') as json_file:
    json.dump(json_data, json_file)

