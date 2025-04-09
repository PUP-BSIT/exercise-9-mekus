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

    for index in range(len(record_list)):
         print(f"RECORD INDEX: {index}")  # Display the record index of an item
         display_record(record_list[index])

def input_integer_field(key):
    while True:
        try:
            # Prompt user to input an integer field
            user_input = int(input(f"Enter {key}: ").strip())
            return user_input
        except ValueError:
            print(f"Invalid input. Please enter a valid number for {key}.")
            continue

# Function to input fields for a new record
def input_fields(record):
    # Prompt user to input Agent name
    record["agent"] = input("Enter Agent: ").strip().capitalize()
    
    VALID_MATCH_RESULT = ("won", "lost")  # Define valid match results
    while True:
        # Prompt user to input match result
        user_input = input("Enter Match Result (Won/Lost): ").strip().lower()
        
        # Check if the input is valid
        if user_input in VALID_MATCH_RESULT:
            record["match_result"] = user_input.capitalize()
            break
        
        print("Invalid input. Please enter 'Won' or 'Lost'.")
    
    INTEGER_FIELDS = ("kills", "deaths", "assists")  # Define integer fields
    for key in INTEGER_FIELDS:
        # Call the function to get integer input
        record[key] = input_integer_field(key)  
            
# Function to add a new record to the list
def add_record(record_list):
    print("\n--- Add a New Record ---")  # Display section title
    
    # Create an empty dictionary for the new record
    record = {}  

    # Use the input fields function to get validated user input
    input_fields(record)  

    record_list.append(record)  # Add the validated record to the list
    print("Record added successfully!")  # Confirmation message
    
# Function to retrieve a record by index
def get_record_by_index(record_list, action):
    print(f"\n--- {action} a Record by index ---")  #Display section title
    
    # Prompt user to input record index
    while True:
        record_index = input(f"Enter record index to {action.lower()}: ")
        if record_index.isdigit():
            record_index = int(record_index)
            break
        
        print("Invalid input. Please enter a valid record index.")
    
    # Checks if the index is out of range
    if record_index < 0 or record_index >= len(record_list):
        print("Record index not found")
        
        # Return None and record index if not found
        return None, record_index
    
    # Return the selected record (dictionary) and record index (int)
    return record_list[record_index], record_index
    
# Function to update an existing record
def update_record(record_list):
    # Check if the record_list is empty
    if len(record_list) == 0:
        print("\nNo records found. Add a record first")
        return
     
    # Assigning the selected record to a variable
    selected_record, _ = get_record_by_index(record_list, "Update")
    
    # Exit the function if selected_record is empty
    if not selected_record:
        return
    
    # Loops through each fields and prompt user input
    input_fields(selected_record)
        
    print("Record updated successfully")  # Confirmation message

# Function to delete a record by index
def delete_record(record_list):
    # Retrieve the record and index from the user input
    selected_record, record_index = get_record_by_index(record_list, "Delete")
    
    # Exit the function if the record index is not found
    if not selected_record:
        return
    
    VALID_CONFIRM = ("yes", "no")  # Define valid confirmation responses
    while True:
        # Confirm deletion
        confirm = input(
            f"Do you want to delete record index {record_index}? (yes/no): "
        ).lower()
        
        # Check if the input is valid
        if confirm in VALID_CONFIRM:
            break
        
        print("Invalid input. Please enter 'yes' or 'no'.")
    
    # Checks if the user confirmed deletion
    if confirm != "yes":
        print ("Deletion canceled.")
        return 
    
    del record_list[record_index]  # delete it from the list
    print ("Record deleted successfully!")

# Function to search a record
def search_record(record_list):
    # Retrieve the record and index from the user input
    selected_record, record_index = get_record_by_index(record_list, "Search")
    
    # Exit the function if the record index is not found
    if not selected_record:
        return

    # Display the record details
    print(f"\nRECORD INDEX: {record_index}")
    display_record(selected_record)

# Main function to run the program
def main():
    record_list = []  # Initialize an empty list to store records

    # Infinite loop to keep the program running until the user chooses to exit
    while True:
        print(
            "\n [1] List All"
            "\n [2] Add"
            "\n [3] Update"
            "\n [4] Delete"
            "\n [5] Search"
            "\n [6] Exit"
        )
        
        # Prompt user to select an option
        try:
            # Try converting the user's input to an integer for menu selection
            choice = int(input("Enter your choice: "))
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input. Please enter a number.")
            continue

        # Check the user's choice and call the corresponding function
        match choice:
            case 1:
                # Call list_all_records()
                list_all_records(record_list) 
            case 2:
                # Call add_record()
                add_record(record_list)
            case 3:
                # Call update_record()
                update_record(record_list)
            case 4: 
                # Call delete_record()
                delete_record(record_list)
            case 5:
                # Call search_record()
                search_record(record_list)
            case 6:
                break
            case _:
                print("invalid choice!")

# Execute the main function
main()