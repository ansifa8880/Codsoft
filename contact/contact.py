class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}"

    def __repr__(self):
        return f"Contact('{self.name}', '{self.phone}', '{self.email}', '{self.address}')"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts.append(Contact(name, phone, email, address))
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("Contact list is empty.")
    else:
        print("Contact List:")
        print("-" * 20)
        for i, contact in enumerate(contacts, start=1):
            print(f"Contact {i}:")
            print(contact)
            print("-" * 20)

def search_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            print(contact)
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for i, contact in enumerate(contacts):
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            print(f"Contact {i+1}:")
            print(contact)
            print("-" * 20)
            name = input("Enter new name (leave blank to keep current): ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            if name:
                contact.name = name
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if address:
                contact.address = address
            print("Contact updated successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

def delete_contact():
    search_term = input("Enter name or phone number to search: ")
    found = False
    for i, contact in enumerate(contacts):
        if search_term.lower() in contact.name.lower() or search_term in contact.phone:
            del contacts[i]
            print("Contact deleted successfully!")
            found = True
            break
    if not found:
        print("Contact not found.")

contacts = []

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
