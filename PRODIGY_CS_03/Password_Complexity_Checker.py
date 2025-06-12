import re

def assess_password_strength(password):
    """Assess the strength of a given password based on 5 criteria."""
    has_numbers = any(char.isdigit() for char in password)
    has_upper_case = any(char.isupper() for char in password)
    has_lower_case = any(char.islower() for char in password)
    meets_length_requirement = len(password) >= 8
    has_special_characters = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    criteria_met = sum([
        has_numbers,
        has_upper_case,
        has_lower_case,
        meets_length_requirement,
        has_special_characters
    ])

    if criteria_met == 5:
        return " Password Strength: Very Strong (All criteria met)"
    elif criteria_met == 4:
        return " Password Strength: Strong (4 out of 5 criteria met)"
    elif criteria_met == 3:
        return " Password Strength: Moderate (3 out of 5 criteria met)"
    else:
        return " Password Strength: Weak (Less than 3 criteria met)"

def display_tips():
    print("---------------------------------------------------------------")
    print("Tips for Creating a Strong and Secure Password:")
    print("---------------------------------------------------------------")
    tips = [
        "1. Use at least 12 characters for better strength.",
        "2. Mix uppercase, lowercase, numbers, and symbols.",
        "3. Avoid common words or repeated characters.",
        "4. Don’t use personal info (e.g., birth dates, names).",
        "5. Create a passphrase from multiple unrelated words.",
        "6. Use different passwords for each account.",
        "7. Change your passwords regularly.",
        "8. Enable 2FA (Two-Factor Authentication).",
        "9. Watch out for phishing websites.",
        "10. Use a password manager to keep track securely."
    ]
    for tip in tips:
        print(tip)

def mask_password(password):
    """Mask the password for display (show first and last characters only)."""
    if len(password) > 2:
        return password[0] + "#" * (len(password) - 2) + password[-1]
    else:
        return "*" * len(password)

def main():
    print("\n================ Password Strength Checker =================\n")
    display_tips()

    password = input("\n Enter the password to check: ").strip()

    if not password:
        print(" Password cannot be empty. Please try again.")
        return

    masked = mask_password(password)
    result = assess_password_strength(password)

    print("\n---------------------------------------------------------------")
    print(f"Masked Password: {masked}")
    print(result)
    print("---------------------------------------------------------------\n")

if __name__ == "__main__":
    main()

