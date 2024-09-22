---------------------------------------INSTRUCTION-TO-RUN-APPLICAATION--------------------------

1. First install the python in your computer'
2. Then go to the project folder and open terminal and run the command  'pip install -r requirements.txt' this command   will install all the dependencies required for the project.
3. Now brfore following the 4th step please do install MySql, and create a database with name students_db, then using the command 'python orms.py' to create all related tables in database.
4. Then to run the application if you are using any of the python code editors then on clicking run button, the server will start automatically, if not in terminal type 'python server.py' it will also start the application.
5. Then click on the server URL CTRL+Click or directly copy and paste the URL in any browser it will disply the UI for application. 
6. Now using the application we can add data and view the aggregatedd data, also add courses too, ui is dynamic any
chnages on the data will reflect on the Analytics tab and related pages.


----------------------------------------------REQUIRE-MENT----------------------------------------
"""
We would like to develop an application using flask and mysql for managing Student and  Courses .
Create a page for creation of Course with below attributes:
Name
Duration
Fee


Create a page for Student registration with below attributes :
First Name
Last Name
Date of Birth
Address
Course (should be derived from Course )


We should be able to view all Students and Edit,Delete them.
Report :  create a page to display the count of students per course  and how much fee they paid for the course.
Course    Student count       Total Fee
cou-A                      3                 5000
cou-B                      2                 15500
"""
---------------------------------------------API-DOCS----------------------------------------------------
Note: I tried to create SwaggerUI but with flask it was bit difficult and some libraries are found to be outdated, since i already delayed my submisison so i avoided creating the SwaggerUI, i know its difficult but i provided the apidetails below have a look.


1. I followed the class approach to crate the rest services three classes are created to named, RegisterStudent, StudentCourses, AggregateAnalytics. ALL the CRUD operation are done in RegisterStudent, StudentCourses only read operation is available for AggregateAnalytics.

---Summary is  Below------------>
1) RegisterStudent
   *END-POINT- '/students'

   *GET-API
   It gathers all data from Students table and has no request body.

   *POST-API
   It registers students and do have arequest body.
   {
    "first_name":"xys",
    "last_name":"tyu",
    "dob":"1907-09-23" (YYYY-mm-dd),
    "address":"Hyd",
    "course":"Physics"
   }

   *PUT-API
   It helps to update the data about student, and have a request body.
   {
    "name":"xys",
    "paid_fees":1200,
    "dob":"1907-09-23" (YYYY-mm-dd),
    "address":"Hyd",
    "course":"Physics"
   }

   *DELETE-API
    It helps to remove the student data based on name and dob and course he has taken.
   {
    "name":"xys",
    "dob":"1907-09-23", (YYYY-mm-dd)
     "course":"Physics"
   }

2) RegisterStudent
   *END-POINT- '/students/courses'

   *GET-API
    It gathers all data from Courses table and has no request body.

   *POST-API
   This api helps to add new courses to the database from which student can select the course.
   {
    "course_name":"Physics",
    "fee":":1200,
    "course_start":"1907-09-23" (YYYY-mm-dd),
    "course_end":"1907-11-23" (YYYY-mm-dd),
   }

   *PUT-API
   This api helps to update the course in case of there is some chnage of plans to the courses.
   {
    "course_name":"Physics",
    "fee":":1200,
    "course_start":"1907-09-23" (YYYY-mm-dd),
    "course_end":"1907-11-23" (YYYY-mm-dd),
   }

  *DELETE-API
   This API helps to delete the courses.
   { "course_name":"Physics"}

2) AggregateAnalytics
   It has only one API a separate class is created because in future may be more, apis could be created realted to analytics

   *END-POINT- '/students/courses/analytics'

   *GET-API
    It gathers all aggregated data for analytics and sends it to the UI for analysis and has no 
    request body or arg parameters.
   
----------------------------Final Thoughts--------------------------------------------
Some importamt things are missing i know but, since i already took enough time for sunmission, i hope i gave my best.
 





