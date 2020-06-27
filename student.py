def list_courses(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------
    quantity = 0
    print("Courses registered: ")
    for x in range(len(c_list)):
        if id in r_list[x]:
            print(c_list[x])
            quantity += 1
    print(f"Total number: {quantity}\n")




def add_course(id, c_list, r_list, m_list):

    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    to_add = input("Enter the course you want to add: ")
    if to_add not in c_list:
        print("Course not found.\n")
        return
    for x in range(len(c_list)):
        if c_list[x] == to_add:
            if id in r_list[x]:
                print("You are already enrolled in that course.\n")
                return
    for x in range(len(c_list)):
        if c_list[x] == to_add:
            if len(r_list[x]) == m_list[x]:
                print("Course already full.\n")
                return
    for x in range(len(c_list)):
        if c_list[x] == to_add:
            r_list[x].append(id)
            print("Course added.\n")
            return
    print("There has been an error.")







def drop_course(id, c_list, r_list):

    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    to_drop = input("Enter course you want to drop: ")
    if to_drop not in c_list:
        print("Course not found.\n")
        return
    for x in range(len(c_list)):
        if c_list[x] == to_drop:
            if id not in r_list[x]:
                print("You are not enrolled in that course.\n")
                return
    for x in range(len(c_list)):
        if c_list[x] == to_drop:
            r_list[x].remove(id)
            print("Course dropped.\n")
            return
    print("There has been an error.")

