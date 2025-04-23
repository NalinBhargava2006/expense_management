import csv

expenses = []
password = 1234
filename = "expenses.csv"

def user_options():
    global expenses
    while True:
        print("\n=============User Options============")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Return to main menu")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter the username: ")
            category = input("Enter the expense category: ")
            amount = float(input("Enter the expense amount: "))
            expenses.append((username, (category, amount)))
            print("Expense added successfully!\n")

        elif choice == "2":
            username = input("Enter the username: ")
            total = sum(float(i[1][1]) for i in expenses if i[0] == username)
            print("Total Expenses:", total)

        elif choice == "3":
            username = input("Enter the username: ")
            print("Expenses by Category:")
            for i in expenses:
                if i[0] == username:
                    print(i[1][0], ":", i[1][1])

        elif choice == "4":
            break

def admin_settings():
    global password
    while True:
        print("\n============Admin Settings===========")
        print("1. Print all the Usernames")
        print("2. Change password")
        print("3. Return to main menu")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin = int(input("Enter the Admin Password: "))
            if admin == password:
                print("Expenses by Username:")
                for i in expenses:
                    print(i[0])
                    print(i[1][0], ":", i[1][1])
            else:
                print("Access Denied")

        elif choice == "2":
            admin = int(input("Enter the Current Admin Password: "))
            if admin == password:
                password = int(input("Enter the New Admin Password: "))
                print("Password Changed successfully.")
                print("NOTE: Running the program again will reset it.")

        elif choice == "3":
            break

def memory_options():
    global expenses
    while True:
        print("\n============Memory Options===========")
        print("1. Save Data")
        print("2. Load Data")
        print("3. Return to main menu")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            with open(filename, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                for entry in expenses:
                    writer.writerow([entry[0], entry[1][0], entry[1][1]])
            print("Data saved.")

        elif choice == "2":
            with open(filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                expenses = [(row[0], (row[1], float(row[2]))) for row in reader]
            print("Data loaded.")

        elif choice == "3":
            break

def main():
    while True:
        print("\n===========Expense Tracker===========")
        print("1. Open User Options")
        print("2. Open Admin Settings")
        print("3. Memory options")
        print("4. Quit")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_options()
        elif choice == "2":
            admin_settings()
        elif choice == "3":
            memory_options()
        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
