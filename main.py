# Function to display a record
def display_record(record):
    for key, value in record.items():
        print(f"\t{key}: {value}")

# Function to iterate and display record_list
def list_all_records(record_list):
    for i in range(len(record_list)):
        print(f"RECORD ID: {i + 1}")  # Display the record ID of an item
        display_record(record_list[i])

# TODO: Implement a function to add a record 
# ASSIGNED TO: Rollan Dazo

# TODO: Implement a function to update a record
# ASSIGNED TO: John Albert Olazo

# TODO: Implement a function to delete a record 
# ASSIGNED TO: Jermaine Raz ehl Agulto

# TODO: Implement a function to search for a record
# ASSIGNED TO: Joshua Serohijos

# TODO: Implement the main function for the program logic
# ASSIGNED TO: All
def main():
    record_list = []

    while True:
        print(
            "\n [1] List All"
            "\n [2] Add"
            "\n [3] Update"
            "\n [4] Delete"
            "\n [5] Search"
            "\n [6] Exit"
        )
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4: 
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print("invalid choice!")

main()