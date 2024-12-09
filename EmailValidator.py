Special = " !#$%^&*()+="

def validate_email(email):
    """Function that ensures the users input is an email"""
    if "@" not in email or "." not in email:
        return "Email must contain '@' and '.'"
    if any(char in Special for char in email):
        return "Email contains invalid characters."
    return "Email is valid."

# Prompt the user for input
email = input("Enter an email address: ")
print(validate_email(email))
