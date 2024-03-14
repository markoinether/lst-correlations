import pandas as pd

# Load the data
df = pd.read_csv('combined_cg_dl_data_clean.csv')

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Ensure the data is in numeric format
df['Lido.5'] = pd.to_numeric(df['Lido.5'], errors='coerce')
df['market_cap'] = pd.to_numeric(df['market_cap'], errors='coerce')

# Drop rows where any of the two columns have NaN values to ensure valid correlations
df.dropna(subset=['Lido.5', 'market_cap'], inplace=True)

# Calculate the correlation for the entire time series
overall_correlation = df['Lido.5'].corr(df['market_cap'])
print(f"Overall Correlation between 'Lido.5' and 'market_cap': {overall_correlation}")

# Group by year
df['Year'] = df['Date'].dt.to_period('Y')

# Calculate the correlation for each year
yearly_correlations = df.groupby('Year').apply(lambda x: x['Lido.5'].corr(x['market_cap']))

# Output the results
print("\nYearly Correlations:")
print(yearly_correlations)

# Comprehensive statistics for 'Lido.5'
lido_stats = df['Lido.5'].describe()

# Comprehensive statistics for 'market_cap'
market_cap_stats = df['market_cap'].describe()

# Output the statistics
print("\nStatistics for 'Lido.5':")
print(lido_stats)
print("\nStatistics for 'market_cap':")
print(market_cap_stats)

# Additional Statistics
print("\nAdditional Statistics:")
print(f"Skewness for 'Lido.5': {df['Lido.5'].skew()}")
print(f"Skewness for 'market_cap': {df['market_cap'].skew()}")
print(f"Kurtosis for 'Lido.5': {df['Lido.5'].kurt()}")
print(f"Kurtosis for 'market_cap': {df['market_cap'].kurt()}")

# Save the correlation results to a CSV
yearly_correlations.to_csv('yearly_correlations_clean.csv', header=True)

# Indicate the script has completed and output path
print("Script completed. Yearly correlations saved to 'yearly_correlations_clean.csv'.")
