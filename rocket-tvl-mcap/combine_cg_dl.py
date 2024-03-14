import pandas as pd

# Step 1: Initialize the name for the new file
new_file = "rocket_combined_cg_dl_data.csv"

# Step 2: Read the data from lido_formatted.csv and select required columns
lido_df = pd.read_csv("rocket_formatted.csv")[["Date", "Rocket-TVL"]]

# Create a new dataframe with selected columns
combined_df = lido_df.copy()

# Step 3: Read the data from ldo-usd-max_formatted.csv
ldo_df = pd.read_csv("rpl-usd-max_formatted.csv")

# Ensure the 'Date' column is in string format for proper comparison
combined_df["Date"] = combined_df["Date"].astype(str)

# Iterate through the ldo-usd-max_formatted.csv DataFrame
for index, row in ldo_df.iterrows():
    # Find the matching date in combined_df
    match = combined_df["Date"] == row["snapped_at"]
    if match.any():
        # If a match is found, copy the 'market_cap' value to the new dataframe
        combined_df.loc[match, "market_cap"] = row["market_cap"]

# Save the new dataframe to a CSV file
combined_df.to_csv(new_file, index=False)

print(f"New file '{new_file}' created with updated data.")
