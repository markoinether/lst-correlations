import pandas as pd

# Load the data
df = pd.read_csv("sd_combined_cg_dl_data_clean.csv")

# Convert the 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Ensure the data is in numeric format
df["Stader-TVL-total"] = pd.to_numeric(df["Stader-TVL-total"], errors="coerce")
df["market_cap"] = pd.to_numeric(df["market_cap"], errors="coerce")

# Drop rows where any of the two columns have NaN values to ensure valid correlations
df.dropna(subset=["Stader-TVL-total", "market_cap"], inplace=True)

# Calculate the correlation for the entire time series
overall_correlation = df["Stader-TVL-total"].corr(df["market_cap"])
print(
    f"Overall Correlation between 'Stader-TVL-total' and 'market_cap': {overall_correlation}"
)

# Group by quarter
df["Quarter"] = df["Date"].dt.to_period("Q")

# Calculate the correlation for each quarter
quarterly_correlations = df.groupby("Quarter").apply(
    lambda x: x["Stader-TVL-total"].corr(x["market_cap"])
)

# Output the results
print("\nQuarterly Correlations:")
print(quarterly_correlations)

# Comprehensive statistics for 'Stader-TVL-total'
lido_stats = df["Stader-TVL-total"].describe()

# Comprehensive statistics for 'market_cap'
market_cap_stats = df["market_cap"].describe()

# Output the statistics
print("\nStatistics for 'Stader-TVL-total':")
print(lido_stats)
print("\nStatistics for 'market_cap':")
print(market_cap_stats)

# Additional Statistics
print("\nAdditional Statistics:")
print(f"Skewness for 'Stader-TVL-total': {df['Stader-TVL-total'].skew()}")
print(f"Skewness for 'market_cap': {df['market_cap'].skew()}")
print(f"Kurtosis for 'Stader-TVL-total': {df['Stader-TVL-total'].kurt()}")
print(f"Kurtosis for 'market_cap': {df['market_cap'].kurt()}")

# Save the correlation results to a CSV if needed
quarterly_correlations.to_csv("quarterly_correlations_clean.csv")
