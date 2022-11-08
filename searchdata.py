import mysql.connector


con = mysql.connector.connect(
    user="ueiforctqwwdmvnx",
    password="LDtM1YA1kKOzEfOeplHC",
    host="bzczr0tdsxjv3b9xkz8l-mysql.services.clever-cloud.com",
    database="bzczr0tdsxjv3b9xkz8l",
)

cur = con.cursor()


# input function to process inputs given by the user
def search(roll, mailch):

    cur.execute("SELECT * FROM STUDENTS WHERE ROLLNO = %s", [roll])

    studata = [i for i in cur]

# if input is 'y' or 'Y', then the user wants the email to be sent
    if mailch == 'y' or mailch == 'Y':

        stuname = studata[0][2]
        roll = studata[0][1]
        age = studata[0][7]
        gender = studata[0][3]
        residence = f"{studata[0][5]} {studata[0][4]}"
        lecs = studata[0][9]
        emailid = studata[0][8]

        # making a report pdf by taking some data from above
        from genreport import genpdf
        genpdf(stuname, roll, age, gender, residence, lecs)

        # sends the pdf file to the specified email id of the candidate
        from mailto import sendmail
        sendmail(emailid, stuname)


if __name__ == "__main__":
    search(2, 'y')

