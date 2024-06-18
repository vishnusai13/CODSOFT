import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

# Load contacts from the file
def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to the file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    
    save_contacts(contacts)
    print(f"Contact {name} added successfully.")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ")
    
    found_contacts = {name: details for name, details in contacts.items() if search_term.lower() in name.lower() or search_term in details['phone']}
    
    if found_contacts:
        for name, details in found_contacts.items():
            print(f"\nName: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
    else:
        print("No contact found.")

# Update a contact's details
def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    
    if name in contacts:
        print("Enter new details (leave blank to keep current value):")
        phone = input(f"New phone number (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        
        save_contacts(contacts)
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found.")

# Main function to run the Contact Book application
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
