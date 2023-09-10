import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'your_dataset.csv' with your actual file path)
df = pd.read_csv('unnati_phase1_data_revised.csv')

# Assuming 'Time' is in the format 'HH:MM' (24-hour format)
# Extract the hour from the 'Time' column
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
val=['cas_fcw',"cas_pcw","cas_ldw","cas_hmw"]
# Create a bar plot to visualize the hourly rate of each crash indication
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Hour', hue='Alert')
plt.xlabel('Hour of the Day')
plt.ylabel('Count')
plt.title('Hourly Rate of Crash Indications')
plt.legend(title='Crash Indicator', loc='upper right')
plt.xticks(rotation=45)
plt.show()
