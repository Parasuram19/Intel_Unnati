import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'your_dataset.csv' with your actual file path)
df = pd.read_csv('unnati_phase1_data_revised.csv')

# Assuming 'Time' is in the format 'HH:MM' (24-hour format)
# Extract the hour from the 'Time' column
df['Hour'] = pd.to_datetime(df['Time']).dt.hour

# Define a threshold for distinguishing day and night (e.g., 6 AM to 6 PM)
daytime_threshold = (6, 18)

# Create a new column 'DayNight' based on the threshold
df['DayNight'] = df['Hour'].apply(lambda x: 'Day' if daytime_threshold[0] <= x < daytime_threshold[1] else 'Night')

# Create a bar plot to visualize the counts of each crash indicator during Day vs. Night
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Alert', hue='DayNight')
plt.xticks(rotation=45)
plt.xlabel('Crash Indicator')
plt.ylabel('Count')
plt.title('Crash Indicators during Day vs. Night')
plt.legend(title='DayNight')
plt.show()
