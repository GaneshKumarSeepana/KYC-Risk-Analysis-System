import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/kyc_output.csv')

# Count risk levels
risk_counts = df['Risk_Level'].value_counts()

# Plot pie chart
plt.figure(figsize=(6,6))
risk_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title('Customer Risk Distribution')

plt.show()

# Bar chart
plt.figure(figsize=(8,5))
risk_counts.plot(kind='bar')
plt.title('Risk Level Count')
plt.xlabel('Risk Level')
plt.ylabel('Number of Customers')

plt.show()