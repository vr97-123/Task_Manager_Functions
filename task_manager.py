##Python file: task_manager.py
# For a better output visualisation, please open this file in PyCharm, Thank you.

#=====importing libraries===========
# Datetime module imported to validate the correct format to be entered by the user on the 'Register New User Section'.
import datetime
from datetime import date
from datetime import datetime

#=====General variables for constant use===========
# General variables declared - for text formatting as well as for 'today' date - to be used throughout the program.
WHITE = "\033[0m"
ORANGE = "\033[33m"
PURPLE = "\033[35m"
GREY = "\033[37m"
DARKGREY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
DARKCYAN = "\033[36m"
ITALIC_S = "\x1B[3m"
ITALIC_E = "\x1B[0m"
todays_date = date.today().strftime("%d %b %Y")


#====Login Section====
# This function called "login()" which is used to authenticate a user.
def login():
    # When the function is called, it will print out the programme introduction
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"\t\t\t\t\t\t\t\t{DARKCYAN}SMALL BUSINESS TASK MANAGER{WHITE}\n"
          f"───────────────────────────────────────────────────────────────────────────────────────────────")
    # A while loop is implemented to keep running the login process until a successful login is achieved.
    while True:
        # Inside the while loop, the code prompts the user to enter a username and checks if the entered username
        # already exists by calling a function called "check_user_exists(username)".
        # Take input for username
        username = input("Enter Your Username: ")
        # Check if the entered username already exists
        if not check_user_exists(username):
            # If the function returns False, it means the username does not exist and a message will be displayed
            # to the user saying that the account could not be found.
            print(f"{RED}Sorry, We Can't Find An Account On That User Name.{WHITE}\n"
                  f"───────────────────────────────────────────────────────────────────────────────────────────────")
            continue
        # If the function returns True, it means the username exists and the code prompts the user to enter a password.
        # Take input for password
        password = input("Enter Your Password: ")
        # Then it opens a file called "user.txt" and reads all the lines in the file.
        # Open the user.txt file
        with open('user.txt', 'r', encoding='utf-8-sig') as f:
            # Read all lines in the file
            lines = f.readlines()
            # It then iterates through each line, splitting it by ',' and checking if the entered username and password
            # match with the one in the file.
            # Iterate through each line
            for line in lines:
                # Split the line by ',' and check if the entered username and password match
                # If a match is found, it prints a message saying "Login Successful." and returns the username.
                if username == line.split(',')[0].strip() and password == line.split(',')[1].strip():
                    print(f"{GREEN}Login Successful.{WHITE}")
                    return username
        # If no match is found, it prints a message saying "Incorrect Username or Password. Please Try Again."
        print(f"{RED}Incorrect Username Or Password. Please Try Again.{WHITE}\n"
              f"───────────────────────────────────────────────────────────────────────────────────────────────")


#====Main Menu Section====
# This function named "main_menu" that takes in a parameter "username".
def main_menu(username):
    # The function contains a while loop that runs indefinitely until the "break" statement is reached. Within the loop,
    # it first prints out a formatted string that creates a visual menu with different options for the user to choose
    # from. The options include "Register User", "Add Task", "View All Tasks", "View My Tasks", and "Exit".
    while True:
        print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
              f"\t\t\t\t\t\t\t\t\t\t   {BLUE}MAIN MENU{WHITE}\n"
              f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
              f"[ r  ] - Register User\n"
              f"[ a  ] - Add Task\n"
              f"[ va ] - View All Tasks\n"
              f"[ vm ] - View My Tasks\n"
              f"[ e  ] - Exit")
        # Only display this menu option if 'admin' is logged in.
        # If the passed in "username" is "admin", it will also include the options "Generate Reports" and
        # "Display Statistics" in the menu.
        if username == "admin":
            print(f"[ gr ] - Generate Reports\n"
                  f"[ ds ] - Display Statistics")
        # Inform user of option to return to main menu.
        print(f"{ITALIC_S}=>Note: Please Enter '-1' To Return To This Main Menu Or To Go Back On Further Menus.<={ITALIC_E}\n"
              f"───────────────────────────────────────────────────────────────────────────────────────────────")
        # The function then prompts the user to enter a choice and uses a series of "if-elif" statements to determine
        # what action to take based on the user's choice. If the user enters "r", it will call the "reg_user()"
        # function. If the user enters "a", it will call the "add_task()" function and so on. The function also
        # includes a message to inform the user that they can enter "-1" to return to the main menu or to go back
        # on further menus.
        choice = input("Please Select One Of The Above Options: \t").lower()
        if choice == "r":
            reg_user()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all()
        elif choice == "vm":
            view_mine(username)
        elif choice == "gr":
            gen_reports()
        elif choice == "ds":
            display_stats()
        elif choice == "e":
            break
        # If the user enters an invalid choice, it will print an error message.
        else:
            print(f"{RED}Invalid choice. Please Try Again.{WHITE}\n"
                  f"───────────────────────────────────────────────────────────────────────────────────────────────")


