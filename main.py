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

@app.route('/phone/create/')
def phone_create():

    query_params = request.args
    value = int(query_params.get('value'))


    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = f"""
    INSERT INTO phones
    values (null, {value})
    """
    cur.execute(sql)
    con.commit()
    con.close()
    return 'Phone was Created'

@app.route('/phone/delete/')
def phones_delete():

    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = """
    DELETE FROM phones;
    """
    cur.execute(sql)
    con.commit()
    con.close()
    return 'All phones were deleted'

@app.route('/phone/list/')
def phone_list():

    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = """
    SELECT * FROM phones;
    """
    cur.execute(sql)
    phones_list = cur.fetchall()
    con.close()
    return str(phones_list)

@app.route('/phone/update/')
def phones_update():
    query_params = request.args
    value = int(query_params.get('value'))

    import sqlite3

    con = sqlite3.connect("./phones.db")
    cur = con.cursor()
    sql = f"""
    UPDATE phones SET value={value};
    """
    cur.execute(sql)
    con.commit()
    con.close()
    return 'All phones were updated'

if __name__ == "__main__":
    app.run()
