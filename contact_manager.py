contacts = {}


class DuplicateContactError(Exception):
    pass


def add_contact(name, phone):
    """Add a contact to the contact list."""
    if name not in contacts:
        contacts[name] = phone
        print(f"{name} has been added!")
    else:
        raise DuplicateContactError("Contact already exists!")


def find_contact(name):
    """Find a contact from the contact list."""
    # Handles cases where the contact does not exist
    try:
        phone_number = contacts[name]
        print(f"{name}'s phone number is {phone_number}")
        return phone_number
    except KeyError:
        print("Contact not found.")
        return None


def delete_contact(name):
    """Delete a contact from the contact list."""
    # Handles cases where the contact does not exist
    try:
        del contacts[name]
        print(f"{name} has been deleted!")
    except KeyError:
        print("Not able to delete this contact.")


def main():
    """Main function that starts the contact manager."""
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")

        # Handles cases where input is not an Integer
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Choice.")
            continue

        if choice == 1:
            # Handles cases where user tries to add a duplicate contact
            try:
                name = input("Enter contact name: ")
                phone = input("Enter phone number: ")
                add_contact(name, phone)
            except DuplicateContactError as error:
                print(error)

        elif choice == 2:
            name = input("Enter name to find: ")
            find_contact(name)

        elif choice == 3:
            name = input("Enter name to delete: ")
            delete_contact(name)

        elif choice == 4:
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()