# This function called check_user_exists() which takes a single parameter called username to check if user
# is already registered
def check_user_exists(username):
    # The function uses a with statement to open a file called 'user.txt' in read mode
    # Open the user.txt file
    with open('user.txt', 'r', encoding='utf-8-sig') as f:
        # The file is read and all lines are stored in a variable called lines.
        lines = f.readlines()
        # Iterate through each line
        # A for loop is used to iterate through each line in the lines variable. Within the for loop, the line variable
        # is split by a comma and the first element is accessed using indexing. This element is then stripped of any
        # whitespace using the strip() method.The resulting value is then compared to the username parameter passed to
        # the function. If they match, the function returns True immediately. If the loop completes without finding a
        # match, the function returns False.
        # Read all lines in the file
        for line in lines:
            # Split the line by ',' and check if the entered username matches
            if username == line.split(',')[0].strip():
                return True
    return False


# ====Register New User Section====
# This function called "reg_user()" that is used to register new users.
def reg_user():
    # The function first checks if the current user is "admin", and if not, it prints a message saying that only "admin"
    # can register new users. If the current user is "admin", it then enters a while loop that prompts the user to
    # enter a new username. If the user enters "-1", the loop breaks and the function returns to the main menu.
    if username != 'admin':
        print(f"{RED}Sorry, Only Admin Can Register New Users.{WHITE}")
    else:
        print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
              f"\t\t\t\t\t\t\t\t\t\t{CYAN}REGISTER NEW USER{WHITE}\n"
              f"───────────────────────────────────────────────────────────────────────────────────────────────")
        while True:
            new_user = input(f"Please Enter A New User Name: ")
            if new_user == "-1":
                print(f"{ITALIC_S}{GREEN}=> Returning To Main Menu <={ITALIC_E}{WHITE}")
                break
            # The code then opens a file called "user.txt" in read mode and iterates over each line in the file. Each
            # line is split by ", " and the first element (username) is assigned to the variable "user". If the new
            # username entered by the user matches an existing username in the file, the user is prompted to enter a
            # new username again. If no match is found, the user is prompted to enter a password and confirm it.
            with open("user.txt", "r", encoding='utf-8-sig') as user_file:
                for line in user_file:
                    user = line.strip().split(", ")[0]
                    if new_user == user:
                        print(f"{RED}This Username Already Exists. Please Try Again.{WHITE}")
                        break
                else:
                    password = input(f"Please Enter A Password For The New User: ")
                    confirm = input(f"Please Confirm The Password entered: ")
                    if password == "-1":
                        print(f"{ITALIC_S}{GREEN}=>Returning to Main Menu.<={ITALIC_E}{WHITE}")
                        user_file.close()
                        break
                    # If the password and confirmation match, the new username and password are added to the "user.txt"
                    # file in append mode. If the passwords do not match, the user is prompted to try again. The loop
                    # continues until a new user is successfully added or the user chooses to return to the main menu.
                    if password == confirm:
                        with open("user.txt", "a", encoding='utf-8-sig') as user_file:
                            user_file.write(f"{new_user}, {password}\n")
                        print(f"{GREEN}New Username And Password Have Been Successfully Added.{WHITE}")
                        break
                    else:
                        print(f"{RED}Passwords Do Not match. Please try again.{WHITE}")
        return


