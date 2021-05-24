from faker import Faker
import random
import string
import re
import csv
import requests


def read_requirements() -> str:
    requirements = open("requirements.txt", "r")
    result_read = requirements.readlines()
    list_requirements = []
    for index in range(len(result_read)):
        list_requirements.append(result_read[index][:-2])
    result = "\n".join(list_requirements)
    return result



def random_users(number_user: int = 100) -> str:
    fake = Faker()
    users_list = []

    for _ in range(number_user):
        letters = string.ascii_letters
        random_name = "".join([fake.name()])
        result_name = re.findall(r'[A-Z][a-z]*\b', random_name)
        random_symbols_list = [letters[random.randint(0, len(letters) - 1)] for _ in range(random.randint(5, 15))]
        random_symbols = "".join(random_symbols_list)
        user = "".join([f"{result_name[0]} {random_symbols}@mail.com"])
        users_list.append(user)
        users_list.append("\n")

    return "".join(users_list)


def average_weight_and_height() -> str:
    list_inches = []
    list_pounds = []


    with open("hw.csv") as file:
        reader = csv.DictReader(file)

        for row in reader:
            list_inches.append(float(row[' "Height(Inches)"']))
            list_pounds.append(float(row[' "Weight(Pounds)"']))

    average_height_centimeters = sum(list_inches) / len(list_inches) * 2.54
    average_weight_kg = sum(list_pounds) / len(list_pounds) / 2.205
    result_data = f"{str(average_height_centimeters)}, {str(average_weight_kg)}"

    return result_data


def mans_in_space_now() -> str:

    r = requests.get("http://api.open-notify.org/astros.json")
    result = r.json()["number"]
    return str(result)


