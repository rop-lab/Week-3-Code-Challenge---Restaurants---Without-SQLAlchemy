from helpers import(list_customers, list_restaurant, list_reviews)


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            list_customers()
        elif choice == "2":
            list_restaurant()
        elif choice == "3":
            list_reviews()
        
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
def display_menu():
    print("1. list_customers")
    print("2. list_restaurant")
    print("3. list_reviews")
    print("4. Exit")

if __name__ == "__main__":

    main()