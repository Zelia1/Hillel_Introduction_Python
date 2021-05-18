from flask import Flask, request
from utils import read_requirements
from utils import random_users
from utils import average_weight_and_height
from utils import mans_in_space_now

app = Flask("MyApplication")


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/requirements/')
def requiremets():
    return read_requirements()


@app.route('/generate-users/')
def generate_users():
    query_params = request.args
    default_number_user = 100
    minimum_number_user = 1
    maximum_number_user = 1000
    number_user = query_params.get('number_user') or ''
    if number_user.isdigit():
        number_user = int(number_user)
        if number_user < minimum_number_user or number_user > maximum_number_user:
            number_user = default_number_user
    else:
        number_user = default_number_user
    return random_users(number_user)


@app.route('/mean/')
def average_output():
    return average_weight_and_height()

@app.route('/space/')
def mans_in_space():
    return mans_in_space_now()

if __name__ == "__main__":
    app.run()