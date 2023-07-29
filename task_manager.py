# NOTE COMPULSORY TASK PART 1 AND PART 2

'''
This program can be used by a small business to manage tasks assigned
to each member of the team. It makes use of the following text files:
1. user.txt - stores the username and password for each user that has permisson
to use the program.
2. tasks.txt - stores a list of all the tasks that the team is working on.
'''
#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# Placeholder variable for the list of usernames.
usernames = []
# Placeholder variable for the list of passwords.
passwords = []

# Opening the user.txt text file in read mode.
with open("user.txt", "r", encoding="utf-8") as f:   
    for lines in f:
        # Removing all the new line charecters (\n).
        temp = lines.strip()
        # Converting the string into a list by using a 
        # comma and space delimeter.
        temp = lines.split(", ")
        # Amending the usernames list with each username.
        usernames.append(temp[0].strip())
        # Amending the passwords list with each password.
        passwords.append(temp[1].strip())

# Control/counter variable to control the number of times
# the user attempts to login.
counter = 0
# This boolean is used to grant access to the menu once 
# the user successfully logs in.
is_valid = False
# This valid_username global variable is used to check if the person logged in
# has any tasks to show when vm is selected from the menu.
valid_username = ""
# Password global variable just in case I need to use it later.
valid_password = ""

# This while loop gives the user 3 chances to enter the correct
# login details.
while counter < 3:
    # Ask the user to enter their valid username and password.
    login = input("Enter your username and password as follows:\nFirst, the username followed by a comma, a space and then the password.\n")
    delimeter = ", "
    
    # This loop checks the format of the users input. The counter does not count
    # until the user enters the username and password in the correct format as
    # instructed.
    while True:
        # Empty space check
        if not login:
            login = input("You have not entered a anything. Please enter as follows:\nFirst, the username followed by a comma, a space and then the password.\n")
            continue

        # Number check
        if login.isnumeric():
            login = input("Enter a username and password. Not a number:\nFirst, the username followed by a comma, a space and then the password.\n")
            continue

        # comma and space check
        if delimeter not in login:
            login = input("You have entered incorrectly:\nFirst, the username followed by a comma, a space and then the password.\n")
            continue

        else:
            # Breaks out the loop if the correct format is entered
            break

    # Removing all the new line charecters (\n).
    login = login.strip()
    # Converting the string into a list by using a 
    # comma and space delimeter.
    login = login.split(", ")
    # Setting the username to the first word entered by the user.
    username = login[0]
    # Setting the password to the second word entered by the user.
    password = login[1]

    # Checking if the username and password provided by the user are
    # in the lists of usernames and passwords that were created earlier.
    if username in usernames and password in passwords:
        # Set the is_valid boolean to true in order to present the 
        # menu to the user.
        valid_login = True
        # Set the valid_username variable to the valid username.
        valid_username = username
        # Set the valid_password variable to the valid password.
        valid_password = password
        # Inform the user that they have permission to continue.
        print("ACCESS GRANTED! You may proceed.\n")
        # Terminates the loop as soon as the correct details 
        # are entered.
        break
    # If the incorrect username and password is entered, the 
    # following happens.
    else:
        # The counter is incremented by one each time an incorrect value 
        # is entered.
        counter += 1
        # When the counter reaches 3, the program terminates.
        if counter == 3:
            # Telling the user they are not permitted to continue to the menu.
            print("You have entered incorrectly on 3 attempts. ACCESS DENIED!\nGoodbye!")
            break

        # Telling the user how many chances they have left to enter the correct
        # login details.
        print(f"Incorrect username or password. You have {3 - counter} attempts left.")