# ====Add Task Section====
# This function called "add_task()" that is used to add new tasks.
def add_task():
    # The function starts by printing a message to indicate that the user is in the "Add Task" section of the program.
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"\t\t\t\t\t\t\t\t\t\t\t{MAGENTA}ADD TASK{WHITE}\n"
          f"───────────────────────────────────────────────────────────────────────────────────────────────")
    # It then creates an empty list called "login_user" and opens a file called "user.txt" in read mode. The code then
    # iterates over each line in the file, splitting each line by ", " and storing the username in the "login_user"
    # list. The "user.txt" file is then closed.
    login_user = []
    # === Add task user assignment ===
    # Open the 'user.txt' file where users are enrolled on reading mode only for user validation.
    user_file = open("user.txt", "r", encoding='utf-8-sig')
    for line in user_file:
        username, password = (line.strip("\n").split(", "))
        login_user.append(username)
    user_file.close()
    # The code then prompts the user to enter the username of the person the task is assigned to, and checks if the
    # entered username is in the "login_user" list. If not, the user is prompted to enter a valid username.
    # request the user details
    assigned_user = input(f"Who Is This Task Assigned To? Please Enter The Username\n==> ")
    # Additional function to return to main menu is '-1' is entered.
    if assigned_user == "-1":
        print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
        user_file.close()
        return
    user_file = open("user.txt", "r", encoding='utf-8-sig')
    # Validation through while loop and checking that user is in 'user.txt' and notify user accordingly.
    while assigned_user not in login_user:
        assigned_user = input(f"{RED}Username \'{assigned_user}\' Not Recognised.{WHITE}\nPlease Try Again:\n==> ")
    # Close the 'user.txt' file as it is no loger required.
    user_file.close()
    # The code then prompts the user to enter the title and description of the task, and the due date for the task. The
    # due date is passed through a function called "store_date()" before being stored.
    # === Add task title === Prompting the user for task title.
    task_title = input(f"Please Enter The Title Of The Task:\n==> ")
    # Additional function to return to main menu is '-1' is entered.
    if task_title == "-1":
        print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
        user_file.close()
        return
    # === Add task description === Prompting the user for task description.
    task_description = input(f"Please Enter The description Of The Task:\n==> ")
    # Additional function to return to main menu is '-1' is entered.
    if task_description == "-1":
        print(f"{ITALIC_S}{GREEN}=> Returning to Main Menu <={ITALIC_E}{WHITE}")
        user_file.close()
        return
    # === Add Task due date === Prompting the user for task due date.
    task_due_date = input(f"Please Enter The Due Date For The Task (DD/MM/YY):\n==> ").split("/")
    # call function
    task_due_date = store_date(task_due_date)
    while True:
        task_status = input("Has the task been concluded (Y/N)?\n==> ")
        if task_status == "" or not task_status[0].lower() in ["y", "n"]:
            print(f"{RED}Wrong Format. Please answer yes or no!{WHITE}")
        else:
            break
    # The code then prompts the user to enter whether the task is completed or not. If the user enters "Y" the task is
    # marked as completed, if the user enters "N" the task is marked as not completed.
    if task_status[0].lower() == 'y':
        task_status = "Yes"
    if task_status[0].lower() == 'n':
        task_status = "No"
    # Finally, the code opens a file called "tasks.txt" in append mode and writes the task information (username,
    # title, description, creation date, due date, and completion status) to the file. The file is then closed and
    # the user is notified that the task has been added successfully.
    # Open the 'tasks.txt' file on appending mode to append the above information.
    tasks_file = open("tasks.txt", "a", encoding='utf-8-sig')
    tasks_file.write(f"\n{assigned_user}, {task_title}, {task_description}, {todays_date}, {task_due_date}, "
                     f"{task_status}")
    # close the 'tasks.txt' file once information is stored and advise the user accordingly.
    tasks_file.close()
    print(f"{GREEN}New Task Has Been Added Successfully On {todays_date}.{WHITE}")


# This function called "store_date()" that is used to store the due date for a task in a specific format.
def store_date(task_due_date):
    # It takes one parameter, "task_due_date" which is in the form of a list of three elements [day, month, year]
    # separated by "/".
    while True:
        # The function enters into a while loop, where it first checks the length of the day, month and year. If the
        # length of the day is greater than 2 or the length of the month is greater than 2 or the length of the year is
        # not equal to 2, it prompts the user to enter the due date again in the correct format.
        day, month, year = task_due_date[0], task_due_date[1], task_due_date[2]
        if len(day) > 2 or len(month) > 2 or len(year) != 2:
            task_due_date = input(f"{RED}Wrong Format date.{WHITE}\n"
                                  f"Please Enter The Due Date For The Task (DD/MM/YY):\n==> ").split("/")
            day, month, year = task_due_date[0], task_due_date[1], task_due_date[2]
        else:
            break
    # When the format is correct, the function then creates a new variable "new_task_due_date" by using the datetime
    # module, by passing in the year, month, and day. The date is then formatted to be in the format of
    # "dd mmm yyyy" using the strftime method.
    # Finally converting onto the format to be stored on file 'dd mmm yyyy'.
    new_task_due_date = datetime(2000 + int(year), int(month), int(day)).strftime("%d %b %Y")
    # Finally, the function returns the formatted date "new_task_due_date" which will be used in the main function
    # to store the date.
    return new_task_due_date


