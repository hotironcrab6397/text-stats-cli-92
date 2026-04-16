import random
import string

def generate_password(size=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(size))
    return password

if __name__ == "__main__":
    print(generate_password())
