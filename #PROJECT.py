#PROJECT


#PROJECT


'''main program-
a) registers elderly citizen in the network
b) registers volunteers
c) asks elders what work they need help with (for e.g. grocery shopping, transportation, etc.)
d) allows volunteers to view the requests for help and accept them'''

citizens = []  # List of dictionaries to store citizens
volunteers = []  # List of dictionaries to store volunteers
def register_user(): #registering people as either volunteers or elder citizens
    print("\n--- Register ---")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    contact = input("Enter your contact number: ")

    role = input("Are you a Citizen (C) or a Volunteer (V)? ").strip().lower()

    if role == 'c':
        address = input("Enter your address: ")
        helpin= input("Enter only one thing what you need help with:-\n1)Groceries\n2)Care taker\n3)Pet- Care taker\n4)Cleaning\n5)Doing Laundry\n6)Arranging goods\n7)Electrician\n8)Plumber\n9)Beautician\n10)Digital Literacy\n11)Gardening\n12)Medical Aid\n13)Excercise/Trainer/Yoga Instructor\n14)Therapist\n15)Cooking\n16)Transportation\n17)Mechanic\n18)Carpenter\n19)Tailor\n20)Barber: ")
        citizens.append({'name': name, 'age': age, 'contact': contact, 'address': address, 'help': helpin})
        print(f"\nCitizen {name} registered successfully!")

    elif role == 'v':
        skill = input("Enter your skill(s) from the following list:-\n1)Groceries\n2)Care taker\n3)Pet- Care taker\n4)Cleaning\n5)Doing Laundry\n6)Arranging goods\n7)Electrician\n8)Plumber\n9)Beautician\n10)Digital Literacy\n11)Gardening\n12)Medical Aid\n13)Excercise/Trainer/Yoga Instructor\n14)Therapist\n15)Cooking\n16)Transportation\n17)Mechanic\n18)Carpenter\n19)Tailor\n20)Barber: ")
        rate= int(input("Enter the amount that you'd like to charge for your work: "))
        volunteers.append({'name': name, 'age': age, 'contact': contact, 'skill': skill, 'rate':rate})
        print(f"\nVolunteer {name} registered successfully!")
    else:
        print("Invalid input. Please try again.")

def list_users(): #Lists all citizens or volunteers based on user input.
    print("\n--- List Users ---")
    choice = input("Do you want to list Citizens (C) or Volunteers (V)? ").strip().lower()

    if choice == 'c':
        if not citizens: #i.e. if "citizens" list is empty
            print("No citizens registered yet.")
        else: #if the list has minimum 1 entry
            print("\nRegistered Citizens:")
            for i, citizen in enumerate(citizens, 1):
                print(f"{i}. Name: {citizen['name']}, Age: {citizen['age']}, Contact: {citizen['contact']}, Address: {citizen['address']}, Help: {citizen['help']}")

    elif choice == 'v':
        if not volunteers:
            print("No volunteers registered yet.")
        else:
            print("\nRegistered Volunteers:")
            for i, volunteer in enumerate(volunteers, 1):
                print(f"{i}. Name: {volunteer['name']}, Age: {volunteer['age']}, Contact: {volunteer['contact']}, Skill: {volunteer['skill']}, Rate: {volunteer['rate']}")
    else:
        print("Invalid input. Please try again.")

def pair_volunteer_to_citizen():
    """Pairs a volunteer with a citizen and displays the pair."""
    print("\n--- Pair Volunteer to Citizen ---")

    if not citizens or not volunteers:
        print("You need at least one citizen and one volunteer to create a pair.")
        return

    print("\nChoose a Citizen:")
    for i, citizen in enumerate(citizens, 1):
        print(f"{i}. {citizen['name']} {citizen['help']}")

    citizen_choice = int(input("Enter the registration number of the citizen: ")) - 1

    print("\nChoose a Volunteer:")
    for i, volunteer in enumerate(volunteers, 1):
        for j in citizens:
            if j['help'] in volunteer['skill']:
                print(f"{i}. {volunteer['name']} : {volunteer['skill']}\nRate = {volunteer['rate']}")
    volunteer_choice = int(input("Enter the registration number of the volunteer: ")) - 1

    citizen = citizens[citizen_choice]
    volunteer = volunteers[volunteer_choice]

    print(f"\nPair Created: {volunteer['name']} will help {citizen['name']}.")
    print(f"Contact {volunteer['name']} at {volunteer['contact']}.")

