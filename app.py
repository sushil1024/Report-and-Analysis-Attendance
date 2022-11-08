# Document: Report and Analysis of Attendance
# Created on: October 01, 2022, 9:00:00 PM
# Last Updated: November 04, 2022, 9:00:00 PM
# Author: Sushil Waghmare


from flask import Flask, render_template, request, send_from_directory, flash
import mysql.connector
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sushil1024'


# connection for mysql database
con = mysql.connector.connect(
    user="ueiforctqwwdmvnx",
    password="LDtM1YA1kKOzEfOeplHC",
    host="bzczr0tdsxjv3b9xkz8l-mysql.services.clever-cloud.com",
    database="bzczr0tdsxjv3b9xkz8l",
)


# database cursor
cur = con.cursor()


# the fav icon
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


# choice page for admin
@app.route("/choice")
def choice():
    return render_template("choice.html")


# add a student
@app.route("/entry", methods=['GET', 'POST'])
def entry():
    flash("")
    if request.method == 'POST':
        stuname = request.form.get('stuname')
        gender = request.form.get('gender')
        country = request.form.get('country')
        city = request.form.get('city')
        contactno = request.form.get('contactno')
        age = request.form.get('age')
        emailid = request.form.get('emailid')
        attend = request.form.get('attend')

        # validation for emailid
        cur.execute("SELECT * FROM STUDENTS WHERE EMAILID = %s", [emailid])
        checkemail = cur.fetchall()

        # validation for contact
        cur.execute("SELECT * FROM STUDENTS WHERE CONTACTNO = %s", [contactno])
        checkmob = cur.fetchall()

        if len(checkemail) != 0 or len(checkmob) != 0:
            flash("Email Id/Contact No. is already registered")

        # if email id / contact no are not repeated
        else:
            # inserting input to the database
            cur.execute("INSERT INTO STUDENTS SELECT STUID+1, ROLLNO+1, %s, %s, %s, %s, %s, %s, %s, %s FROM STUDENTS ORDER BY STUID DESC LIMIT 1", [stuname, gender, country, city, contactno, age, emailid, attend])
            con.commit()
            flash("Student added successfully")

    return render_template("entry.html")


# input page to input roll number of the candidate
@app.route("/inputs", methods=['GET', 'POST'])
def inputs():
    if request.method == 'POST':

        flash("")

        # request for taken input
        studentrollno = request.form['studentrollno']
        mailch = request.form['mailch']

        cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
        data = cur.fetchall()
        print(data)

        # if entered data not found in database
        if len(data) == 0:
            flash("Roll Number not found!")

        else:

            flash(f"Roll Number found!")

            # taken inputs will be passed to another function for further process
            from searchdata import search
            search(studentrollno, mailch)

            # check if user opted for emailing the report
            if mailch == 'y' or mailch == 'Y':
                flash("Email sent")

    return render_template("input.html")


# delete a student
@app.route("/delroll", methods=['GET', 'POST'])
def delroll():
    if request.method == 'POST':

        flash("")

        studentrollno = request.form['studentrollno']

        # look for the student with given roll number
        cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
        data = cur.fetchall()

        # if data not found
        if len(data) == 0:
            flash("Roll number not found!")

        else:

            flash("Roll number found!")

            # deletion of record
            cur.execute("DELETE FROM STUDENTS WHERE ROLLNO = %s", [studentrollno])
            con.commit()

            flash("Record deleted!")

    return render_template("delroll.html")


# display all the data in a frame
@app.route("/resultframe")
def resultframe():
    cur.execute("SELECT * FROM STUDENTS")
    temp = cur.fetchall()
    return render_template("resultframe.html", temp=temp)


# display all the data
@app.route("/result")
def result():
    cur.execute("SELECT * FROM STUDENTS")
    temp = cur.fetchall()
    return render_template("result.html", temp=temp)


if __name__ == "__main__":
    app.run(debug=True)
