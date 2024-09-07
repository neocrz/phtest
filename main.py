import hashlib
import base64
import getpass


def ask_input(prompt):
    while True:
        value = getpass.getpass(prompt)
        confirm_value = getpass.getpass("Confirm " + prompt.lower())

        if value == confirm_value:
            return value
        else:
            print("Inputs do not match. Please try again.\n")


def generate(key, m, length=16):
    combined = key + m
    hash_object = hashlib.sha256(combined.encode())

    # Convert the hash to base64 to make it more readable and password-friendly
    pw = base64.urlsafe_b64encode(hash_object.digest()).decode('utf-8')

    # Return the first 'length' characters of the password
    return pw[:length]

# Main part of the script

# Ask for master password with confirmation (hidden input)
m = ask_input("Enter m: ")

# Ask for site key (hidden input)
key = ask_input("Enter the key: ")

# Generate and print the password
pw = generate(key, m, length=32)
print(f"\nGenerated: {pw}")