def main():
    """Main menu to navigate through the program."""
    while True:
        print("\n=== Elderly Citizens Help Network ===")
        print("1. Register User")
        print("2. List Users")
        print("3. Pair Volunteer with Citizen")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            register_user()
        elif choice == '2':
            list_users()
        elif choice == '3':
            pair_volunteer_to_citizen()
        elif choice == '4':
            print("Exiting the program. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")
#end of main program


'''Medicine reminder'''
import time
from datetime import datetime
medicine_schedule = []
def add_medicine():
    print("\n--- Add Medicine ---")
    name = input("Enter the name of the medicine: ")
    time_to_take = input("Enter the time to take (in HH:MM, 24-hour format): ") #"23:24"

    try:
        datetime.strptime(time_to_take, "%H:%M")
        medicine_schedule.append({'name': name, 'time': time_to_take})
        print(f"Medicine '{name}' scheduled at {time_to_take} successfully!")
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM format.")


def show_schedule():
    """Display the list of medicines with their scheduled times."""
    print("\n--- Medicine Schedule ---")
    if not medicine_schedule:
        print("No medicines scheduled.")
    else:
        for i, med in enumerate(medicine_schedule, 1):
            print(f"{i}. {med['name']} at {med['time']}")


def check_reminders():
    """Check every minute to see if it's time to take any medicine."""
    print("\n--- Medicine Reminder Service Started ---")
    while True:
        now = datetime.now().strftime("%H:%M")
        for med in medicine_schedule:
            if med['time'] == now:
                print(f"\nReminder: Time to take your medicine '{med['name']}'!")

        time.sleep(60)  # Check every 60 seconds


def medicine():
    """Main menu to navigate the program."""
    while True:
        print("\n=== Medicine Reminder System ===")
        print("1. Add Medicine")
        print("2. Show Medicine Schedule")
        print("3. Start Reminder Service")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_medicine()
        elif choice == '2':
            show_schedule()
        elif choice == '3':
            check_reminders()
        elif choice == '4':
            print("Exiting the program. Stay healthy!")
            break
        else:
            print("Invalid choice. Please try again.")
#end of medicine program


'''To-do List'''
from datetime import datetime, timedelta
import time
todo_list = []
def add_task():
    """Add a new task with a deadline."""
    print("\n--- Add Task ---")
    task_name = input("Enter the task description: ")
    due_date = input("Enter the due date (in YYYY-MM-DD format): ")

    try:
        # Validate the date input
        datetime.strptime(due_date, "%Y-%m-%d")
        todo_list.append({'task': task_name, 'date': due_date})
        print(f"Task '{task_name}' added for {due_date}!")
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")

def show_tasks():
    """Display all tasks with their deadlines."""
    print("\n--- To-Do List ---")
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. Task: {task['task']}, Due Date: {task['date']}")

def check_reminder():
    """Check if any task is due today."""
    print("\n--- Checking Reminders ---")
    today = datetime.now().strftime("%Y-%m-%d")

    tasks_due_today = [task for task in todo_list if task['date'] == today]

    if tasks_due_today:
        print("\nReminder: You have tasks due today!")
        for task in tasks_due_today:
            print(f" - {task['task']}")
    else:
        print("No tasks are due today.")

def reminder_service():
    """Start the reminder service to check for tasks daily."""
    print("\n--- Reminder Service Started ---")
    while True:
        check_reminder()
        print("\nNext reminder check will be in 24 hours.")
        time.sleep(86400)  # Wait for 24 hours (86400 seconds)

def to_do_lists():
    """Main menu to navigate the program."""
    while True:
        print("\n=== To-Do List for Elderly Citizens ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Start Reminder Service")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_task()
        elif choice == '2':
            show_tasks()
        elif choice == '3':
            reminder_service()
        elif choice == '4':
            print("Exiting the program. Stay productive!")
            break
        else:
            print("Invalid choice. Please try again.")
#end of to-do list program

#menu based program: taking input as to what option does the user want to select

CHOICE=int(input("1- Elderly Citizen Help Network \n2- Medicine Reminder System\n3- To-do List\nEnter your choice: "))
if CHOICE==1:
    main()
elif CHOICE==2:
    medicine()
elif CHOICE==3:
    to_do_lists()
else:
    print("\nEnter a valid choice")
