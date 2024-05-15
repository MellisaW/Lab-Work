import pandas as pd

from functions import generate_email

from constraints import generate_email_with_uniqueness

from constraints import determine_gender

df = pd.read_excel("Test Files.xlsx")

df['Email'] = df['Student Name'].apply(generate_email)

df['Email'] = df['Email'].apply(generate_email_with_uniqueness)

df.to_csv("output.csv", index=False)
df.to_csv("student_emails.csv", index=False)
df.to_csv("student_emails.tsv", sep='\t', index=False)

df['Gender'] = df['Student Name'].apply(determine_gender)

male_students = df[df['Gender'] == 'Male']
female_students = df[df['Gender'] == 'Female']

num_male_students = len(male_students)
num_female_students = len(female_students)

print("Number of Male Students:", num_male_students)
print("Number of Female Students:", num_female_students)



