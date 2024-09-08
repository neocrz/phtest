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


def generate(key, m, length=32):
    combined = key + m
    hash_object = hashlib.sha256(combined.encode())

    pw = base64.urlsafe_b64encode(hash_object.digest()).decode('utf-8')

    return pw[:length]

m = ask_input("Enter m: ")

def main():
    while(True):
        size = input("Enter key size (default 32): ")
        size = (int(size) if len(size) != 0 else 32)
        key = ask_input("Enter the key: ")
        pw = generate(key, m, length=size)
        print(f"\nGenerated: {pw}\n")

if __name__ == '__main__':
    main()
