contact = {}

def start():
    print("Welcome to our contact app")
    name = input("Enter name: ")
    print("Hello", name + ", would you like to create contacts?")
    print("For new contacts type 'New'")
    print("For viewing contacts type 'Contacts'")

    choice = input('Go to: ').lower()

    if choice == 'new':
        New_function(name)
    elif choice == 'contacts':
        Contacts_function()
    else:
        print("Invalid choice ")
        start()

def New_function(name):
    print("Enter name:", name)
    number = input("Enter a number: ")
    contact[name] = number
    print("Contact created.")
    prompt_next_action()

def Contacts_function():
    if not contact:
        print("You don't have any contacts yet.")
    else:
        print("\nYour contacts:")
        for name, number in contact.items():
            print("Name:", name)
            print("Number:", number)
            print("---------")
    prompt_next_action()

def prompt_next_action():
    print("\nWould you like to make more contacts or check current contacts?")
    print("To make new contacts type in 'New'")
    print("To check current contacts type in 'Contacts'")
    choice = input("Go to: ").lower()
    
    if choice == 'new':
        New_function(name)
    elif choice == 'contacts':
        Contacts_function()
    else:
        print("Invalid choice. Please try again.")
        prompt_next_action()

start()