# ====View All Tasks Section====
# This function called "view_all()" that is used to view all tasks that have been added to the program.
def view_all():
    # The function starts by printing a message to indicate that the user is in the "View All Tasks" section
    # of the program.
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"\t\t\t\t\t\t\t\t\t\t{YELLOW}VIEW ALL TASKS{WHITE}")
    # It then opens a file called "tasks.txt" in read mode, reads all the lines of the file and assigns the contents to
    # a variable "tasks_details".
    # Open the 'tasks.txt' file on reading mode to read the lines of the file for the relevant information.
    tasks_file = open("tasks.txt", "r", encoding='utf-8-sig')
    tasks_details = tasks_file.readlines()
    # To assess the amount of tasks in total
    # The code then gets the length of the tasks_details using the len function, and assigns it to the variable
    # total_tasks. This variable is used to show the total number of tasks in the file.
    total_tasks = len(tasks_details)
    # for loop through each line of the file, enumerating each task and output the information accordingly.
    # The code then uses a for loop to iterate over the lines in the "tasks_details" variable, and for each line, it
    # splits the line by ", " and assigns the resulting list to the "tasks_details" variable. The for loop enumerates
    # the tasks starting from 1, and for each task, it prints the task information (task title, assigned to, date
    # assigned, due date, task complete, and task description) in a specific format.
    for pos, line in enumerate(tasks_details, 1):
        # Split that line where there is comma and space.
        tasks_details = line.rstrip('\n').split(", ")
        # Then print the results in the format shown in the Output 2
        print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
              f"Task {pos} :\t\t\t\t{tasks_details[1]}\n"
              f"Assigned To:\t\t\t{tasks_details[0]}\n"
              f"Date Assigned:\t\t\t{tasks_details[3]}\n"
              f"Due Date:\t\t\t\t{tasks_details[4]}\n"
              f"Task Complete?:\t\t\t{tasks_details[5]}\n"
              f"Task description:\n{tasks_details[2]}")
    # Prompt the user accordingly and close the 'tasks.txt' file as no loger required.
    # Finally, the code prints a message indicating that all the tasks have been listed above and the current date.
    # The file is then closed as it is no longer needed.
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"{GREEN}All {total_tasks} Have Been Listed Above ({todays_date}).{WHITE}")
    tasks_file.close()


# ====View My Tasks Section====
# This function called "view_mine()" that is used to view all tasks that have been assigned to the currently
# logged-in user.
def view_mine(username):
    # The function takes one parameter "username" which is the username of the currently logged-in user. The function
    # starts by printing a message to indicate that the user is in the "View My Tasks" section of the program.
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"\t\t\t\t\t\t\t\t\t\t{GREY}VIEW MY TASKS{WHITE}")
    # The function then opens a file called "tasks.txt" in read mode, reads all the lines of the file, and uses a for
    # loop to iterate over the lines. For each line, it splits the line by ", " and assigns the resulting list to the
    # variable "task". If the first element in the list (username) matches the currently logged-in user, it appends the
    # task to the list "tasks".
    tasks = []
    with open("tasks.txt", "r", encoding='utf-8-sig') as f:
        for line in f:
            task = line.strip().split(", ")
            if task[0] == username:
                tasks.append(task)
    # If the list "tasks" is empty, it prints a message indicating that the user does not have any tasks assigned, and
    # returns to the main menu.
    if not tasks:
        print(f"{GREEN} You Don't Have Tasks Assigned.\n=> Returning To Main Menu <={WHITE}")
    else:
        # If the list is not empty, the function enters a while loop. Inside the while loop, it prints the header of
        # the table and all the tasks assigned to the user in a specific format. It then prompts the user to enter the
        # task number to view the details, or -1 to return to the main menu.
        while True:
            headers = ["Task Nr.", "Task Title", "                            Due Date", "  Task Closed?"]
            print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
                  f"The following tasks have been assigned to \'{username}\': ")
            print("    ".join(headers))
            for i, task in enumerate(tasks):
                length = int(len(task[1]))
                char = 35 - length
                print(f"{i + 1}.         {task[1]}", " " * char, f"\t- {task[4]} - {task[5]}")
            choice = input(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
                           f"Enter The Task Number To View Details. Enter -1 to return to main menu: ")

            if choice == "-1":
                print(f"{ITALIC_S}{GREEN}=> Returning To Main Menu <={ITALIC_E}{WHITE}")
                break

            elif not choice.isdigit() or int(choice) < 1 or int(choice) > len(tasks):
                print(f"{RED}Invalid choice. Please Try Again.{WHITE}")

            else:
                # If the user enters a valid task number, it shows the task details and prompt the user to mark the
                # task as complete, edit the task or return to the main menu.
                task = tasks[int(choice) - 1]
                if task[5] == "Yes":
                    print(f"{RED}This Task Has Already Been Completed.{WHITE}")
                else:
                    while True:
                        print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
                              f"You Have Chosen The Following Task:\n"
                              f"Task Title:\t\t\t\t{task[1]}\n"
                              f"Task Description:\t\t{task[2]}\n"
                              f"Assigned To:\t\t\t{task[0]}\n"
                              f"Assigned Date:\t\t\t{task[3]}\n"
                              f"Due Date:\t\t\t\t{task[4]}\n"
                              f"Task Complete?:\t\t\t{task[5]}\n"
                              f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
                              f"Please Select One Of The Following Options:")
                        edit_choice = input("[  1. ] - Mark The Task As Complete\n"
                                            "[  2. ] - Edit Task\n"
                                            "[ -1. ] - To Go Back\n"
                                            "Please Enter Your Choice: ")
                        # If the user chooses to mark the task as complete, it calls the "mark_complete()" function and
                        # passes the task as an argument. If the user chooses to edit the task, it calls the
                        # "edit_task()" function and passes the task as an argument.
                        if edit_choice == "1":
                            mark_complete(task)
                            break
                        elif edit_choice == "2":
                            edit_task(task)
                            tasks = []
                            with open("tasks.txt", "r", encoding='utf-8-sig') as f:
                                for line in f:
                                    task = line.strip().split(", ")
                                    if task[0] == username:
                                        tasks.append(task)
                            break
                        # The loop continues until the user enters -1 to return to the main menu. Once the user exits
                        # the loop, the function closes the "tasks.txt" file and the code execution returns to the
                        # main menu.
                        elif edit_choice == "-1":
                            break
                        else:
                            print(f"{RED}Invalid choice. Please try again.{WHITE}")


