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


# This function checks if the goal is available among the input children or not
def is_goal_available(children):
    for i in children:
        if i.content.find('p') != -1:
            return i
    return False



# This function checks if input location is available among the input children or not
def is_local_goal_available(children, location):
    for i in children:
        if i.location.row == location.row and i.location.column == location.column:
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


# This function is used to find the proper location of the robot to push the butter
def ids_location_finder(input_array, row, column, start_location, local_goal_location):
    finished = False
    allowed_depth = 1
    current_depth = 0
    current_node = Node(start_location)
    current_node.children = butter_children_finder(input_array, current_node, row, column)
    current_node.content = input_array[start_location.row][start_location.column]
    path = [current_node]
    butter_node = ""
    failure = False

    while True:
        while current_depth < allowed_depth:
            if len(current_node.children) != 0:
                is_local_goal_available_result = is_local_goal_available(current_node.children, local_goal_location)
                if is_local_goal_available_result == False:
                    [next_node, index] = minimum_cost_finder(current_node.children)
                    current_node.children.pop(index)
                    current_node = next_node
                    path.append(current_node)
                    current_depth += 1
                    current_node.children = butter_children_finder(input_array, current_node, row, column)




                else:
                    butter_node = is_local_goal_available_result
                    finished = True
                    break

            else:
                if current_node.parent != "":
                    current_node = current_node.parent
                    path.append(current_node)
                    current_depth = current_depth - 1

                else:
                    current_depth = 0
                    if allowed_depth >= 100000:
                        failure = True
                        break
                    allowed_depth = allowed_depth + 1
                    current_node = Node(start_location)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    current_node.content = input_array[start_location.row][start_location.column]
                    path = [current_node]



        if failure:
            return [failure, path]
        if finished:
            break
        else:
            current_depth = current_depth - 1
            current_node = current_node.parent
            path.append(current_node)



    path.append(butter_node)
    return [failure, path]


# This function is used to find the goal of the input file by IDS algorithm
def ids_goal_finder(input_array, row, column, start_location):
    finished = False
    allowed_depth = 1
    current_depth = 0
    current_node = Node(start_location)
    current_node.children = butter_children_finder(input_array, current_node, row, column)
    current_node.content = input_array[start_location.row][start_location.column]
    path = [current_node]
    butter_node = ""
    failure = False

    while True:
        while current_depth < allowed_depth:
            if len(current_node.children) != 0:
                is_goal_available_result = is_goal_available(current_node.children)
                if is_goal_available_result == False:
                    [next_node, index] = minimum_cost_finder(current_node.children)
                    current_node.children.pop(index)
                    current_node = next_node
                    path.append(current_node)
                    current_depth += 1
                    current_node.children = butter_children_finder(input_array, current_node, row, column)




                else:
                    butter_node = is_goal_available_result
                    finished = True
                    break

            else:
                if current_node.parent != "":
                    current_node = current_node.parent
                    path.append(current_node)
                    current_depth = current_depth - 1

                else:
                    current_depth = 0
                    if allowed_depth >= 100000:
                        failure = True
                        break
                    allowed_depth = allowed_depth + 1
                    current_node = Node(start_location)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    current_node.content = input_array[start_location.row][start_location.column]
                    path = [current_node]



        if failure:
            return [failure, path]
        if finished:
            break
        else:
            current_depth = current_depth - 1
            current_node = current_node.parent
            path.append(current_node)



    path.append(butter_node)
    return [failure, path]


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
    butter_finding_failure = False


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
                    if allowed_depth >= 100000:
                        butter_finding_failure = True
                        break
                    allowed_depth = allowed_depth + 1
                    current_node = Node(robot_location)
                    current_node.children = butter_children_finder(input_array, current_node, row, column)
                    current_node.content = input_array[robot_location.row][robot_location.column]
                    path = [current_node]



        if butter_finding_failure:
            print("UNABLE TO FIND A PATH TO THE BUTTER BY IDS")
            return 0
        if finished:
            break
        else:
            current_depth = current_depth - 1
            current_node = current_node.parent
            path.append(current_node)





    # print("path: ")
    for i in path:
        print(str(i.location.row) + ", " + str(i.location.column))
    # print("===============")
    # print("Butter location: ")
    # print(str(butter_node.location.row) + ", " + str(butter_node.location.column))
    # print("current location: ")
    # print(str(current_node.location.row) + ", " + str(current_node.location.column))


    robot_location = current_node.location
    [goal_finding_failure, local_path] = ids_goal_finder(input_array, row, column, butter_node.location)
    if goal_finding_failure:
        print("UNABLE TO FIND A PATH FROM BUTTER TO THE GOAL BY IDS")
    else:
        copy_input_array = input_array

        i = 1
        while i < len(local_path):
            current_butter_location = local_path[i].location
            previous_butter_location = local_path[i - 1].location
            copy_input_array[current_butter_location.row][current_butter_location.column] = "x"


            if current_butter_location.row == previous_butter_location.row and current_butter_location.column == previous_butter_location.column - 1:
                if copy_input_array[previous_butter_location.row][previous_butter_location.column + 1] != "x":
                    local_goal_location = Location(previous_butter_location.row, previous_butter_location.column + 1)
                    [behind_the_butter_finding_failure, behind_the_butter_path] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location)
                    if behind_the_butter_finding_failure:
                        print("UNABLE TO FIND A PATH A PROPER LOCATION TO MOVE THE BUTTER")
                        break

                    else:
                        for j in behind_the_butter_path:
                            path.append(j)
                        robot_location = local_goal_location

                else:
                    print("UNABLE TO FIND A PATH A PROPER LOCATION TO MOVE THE BUTTER")
                    break

                # here here here copy the above if with proper values







            i += 1


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






































































