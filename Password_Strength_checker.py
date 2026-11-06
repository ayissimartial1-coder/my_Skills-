import string
import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("- Make it longer (at least 12 characters recommended).")
    else:
        feedback.append("- Password is too short (minimum 8 characters required).")
            
    common_weak_words = ["password", "123456", "admin", "welcome", "qwerty"]
    if password.lower() in common_weak_words:
        score -= 2
        feedback.append("- Avoid common dictionary words or predictable patterns.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("- Add uppercase letters (A-Z).")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("- Add lowercase letters (a-z).")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("- Add numbers (0-9).")

    special_chars = re.escape(string.punctuation)
    if re.search(f'[{special_chars}]', password):
        score += 1
    else:
        feedback.append("- Add special characters (e.g., !, @, #, $).")

    if score >= 6:
        strength = "Strong 🟢"
    elif score >= 4:
        strength = "Medium 🟡"
    else:
        strength = "Weak 🔴"

    return strength, feedback

if __name__ == "__main__":
    user_password = input("Enter a password to test its strength: ")
    rating, suggestions = check_password_strength(user_password)
    
    print(f"\nPassword Strength: {rating}")
    
    if suggestions:
        print("\nSuggestions to make it stronger:")
        for tip in suggestions:
            print(tip)
