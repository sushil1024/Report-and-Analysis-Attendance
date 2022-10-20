import mysql.connector

con = mysql.connector.connect(
    user="root",
    password="r00t",
    host="localhost",
    database="fynd",
)

cur = con.cursor()


# cur.execute("SELECT * FROM STUDENTS;")
#
# for i in cur:
#     print(i)


# input function to process inputs given by the user
def search(roll, mailch):

    res = cur.execute(f"SELECT * FROM STUDENTS WHERE ROLLNO = {roll};")

    if (i for i in cur) == "":
        print("data not found")
    else:
        for i in cur:
            print(i)

    con.close()

# # if input is 'y' or 'Y', then the user wants the email to be sent
#     if mailch == 'y' or mailch == 'Y':
#
#         # making a report pdf by taking some data from above
#         from genreport import genpdf
#         # genpdf(studentname, roll, dob, age, gender, residence, lecs)
#
#         # sends the pdf file to the specified email id of the candidate
#         from mailto import sendmail
#         # sendmail(emailid, studentname)


if __name__ == "__main__":
    search(4, 'n')

