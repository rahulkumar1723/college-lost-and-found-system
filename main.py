# main.py

from lost_item import lost_items
from lost_item import add_lost_item
from lost_item import search_lost_item

from found_item import found_items
from found_item import add_found_item
from found_item import search_found_item

from display import display_lost_items
from display import display_found_items


while True:

    print("\n======================================")
    print("       COLLEGE LOST & FOUND SYSTEM")
    print("======================================")

    print("1. Add Lost Item")
    print("2. Add Found Item")
    print("3. Search Lost Item")
    print("4. Search Found Item")
    print("5. Display Lost Items")
    print("6. Display Found Items")
    print("7. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        add_lost_item()


    elif choice == 3:
        search_lost_item()

    elif choice == 4:
        search_found_item()

    elif choice == 5:
        display_lost_items(lost_items)

    elif choice == 6:
        display_found_items(found_items)

    elif choice == 7:
        print("\nThank you for using College Lost & Found System!")
        break

    else:
        print("\nInvalid choice. Please try again.")