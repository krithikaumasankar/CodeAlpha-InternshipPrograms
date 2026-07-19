import re

with open("input.txt", "r") as file:
    content = file.read()

emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', content)

with open("emails.txt", "w") as file:
    if emails:
        for email in emails:
            file.write(email + "\n")
    else:
        file.write("No email addresses found.")

print("Email extraction completed successfully.")
print("Extracted", len(emails), "email address(es).")
