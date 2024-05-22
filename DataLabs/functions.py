import pandas as pd

df = pd.read_excel("Test Files.xlsx")
def generate_email(name):
    parts = name.split()

    first_initial = parts[0][0]

    last_name = parts[-1]

    last_name = ''.join(e for e in last_name if e.isalnum())

    email = f"{first_initial}{last_name.lower()}@gmail.com"

    return email


df['Email Address'] = df['Student Name'].apply(generate_email)

print(df)