import pandas as pd

import logging

from functions import generate_email

from constraints import generate_email_with_uniqueness

df = pd.read_excel("Test Files.xlsx")

df['Email'] = df['Student Name'].apply(generate_email)

df['Email'] = df['Email'].apply(generate_email_with_uniqueness)

df.to_csv("output.csv", index=False)
df.to_csv("student_emails.csv", index=False)
df.to_csv("student_emails.tsv", sep='\t', index=False)


male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

num_male_students = len(male_students)
num_female_students = len(female_students)

print("Number of Male Students:", num_male_students)
print("Number of Female Students:", num_female_students)


