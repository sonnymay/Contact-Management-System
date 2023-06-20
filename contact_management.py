class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, email, phone):
        contact = Contact(name, email, phone)
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Email: {contact.email}, Phone: {contact.phone}")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully")
                return
        print(f"Contact {name} not found")

def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            phone = input("Enter phone: ")
            manager.add_contact(name, email, phone)
        elif choice == 2:
            manager.display_contacts()
        elif choice == 3:
            name = input("Enter name: ")
            manager.delete_contact(name)
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
