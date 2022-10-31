# Document: Report and Analysis of Attendance
# Created on: October 01, 2022, 9:00:00 PM
# Last Updated: October 30, 2022, 9:00:00 PM
# Author: Sushil Waghmare


from flask import Flask, render_template, request, flash
import mysql.connector
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sushil1024'


con = mysql.connector.connect(
    user="ueiforctqwwdmvnx",
    password="LDtM1YA1kKOzEfOeplHC",
    host="bzczr0tdsxjv3b9xkz8l-mysql.services.clever-cloud.com",
    database="bzczr0tdsxjv3b9xkz8l",
)

cur = con.cursor()


# the home page
@app.route("/")
def home():
    return render_template("home.html")


# authentication page
@app.route("/loginstaff")
def login():
    return render_template("loginstaff.html")


@app.route("/choice")
def choice():
    return render_template("choice.html")


@app.route("/entry", methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        stuname = request.form['stuname']
        gender = request.form['gender']
        country = request.form['country']
        contactno = request.form['contactno']
        city = request.form['city']
        age = request.form['age']
        emailid = request.form['emailid']

        cur.execute("INSERT INTO STUDENTS SELECT STUID+1, ROLLNO+1, %s, %s, %s, %s, %s, %s, %s, %s FROM STUDENTS ORDER BY STUID DESC LIMIT 1;", (stuname, gender, country, city, contactno, age, emailid))
        con.commit()

    return render_template("entry.html")


# input page to input roll number of the candidate
@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    data = ""
    if request.method == 'POST':

        # takes input here in post method
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        # taken inputs will be passed to another function for further process
        from searchdata import search
        search(studentrollno, mailch)
        cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
        data = cur.fetchall()
        # return render_template("example.html", value=data)
        # con.close()

    return render_template("input.html", value=data)


@app.route("/result")
def result():
    cur.execute("SELECT * FROM STUDENTS")
    temp = cur.fetchall()
    return render_template("result.html", temp=temp)


if __name__ == "__main__":
    app.run(debug=True)
