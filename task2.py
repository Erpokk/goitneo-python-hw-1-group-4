def parse_input(user_input):
    """
    Parse user input into command and arguments.

    Parameters:
    - user_input (str): User input string.

    Returns:
    - tuple: Command (str) and arguments (list of str).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def change_contact(args, contacts):
    """
    Change contact's phone number.

    Parameters:
    - args (list): List containing name (str) and new phone number (str).
    - contacts (dict): Dictionary containing contacts.

    Returns:
    - str: Message indicating success or failure of contact update.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Contact {name} not found."

def show_all (contacts):
    """
    Display all contacts and their phone numbers.

    Parameters:
    - contacts (dict): Dictionary containing contacts.

    Returns:
    - str: String representation of all contacts.
    """
    all_contacts = []
    for name, phone in contacts.items():
        all_contacts.append(f'{name} {phone}')
    return "\n".join(all_contacts)    
def show_phone(args, contacts):
    """
    Show phone number for a specific contact.

    Parameters:
    - args (list): List containing name (str) of the contact.
    - contacts (dict): Dictionary containing contacts.

    Returns:
    - str: Phone number of the contact or a message indicating contact not found.
    """
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return f"Contact {name} not found." 
def add_contact(args, contacts):
    """
    Add a new contact to the contacts dictionary.

    Parameters:
    - args (list): List containing name (str) and phone number (str) of the new contact.
    - contacts (dict): Dictionary containing contacts.

    Returns:
    - str: Message indicating success or failure of contact addition.
    """
    if args[0] in contacts:
        return "This contact is already in contacts. Use command 'change'"
    else:
        name, phone = args
        contacts[name] = phone
        return "Contact added."

def main():
    """
    Main function to run the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
