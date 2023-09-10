import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV dataset
dataset_path = "C:/Users/nv271/Downloads/cas_ldw.csv"
date_parser = lambda x: pd.to_datetime(x, dayfirst=True, errors='coerce')
df = pd.read_csv(dataset_path, parse_dates=[['Date', 'Time']], date_parser=date_parser)

# Convert the 'Speed' column to numeric
df['Speed'] = pd.to_numeric(df['Speed'], errors='coerce')

# Extract the 'hour' component from the 'Date_Time' column and store it in a new 'hour' column
# This will allow us to analyze data based on the hour of the day
df['hour'] = df['Date_Time'].dt.hour

# Create a new column 'prev_collision' that contains the 'Alert' values shifted by 1 position
# This will help us track the previous collision type for each row
df['prev_collision'] = df['Alert'].shift(1)

# Group the DataFrame by the combinations of 'prev_collision' and 'Alert' columns
# Calculate the size of each group (number of occurrences) and reshape the result as a matrix (unstack)
# Fill missing values with 0 to indicate no occurrences for certain combinations
sequence_counts = df.groupby(['prev_collision', 'Alert']).size().unstack().fillna(0)

# Define the order of Alert categories
alert_order = ['cas_pcw', 'cas_hmw', 'cas_fcw', 'cas_ldw']

# #Temporal patterns - Collisions by hour of the day
# hourly_counts = df.groupby('hour')['Alert'].value_counts().unstack().fillna(0)
# hourly_counts.plot(kind='bar', stacked=True)
# plt.title('Hourly Collision Distribution')
# plt.xlabel('Hour')
# plt.ylabel('Number of Collisions')
# plt.show()

# Spatial patterns - Collision heat map
lat_step_index = 5
long_step_index = 5

# Select latitude and longitude data based on the step indices
selected_lat = df['Lat'][::lat_step_index]
selected_long = df['Long'][::long_step_index]

# Create a scatterplot using the selected data
plt.figure(figsize=(10, 8))
sns.scatterplot(x=selected_long, y=selected_lat, hue='Alert', data=df)
plt.title('Collision Locations')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()

# # Speed patterns - Collisions by speed
# # Create the boxplot with specified category order
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Alert', y='Speed', data=df, order=alert_order)
# plt.title('Collision Types by Speed')
# plt.xlabel('Collision Type')
# plt.ylabel('Speed')
# plt.show()
#
# # Correlations
# numerical_columns = df.select_dtypes(include=['number'])  # Select only numerical columns
#
# # Check for missing values in the numerical columns
# missing_values = numerical_columns.isnull().sum()
# if missing_values.any():
#     print("Warning: There are missing values in the numerical columns.")
#     print("Missing Value Counts:\n", missing_values)
#
# # Calculate the correlation matrix
# correlation_matrix = numerical_columns.corr()
#
# plt.figure(figsize=(10, 8))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix')
# plt.xlabel('Features')
# plt.ylabel('Features')
# plt.show()
#
# # Sequences
# sequence_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
# plt.title('Collision Sequences')
# plt.xlabel('Previous Collision Type')
# plt.ylabel('Number of Occurrences')
# plt.legend(title='Current Collision Type')
# plt.show()
#
# # Anomaly Detection - Speed outliers
# plt.figure(figsize=(10, 6))
# sns.boxplot(x='Alert', y='Speed', data=df, order=alert_order)
# plt.title('Collision Types by Speed (with Outliers)')
# plt.xlabel('Collision Type')
# plt.ylabel('Speed')
# plt.ylim(0, df['Speed'].quantile(0.95))  # Limit y-axis to remove extreme outliers
# plt.show()