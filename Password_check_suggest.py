import random
import string

def generate_password(length=12):
    """Generate a random password."""
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def validate_and_suggest_password(user_password):
    """Validate user's password and suggest a strong password if needed."""
    if len(user_password) < 8:
        print("Password must be at least 8 characters long.")
        return generate_password()
    
    if not re.search(r'[a-z]', user_password):
        print("Password must contain at least one lowercase letter.")
        return generate_password()
    
    if not re.search(r'[A-Z]', user_password):
        print("Password must contain at least one uppercase letter.")
        return generate_password()
    
    if not re.search(r'\d', user_password):
        print("Password must contain at least one digit.")
        return generate_password()
    
    if not re.search(r'[@#$%^&*(),.?":{}|<>]', user_password):
        print("Password must contain at least one special character.")
        return generate_password()
    
    print("Your password is strong!")
    return user_password

## Get password from the user ##
user_password = input("Enter your password: ")

## Validate and suggest a strong password if needed ##
strong_password = validate_and_suggest_password(user_password)
print("Suggested strong password:", strong_password)
