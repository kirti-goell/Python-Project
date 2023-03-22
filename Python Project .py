import os
student_list = []
heading_list = ["Roll No","Student Name","","Class Name","Hindi","English","Maths","Science","Computer","Total Marks","Percentage","Division"]


def MainMenu():
    os.system('cls')
    print("\t\t======================================\n")
    print("\t\t WELCOME TO STUDENT MANAGEMENT SYSTEM\n")
    print("\t\t======================================\n")
    print("\t\t\t | [1] Add Records    |\n")
    print("\t\t\t | [2] Display Records|\n")
    print("\t\t\t | [3] Delete Records |\n")
    print("\t\t\t | [4] Search Records |\n")
    print("\t\t\t | [5] Update Records |\n")
    print("\t\t\t | [0] Exit           |\n")
    print("\t\t======================================\n")    

def addRecords():
    choice = 'y'
    while choice == 'y' or choice == 'Y':
        flag = False
        roll_no = int(input("Enter Roll number:"))
        for data in student_list:
            if roll_no == data[0]:
                flag = True
                break;

        if flag == False:
            
            stu_name = input("Enter student name: ")
            class_name = input("Enter class name: ")
            subject1 = int(input("Enter subject Hindi : "))
            subject2 = int(input("Enter subject English: "))
            subject3 = int(input("Enter subject Maths: "))
            subject4 = int(input("Enter subject Science: "))
            subject5 = int(input("Enter subject Computer: "))
            student_list.append([roll_no, stu_name, class_name, subject1, subject2, subject3, subject4, subject5])
            choice=input("Do you want to add more records [y/n] :: ")
        else:
            print("Record already exist...");
            os.system('pause')
            home()
    MainMenu()
def deleteRecord():
    rno = int(input("Enter Roll no :"))
    index = -1
    flag = False

    for i in range(len(student_list)):
        for j in range(len(student_list[i])):
            if student_list[i][j] == rno:
                index = i
                flag = True
                break;
                

    if flag == True:
        student_list.pop(index)
        print("Record deleted sucessfully...")
    else:
        print("Record not found")    
        
def searchRecord():
  
    flag = False
    rno = int(input("Enter Roll No : "))

    index = 0
    for data in student_list:
        if rno == data[0]:
            print("================================================================================================================")
            print("{0}  {1}  {2}  {3}  {4}  {5}  {6}  {7}  {8}  {9}  {10}  {11}".format(heading_list[0],heading_list[1],heading_list[2],heading_list[3],heading_list[4],heading_list[5],heading_list[6],heading_list[7],heading_list[8],heading_list[9],heading_list[10],heading_list[11]))
            print("================================================================================================================")    

            total_marks = 0
            fail = 0
            div = ""
            per = 0
            total_marks+=data[3] + data[4] + data[5]+ data[6] + data[7]
            if data[3] < 40:
                fail += 1
            if data[4] < 40:
                fail += 1
            if data[5] < 40:
                fail += 1
            if data[6] < 40:
                fail += 1
            if data[7] < 40:
                fail += 1

            if fail == 0:
                per = total_marks / 5
                if per >=40 and per<50:
                    div = "Third"
                elif per >= 50 and per < 60:
                    div = "Second"
                elif per >= 60 and per < 75:
                    div = "First"
                elif per >= 75:
                    div = "Merit"
            elif fail == 1:
                div = "Re-Appear"
            elif fail > 1:
                div = "Fail"
            
            print("{:<9}{:<16}{:13}{:<10}{:<7}{:<8}{:<8}{:<10}{:<12}{:<12}{:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],total_marks,per,div))
            flag = True
            break;

    if flag == False:
        print("Record not found")

        
def DisplayRecords():

    total_marks = 0
    print("================================================================================================================")
    print("{0}  {1}  {2}  {3}  {4}  {5}  {6}  {7}  {8}  {9}  {10}  {11}".format(heading_list[0],heading_list[1],heading_list[2],heading_list[3],heading_list[4],heading_list[5],heading_list[6],heading_list[7],heading_list[8],heading_list[9],heading_list[10],heading_list[11]))
    print("================================================================================================================")    
    for data in student_list:
        fail = 0
        div = ""
        per = 0
        total_marks+=data[3] + data[4] + data[5]+ data[6] + data[7]
        if data[3] < 40:
            fail += 1
        if data[4] < 40:
            fail += 1
        if data[5] < 40:
            fail += 1
        if data[6] < 40:
            fail += 1
        if data[7] < 40:
            fail += 1

        if fail == 0:

            #print("Total Marks : ", total_marks)
            per = total_marks / 5
           
            #print("Per : ", per),
            if per >=40 and per<50:
                div = "Third"
            elif per >= 50 and per < 60:
                div = "Second"
            elif per >= 60 and per < 75:
                div = "First"
            elif per >= 75:
                div = "Merit"
        elif fail == 1:
            div = "Re-Appear"
        elif fail > 1:
            div = "Fail"
        print("{:<9}{:<16}{:13}{:<10}{:<7}{:<8}{:<8}{:<10}{:<12}{:<12}{:<20}".format(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],total_marks,per,div))

def updateRecord():
    flag = False
    rno = int(input("Enter Roll No : "))
    index = 0
    ch = "y"
    
    for data in student_list:
        if rno == data[0]:
            print("Student Name : ",data[1])
            ch = input("Do want to change this record [y/n]: ")
            if ch == "y" or ch == "Y":
                stu_name = input("Enter student name: ")
                data[1] = stu_name
          
            print("Class Name : ",data[2])
            ch = input("Do want to change this record [y/n]: ")            
            if ch == "y":
                class_name = input("Enter class name: ")
                data[2] = class_name
            
            
            print("Hindi : ",data[3])
            ch = input("Do want to change this record [y/n]: ")            
            if ch == "y":
                subject1 = int(input("Enter subject Hindi : "))
                data[3] = subject1            
            
            print("English : ",data[4])
            ch = input("Do want to change this record [y/n]: ")            
            if ch == "y":
                subject2 = int(input("Enter subject English : "))
                data[4] = subject2            
            
            print("Maths : ",data[5])
            ch = input("Do want to change this record [y/n]: ")            
            if ch == "y":
                subject3 = int(input("Enter subject English : "))
                data[5] = subject3            
        
            print("Science : ",data[6])
            ch = input("Do want to change this record [y/n]: ")           
            if ch == "y":
                subject4 = int(input("Enter subject Science : "))
                data[6] = subject4            
        
            print("Computer : ",data[7])
            ch = input("Do want to change this record [y/n]: ")           
            if ch == "y":
                subject5 = int(input("Enter subject Computer : "))
                data[7] = subject5            
             
            flag = True
            break;

    if flag == False:
        print("Record not found")

    
def home():
    MainMenu()
    ch = 1
    while ch!=0:
        ch=int(input("\t\t\t Enter your choice :: "))
        if ch == 1:
            addRecords()
        elif ch == 2:
            os.system('cls')
            DisplayRecords()
            os.system('pause')
            home()
        elif ch == 3:
            deleteRecord()
            home()
        elif ch == 4:
            os.system('cls')
            searchRecord()
            os.system('pause')
            home()
        elif ch == 5:
            os.system('cls')
            updateRecord()
            os.system('pause')
            home()
        else:
            exit()

home()
