import time
import random
import string

def generate_unique_email():
    cohort_number = "22"
    numbers = ''.join(random.choices(string.digits, k=3))
    return f"sartayev_madi_{cohort_number}_{numbers}@yandex.kz"

def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))