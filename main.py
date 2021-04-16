
class location:
    row = -1
    column = -1



def robot_location_finder(input_array, row, column):
    i = 0
    while i < row:
        j = 0
        while j < column:

            if input_array[i][j].find("r") != -1:
                robot_location = location()
                robot_location.row = i
                robot_location.column = j
                return robot_location

            j += 1

        i += 1








def ids_algorithm(input_array, row, column):
    print(str(robot_location_finder(input_array, row, column).row) + "  " + str(robot_location_finder(input_array, row, column).column))


















# Main part of the project starts here
input_file_name = input("Enter the name of the input file: ")
try:
    input_file = open("Inputs/" + input_file_name, "rt")
    row = ""
    while True:
        char = input_file.read(1)
        if char == '\t':
            break
        row += char

    row = int(row)

    column = ""
    while True:
        char = input_file.read(1)
        if char == '\n':
            break
        column += char

    column = int(column)


    input_array = []
    temp_row = []
    new_line = False
    end_of_file = False
    while True:

        cell = ""
        while True:
            char = input_file.read(1)
            if not char:
                end_of_file = True
                break

            if char == '\t':
                break

            if char == '\n':
                new_line = True
                break
            cell += char
        temp_row.append(cell)
        if new_line:
            input_array.append(temp_row)
            temp_row = []
            new_line = False
        if end_of_file:
            input_array.append(temp_row)
            break





    copy_input_array = input_array
    ids_algorithm(copy_input_array, row, column)










    input_file.close()
except (FileExistsError, FileNotFoundError) as e:
    print("This file does not exist in the Inputs folder")






































































