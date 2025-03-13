# Step 1: Create an empty dictionary to store contacts
contacts = {}

# Step 2: Function to add a contact
def add_contact():
    name = input("Enter contact name: ")  # Ask the user for the contact name
    phone = input("Enter phone number: ")  # Ask for the phone number

    # Check if name is not empty and phone contains only digits
    if name == "" or not phone.isdigit():
        print("Invalid input. Name can't be empty, and phone number must contain only digits.")
    else:
        contacts[name] = phone  # Add the contact to the dictionary
        print(f"Contact '{name}' added successfully.")

# Step 3: Function to view all contacts
def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.")
    else:
        print("All contacts:")
        for name, phone in contacts.items():
            print(f"Name: {name}, Phone: {phone}")  # Print each contact's name and phone number

# Step 4: Function to search for a contact by name
def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Found: {name}'s phone number is {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

# Step 5: Function to delete a contact
def delete_contact():
    name = input("Enter the name to delete: ")
    if name in contacts:
        del contacts[name]  # Delete the contact from the dictionary
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

# Step 6: Menu for the user to choose actions
def menu():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the menu function
menu()
