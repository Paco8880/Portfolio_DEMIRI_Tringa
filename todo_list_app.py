# =============================================================================
# Design your own app - Winter Semester 2024 (WS24)
# Graz University of Technology
#
# Student ID  : 11845777
#
# > Ensure you comment your code where necessary.
# > External libraries are not permitted for this assignment.
# =============================================================================


# Initialize an empty list to store tasks
todo_list = []

#Function for the Welcome Message
def display_welcome_message():
    print("||=========================================================||")
    print("|| Welcome to the To-Do List App! Let's organise your day! ||")
    print("||=========================================================||")

#Showcasing the display menu
def display_help_menu():
    print("\n--- To-Do List App Features ---")
    print("0. Show Help Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Switch Tasks Order")
    print("5. Quit")

#Function for "Add Task"
def add_task():
    task = input("Enter the task: ")
    if task == "": 
        print("Empty tasks are not supposed to appear in Your To-Do List! Try adding something else.")
    else:
        todo_list.append(task)
        print(f'Task "{task}" was successfully added to the list!')


#Function for "View Task"
def view_tasks():
    if todo_list:
        print("\nYour To-Do List for today:")
        for index, task in enumerate(todo_list, start=1): #
            print(f"{index}) {task}")                    
    else:                                
        print("There are no tasks in the list at the moment. Create one right now!")


#Function for "Remove Task"
def remove_task():
    if not todo_list: 
        print("There are no tasks in the list at the moment. Create one right now!")
        return # this safely exits the function
    
    print("\nYour To-Do List for today:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}) {task}")

    task_number = input("\nEnter the task number to remove: ") 

    if not task_number.isdigit():  
        print("Invalid task number. Please try again.") 
        return                                             

    task_index = int(task_number) - 1
    if task_index < 0 or task_index >= len(todo_list):
        print("Invalid task number. Please try again.")
    else:
        removed_task = todo_list.pop(task_index) 
        print(f'Task "{removed_task}" was successfully removed from the list!') 

# Function for "Switch Tasks"   
def switch_tasks():
    
    if not todo_list:
        print("There are no tasks in the list at the moment. Create one right now!")
        return

    # Display the list of tasks for reference before any checks
    print("\nYour To-Do List for today:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}) {task}")

    
    if len(todo_list) == 1:
        print("\nThere is no point in switching when there is only one task in the list! Please, try something else.")
        return

    # Prompt for the first task number
    first_task_num = input("\nEnter the first task number: ").strip()
    if not first_task_num.isdigit() or int(first_task_num) - 1 not in range(len(todo_list)):
        print("Invalid task number. Please try again.")  
        return
    first_task_index = int(first_task_num) - 1

    # Prompt for the second task number
    second_task_num = input("Enter the second task number: ").strip()
    if not second_task_num.isdigit() or int(second_task_num) - 1 not in range(len(todo_list)): # Check if the input is a valid digit 
        print("Invalid task number. Please try again.")                                       #and within the list index range
        return
    second_task_index = int(second_task_num) - 1

    
    if first_task_index == second_task_index:
        print("There is no point in switching the task with itself! Please, try something else.")
        return

    # Swap tasks and confirm action
    todo_list[first_task_index], todo_list[second_task_index] = todo_list[second_task_index], todo_list[first_task_index]
    print("Tasks' positions were successfully switched!")



#function for quiting the app
def quit_app():
    print("\nThank you for using the To-Do List App. Goodbye!")
    exit(0)
    
#main code
def prompt_for_action():
    while True:
        user_input = input("\nWhat would you like to do? (enter a command number of your choice 0-5): ")
        
        if not user_input.isdigit():
            print("Please enter a valid number and try again!")
            continue

        command = int(user_input)
        
        if command < 0 or command > 5:
            print("Invalid choice of a number. Please try again.")
        else:
            if command == 0:
                display_help_menu()
            elif command == 1:
                add_task()
            elif command == 2:
                view_tasks()
            elif command == 3:
                remove_task()
            elif command == 4:
                switch_tasks()
            elif command == 5:
                quit_app()


display_welcome_message() # Shows a welcome message to the user when the program starts.
display_help_menu()      # Displays a list of available commands to guide the user.  
prompt_for_action()       # Begins the main loop that prompts the user for input and handles their chosen actions.





