# Document: Report and Analysis of Attendance
# Created on: October 01, 2022, 9:00:00 PM
# Last Updated: October 21, 2022, 9:00:00 PM
# Author: Sushil Waghmare


from flask import Flask, render_template, request, flash
import mysql.connector
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sush1024'


con = mysql.connector.connect(
    user="root",
    password="r00t",
    host="localhost",
    database="fynd",
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


@app.route("/entry", methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        stuname = request.form['stuname']
        gender = request.form['gender']
        country = request.form['country']
        contactno = request.form['contactno']
        city = request.form['city']
        age = request.form['age']
        dob = datetime.datetime.strptime(request.form['dob'], '%Y-%m-%d')
        emailid = request.form['emailid']

        cur.execute("INSERT INTO STUDENTS SELECT STUID+1, ROLLNO+1, %s, %s, %s, %s, %s, %s, DATE_FORMAT(%s, '%d %M %Y'), %s, 30 FROM STUDENTS ORDER BY STUID DESC LIMIT 1;", (stuname, gender, country, city, contactno, age, dob, emailid))
        con.commit()


        # stuname = "sunil waghmare"
        # gender = "male"
        # country = "india"
        # contactno = "1234567890"
        # city = "mumbai"
        # age = "53"
        # dob = "1969-10-22"
        # emailid = "sushilwaghmare2048@gmail.com"
        #
        # cur.execute("INSERT INTO STUDENTS SELECT STUID+1, ROLLNO+1, %s, %s, %s, %s, %s, %s, DATE_FORMAT(%s, '%d %M %Y'), %s, 30 FROM STUDENTS ORDER BY STUID DESC LIMIT 1;", (stuname, gender, country, city, contactno, age, dob, emailid))
        # con.commit()

    return render_template("entry.html")


# input page to input roll number of the candidate
@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':

        # takes input here in post method
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        # taken inputs will be passed to another function for further process
        from searchdata import search
        search(studentrollno, mailch)

    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
