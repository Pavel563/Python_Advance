import string
import random
from faker import Faker
import csv
import requests


def generate_password(length: int = 10) -> str:
    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)

    return password


def generate_users(count: int = 100):
    fake = Faker()
    users = []
    for user in range(count):
        string_line = [chr(number) for number in range(ord('a'), ord('z') + 1)]
        string_line = ''.join([random.choice(string_line) for element in range(random.randint(5, 7))])
        email = string_line + '@gmail.com'
        name = str(fake.name())
        user = {'name': name, 'email': email}

        users.append(user)

    return users


def requirements():
    with open("requirements.txt", "r") as file:
        data = file.read()
        return data


def mean_def():
    with open("hw (2) (1).csv", "r") as file:
        reader = csv.DictReader(file)
        weight_sum = 0
        height_sum = 0
        count = 0
        for line in reader:
            count += 1
            weight = line['Weight(Pounds)'].lstrip()
            height = line['Height(Inches)'].lstrip()
            weight_sum += float(weight)
            height_sum += float(height)
        weight = weight_sum / count
        height = height_sum / count
        height = int(height) * 2.54
        weight = int(weight) / 2.205
        data = {'Средний вес(кг)': weight, 'Средний рост(см)': height}
    return data


def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    r = dict(r.json())
    count = str(r['number'])
    return f"Количество космонавтов в настоящий момент:{count}"
