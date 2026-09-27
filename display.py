# display.py


def display_lost_items(items):
    print("\n========== LOST ITEMS ==========")

    if len(items) == 0:
        print("No lost items available.")
    else:
        for i in range(len(items)):
            print("\nItem Number:", i + 1)
            print("Item:", items[i]["item"])
            print("Location:", items[i]["location"])
            print("Date:", items[i]["date"])
            print("Contact:", items[i]["contact"])


def display_found_items(items):
    print("\n========== FOUND ITEMS ==========")

    if len(items) == 0:
        print("No found items available.")
    else:
        for i in range(len(items)):
            print("\nItem Number:", i + 1)
            print("Item:", items[i]["item"])
            print("Location:", items[i]["location"])
            print("Date:", items[i]["date"])
            print("Contact:", items[i]["contact"])