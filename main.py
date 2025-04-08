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
        "Agent": agent,
        "Match Result": match_result,
        "Kills": kills,
        "Deaths": deaths,
        "Assists": assists
    }

    # Append the new record to the main record list
    record_list.append(record) 
    print("Record added successfully!") # Confirmation message
    
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
                # Call list_all_records()
                list_all_records(record_list) 
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