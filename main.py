# This class determines the location of nodes
class Location:
    def __init__(self, input_row, input_column):
        self.row = input_row
        self.column = input_column


    row = -1
    column = -1


# This class simulates the nodes in the search graph
class Node:
    def __init__(self, input_location):
        self.location = input_location




    location = ""
    parent = ""
    children = []
    content = ""
    cost = ""









# This function checks if the input location is available in input array or not
def does_exist(input_array, input_row, input_column, row, column):
    if 0 <= input_row < row and 0 <= input_column < column:
        return True
    return False


# This function finds the robot location
def robot_location_finder(input_array, row, column):
    i = 0
    while i < row:
        j = 0
        while j < column:

            if input_array[i][j].find("r") != -1:
                robot_location = Location(i, j)
                return robot_location

            j += 1

        i += 1


# This function checks if the butter is available among the input children or not
def is_butter_available(children):
    for i in children:
        if i.content.find('b') != -1:
            return i
    return False


# This function finds the cost of the input node
def cost_finder(node):
    content = node.content
    if content.find('p') == -1 and content.find('b') == -1 and content.find('r') == -1:
        return int(content)

    content = content.rstrip(content[-1])
    return int(content)


# This function prints the map of the search
def map_printer(input_array):
    for i in input_array:
        row = ""
        for j in i:
            row += j + " " * (8 - len(j))
        print(row)





# This function finds the node with the minimum cost
def minimum_cost_finder(input_list):
    minimum_cost_node = input_list[0]
    index = 0
    i = 1
    while i < len(input_list):
        if input_list[i].cost < minimum_cost_node.cost:
            minimum_cost_node = input_list[i]
            index = i
        i += 1

    return [minimum_cost_node, index]









# This function finds the children of the input node while searching for the first butter
def butter_children_finder(input_array, node, row, column):
    node_row = node.location.row
    node_column = node.location.column
    children = []
    if does_exist(input_array, node_row, node_column + 1, row, column):
        if input_array[node_row][node_column + 1] != "x":
            child = Node(Location(node_row, node_column + 1))
            child.parent = node
            child.content = input_array[node_row][node_column + 1]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row, node_column - 1, row, column):
        if input_array[node_row][node_column - 1] != "x":
            child = Node(Location(node_row, node_column - 1))
            child.parent = node
            child.content = input_array[node_row][node_column - 1]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row + 1, node_column, row, column):
        if input_array[node_row + 1][node_column] != "x":
            child = Node(Location(node_row + 1, node_column))
            child.parent = node
            child.content = input_array[node_row + 1][node_column]
            child.cost = cost_finder(child)
            children.append(child)

    if does_exist(input_array, node_row - 1, node_column, row, column):
        if input_array[node_row - 1][node_column] != "x":
            child = Node(Location(node_row - 1, node_column))
            child.parent = node
            child.content = input_array[node_row - 1][node_column]
            child.cost = cost_finder(child)
            children.append(child)



    if node.parent != "":
        parent_node = node.parent
        for i in children:
            if i.location.row == parent_node.location.row and i.location.column == parent_node.location.column:
                children.remove(i)
                break

    return children


# This function moves the robot to the cell which is behind the butter
def behind_butter_finder(input_array, row, column, robot_location):
    finished = False
    allowed_depth = 1
    current_depth = 0
    current_node = Node(robot_location)
    current_node.children = butter_children_finder(input_array, current_node, row, column)
    current_node.content = input_array[robot_location.row][robot_location.column]
    path = [current_node]
    butter_node = ""

    while True:
        while current_depth < allowed_depth:
            if len(current_node.children) != 0:
                is_butter_available_result = is_butter_available(current_node.children)
                if is_butter_available_result == False:
                    [next_node, index] = minimum_cost_finder(current_node.children)
                    current_node.children.pop(index)
                    current_node = next_node
                    path.append(current_node)
                    current_depth += 1
                    current_node.children = butter_children_finder(input_array, current_node, row, column)







                else:
                    butter_node = is_butter_available_result
                    finished = True
                    break

            else:
                if current_node.parent != "":
                    current_node = current_node.parent
                    path.append(current_node)
                    current_depth = current_depth - 1

                else:
                    current_depth = 0
                    allowed_depth = allowed_depth + 1
                    current_node = Node(robot_location)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    current_node.content = input_array[robot_location.row][robot_location.column]

        if finished:
            break
        else:
            current_depth = current_depth - 1
            current_node = current_node.parent
            path.append(current_node)



    path += butter_node
    return path




# This function implements the IDS algorithm
def ids_algorithm(input_array, row, column):
    robot_location = robot_location_finder(input_array, row, column)
    finished = False
    allowed_depth = 1
    current_depth = 0
    current_node = Node(robot_location)
    current_node.children = butter_children_finder(input_array, current_node, row, column)
    current_node.content = input_array[robot_location.row][robot_location.column]
    path = [current_node]
    butter_node = ""


    while True:
        while current_depth < allowed_depth:
            if len(current_node.children) != 0:
                is_butter_available_result = is_butter_available(current_node.children)
                if is_butter_available_result == False:
                    [next_node, index] = minimum_cost_finder(current_node.children)
                    current_node.children.pop(index)
                    current_node = next_node
                    path.append(current_node)
                    current_depth += 1
                    current_node.children = butter_children_finder(input_array, current_node, row, column)







                else:
                    butter_node = is_butter_available_result
                    finished = True
                    break

            else:
                if current_node.parent != "":
                    current_node = current_node.parent
                    path.append(current_node)
                    current_depth = current_depth - 1

                else:
                    current_depth = 0
                    allowed_depth = allowed_depth + 1
                    current_node = Node(robot_location)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    current_node.content = input_array[robot_location.row][robot_location.column]





        if finished:
            break
        else:
            current_depth = current_depth - 1
            current_node = current_node.parent
            path.append(current_node)





    # print("path: ")
    # for i in path:
    #     print(str(i.location.row) + ", " + str(i.location.column))
    # print("===============")
    # print("Butter location: ")
    # print(str(butter_node.location.row) + ", " + str(butter_node.location.column))
    # print("current location: ")
    # print(str(current_node.location.row) + ", " + str(current_node.location.column))



    copy_input_array = input_array
    i = 0
    while i < row:
        j = 0
        while j < column:
            print(copy_input_array[i][j].find("b"))
            if copy_input_array[i][j].find("b") != -1:
                copy_input_array[i][j] = "x"


            j += 1

        i += 1

    robot_location = current_node.location
    goal_finished = False
    allowed_depth = 1
    current_depth = 0


    current_node = Node(robot_location)
    current_node.children = butter_children_finder(input_array, current_node, row, column)
    current_node.content = input_array[robot_location.row][robot_location.column]
    new_path = []

    butter_node.children = butter_children_finder(copy_input_array, butter_node, row, column)

    while True:

        if len(butter_node.children) != 0:
            [next_node, index] = minimum_cost_finder(butter_node.children)
            if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column - 1:
                if copy_input_array[butter_node.location.row][butter_node.location.column + 1] != "x":
















                else:
                    butter_node.children.pop(index)

            if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column + 1:
                pass

            if next_node.location.row == butter_node.location.row - 1 and next_node.location.column == butter_node.location.column:
                pass

            if next_node.location.row == butter_node.location.row + 1 and next_node.location.column == butter_node.location.column:
                pass


        else:
            print("FAILURE")
            break

















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






































































