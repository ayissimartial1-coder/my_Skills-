import re

user_name = input("Enter your username: ")
password = input("Enter your password: ")

def password_strength(password):
        if password.lower() == user_name.lower() or password.upper() == user_name.upper():
             return "Red flag: Password should not be the same as the username"
        
        elif len(password) < 10 and not (re.search(r'[@$!%*?&]', password) or re.search(r'[A-Z]', password) or re.search(r'[a-z]', password) or re.search(r'[0-9]', password)):
            return "Weak flag: Password must be at least 10 characters long and include a special character"
        
        elif re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password) and re.search(r'[@$!%*?&]', password):
            return "Strong password"
        else:
            return "Medium"

strength = password_strength(password)
print(f"Password strength: {strength}")