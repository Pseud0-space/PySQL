# PySQL
This project comprises of 5431 lines of source code and 'Images' folder containing all the required Images for the application 

1. A file named as "MySQL_Password.txt" containing the MySQL root password
2. A file named as "MySQL_DB.txt" containing the name of MySQL Database used

# Python imports - 

- PyQt5
- mysql-connector
- cryptography
- base64
- os
- sys

# Table and Backend Info
for the mysql backend it requires 6 tables here is the description of all tables used:-
table:- feeinfo
+------------+-------------+------+-----+---------+-------+
| Field      | Type        | Null | Key | Default | Extra |
+------------+-------------+------+-----+---------+-------+
| STUDENT_ID | int         | NO   |     | NULL    |       |
| FEE_ID     | int         | NO   |     | NULL    |       |
| NAME       | char(250)   | NO   |     | NULL    |       |
| TOTAL_FEE  | float       | YES  |     | NULL    |       |
| FEE_PAID   | float       | YES  |     | NULL    |       |
| FEE_DUE    | float       | YES  |     | NULL    |       |
| CLASS      | varchar(12) | YES  |     | NULL    |       |
+------------+-------------+------+-----+---------+-------+

table:- image
+------------+----------+------+-----+---------+-------+
| Field      | Type     | Null | Key | Default | Extra |
+------------+----------+------+-----+---------+-------+
| Student_ID | int      | YES  |     | NULL    |       |
| IMAGE      | longblob | NO   |     | NULL    |       |
+------------+----------+------+-----+---------+-------+

table:- login
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| NAME        | char(255)    | NO   |     | NULL    |       |
| PASSWORD    | varchar(255) | NO   |     | NULL    |       |
| CLASS       | int          | YES  |     | NULL    |       |
| SECTION     | char(3)      | YES  |     | NULL    |       |
| ROLL_NUMBER | int          | YES  |     | NULL    |       |
| STUDENT_ID  | int          | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+

table:- personalinfo
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| STUDENT_ID   | int          | YES  |     | NULL    |       |
| NAME         | char(255)    | YES  |     | NULL    |       |
| FATHER_NAME  | char(255)    | YES  |     | NULL    |       |
| MOTHER_NAME  | char(255)    | YES  |     | NULL    |       |
| AGE          | int          | YES  |     | NULL    |       |
| ADDRESS      | varchar(255) | YES  |     | NULL    |       |
| PHONE_NUMBER | varchar(255) | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+

table:-studentinfo
+-------------+------------+------+-----+---------+-------+
| Field       | Type       | Null | Key | Default | Extra |
+-------------+------------+------+-----+---------+-------+
| STUDENT_ID  | int        | NO   | PRI | NULL    |       |
| _NAME_      | char(255)  | NO   |     | NULL    |       |
| CLASS       | int        | YES  |     | NULL    |       |
| SEC         | varchar(4) | YES  |     | NULL    |       |
| ROLL_NUMBER | int        | YES  |     | NULL    |       |
| BLOOD_GROUP | varchar(5) | YES  |     | NULL    |       |
| GENDER      | char(2)    | YES  |     | NULL    |       |
+-------------+------------+------+-----+---------+-------+

table:- subjectinfo
+--------------------+-----------+------+-----+---------+-------+
| Field              | Type      | Null | Key | Default | Extra |
+--------------------+-----------+------+-----+---------+-------+
| STUDENT_ID         | int       | NO   |     | NULL    |       |
| NAME               | char(250) | NO   |     | NULL    |       |
| CHEMISTRY          | char(250) | YES  |     | NULL    |       |
| ENGLISH            | char(250) | YES  |     | NULL    |       |
| BIOLOGY            | char(250) | YES  |     | NULL    |       |
| HISTORY            | char(250) | YES  |     | NULL    |       |
| ECONOMICS          | char(250) | YES  |     | NULL    |       |
| GEOGRAPHY          | char(250) | YES  |     | NULL    |       |
| SOCIOLOGY          | char(250) | YES  |     | NULL    |       |
| PHYSICS            | char(250) | YES  |     | NULL    |       |
| PAINTING           | char(250) | YES  |     | NULL    |       |
| POLITICAL_SCIENCE  | char(250) | YES  |     | NULL    |       |
| COMPUTER_SCIENCE   | char(250) | YES  |     | NULL    |       |
| BUSINESS_STUDIES   | char(250) | YES  |     | NULL    |       |
| PHYSICAL_EDUCATION | char(250) | YES  |     | NULL    |       |
| MATHEMATICS        | char(250) | YES  |     | NULL    |       |
| HOME_SCIENCE       | char(250) | YES  |     | NULL    |       |
| PSYCHOLOGY         | char(250) | YES  |     | NULL    |       |
| ACCOUNTANCY        | char(250) | YES  |     | NULL    |       |
+--------------------+-----------+------+-----+---------+-------+
