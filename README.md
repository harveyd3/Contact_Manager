Robust Contact Manager
-

Project Overview
-
The Robust Contact Manager is a Python program that lets its users add, find, or even delete
a contact from their contact list. The program uses a dictionary to store the names and phone
numbers. The program starts with a menu that the user selects from then after they select their
choice, they are able to use the program to their desire.

This project highlights error handling, the prevention of duplicate results, and testing programs
with Python's built-in unittest.

Bugs Fixed and Improvements
-
Invalid Menu:
    
    Added ValueError to handle input that cannot be converted to an integer.

Missing Contacts:
    
    Added KeyError to handle seaching for/deleting contacts that do not exist.

Duplicate Contacts:
    
    Created a DuplicateContactError exception to stop a contact from being added more than one time.

Error Messages:

    Added clear output messages to users so they know when a contact cannot be found, added, or deleted.

Unit Testing:

    Created tests using unittest to verify program is running without issues. 

How to Run the Program
-
1) Open Python compiler
2) Run the "contact_manager.py" file
3) Follow the menu prompts as given within the program

How to Run the Tests
-
1) Open Python compiler
2) Run the "test_contact_manager.py" file
3) Look at the terminal to determine any errors or issues within the code

Author
-
Da'Quantae Harvey
    