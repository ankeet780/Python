# Function to read furniture data from the text file
# This function loads the inventory data into a list for easy access
def read_furniture_data(file_name):
    '''
   The function read_furniture_data is used to read and process furniture data from a text file.
   It opens the specified file, reads each line, splits the line into individual furniture details,
   and converts the quantity and price into integer and float types, respectively.
   '''
    furniture_list = [] # creating empty list
    try:
        with open(file_name, 'r') as file:
            for line in file:
                details = line.strip().split(', ')
                details[3] = int(details[3])  # Convert Quantity into integer
                details[4] = float(details[4].strip('$'))  # Convert Price into float
                furniture_list.append(details) # add each piece of furniture to the list
    except FileNotFoundError: # check if file not found
        print("File not found. Please ensure 'furniture.txt' exists.")
    return furniture_list # return furniture list
