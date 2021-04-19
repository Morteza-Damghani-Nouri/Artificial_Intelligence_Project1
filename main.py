import random
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


# This function finds the first children node of the input array
def first_children_finder(input_list):
    random_number = random.randint(0, (len(input_list) - 1))
    return [input_list[random_number], random_number]


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


# This function finds the children of the input node while searching for the first butter
def goal_children_finder(input_array, node, row, column):
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
                    [next_node, index] = first_children_finder(current_node.children)
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


# This function copies the input array
def array_copier(input_array):
    copied_array = []
    for i in input_array:
        copied_array.append(i)
    return copied_array


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
                    [next_node, index] = first_children_finder(current_node.children)
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
                    [next_node, index] = first_children_finder(current_node.children)
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
    # for i in path:
    #    print(str(i.location.row) + ", " + str(i.location.column))
    # print("===============")
    # print("Butter location: ")
    # print(str(butter_node.location.row) + ", " + str(butter_node.location.column))
    # print("current location: ")
    # print(str(current_node.location.row) + ", " + str(current_node.location.column))


    # HEEEEEEEERE is the proper place to put that algorithm in my_algorithm2

    copy_input_array = array_copier(input_array)



    map_printer(copy_input_array)

    print("The butter node location is: " + str(butter_node.location.row) + ", " + str(butter_node.location.column))
    robot_location = current_node.location
    goal_finished = False

    # ****** Butter_node location stored here
    first_butter_node = butter_node

    butter_path = [butter_node.location]
    butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

    while True:
        if len(butter_node.children) != 0:
            [next_node, index] = first_children_finder(butter_node.children)
            print("The next node is: " + str(next_node.location.row) + ", " + str(next_node.location.column))
            print("The butter node is: " + str(butter_node.location.row) + ", " + str(butter_node.location.column))
            print("The robot node is: " + str(robot_location.row) + ", " + str(robot_location.column))
            print("The children locations are: ")
            for m in butter_node.children:
                print(str(m.location.row) + ", " + str(m.location.column))

            if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column - 1:
                # print("here1")
                if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column + 1, row, column) and copy_input_array[butter_node.location.row][butter_node.location.column + 1] != "x":
                    local_goal_location = Location(butter_node.location.row, butter_node.location.column + 1)
                    if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                        [failure_result, local_path] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location)
                    else:
                        failure_result = False
                        local_path = []

                    if not failure_result:
                        for k in local_path:
                            path.append(k)

                    if failure_result:
                        butter_node.children.pop(index)

                    else:
                        robot_location = butter_node.location
                        butter_path.append(next_node.location)
                        if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                            goal_finished = True
                            break
                        copy_input_array[butter_node.location.row][butter_node.location.column] = input_array[butter_node.location.row][butter_node.location.column]
                        if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                            copy_input_array[butter_node.location.row][butter_node.location.column] = copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                        # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                        butter_node = Node(Location(next_node.location.row, next_node.location.column))
                        print("*** The map is: ")
                        map_printer(copy_input_array)
                        print("================")
                        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

                else:
                    butter_node.children.pop(index)

            if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column + 1:

                if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column - 1, row, column) and copy_input_array[butter_node.location.row][butter_node.location.column - 1] != "x":
                    # print("here in 2")
                    local_goal_location = Location(butter_node.location.row, butter_node.location.column - 1)
                    if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                        [failure_result, local_path] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location)
                    else:
                        failure_result = False
                        local_path = []

                    if not failure_result:
                        for k in local_path:
                            path.append(k)

                    if failure_result:
                        butter_node.children.pop(index)

                    else:
                        robot_location = butter_node.location
                        butter_path.append(next_node.location)
                        if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                            goal_finished = True
                            break
                        copy_input_array[butter_node.location.row][butter_node.location.column] = input_array[butter_node.location.row][butter_node.location.column]
                        if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                            copy_input_array[butter_node.location.row][butter_node.location.column] = copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                        # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                        butter_node = Node(Location(next_node.location.row, next_node.location.column))
                        print("*** The map is: ")
                        map_printer(copy_input_array)
                        print("================")
                        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                else:
                    butter_node.children.pop(index)

            if next_node.location.row == butter_node.location.row - 1 and next_node.location.column == butter_node.location.column:
                # print("here3")
                if does_exist(copy_input_array, butter_node.location.row + 1, butter_node.location.column, row, column) and copy_input_array[butter_node.location.row + 1][butter_node.location.column] != "x":
                    local_goal_location = Location(butter_node.location.row + 1, butter_node.location.column)
                    if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                        [failure_result, local_path] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location)
                    else:
                        failure_result = False
                        local_path = []

                    if not failure_result:
                        for k in local_path:
                            path.append(k)

                    if failure_result:
                        butter_node.children.pop(index)

                    else:
                        robot_location = butter_node.location
                        butter_path.append(next_node.location)
                        if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                            goal_finished = True
                            break
                        copy_input_array[butter_node.location.row][butter_node.location.column] = input_array[butter_node.location.row][butter_node.location.column]
                        if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                            copy_input_array[butter_node.location.row][butter_node.location.column] = copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                        # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                        butter_node = Node(Location(next_node.location.row, next_node.location.column))
                        print("*** The map is: ")
                        map_printer(copy_input_array)
                        print("================")
                        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                else:
                    butter_node.children.pop(index)

            if next_node.location.row == butter_node.location.row + 1 and next_node.location.column == butter_node.location.column:
                # print("here4")
                if does_exist(copy_input_array, butter_node.location.row - 1, butter_node.location.column, row, column) and copy_input_array[butter_node.location.row - 1][butter_node.location.column] != "x":
                    local_goal_location = Location(butter_node.location.row - 1, butter_node.location.column)
                    if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                        [failure_result, local_path] = ids_location_finder(copy_input_array, row, column, robot_location, local_goal_location)
                    else:
                        failure_result = False
                        local_path = []

                    if not failure_result:
                        for k in local_path:
                            path.append(k)

                    if failure_result:
                        butter_node.children.pop(index)

                    else:
                        robot_location = butter_node.location
                        butter_path.append(next_node.location)
                        if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                            goal_finished = True
                            break
                        copy_input_array[butter_node.location.row][butter_node.location.column] = input_array[butter_node.location.row][butter_node.location.column]
                        if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                            copy_input_array[butter_node.location.row][butter_node.location.column] = copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                        # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                        butter_node = Node(Location(next_node.location.row, next_node.location.column))
                        print("*** The map is: ")
                        map_printer(copy_input_array)
                        print("================")
                        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

                else:
                    butter_node.children.pop(index)


        else:
            if (butter_node.location.row == 0 and butter_node.location.column == 0) or (butter_node.location.row == 0 and butter_node.location.column == column - 1) or (butter_node.location.row == row - 1 and butter_node.location.column == 0) or (butter_node.location.row == row - 1 and butter_node.location.column == column - 1):
                robot_location = butter_node.location
                butter_path.append(next_node.location)
                if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                    goal_finished = True
                    break
                copy_input_array[butter_node.location.row][butter_node.location.column] = input_array[butter_node.location.row][butter_node.location.column]
                if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                    copy_input_array[butter_node.location.row][butter_node.location.column] = copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                butter_node = Node(Location(next_node.location.row, next_node.location.column))
                print("*** The map is: ")
                map_printer(copy_input_array)
                print("================")
                butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
            else:
                print("FAILURE")
                break




    if goal_finished:
        print("GOAL FOUND")




    print("=================")
    print("The robot path: ")
    for i in path:
        print(str(i.location.row) + ", " + str(i.location.column))

    print("=================")











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





    copy_input_array = array_copier(input_array)
    ids_algorithm(copy_input_array, row, column)










    input_file.close()
except (FileExistsError, FileNotFoundError) as e:
    print("This file does not exist in the Inputs folder")






































