# This loop only executes once the correct username and password is entered.
while valid_login:
    # Cheking to see if the logged in user is admin or not, so a different 
    # menu can be displayed.
    if valid_username == "admin":
        #presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        s - View statistics
        e - Exit
        : ''').lower()
    else:
        #presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()


    if menu == 'r' and valid_username == "admin":
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        
        # Ask the user to create a new username.
        new_username = input("Create a new username: ")
        # Ask the user to create a new password.
        new_password = input("Create a new password: ")
        # Ask the user to confirm the new password.
        new_password_confirmation = input("Confirm password: ")
        # This loop will run until the user enters matching passwords.
        while True:
            # Checking to see if the user confirmed the password correctly.
            if new_password_confirmation == new_password:
                # Opening the user.txt text file in read mode
                with open("user.txt", "a", encoding="utf-8") as f:
                    # Appending the new username and password to the
                    # # user.txt text file. 
                    f.write(f"\n{new_username}, {new_password}")
                    print("Success! A new user has been created.")
                # This break terminates the loop as soon as the passwords match.
                break
            else:
                # Telling the user to re-enter the confirmation password so 
                # that it matches the first password.
                new_password_confirmation = input("Your passwords don't match. Try again. ")

    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        # Placeholder variable for the contents of the user.txt text file after we
        # have read it.
        content = ""

        # Opening the user.txt text file in read mode.
        with open("user.txt", "r", encoding="utf-8") as f:
            for line in f:
                content += line

        # First we check if the person the task will be assigned to is part of the team.
        while True:
            # Ask the user to enter the username of the person the task is assigned to.
            username = input("Enter the username of the person the task is assigned to: ")
            # Checking to see if the person exists in the user.txt text file that we
            # opened above.
            if username in content:
                break
            else:
                # Message presented to the user every time they enter a member
                # who is not a valid user.
                print(f"{username} is not a member of this team. Try again.")

        # Ask the user to enter a title for the new task.
        task_title = input("Enter the title of the task:\n")
        # Ask the user to enter a description of the new task.
        task_description = input("Enter the description of the task:\n")
        # Ask the user to enter a due date for the new task.
        due_date = input("Enter the due date for this task as follows,\nday Month Year: ")
        # Using the datetime module to get the current date and set it as the
        # date the task was created.
        d = datetime.date.today()
        # Using the time string format to present the date in the format we want.
        assigned_date = d.strftime("%d %b %Y")
        # This variable will always be "No" when a new task is created. It indicates
        # weather or not the task is complete. 
        is_completed = "No"
        # Opening the tasks.txt text file in append mode.
        with open("tasks.txt", "a", encoding="utf-8") as f:
            # Writing the new task in the tasks.txt text file.
            f.write(f"\n{username}, {task_title}, {task_description}, {assigned_date}, {due_date}, {is_completed}")
            print("Success! A new task has been added.")

    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        # Opening the tasks.txt text file in read mode
        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                # Removing all the new line charecters (\n).
                text = line.strip()
                # Converting the string into a list by using a
                # comma and space delimeter.    
                text = line.split(", ")

                # Displaying the task information using the values 
                # from index 0 to 5 of the task list created in the line above.           
                print(f"Assigned to:\t{text[0]}")
                print(f"Task:\t\t{text[1]}")
                print(f"Task description:\n {text[2]}")
                print(f"Date assigned:\t{text[3]}")
                print(f"Due date:\t{text[4]}")
                print(f"Task complete?\t{text[5]}")
                print()


    elif menu == 'vm':
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        with open("tasks.txt", "r", encoding="utf-8") as f:
            for line in f:
                # Searching for the line with the username that
                # is currently logged in so that the task can 
                # be presented to the user.
                if username in line:
                    # Removing all the new line charecters (\n).
                    text = line.strip()
                    # Converting the string into a list by using a
                    # comma and space delimeter.                
                    text = line.split(", ")

                    # Displaying the task information to the user using the values
                    # from index 0 to 5 of the task list created in the line above.               
                    print(f"Assigned to:\t{text[0]}")
                    print(f"Task:\t\t{text[1]}")
                    print(f"Task description:\n {text[2]}")
                    print(f"Date assigned:\t{text[3]}")
                    print(f"Due date:\t{text[4]}")
                    print(f"Task complete?\t{text[5]}")
                    print() 
                
    elif menu == 's' and valid_username == "admin":
        '''The admin user is provided with a new menu option that allows
           them to display statistics. When this menu option is selected, the
           total number of tasks and the total number of users should be
           displayed in a user-friendly manner.'''
        
        # Counter variable for the number of users in the team.
        num_of_users = 0
        # Opening the user.txt text file in read mode.
        with open("user.txt", "r", encoding="utf-8") as users:
            for line in users:
                # Incrementing the number of users by 1 each time.
                num_of_users += 1

        # Counter variable for the number of tasks.
        num_of_tasks = 0
        # Opening the tasks.txt text file in read mode.
        with open("tasks.txt", "r", encoding="utf-8") as tasks:
            for line in tasks:
                # Incrementing the number of tasks by 1 each time.
                num_of_tasks += 1

        print(f"Total number of users: {num_of_users}")
        print(f"Total number of tasks: {num_of_tasks}")

    # This part is used when the user wants to exit the program.
    elif menu == 'e':
        print('Goodbye!!!')
        # This function closes the program.
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
