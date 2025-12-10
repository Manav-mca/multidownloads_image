import re

# text = int(input("Enter your phone number"))


# # Search for a 10-digit number
# match = re.search(r"\d{10}", text)

# if match:
#     print("Found:", match.group())
# else:
#     print("No match found")


# text = input("Enter your email !: ")

# # Find email
# email = re.search(r"\w+@\w+\.\w+", text)
# print("Email:", email.group() if email else "Not found")

# text2 = int(input("Enter your phone number! :"))
# phone = re.search(r"\d{3}\d{3}\d{4}", text2)
# print("Phone:", phone.group() if phone else "Not found")


import re

# Basic patterns
r"\d"      # Any digit (0-9)
r"\w"      # Any word character (a-z, A-Z, 0-9, _)
r"\s"      # Any whitespace
r"."       # Any character except newline
r"^"       # Start of string
r"$"       # End of string

# Quantifiers
r"\d+"     # One or more digits
r"\d*"     # Zero or more digits
r"\d?"     # Zero or one digit
r"\d{3}"   # Exactly 3 digits
r"\d{2,5}" # 2 to 5 digits

# Examples
text = "Email: user@example.com, Phone: 123-456-7890"

# Find email
email = re.search(r"\w+@\w+\.\w+", text)
print("Email:", email.group() if email else "Not found")

# Find phone
phone = re.search(r"\d{3}-\d{3}-\d{4}", text)
print("Phone:", phone.group() if phone else "Not found")

# Find all digits
digits = re.findall(r"\d+", text)
print("All numbers:", digits)

# Replace
clean_text = re.sub(r"\d", "X", text)
print("Masked:", clean_text)
