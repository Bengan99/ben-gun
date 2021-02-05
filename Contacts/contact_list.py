import contact_list_functions
import sys

def main ():
    contact_list = []
    while True:

        choice = int(input("Sta bi ste da radite? \n"
                            "(1) Add Contact \n"
                            "(2) Remove Contact \n"
                            "(3) Pogledaj kontakt \n"
                            "(4) Exit "))
        if choice == 4:
            sys.exit(0)
        if choice == 1:
            contact_list_functions.new_contact(contact_list)
        if choice == 2:
            contact_list_functions.remove_contact(contact_list)
        if choice == 3:
            contact_list_functions.view_contact(contact_list)

main()
