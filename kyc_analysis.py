import pandas as pd

# Load dataset
df = pd.read_csv('data/customer_data.csv')

# Risk calculation function
def calculate_risk(row):
    risk_score = 0

    # PAN not verified
    if row['PAN_Verified'] == 'No':
        risk_score += 2

    # Address not verified
    if row['Address_Verified'] == 'No':
        risk_score += 1

    # High transaction amount
    if row['Transaction_Amount'] > 50000:
        risk_score += 2

    # Suspicious country
    if row['Country'] == 'Unknown' or row['Country'] == 'Nigeria':
        risk_score += 1

    # Risk classification
    if risk_score >= 4:
        return 'High Risk'
    elif risk_score >= 2:
        return 'Medium Risk'
    else:
        return 'Low Risk'

# Apply risk logic
df['Risk_Level'] = df.apply(calculate_risk, axis=1)

# Save output
df.to_csv('data/kyc_output.csv', index=False)

# Display output
print("KYC Risk Analysis Completed")
print(df)