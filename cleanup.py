import pandas as pd

### Due to time constraints the development of this code was aided by google gemini
df = pd.read_csv('finance.csv')

df_loans = df[df['has_loan'] == 'Yes'].copy()

selected_cols = [
    'age', 'gender', 'education_level', 'employment_status', 
    'monthly_income_usd', 'monthly_expenses_usd', 'savings_usd', 'loan_interest_rate_pct'
]
df_final = df_loans[selected_cols]

categorical_cols = ['gender', 'education_level', 'employment_status']

for col in categorical_cols:
    df_final[col] = df_final[col].astype('category').cat.codes

df_final.head(13000).to_csv('cleaned_finance.csv', index=False)

print("Cleaning complete. Categorical variables encoded.")
print(df_final.head())