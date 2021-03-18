#!/usr/bin/env python
# coding: utf-8

# In[157]:


import os 
os.getcwd()


# In[173]:


import mysql.connector as conn, csv


# In[174]:


mydb = conn.connect(
    host="localhost",
    user="root",
    password="@Gazaslim2013",
    database="Academics"
)
print("mydb connection success!")


# In[175]:


# Create cursor object
mycursor = mydb.cursor()


# In[176]:


mycursor.execute("CREATE DATABASE IF NOT EXISTS Academics")
print("Academic Database created")


# In[177]:


#view the databases
mycursor.execute("SHOW DATABASES")
#print all databases
for db in mycursor:
    print(db)


# In[178]:


#create college table
mycursor.execute ('''CREATE TABLE IF NOT EXISTS College (
                    College_id INT primary key NOT NULL,
                    College_Name TEXT NOT NULL,
                    College_city VARCHAR(50) NOT NULL,
                    College_country TEXT NOT NULL);''')


# In[179]:


#import csv file
with open('C:\python\Assignment\mysql\College.csv', 'r') as coll_csv:
    reader = csv.reader(coll_csv)
    #next(reader)  
    for rows in reader:
        mycursor.execute(
            "INSERT IGNORE INTO College(College_id, College_Name, College_city, College_country) VALUES( %s, %s, %s, %s);", rows)
        mydb.commit()
print("Details successfully entered into college table:")


# In[180]:


#Get database tables
mycursor.execute("SHOW TABLES")
for tables in mycursor:
    print(tables)


# In[181]:


#create professor table
mycursor.execute ('''CREATE TABLE IF NOT EXISTS Professor (
                    teacher_id INT PRIMARY KEY NOT NULL,
                    Teacher_Name TEXT NOT NULL,
                    College_id INT NOT NULL,
                    Date_joined DATE NOT NULL,
                    Speciality VARCHAR(20) NOT NULL,
                    Salary REAL NOT NULL,
                    Experience VARCHAR(20) NOT NULL,
                    FOREIGN KEY (College_id) references College(College_id));''')


# In[182]:


#import csv file
with open('C:\python\Assignment\mysql\professor.csv', 'r') as prof_csv:
    next(prof_csv)
    reader = csv.reader(prof_csv)
    for rows in reader:
        mycursor.execute(
            "INSERT IGNORE INTO professor(teacher_id, Teacher_Name, College_id, Date_joined, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s, %s);", rows)
        mydb.commit()
print("Details successfully entered into professor table:")


# In[183]:


#Create student table
mycursor.execute('''CREATE TABLE IF NOT EXISTS student (
                   Student_id INT(10) PRIMARY KEY NOT NULL,
                   Student_Name VARCHAR(20) NOT NULL,
                   Student_Email VARCHAR(20) NOT NULL,
                   College_id INT NOT NULL, 
                   Date_joined DATE NOT NULL, 
                   Major_taken VARCHAR(50) NOT NULL,
                   College_Level VARCHAR(100) NOT NULL,
                   FOREIGN KEY (College_id) REFERENCES college(College_id));''')


# In[184]:


# import student csv
with open('C:\python\Assignment\mysql\Students.csv', 'r') as stud_csv:
    next(stud_csv)
    reader = csv.reader(stud_csv)
    for rows in reader:
        mycursor.execute(
            "INSERT IGNORE INTO Student(Student_id, Student_Name, College_id, Date_joined, Major_taken, College_Level) VALUES (%s, %s, %s, %s, %s, %s);", rows)
        mydb.commit()
print("Details successfully entered into student table:")


# In[185]:


def school():
    mycursor.execute(''' SELECT * 
                        FROM Student 
                        INNER JOIN College
                        ON College.College_id = Student.College_id
                        INNER JOIN Professor
                        ON college.College_id = Professor.College_id; ''')
    
    print("\t\t inner join result:\n \t\t ------------------\n")
    for i in mycursor.fetchall():
        print(i, '\n')

school()

mycursor.close()

