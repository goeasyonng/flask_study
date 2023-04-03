from flaskext.mysql import MySQL
from flask import Flask
from flask import jsonify
from flask import request
import random
from random import randrange

app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'dbmasteruser'
app.config['MYSQL_DATABASE_PASSWORD'] = '123123123'
app.config['MYSQL_DATABASE_HOST'] = 'ls-ed7c6cfd2a9a01bf9411cda04bb53b7583775cb8.ce9zqwpjj5xx.ap-northeast-2.rds.amazonaws.com'
app.config['MYSQL_DATABASE_DB'] = 'db1'
mysql.init_app(app)

@app.route("/generate_user", methods=['GET'])
def userGenerate(): # 유저 랜덤 생성 후 생성된 유저 보여주기

    # 유저생성 코드
    password_list = []
    name_list = []
    gender_list = []
    birthday_list = []
    age_list = []
    company_list = []

    for i in range(10):
        last_name = ["김", "미", "박", "황", "이"]
        first_name = ["보", "인", "지", "사", "모", "태", "하", "주", "희", "모", "태", "병", "건"]

        password = randrange(1000,9999,1)
        name = str(random.choice(last_name)) + str(random.choice(first_name)) + str(random.choice(first_name))
        gender = random.choice(["male", "female"])
        birthday = randrange(600000, 999999,1)
        age = randrange(1, 100, 1)
        company = random.choice(["samsung", "lg", "hyundai"])

        password_list.append(password)
        name_list.append(name)
        gender_list.append(gender)
        birthday_list.append(birthday)
        age_list.append(age)
        company_list.append(company)

    # db 코드
    conn = mysql.connect()
    cursor = conn.cursor()

    for i in range(10):
        cursor.execute(
            f"""
            INSERT INTO 
                user(id,password, name, gender, birthday, age, company) 
            VALUES
                ('{password_list[i]}', '{name_list[i]}', '{gender_list[i]}', 
                '{birthday_list[i]}', {age_list[i]}, '{company_list[i]}')
            """
        )
        
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'result':"success"})
