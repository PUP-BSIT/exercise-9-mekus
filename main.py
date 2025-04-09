# Function to display a record
def display_record(record):
    for key, value in record.items():
        print(f"----{key}: {value}")

# Function to iterate and display record_list
def list_all_records(record_list):
    print("\n --- Display Records ---") # Display section title

    # Checks if the record_list is empty
    if len(record_list) == 0:
        print("No records found. Add a record first")
        return

    for i in range(len(record_list)):
         print(f"RECORD ID: {i + 1}")  # Display the record ID of an item
         display_record(record_list[i])

# Function to add a new record to the list
def add_record(record_list):
    print("\n--- Add a New Record ---")  # Display section title

    # Define the fields for the record
    record_keys = ["agent", "match_result", "kills", "deaths", "assists"]
    record = {}

    # Loop through each field and prompt user input
    for item in record_keys:
        user_input = input(f"Enter {item.replace('_', ' ').title()}: ")
        record[item] = user_input

    # Append the new record to the main record list
    record_list.append(record)
    print("Record added successfully!")  # Confirmation message
    
# Function to retrieve a record by ID
def get_record_by_id(record_list, action):
    print(f"\n--- {action} a Record by ID ---")  #Display section title
    
    # Prompt user to input record ID
    record_id = int(input(f"Enter record ID to {action.lower()}: "))
    index = record_id - 1  # Convert record ID to index
    
    # Checks if the index is out of range
    if index < 0 or index >= len(record_list):
        print("Record ID not found")
        return None, record_id
    
    # Return the selected record (dictionary) and record ID (int)
    return record_list[index], record_id
    
# Function to update an existing record
def update_record(record_list):
    # Assigning the selected record to a variable
    selected_record, _ = get_record_by_id(record_list, "Update")
    
    # Exit the function if selected_record is empty
    if not selected_record:
        return
    
    # Loops through each fields and prompt user input
    for key in selected_record:
        user_input = input(f"Enter {key.replace('_', ' ').title()}: ")
        selected_record[key] = user_input
        
    print("Record updated successfully")  # Confirmation message

# Function to delete a record by ID
def delete_record(record_list):
    print("\n--- Delete a Record by ID ---")  # Display section title

    # Prompt user to input record ID
    record_id = int(input("Enter record ID to delete: "))

    # Convert record ID to index
    index = record_id - 1

    # Check if the index is out of range
    if index < 0 or index >= len(record_list):
        print("Record ID not found.")
        return

    # Confirm deletion
    confirm = input (
        f"Do you want to delete record ID {record_id}? (yes/no): "
        )
    if confirm.lower() != "yes":
        print ("Deletion canceled.")
        return 
    del record_list[index]  # delete it from the list
    print ("Record deleted successfully!")
   
def search_record(record_list):
    # Retrieve the record and ID from the user input
    selected_record, record_id = get_record_by_id(record_list, "Search")
    
    # Exit the function if the record ID is not found
    if not selected_record:
        return

    # Display the record details
    print(f"\nRECORD ID: {record_id}")
    display_record(selected_record)

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
                update_record(record_list)
            case 4: 
                delete_record(record_list)
            case 5:
                # Call search_record()
                search_record(record_list)
            case 6:
                break
            case _:
                print("invalid choice!")

main()