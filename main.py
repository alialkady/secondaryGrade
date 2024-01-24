import pandas as pd
# Load the Excel file into a pandas DataFrame
#file_path = 'secondarygrade.csv'
file_path = 'secondarygrade.csv'
df = pd.read_csv(file_path)

# Prompt user for a name
name = input("Enter name: ")

# Find the row based on the name
row_data = df[df['الاسم'] == name]

# Check if the name exists in the DataFrame
if not row_data.empty:
    print("Row Data:")
    print(row_data)
else:
    print(f"No data found for the name: {name}")
