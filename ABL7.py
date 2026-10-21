
print("Password Policy Validation Engine")

password = input("Enter your password: ")

if len(password) < 8:
    print("Invalid Password: Must contain at least 8 characters")
elif not any(ch.isupper() for ch in password):
    print("Invalid Password: Must contain an uppercase letter")
elif not any(ch.islower() for ch in password):
    print("Invalid Password: Must contain a lowercase letter")
elif not any(ch.isdigit() for ch in password):
    print("Invalid Password: Must contain a number")
elif not any(not ch.isalnum() for ch in password):
    print("Invalid Password: Must contain a special character")
else:
    print("Valid Password!")
