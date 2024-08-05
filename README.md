# SCHOOL MANAGEMENT SYSTEM

#### Video Demo : https://youtu.be/09B4b1Qs9J0
### Description
School Management System is a project that allows users to manage the records of the students and teachers bound to the respective school.

### Features
- Stores records to a CSV file which makes it more readable using software such as Excel.

- Shows the records ( including Id, name and email ) of the students and the teachers of the respective school.

- Add more students as well as teachers record to the respective CSV file of the students and the teachers.
  
- In Case a student or a teacher leave the school, their data can be easily removed.
  
- Searching students and teachers record based on either of their name, id or email provides more flexibility.

### Step-by-step Guide
**1. Execute the Program:**
- Execute the program by using the command python project.py

**2. Manage Students or Teachers:** 
- Once the program is executed we can see a menu showing on whether to  manage students or teachers or to exit. The program asks user to enter a key based on what the user wants to manage for example: 'S' to manage Students.

**3. Manage Students:**
- On entering 'S', a new 'Manage Students' menu appears which includes the options like show students, remove, students, search students. Just like before user have to enter a key associated with option to use the that feature.

    **a. Show Students:**
     - When user selects show students option, all the records of the students stored in 'students.csv' file are listed in a tabular form.
    
    **b. Add Students:**
    - When user selects add student option, the program step-by-step asks for the student ID, first name, last name and email. The student ID and email are validated as per school ( ID = "PMC_SXXX", email = "forexample1@pmc.edu.n"'). After all the data is entered correctly, the student record is saved.

    **c. Remove Students**
    - When user selects remove student otption, the program asks for the student ID from the user and as per that ID the record is deleted.

    **d. Search Students**
    - When user selects search students option, the program asks user on what basis to search the student like id, name, email. User have to choose one of the 3 enter the student data then the program search student record based on the given data.
    
    **e. Back or Exit**
    - User can enter 'B' to go back to main menu or 'E' to exit the program.
  
**3. Manage Teachers:**
- User can manage teachers records by selecting "Manage Teachers" option at main menu. Selecting 'manage teachers' will show a new menu including the options show teachers, add teachers, remove, teachers, search teachers. These features can be used just like we talked above on manage students topic.
___
***As the data is stored in the CSV files. Even when we end the program, the data is not erased and can be accessed next time we execute the program. The code can be modified such as the student and teachers ID as well as their email to make the system for respective school.***

-Project By Aashish Bogati