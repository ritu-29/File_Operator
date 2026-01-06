from datetime import datetime

class Journal:
    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        try:
            entry = input("Enter entry: ")
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a") as file:
                file.write(f"[{ts}]\n{entry}\n")
            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied")
    
    def view(self):
        try:
            with open(self.filename, "r") as file:
                f = file.read()

                if f.strip() == "":
                    print("Entries not found...Add New Entry!")
                    
                else:
                    print("\n Journal Entries:")
                    print(f)

        except FileNotFoundError:
            print("File Not Found!")
        
        
    def search(self):
        try:
            keyword = input("Enter keyword or date: ").lower()

            with open(self.filename, "r") as file:
                print("Matching Entries:")
    
                found = False
                for line in file:
                    if keyword in line.lower():
                        print(line.strip())
                        found = True

                if not found:
                    print("No matching entries")

        except FileNotFoundError:
            print("File not found...")

    def delete(self):
        confirm = input("Delete all entries? (yes/no): ").lower()

        if confirm == "yes":
            try:
                with open(self.filename, "w"):
                    pass
                    print("All entries deleted.")
            except PermissionError:
                print("Permission denied.")
        else:
            print("Deletion cancelled.")

def main():
    jn = Journal()

    while True:
        print("\n---Welcome---")
        print("Please select one:")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                jn.add_entry()
            elif choice == 2:
                jn.view()
            elif choice == 3:
                jn.search()
            elif choice == 4:
                jn.delete()
            elif choice == 5:
                print("Thank you for using Journal Manager....")
                break
            else:
                print("Invalid option.")

        except ValueError:
            print("Invalid input..")

main()
    