# Schooldb
#1:  Create a MySQL database connection Python programming. Call it Academics. 

# 2:  Write a Python program to create the 3 MySQL tables and and populate them with records from a CSV/text file.

# 3:  Using Python and MySQL, display records from the 3 joined tables on the screen:

#a) College:
    College_id
    College_Name
    College_city
    College_country
    

# b) Professor:
    teacher_id
    Teacher_Name
    College_id
    Date_joined
    Speciality
    Salary
    Experience

# c) Student:
    Student_id
    Student_Name
    College_id
    Date_joined
    Major_taken
    College_Level
    
 # 4: Create 10 fictitious records for students, Professors and the College.
For college table just create 5 records. Assuming that there are 5 colleges in different towns and countries all over Africa. 

Join these three tables by College_Id and then print and display the records on the screen.       


## steps in solving this problem:
-   Create mysql database called academics 
-   create  College, Proffessor and Student tables in the db
-   populate your table with records from CSV files for each
-   create a function where you join the three tables by the college id.
