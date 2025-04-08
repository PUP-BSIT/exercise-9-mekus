# Function to display a record
def display_record(record):
    for key, value in record.items():
        print(f"\t{key}: {value}")

# Function to iterate and display record_list
def list_all_records(record_list):
    for i in range(len(record_list)):
        print(f"RECORD ID: {i + 1}")  # Display the record ID of an item
        display_record(record_list[i])

# Function to add a new record to the list
def add_record(record_list):
    print("\n--- Add a New Record ---") # Display section title
    
    # Get user input for each field of the record
    agent = input("Enter Agent: ")
    match_result = input("Enter Match Result (Won/Lose): ")
    kills = input("Enter Kills: ")
    deaths = input("Enter Deaths: ")
    assists = input("Enter Assists: ")

    # Create a new record using the input values
    record = {
        "agent": agent,
        "match_result": match_result,
        "kills": kills,
        "deaths": deaths,
        "assists": assists
    }

    # Append the new record to the main record list
    record_list.append(record) 
    print("Record added successfully!") # Confirmation message
    
# TODO: Implement a function to update a record
# ASSIGNED TO: John Albert Olazo

# TODO: Implement a function to delete a record 
# ASSIGNED TO: Jermaine Raz ehl Agulto

def search_record(record_list):
    print("\n--- Search a Record by ID ---") # Display section title
    
    # Prompt user to enter a record ID to search
    record_id = int(input("Enter the record ID to search: "))

    # Check if the input is a number
    if not record_id:
        print("Invalid input! Please enter a valid number.")
        return

    # Convert record ID to index
    index = record_id - 1

    # Check if the index is out of range
    if index < 0 or index >= len(record_list):
        print("Record ID not found.")
        return

    # If the record exists, display the record details
    print(f"\nRECORD ID: {record_id}")
    display_record(record_list[index])
    print()

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
                # Call list_all_records()
                list_all_records(record_list) 
            case 2:
                # Call add_record()
                add_record(record_list)
            case 3:
                pass
            case 4: 
                pass
            case 5:
                # Call search_record()
                search_record(record_list)
            case 6:
                break
            case _:
                print("invalid choice!")

main()