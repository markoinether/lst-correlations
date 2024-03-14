import pandas as pd

# Read the CSV file
df = pd.read_csv('rocket-pool.csv')

# Convert the 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Format the 'Date' column to the Excel-recognized format
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

# Define the new file name
new_file_name = 'rocket_formatted.csv'

# Write the updated DataFrame to a new CSV file
df.to_csv(new_file_name, index=False)

print(f"New file created: {new_file_name}")
