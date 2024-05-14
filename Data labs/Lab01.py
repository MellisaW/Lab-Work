import pandas as pd

df = pd.read_excel("Test Files.xlsx")


def generate_email(name):
    parts = name.split()

    first_initial = parts[0][0]

    last_name = parts[-1]

    last_name = ''.join(e for e in last_name if e.isalnum())

    email = f"{first_initial}{last_name.lower()}@gmail.com"

    return email


df['Email'] = df['Student Name'].apply(generate_email)

print(df)

generated_emails = set()
def generate_email_with_uniqueness(name):
    email = generate_email(name)
    while email in generated_emails:
        email = generate_email(name)
    generated_emails.add(email)
    return email

df['Email'] = df['Student Name'].apply(generate_email_with_uniqueness)


df.to_csv("student_emails.csv", index=False)
df.to_csv("student_emails.tsv", sep='\t', index=False)







