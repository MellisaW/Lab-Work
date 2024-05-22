import pandas as pd
import re

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


male_students = df[df['Gender'] == 'M']
female_students = df[df['Gender'] == 'F']

with pd.ExcelWriter('separated_students.xlsx') as writer:
    male_students.to_excel(writer, sheet_name='Male Students', index=False)
    female_students.to_excel(writer, sheet_name='Female Students', index=False)

num_male_students = len(male_students)
num_female_students = len(female_students)

print("Number of Male Students:", num_male_students)
print("Number of Female Students:", num_female_students)

print("Male Students:")
print(male_students)
print("\nFemale Students:")
print(female_students)

pattern = r'[^\w\s]'

names_with_special_chars = df[df['Student Name'].str.contains(pattern, na=False)]

print("Names of students with special characters:")
print(names_with_special_chars['Student Name'])


df.to_csv("student_emails.csv", index=False)
df.to_csv("student_emails.tsv", sep='\t', index=False)




merged_df = pd.concat([male_students, female_students], ignore_index = True)

shuffled_df = merged_df.sample(frac=1).reset_index(drop=True)

shuffled_df.to_json("shuffled_data.json", orient="records")

shuffled_df.to_json("shuffled_data.json1", orient="records", lines=True)



import json

import random


with open('shuffled_data.json', 'r') as file:
    shuffled_data = json.load(file)

combined_data = {
    "id": "0",
    "student_number": "123449",
    "additional_details": [
        {
            "dob": "2000-2-27",
            "gender": "m",
            "special_character": ["yes"],
            "name_similar": ["no"]
        }
    ]
}

with open('combined_data.json2', 'w') as file:
    for detail in combined_data["additional_details"]:
        json.dump(detail, file)
        file.write('\n')

















