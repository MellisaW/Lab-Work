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


def determine_gender(name):
    last_letter = name.split()[0][-1].lower()
    if last_letter in ['a', 'e', 'y']:
        return 'Female'
    else:
        return 'Male'

df['Gender'] = df['Student Name'].apply(determine_gender)