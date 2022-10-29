import mysql.connector

con = mysql.connector.connect(
    user="ueiforctqwwdmvnx",
    password="LDtM1YA1kKOzEfOeplHC",
    host="bzczr0tdsxjv3b9xkz8l-mysql.services.clever-cloud.com",
    database="bzczr0tdsxjv3b9xkz8l",
)

cur = con.cursor()


# create table
# cur.execute("create table STUDENTS( STUID INT PRIMARY KEY AUTO_INCREMENT not null, ROLLNO INT not null, STUNAME VARCHAR(255) not null, GENDER VARCHAR(100) not null, COUNTRY VARCHAR(100), CITY VARCHAR(100), CONTACTNO VARCHAR(100), AGE INT not null, DOB DATE not null, EMAILID VARCHAR(100) not null, ATTEND int not null);")
# con.commit()

# describe table
# cur.execute("desc STUDENTS;")
#
# for i in cur:
#     print(i)


# insert initial value (first value)
# cur.execute('''insert into STUDENTS values(
# 	1,
# 	1,
# 	'sushil',
# 	'male',
#     null,
#     null,
#     null,
#     25,
#     '1997-04-01',
#     'sushilwaghmare2048@gmail.com',
#     50
# );''')
# con.commit()

cur.execute("select * from STUDENTS;")
for i in cur:
    print(i)

con.close()

print("successful")
