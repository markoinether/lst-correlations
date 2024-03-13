
import pandas as pd

# Read the CSV file
df = pd.read_csv('ldo-usd-max.csv')

# Convert the 'Date' column to datetime objects
df['snapped_at'] = pd.to_datetime(df['snapped_at'])

# Format the 'Date' column to the Excel-recognized format
df['snapped_at'] = df['snapped_at'].dt.strftime('%Y-%m-%d')

# Define the new file name
new_file_name = 'ldo-usd-max_formatted.csv'

# Write the updated DataFrame to a new CSV file
df.to_csv(new_file_name, index=False)

print(f"New file created: {new_file_name}")
