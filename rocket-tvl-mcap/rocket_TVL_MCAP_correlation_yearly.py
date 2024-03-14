import pandas as pd

# Load the data
df = pd.read_csv("rocket_combined_cg_dl_data_clean.csv")

# Convert the 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Ensure the data is in numeric format
df["Rocket-TVL"] = pd.to_numeric(df["Rocket-TVL"], errors="coerce")
df["market_cap"] = pd.to_numeric(df["market_cap"], errors="coerce")

# Drop rows where any of the two columns have NaN values to ensure valid correlations
df.dropna(subset=["Rocket-TVL", "market_cap"], inplace=True)

# Calculate the correlation for the entire time series
overall_correlation = df["Rocket-TVL"].corr(df["market_cap"])
print(
    f"Overall Correlation between 'Rocket-TVL' and 'market_cap': {overall_correlation}"
)

# Group by year
df["Year"] = df["Date"].dt.to_period("Y")

# Calculate the correlation for each year
yearly_correlations = df.groupby("Year").apply(
    lambda x: x["Rocket-TVL"].corr(x["market_cap"])
)

# Output the results
print("\nYearly Correlations:")
print(yearly_correlations)

# Comprehensive statistics for 'Rocket-TVL'
lido_stats = df["Rocket-TVL"].describe()

# Comprehensive statistics for 'market_cap'
market_cap_stats = df["market_cap"].describe()

# Output the statistics
print("\nStatistics for 'Rocket-TVL':")
print(lido_stats)
print("\nStatistics for 'market_cap':")
print(market_cap_stats)

# Additional Statistics
print("\nAdditional Statistics:")
print(f"Skewness for 'Rocket-TVL': {df['Rocket-TVL'].skew()}")
print(f"Skewness for 'market_cap': {df['market_cap'].skew()}")
print(f"Kurtosis for 'Rocket-TVL': {df['Rocket-TVL'].kurt()}")
print(f"Kurtosis for 'market_cap': {df['market_cap'].kurt()}")

# Save the correlation results to a CSV
yearly_correlations.to_csv("yearly_correlations_clean.csv", header=True)

# Indicate the script has completed and output path
print("Script completed. Yearly correlations saved to 'yearly_correlations_clean.csv'.")
