import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'your_dataset.csv' with your actual file path)
df = pd.read_csv("unnati_phase1_data_revised.csv")

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Visualize the distribution of numerical features
numeric_features = df.select_dtypes(include=['float64', 'int64'])
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))

for i, col in enumerate(numeric_features.columns):
    plt.subplot(2, 2, i + 1)
    sns.histplot(data=df, x=col, kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

# Visualize the relationship between variables (e.g., scatter plots)
sns.pairplot(df[numeric_features.columns])
plt.show()

# Visualize categorical data (e.g., 'Alert' column)
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Alert')
plt.xticks(rotation=45)
plt.title('Distribution of Alert Types')
plt.show()

# Temporal analysis (e.g., date and time)
df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Alert'])
plt.xlabel('Date')
plt.ylabel('Alert')
plt.title('Crash Indicator Over Time')
plt.grid(True)
plt.show()
