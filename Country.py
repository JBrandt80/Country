# Jeffrey Brandt
# CIS261
# Country

def display_menu():
    print("\nCOMMAND MENU")
    print("view - View a country")
    print("add  - Add a country")
    print("del  - Delete a country")
    print("exit - Exit program")

def initialize_country_dict():
    return {"US": "United States", "CA": "Canada", "JP": "Japan"}

def view_country(country_dict):
    print("\nAvailable country codes:")
    for code in country_dict:
        print(f"-{code}")
    user_key = input("Enter country code: ")
    if user_key in country_dict:
        print(f"Country name: {country_dict[user_key]}")
    else:
        print("Invalid code entered.")

def add_country(country_dict):
    code = input("Enter new country code: ")
    if code in country_dict:
        print("Code already exists.")
    else:
        name = input("Enter country name: ")
        country_dict[code] = name
        print(f"{name} added successfully.")

def delete_country(country_dict):
    code = input("Enter country code: ")
    if code in country_dict:
        name = country_dict[code]
        del country_dict[code]
        print(f"{name} was deleted.")
    else:
        print("Invalid code entered.")

def main():
    country_dict = initialize_country_dict()
    while True:
        display_menu()
        choice = input("Enter menu option: ")
        if choice == "view":
            view_country(country_dict)
        elif choice == "add":
            add_country(country_dict)
        elif choice == "del":
            delete_country(country_dict)
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__=="__main__":
    main()