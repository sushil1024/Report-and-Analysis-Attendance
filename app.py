# Document: Report and Analysis of Attendance
# Created on: October 01, 2022, 9:00:00 PM
# Last Updated: October 30, 2022, 9:00:00 PM
# Author: Sushil Waghmare


from flask import Flask, render_template, request, send_from_directory
import mysql.connector
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sushil1024'


con = mysql.connector.connect(
    user="ueiforctqwwdmvnx",
    password="LDtM1YA1kKOzEfOeplHC",
    host="bzczr0tdsxjv3b9xkz8l-mysql.services.clever-cloud.com",
    database="bzczr0tdsxjv3b9xkz8l",
)

# used to test on local machine
# con = mysql.connector.connect(
#     user="root",
#     password="r00t",
#     host="localhost",
#     database="fynd"
# )

cur = con.cursor()


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


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
        stuname = request.form.get('stuname')
        gender = request.form.get('gender')
        country = request.form.get('country')
        city = request.form.get('city')
        contactno = request.form.get('contactno')
        age = request.form.get('age')
        emailid = request.form.get('emailid')
        attend = request.form.get('attend')

        cur.execute("INSERT INTO STUDENTS SELECT STUID+1, ROLLNO+1, %s, %s, %s, %s, %s, %s, %s, %s FROM STUDENTS ORDER BY STUID DESC LIMIT 1", [stuname, gender, country, city, contactno, age, emailid, attend])
        con.commit()

    return render_template("entry.html")


# input page to input roll number of the candidate
@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':

        # takes input here in post method
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
        data = cur.fetchall()
        print(data)

        if len(data) == 0:
            return render_template("notfoundstu.html")
        else:
            # taken inputs will be passed to another function for further process
            from searchdata import search
            search(studentrollno, mailch)
            return render_template("resultone.html", temp=data)
        # con.close()

    return render_template("input.html")


@app.route("/delroll", methods=['GET', 'POST'])
def delroll():
    if request.method == 'POST':
        studentrollno = request.form['studentrollno']
        cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
        data = cur.fetchall()
        if len(data) == 0:
            return render_template("notfound.html")
        cur.execute("DELETE FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
        con.commit()

    return render_template("delroll.html")


@app.route("/resultframe")
def resultframe():
    cur.execute("SELECT * FROM STUDENTS")
    temp = cur.fetchall()
    return render_template("resultframe.html", temp=temp)


@app.route("/result")
def result():
    cur.execute("SELECT * FROM STUDENTS")
    temp = cur.fetchall()
    return render_template("result.html", temp=temp)


if __name__ == "__main__":
    app.run(debug=True)
