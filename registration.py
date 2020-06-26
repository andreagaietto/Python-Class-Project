# ----------------------------------------------------------------
# Author: Andrea Gaietto
# Date: June 2020
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

import student


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003', '1001'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]
    id = 1
    while id != "0":
        id = input("Enter ID to log in, or 0 to quit: ")
        if id == "0":
            break
        success = login(id, student_list)
        if success == True:
            decision_tree = "1"
            while decision_tree != "0":
                decision_tree = input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: ")
                if decision_tree == "1":
                    student.add_course(id, course_list, roster_list, max_size_list)
                elif decision_tree == "2":
                    student.drop_course(id, course_list, roster_list)
                elif decision_tree == "3":
                    student.list_courses(id, course_list, roster_list)
                elif decision_tree == "0":
                    print("Session ended.")
                    break
                else:
                    print("Incorrect choice.")
        else:
            print("ID or PIN incorrect.")


def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin = input("Enter PIN: ")
    for x in s_list:
        if x[0] == id:
            if x[1] == pin:
                return True
    return False


main()