# This function called "mark_complete()" that takes in a single argument, "task", marking the task completed
def mark_complete(task):
    # The function first updates the 6th element of the task list to be "Yes" and the 4th element of the task list to
    # be the value of the variable "todays_date".
    task[5] = "Yes"
    task[3] = todays_date
    # The function then opens a text file called "tasks.txt" in read mode with the UTF-8-SIG encoding, reads all the
    # lines in the file, and then opens the same text file in write mode with the same encoding. It then iterates
    # through each line in the read lines and checks if the second element of the line (after being split by ", ") is
    # not equal to the second element of the task list. If it is not equal, it writes the original line to the text
    # file. If it is equal, it writes the updated task list with a newline character at the end.
    with open("tasks.txt", "r", encoding='utf-8-sig') as f:
        lines = f.readlines()
    with open("tasks.txt", "w", encoding='utf-8-sig') as f:
        for line in lines:
            if line.strip().split(", ")[1] != task[1]:
                f.write(line)
            else:
                f.write(", ".join(task))
                f.write("\n")
    # Lastly, it prints a message with the text "Task Marked As complete On {todays_date}." where {todays_date} is the
    # value of the variable "todays_date".
    print(f"{GREEN}Task Marked As complete On {todays_date}.{WHITE}")


# This function called "edit_task()" that takes in a single argument, "task"
def edit_task(task):
    # Inside the function, it enters an infinite loop (while True) that displays a menu of options for editing the task.
    # The menu options are "Edit assignee", "Edit due date", and "To Go Back".
    while True:
        edit_choice = input(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
                            f"[  1. ] - Edit assignee\n"
                            f"[  2. ] - Edit due date\n"
                            f"[ -1. ] - To Go Back\n"
                            f"Please Enter Your choice: ")
        # The user is prompted to input their choice, and the function then enters a series of if-elif statements to
        # handle the user's choice. If the user chooses option 1, the function prompts the user to enter a new assignee,
        # and then uses a separate function "check_user_exists(task[0])" to check if the new assignee exists. If the
        # user does not exist, the function displays an error message and prompts the user to enter a new assignee.
        if edit_choice == "1":
            initial_user = task[0]
            while True:
                task[0] = input("Enter New Assignee: ")
                if not check_user_exists(task[0]):
                    print(f"{RED}Sorry, We Can't Find An Account On That User Name.{WHITE}\n"
                          f"───────────────────────────────────────────────────────────────────────────────────────────────")
                    continue
                # If the user exists, the function updates the 4th element of the task list to be the value of the
                # variable "todays_date", opens a text file called "tasks.txt" in read mode, reads all the lines in the
                # file, and then opens the same text file in write mode with the same encoding.
                else:
                    task[3] = todays_date
                    with open("tasks.txt", "r", encoding='utf-8-sig') as f:
                        lines = f.readlines()
                    with open("tasks.txt", "w", encoding='utf-8-sig') as f:
                        # It then iterates through each line in the read lines and checks if the second element of the
                        # line (after being split by ", ") is not equal to the second element of the task list. If it
                        # is not equal, it writes the original line to the text file. If it is equal, it writes the
                        # updated task list with a newline character at the end.
                        for line in lines:
                            if line.strip().split(", ")[1] != task[1]:
                                f.write(line)
                            else:
                                f.write(", ".join(task))
                                f.write("\n")
                    # Lastly, it prints a message with the text "Assigned User Updated from {initial_user} to {task[0]}.
                    # Task Edited On {todays_date}." where {initial_user} is the initial assignee and {task[0]} is the
                    # new assignee and {todays_date} is the value of the variable "todays_date".
                    print(f"{GREEN}Assigned User Updated from \'{initial_user}\' to \'{task[0]}\'. "
                          f"Task Edited On {todays_date}.{WHITE}")
                    return
        # If the user chooses option 2, the function prompts the user to enter a new due date, and then updates the 5th
        # element of the task list to be the value of the new due date and the 4th element of the task list to be the
        # value of the variable "todays_date", opens a text file called "tasks.txt" in read mode, reads all the lines
        # in the file, and then opens the same text file in write mode with the same encoding.
        elif edit_choice == "2":
            initial_due_date = task[4]
            task[4] = input("Please Enter The New Due Date For The Task (DD/MM/YY):\n==> ").split("/")
            task_due_date = task[4]
            task[4] = store_date(task_due_date)
            task[3] = todays_date
            with open("tasks.txt", "r", encoding='utf-8-sig') as f:
                lines = f.readlines()
            with open("tasks.txt", "w", encoding='utf-8-sig') as f:
                # It then iterates through each line in the read lines and checks if the second element of the line
                # (after being split by ", ") is not equal to the second element of the task list. If it is not equal,
                # it writes the original line to the text file. If it is equal, it writes the updated task list with a
                # newline character at the end.
                for line in lines:
                    if line.strip().split(", ")[1] != task[1]:
                        f.write(line)
                    else:
                        f.write(", ".join(task))
                        f.write("\n")
            # Lastly, it prints a message with the text "Due Date Has Been Updated from {initial_due_date} to {task[4]}.
            # Task Edited On {todays_date}." where {initial_due_date} is the initial due date, {task[4]} is the new due
            # date and {todays_date} is the value of the variable "todays_date".
            print(f"{GREEN}Due Date Has Been Updated from \'{initial_due_date}\' to \'{task[4]}. "
                  f"Task Edited On {todays_date}.{WHITE}")
            return
        # If the user chooses option -1, the function breaks the infinite loop and exits.
        elif edit_choice == "-1":
            break
        # If the user enters any other choice, the function displays an error message "Invalid choice.
        # Please try again.".
        else:
            print(f"{RED}Invalid choice. Please try again.{WHITE}")

