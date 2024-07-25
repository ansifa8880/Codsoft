import random
import string

def generate_password(length, complexity):
    if complexity == "Weak":
        characters = string.ascii_lowercase
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter password length: "))
    complexity = input("Enter password complexity (Weak, Medium, Strong): ")
    password = generate_password(length, complexity)
    print("Generated Password: ", password)

if __name__ == "__main__":
    main()



