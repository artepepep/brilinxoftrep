import random
import string


def generate_password(length: int):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def get_username_from_email(email: str):
    index_of_email_symbol = email.index('@')
    username = email[:index_of_email_symbol]
    return username