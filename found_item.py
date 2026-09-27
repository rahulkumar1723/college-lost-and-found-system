# found_item.py

found_items = []


def add_found_item():
    print("\n--- ADD FOUND ITEM ---")

    item = input("Enter item name: ")
    location = input("Enter where you found it: ")
    date = input("Enter date: ")
    contact = input("Enter your contact number: ")

    record = {
        "item": item,
        "location": location,
        "date": date,
        "contact": contact
    }

    found_items.append(record)

    print("Found item added successfully!")


def search_found_item():
    print("\n--- SEARCH FOUND ITEM ---")

    search = input("Enter item name to search: ")

    found = False

    for record in found_items:
        if record["item"].lower() == search.lower():
            print("\nItem:", record["item"])
            print("Location:", record["location"])
            print("Date:", record["date"])
            print("Contact:", record["contact"])
            found = True

    if found == False:
        print("No matching found item.")