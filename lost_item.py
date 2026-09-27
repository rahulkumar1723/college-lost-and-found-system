# lost_item.py

lost_items = []


def add_lost_item():
    print("\n--- ADD LOST ITEM ---")

    item = input("Enter item name: ")
    location = input("Enter where you lost it: ")
    date = input("Enter date: ")
    contact = input("Enter contact number: ")

    record = {
        "item": item,
        "location": location,
        "date": date,
        "contact": contact
    }

    lost_items.append(record)

    print("Lost item added successfully!")


def search_lost_item():
    print("\n--- SEARCH LOST ITEM ---")

    search = input("Enter item name to search: ")

    found = False

    for record in lost_items:
        if record["item"].lower() == search.lower():
            print("\nItem:", record["item"])
            print("Location:", record["location"])
            print("Date:", record["date"])
            print("Contact:", record["contact"])
            found = True

    if found == False:
        print("No matching lost item found.")