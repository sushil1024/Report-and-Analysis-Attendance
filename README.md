# Report-and-Analysis-Attendance

Data will be stored in database, report will be generated on request and analysis will be shown in the report. The report will be mailed to the particular email id of the candidate.

# Abstract
The project focuses on analysing attendance and generating a report based on the data of the student stored in the database. The student can opt for the report and check whether or not he/she is in the defaulter's list. The generated report will be emailed to the student's email address stored in the database. A staff with password authentication can add new student or delete an existing one and can view all the students with their details in a table format. The generating of the report is done through fpdf module and includes pie chart of the student's attended and unattended lectures. The report includes all the details of the student with the pie chart and will be emailed personally to that student.


# Installation

- Clone this repository
```
git clone https://github.com/sushil1024/Report-and-Analysis-Attendance
```

- Installation

Run "app.py"


# Requirements
gunicorn
Flask==2.0.2
fpdf==1.7.2
fpdf2==2.4.5
matplotlib==3.4.3
yagmail==0.14.260
mysql-connector==2.1.7
mysql-connector-python==8.0.30
Jinja2==3.1.2


# Author
Sushil Sunil Waghmare

