import pandas as pd

df = pd.read_excel("Test Files.xlsx")

generated_emails = set()

from functions import generate_email
def generate_email_with_uniqueness(name):
    email = generate_email(name)
    while email in generated_emails:
        email = generate_email(name)
    generated_emails.add(email)
    return email

df['Email'] = df['Student Name'].apply(generate_email_with_uniqueness)


male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

with pd.ExcelWriter('separated_students.xlsx') as writer:
    male_students.to_excel(writer, sheet_name='Male Students', index=False)
    female_students.to_excel(writer, sheet_name='Female Students', index=False)