# Side Note: OK I confess after one entire week of iterations, trial, errors and blunders I believe that I have managed
# to make this function work as requested on the task assignment... What a challenge...
# This function gen_reports() that generates reports of task statistics.
def gen_reports():
    # The function starts by printing a banner with the title "GENERATE REPORTS", and then proceeds to read data from
    # two text files, "tasks.txt" and "user.txt". It initializes several variables to store statistics, such as the
    # total number of tasks, completed tasks, and overdue tasks.
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"\t\t\t\t\t\t\t\t\t\t{ORANGE}GENERATE REPORTS{WHITE}\n"
          f"───────────────────────────────────────────────────────────────────────────────────────────────")
    # Read data from tasks.txt file
    with open("tasks.txt", "r", encoding='utf-8-sig') as f:
        tasks = f.readlines()
    # Read data from user.txt file
    with open("user.txt", "r", encoding='utf-8-sig') as file:
        usernames = file.readlines()
    # Initialize variables to store statistics
    total_tasks = len(tasks)
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    user_task_count = {}
    user_task_completion = {}
    completed_task_count = {}
    user_incomplete_count = {}
    user_overdue_count = {}
    today = datetime.strptime(todays_date, "%d %b %Y").date()
    # The code then loops through the tasks in the "tasks.txt" file, and for each task, it splits the task data into
    # variables for the assigned user, completion status, and due date. It then uses these variables to update the
    # statistics, such as counting the total number of tasks assigned to each user, and the number of completed,
    # uncompleted, and overdue tasks for each user.
    # Count tasks for each user
    for task in tasks:
        task_data = task.strip().split(", ")
        assigned_user = task_data[0]        # all users from tasks
        completion_status = task_data[-1]   # all yes and nos
        # The code also includes the use of the datetime module, which is used to convert the due date strings from
        # the "tasks.txt" file into date objects for comparison with the current date.
        due_date = datetime.strptime(task_data[-2], "%d %b %Y").date()  # all task due dates
        # Checks if the assigned user is already in the user_task_count dictionary. If they are not, the code adds them
        # to the dictionary with a value of 0.
        if assigned_user not in user_task_count:
            user_task_count[assigned_user] = 0
            # It also creates a new dictionary inside the user_task_completion dictionary with the assigned user as
            # key, with three properties "completed", "uncompleted" and "overdue" as key with initial value as zero
            user_task_completion[assigned_user] = {"completed": 0, "uncompleted": 0, "overdue": 0}
        # Then, it increments the count of tasks assigned to that user by 1
        user_task_count[assigned_user] += 1
        # If the task has been completed, the code increments the count of completed tasks by 1 and increments the
        # number of completed tasks for that user.
        if completion_status == "Yes":
            completed_tasks += 1
            user_task_completion[assigned_user]["completed"] += 1
        # If the task is not completed, the code increments the count of uncompleted tasks by 1, increments the number
        # of uncompleted tasks for that user and if the due date of the task is less than today, it increments the
        # count of overdue tasks and increments the number of overdue tasks for that user.
        else:
            uncompleted_tasks += 1
            user_task_completion[assigned_user]["uncompleted"] += 1
            if due_date < today:
                overdue_tasks += 1
                user_task_completion[assigned_user]["overdue"] += 1
    # After the loop, the code writes the task statistics to a new file, "task_overview.txt". The file includes
    # information such as the total number of tasks, completed tasks, uncompleted tasks, and overdue tasks, as well as
    # the percentage of tasks that are complete, incomplete, and overdue.
    # Write task overview to task_overview.txt
    with open("task_overview.txt", "w", encoding='utf-8-sig') as task_file:
        task_file.write(
            f"─────────────────────────────────────────────────────────────────────────────────────────────\n")
        task_file.write(f"\t\t\t\t\t\t\t\t\t\t{BLUE}TASK OVERVIEW{WHITE}\n")
        task_file.write(
            f"─────────────────────────────────────────────────────────────────────────────────────────────\n")
        task_file.write("Total number of tasks:\t\t\t\t\t\t {}\n".format(total_tasks))
        task_file.write("Total number of completed tasks:\t\t\t {}\n".format(completed_tasks))
        task_file.write("Total number of uncompleted tasks:\t\t\t {}\n".format(uncompleted_tasks))
        task_file.write("Total number of overdue tasks:\t\t\t\t {}\n".format(overdue_tasks))
        #  It calculates this percentage by dividing the number of completed tasks by the total number of tasks and
        #  multiplying by 100. The result is formatted to two decimal places using the :.2f} format specifier.
        task_file.write(
            "Percentage of tasks that are complete:\t\t {:.2f}%\n".format((completed_tasks / total_tasks) * 100))
        # It calculates this percentage by dividing the number of uncompleted tasks by the total number of tasks and
        # multiplying by 100. The result is formatted to two decimal places using the :.2f} format specifier.
        task_file.write(
            "Percentage of tasks that are incomplete:\t {:.2f}%\n".format((uncompleted_tasks / total_tasks) * 100))
        # It calculates this percentage by dividing the number of overdue tasks by the total number of tasks and
        # multiplying by 100. The result is formatted to two decimal places using the :.2f} format specifier.
        task_file.write("Percentage of tasks that are overdue:\t\t {:.2f}%".format((overdue_tasks / total_tasks) * 100))

        # The code also writes the user-specific statistics to another file "user_overview.txt" which includes
        # information such as the total number of tasks assigned to each user, the number of completed, uncompleted,
        # and overdue tasks for each user, and the percentage of tasks that are complete, incomplete, and overdue for
        # each user.
        # Write user overview to user_overview.txt
        with open("user_overview.txt", "w", encoding='utf-8-sig') as user_file:
            user_file.write(
                f"───────────────────────────────────────────────────────────────────────────────────────────────\n")
            user_file.write(f"\t\t\t\t\t\t\t\t\t\t{BLUE}USER OVERVIEW{WHITE}\n")
            user_file.write(
                f"───────────────────────────────────────────────────────────────────────────────────────────────\n")
            user_file.write(
                f"Total number of tasks generated and tracked using the SMALL BUSINESS TASK MANAGER:\t {len(tasks)}\n")
            user_file.write(
                f"Total number of users registered in the SMALL BUSINESS TASK MANAGER:\t\t\t\t {len(usernames)}\n")
            for user in user_task_count:
                user_file.write(
                    f"───────────────────────────────────────────────────────────────────────────────────────────────\n")
                user_file.write(f"Username: {user}\n")
                # creation/uptate three dictionaries: "completed_task_count", "user_incomplete_count", and
                # "user_overdue_count". Each of these dictionaries is associated with the "user" variable, and the
                # values being assigned to them are coming from the dictionary "user_task_completion" which is also
                # associated with the "user" variable, specifically from the "completed", "uncompleted" and "overdue"
                # keys.
                completed_task_count[user] = user_task_completion[user]["completed"]
                user_incomplete_count[user] = user_task_completion[user]["uncompleted"]
                user_overdue_count[user] = user_task_completion[user]["overdue"]
                user_file.write(f"Total number of tasks assigned to\t\t\t\t {user}: {str(user_task_count[user])}\n")
                #  information is retrieved from the dictionary completed_task_count using the user as the key.
                user_file.write(f"Total number of tasks completed by\t\t\t\t {user}: {completed_task_count[user]}\n")
                #  information is retrieved from the dictionary user_incomplete_count using the user as the key.
                user_file.write(
                    f"Total number of tasks not yet completed by\t\t {user}: {user_incomplete_count[user]}\n")
                # information is retrieved from the dictionary user_overdue_count using the user as the key.
                user_file.write(f"Total number of tasks overdue from\t\t\t\t {user}: {user_overdue_count[user]}\n")
                #  It is calculated by dividing the number of completed tasks for the user by the total number of tasks
                #  assigned to the user, and multiplying by 100. The result is rounded to two decimal places using the
                #  round() function.
                user_file.write(
                    f"Percentage of tasks assigned to {user} that have been completed:\t\t\t\t\t\t\t {round((completed_task_count[user] / user_task_count[user]) * 100, 2)}%\n")
                #  It is calculated by dividing the number of uncompleted tasks for the user by the total number of
                #  tasks assigned to the user, and multiplying by 100. The result is rounded to two decimal places
                #  using the round() function.
                user_file.write(
                    f"Percentage of tasks assigned to {user} that must still be completed:\t\t\t\t\t\t {round((user_incomplete_count[user] / user_task_count[user]) * 100, 2)}%\n")
                # It is calculated by dividing the number of overdue tasks for the user by the total number of tasks
                # assigned to the user, and multiplying by 100. The result is rounded to two decimal places using the
                # round() function.
                user_file.write(
                    f"Percentage of tasks assigned to {user} that have not yet been completed and are overdue:\t {round((user_overdue_count[user] / user_task_count[user]) * 100, 2)}%\n")
        # check user in tasks.txt and not in user.txt
        # It opens the "user.txt" file, reads all the lines and create a set of all users, which is stored in
        # 'usernames'. It then opens "tasks.txt" file, reads all the lines and create a set of all users who are
        # assigned tasks, which is stored in 'tasks_usernames'. It calculates the difference between these two sets,
        # which gives the set of users who have been registered in the system but do not have any current tasks
        # assigned. Finally, it then opens the "user_overview.txt" file in append mode, and writes the above calculated
        # set of users to the file.
        with open("user.txt", "r", encoding='utf-8-sig') as file:
            usernames = set(line.strip().split(", ")[0] for line in file)
        with open("tasks.txt", "r", encoding='utf-8-sig') as f:
            tasks_usernames = set(line.strip().split(", ")[0] for line in f)
        not_assigned_user = usernames - tasks_usernames
        with open("user_overview.txt", "a+", encoding='utf-8-sig') as user_file:
            user_file.write(
                f"───────────────────────────────────────────────────────────────────────────────────────────────\n")
            user_file.write(f"The Following Users Have Been Registered In The System And Do Not Have Any Current "
                            f"Tasks Assigned:\nUsernames: " + ", ".join(not_assigned_user))
    print(f"{GREEN}TASK OVERVIEW and USER OVERVIEW Reports Have Been Generated.\n"
          f"Please Visualise Both Reports on the Display Statistics Section.{WHITE}")


