
import datetime
from read import read_furniture_data
from write import write_furniture_data
from operation import manage_purchase, manage_sale, Display_furniture_list, get_valid_number

# Main collection loop of the program
def main():
    '''
   The main function acts as the core loop of the furniture management system, guiding the user through the process of viewing inventory,
   purchasing from manufacturers, selling to customers, and exiting the program.It coordinates the loading and saving of data, ensures
   valid user input, and connects the various functions of the program, making it the central hub for managing the entire process.
   '''
    file_name = 'furniture.txt' # name of the file

    while True:    
        furniture_list = read_furniture_data(file_name) # Load the current furniture data
        Display_furniture_list(furniture_list) # Display the furniture list

        print("\nChoose an option:")
        print("1. Purchase furniture from manufacturer")
        print("2. Sell furniture to customer")
        print("3. Exit")

        while True:
            try:
                choice = get_valid_number("Enter your choice (1 to 3): ")  # get user choices
                if choice < 1 or choice > 3:
                    print("Invalid choice. Please select a valid option.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        Display_furniture_list(furniture_list)

        if choice == 1:
            manage_purchase(furniture_list)  # Handle purchase
            write_furniture_data(file_name, furniture_list)  # Save the updated the data to the file
        elif choice == 2:
            manage_sale(furniture_list)  # Handle sell
            write_furniture_data(file_name, furniture_list)  # Save the updated the data to the file
        elif choice == 3:
             print("Thank you for using our services! See you next time.") # exit the program
             break
        
# Run the main function if the file is executed
main()
