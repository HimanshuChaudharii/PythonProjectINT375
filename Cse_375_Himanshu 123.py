import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
df = pd.read_csv("C:\\Users\\acer\\Downloads\\Traffic_Volumes_AADT (1).csv")
# 1.Load and inspect the dataset

# Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())
# Dataset information (columns, non-null counts, data types)
print("\nDataset Info:")
print(df.info())
# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())
# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())
'''
#2. Handling missing data
'''
#Check for missing values
print("Missing Values (Count):")
print(df.isnull().sum())

print("\nMissing Values (%):")
print((df.isnull().sum() / len(df)) * 100)

#Drop rows with any missing values (if appropriate)
df_dropped_rows = df.dropna()
print("\nData shape after dropping rows with missing values:", df_dropped_rows.shape)

#Drop columns with any missing values (if appropriate)
df_dropped_columns = df.dropna(axis=1)
print("Data shape after dropping columns with missing values:", df_dropped_columns.shape)
'''
#3. Convert a columns to numpy array and perform a calculation
'''
# Step 1: Clean column names
df.columns = df.columns.str.strip()

# Step 2: Confirm column names (optional)
print("Available columns:")
print(df.columns.tolist())

# Step 3: Select 'BACK_AADT' for conversion
column_name = 'BACK_AADT'

# Check if column exists
if column_name in df.columns:
    # Convert to NumPy array
    column_array = df[column_name].to_numpy()

    # Handle potential missing values (optional)
    column_array = np.nan_to_num(column_array, nan=0)

    # Perform calculations
    mean_value = np.mean(column_array)
    squared_array = np.square(column_array)

    # Output
    print(f"\nFirst 5 values in '{column_name}':", column_array[:5])
    print(f"Mean of '{column_name}': {mean_value}")
    print(f"First 5 squared values:", squared_array[:5])
else:
    print(f"\nError: Column '{column_name}' not found.")
'''
#4. create a linePlot to show Traffic trends overtime
'''
# Step 1: Clean column names (remove leading/trailing spaces)
df.columns = df.columns.str.strip()

# Step 2: Handle missing data
# Show missing value count per column
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Drop rows where BOTH BACK_AADT and AHEAD_AADT are missing
df = df.dropna(subset=['BACK_AADT', 'AHEAD_AADT'], how='all')

# Fill remaining missing values with 0
df[['BACK_AADT', 'AHEAD_AADT']] = df[['BACK_AADT', 'AHEAD_AADT']].fillna(0)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

# Step 3: Simulate time axis using row numbers
df['Time'] = range(1, len(df) + 1)

# Step 4: Plot traffic volume trends over simulated time
plt.figure(figsize=(12, 5))
plt.plot(df['Time'], df['BACK_AADT'], marker='o', linestyle='-', color='blue', label='Back AADT')
plt.plot(df['Time'], df['AHEAD_AADT'], marker='x', linestyle='-', color='green', label='Ahead AADT')
plt.xlabel("Time (Simulated)")
plt.ylabel("Traffic Volume (AADT)")
plt.title("Traffic Volume Trend Over Simulated Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#5. Create a barplot for monthly traffic trends
# Clean column names
df.columns = df.columns.str.strip()

# Handle missing data
df = df.dropna(subset=['BACK_AADT', 'AHEAD_AADT'], how='all')
df[['BACK_AADT', 'AHEAD_AADT']] = df[['BACK_AADT', 'AHEAD_AADT']].fillna(0)

# Create fake 'Date' column (daily starting from Jan 2023)
df['Date'] = pd.date_range(start='2023-01-01', periods=len(df), freq='D')

# Extract month name
df['Month'] = df['Date'].dt.strftime('%B')

# Create 'Total_Traffic' column
df['Total_Traffic'] = df['BACK_AADT'] + df['AHEAD_AADT']

# Group by month and sum total traffic
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']

monthly_total = df.groupby('Month')['Total_Traffic'].sum().reindex(month_order).dropna()

# Plot using matplotlib
plt.figure(figsize=(12, 6))
plt.bar(monthly_total.index, monthly_total.values, color='orange')
plt.xlabel("Month")
plt.ylabel("Total Traffic Volume")
plt.title("Monthly Traffic Volume Trends")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
