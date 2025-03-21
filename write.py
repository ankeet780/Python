# Function to write updated furniture data back to the text file
def write_furniture_data(file_name, furniture_list):
    '''
  The write_furniture_data function saves updated furniture data to a specified text file.
  It takes a list of furniture details, formats each item as a string with commas separating
  the values, and writes each formatted string to the file.
    '''
    # writing the furniture list in the file
    with open(file_name, 'w') as file:
        for furniture in furniture_list:
            line = ', '.join(
                [str(furniture[0]), furniture[1], furniture[2], str(furniture[3]), '$' + str(furniture[4])])
            file.write(line + '\n')  # Write the line to the file with a newline character