# This function called "display_stats()" that prints overall statistics about tasks and users.
def display_stats():
    print(f"───────────────────────────────────────────────────────────────────────────────────────────────\n"
          f"\t\t\t\t\t\t\t\t\t  {PURPLE}OVERALL STATISTICS{WHITE}\n"
          f"───────────────────────────────────────────────────────────────────────────────────────────────")
    # Open the 'tasks.txt' file on reading mode to read the lines of the file for the relevant information.
    # Inform the user about the total number of tasks that have been logged and close the associated file afterwards
    tasks_file = open("tasks.txt", "r", encoding='utf-8-sig')
    for line in tasks_file:
        tasks_total = tasks_file.readlines()
        print(f"Total Of Registered Tasks:", len(tasks_total) + 1)
    tasks_file.close()
    # Open the 'user.txt' file on reading mode to read the lines of the file for the relevant information.
    # Inform the user about the total number of users that have been logged and close the associated file afterwards
    user_file = open("user.txt", "r", encoding='utf-8-sig')
    for line in user_file:
        users_total = user_file.readlines()
        print(f"Total Of Registered Users:", len(users_total) + 1)
    user_file.close()
    print(f"{GREEN}These Are The Statics At Today's Date: {todays_date}.{WHITE}")
    # while loop prompts the user to select one of the options "1" or "2" to display the contents of the files
    # "task_overview.txt" or "user_overview.txt" respectively. The user can also select "-1" to exit the loop and
    # the function.
    while True:
        rep_choice = input(f"────────────────────────────────────────────────────────────────────────────────────────"
                           f"───────\nTo Visualise The Reports, Please Select one of the below options:\n"
                           f"[  1. ] - TASK OVERVIEW Report\n"
                           f"[  2. ] - USER OVERVIEW Report\n"
                           f"[ -1. ] - To Go Back\n"
                           f"Please Enter Your Choice: ")
        if rep_choice == "1":
            with open("task_overview.txt", "r", encoding='utf-8-sig') as f:
                print(f.read())
                continue
        elif rep_choice == "2":
            with open("user_overview.txt", "r", encoding='utf-8-sig') as f:
                print(f.read())
                continue
        elif rep_choice == "-1":
            break
        # If the user enters an invalid choice, it will print an error message and prompt the user again.
        else:
            print(f"{RED}Invalid choice. Please try again.{WHITE}")


# Programme Start
# It calls two functions, login() and main_menu(username). The first function call login() is invoked, which prompts
# the user to enter their username and password. It then attempts to match the entered information with a pre-existing
# list of usernames and passwords. If the entered information is valid, the function returns the entered username.
# The second function call main_menu(username) is invoked with the returned value from the previous function call. The
# function main_menu(username) takes the entered username as an argument, and likely uses it to display the main menu
# options to the user and perform actions based on the user's selections.
username = login()
main_menu(username)
