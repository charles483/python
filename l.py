contacts = {}

def start():
    print("Welcome to Contact+")
    name = input("Please enter your name: ")
    print("Hi " + name + ", would you like to check your current contacts or make new ones?")
    print("To make new contacts type in 'New'")
    print("To check current contacts type in 'Contacts'")
    choose = input("Go to: ").lower()
    
    if choose == 'new':
        new_function()
    elif choose == 'contacts':
        contacts_function()
    else:
        print("Invalid choice. Please try again.")
        start()

def new_function():
    print("\nPlease input the name: ")
    contact_name = input()
    print("Please input the number: ")
    contact_number = input()
    contacts[contact_name] = contact_number
    print("Contact created.")
    prompt_next_action()

def contacts_function():
    if not contacts:
        print("You don't have any contacts yet.")
    else:
        print("\nYour contacts:")
        for name, number in contacts.items():
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
        new_function()
    elif choice == 'contacts':
        contacts_function()
    else:
        print("Invalid choice. Please try again.")
        prompt_next_action()

start()
