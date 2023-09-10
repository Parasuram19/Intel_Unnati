import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (replace 'your_dataset.csv' with your actual file path)
df = pd.read_csv('unnati_phase1_data_revised.csv')

# Create a scatter plot to visualize the relationship between speed and alert indications
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Speed', y='Alert', alpha=0.5)
plt.xlabel('Speed')
plt.ylabel('Alert Indication')
plt.title('Speed vs. Alert Indications')
plt.grid(True)
plt.show()
