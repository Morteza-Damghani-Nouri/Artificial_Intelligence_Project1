# A* algorithm is implemented here
def a_star_algorithm(input_array, row, column, input_file_name):
    start_time = time.perf_counter()
    generated_nodes = 0
    opened_nodes = 0
    cost = 0
    butter_finding_part_depth = 0
    goal_finding_part_depth = 0
    butter_count = butter_counter(input_array)
    main_counter = 1
    while main_counter <= butter_count:
        path = []
        i = 0
        j = 0
        while i < row:
            while j < column:
                if input_array[i][j].find("b") != -1:
                    butter_location = Location(i, j)
                    break
            i += 1

        [butter_finding_result, robot_to_butter_path, opened_nodes, generated_nodes, butter_finding_part_depth,
         cost] = a_star_path_finder(input_array, row, column,
                                               robot_location_finder(input_array, row, column),
                                               butter_location_finder(input_array, row, column), opened_nodes,
                                               generated_nodes, butter_location)
        if not butter_finding_result:
            print("The butter path is: ")
            for i in robot_to_butter_path:
                print(str(i.location.row) + ", " + str(i.location.column))

        else:
            return 0

        first_robot_location = robot_to_butter_path[0].location
        copy_input_array = array_copier(input_array, row, column)
        robot_location = robot_to_butter_path[-2].location
        goal_finished = False

        first_butter_node = robot_to_butter_path[-1]
        butter_node = robot_to_butter_path[-1]
        butter_path = [robot_to_butter_path[-1].location]
        robot_to_butter_path.pop(-1)
        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
        for i in robot_to_butter_path:
            path.append(i)

        print("The path from robot location to the butter: ")
        for i in path:
            map_array = x_locator(input_array, row, column)
            map_array[i.location.row][i.location.column] = "r"
            map_array[butter_node.location.row][butter_node.location.column] = "b"
            map_printer(map_array)

        print("BUTTER FOUND")

        print("The path from butter location to the goal: ")
        counter = 1
        while True:
            # A number is chose for infinite loop handling
            if len(butter_node.children) != 0 and counter <= 100000:
                [next_node, index] = first_child_finder(butter_node.children)
                if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column - 1:
                    if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column + 1, row,
                                  column) and copy_input_array[butter_node.location.row][
                        butter_node.location.column + 1] != "x":
                        local_goal_location = Location(butter_node.location.row, butter_node.location.column + 1)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth,
                             output_cost] = a_star_path_finder(copy_input_array, row, column, robot_location,
                                                                          local_goal_location, opened_nodes,
                                                                          generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)
                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                    copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

                    else:
                        butter_node.children.pop(index)

                if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column + 1:

                    if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column - 1, row,
                                  column) and copy_input_array[butter_node.location.row][
                        butter_node.location.column - 1] != "x":
                        local_goal_location = Location(butter_node.location.row, butter_node.location.column - 1)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth,
                             output_cost] = a_star_path_finder(copy_input_array, row, column, robot_location,
                                                                          local_goal_location, opened_nodes,
                                                                          generated_nodes)

                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)

                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                    copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                    else:
                        butter_node.children.pop(index)

                if next_node.location.row == butter_node.location.row - 1 and next_node.location.column == butter_node.location.column:
                    if does_exist(copy_input_array, butter_node.location.row + 1, butter_node.location.column, row,
                                  column) and copy_input_array[butter_node.location.row + 1][
                        butter_node.location.column] != "x":
                        local_goal_location = Location(butter_node.location.row + 1, butter_node.location.column)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth,
                             output_cost] = a_star_path_finder(copy_input_array, row, column, robot_location,
                                                                          local_goal_location, opened_nodes,
                                                                          generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)

                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                    copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                    else:
                        butter_node.children.pop(index)

                if next_node.location.row == butter_node.location.row + 1 and next_node.location.column == butter_node.location.column:
                    if does_exist(copy_input_array, butter_node.location.row - 1, butter_node.location.column, row,
                                  column) and copy_input_array[butter_node.location.row - 1][
                        butter_node.location.column] != "x":
                        local_goal_location = Location(butter_node.location.row - 1, butter_node.location.column)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth,
                             output_cost] = a_star_path_finder(copy_input_array, row, column, robot_location,
                                                                          local_goal_location, opened_nodes,
                                                                          generated_nodes)
                            goal_finding_part_depth += output_depth
                            cost += output_cost
                        else:
                            failure_result = False
                            local_path = []

                        if not failure_result:
                            for k in local_path:
                                path.append(k)
                            for m in local_path:
                                map_array = x_locator(input_array, row, column)
                                map_array[m.location.row][m.location.column] = "r"
                                map_array[butter_node.location.row][butter_node.location.column] = "b"
                                map_printer(map_array)

                        if failure_result:
                            butter_node.children.pop(index)

                        else:
                            robot_location = butter_node.location
                            path.append(Node(robot_location))
                            butter_path.append(next_node.location)
                            if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                                goal_finished = True
                                break
                            copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                input_array[butter_node.location.row][butter_node.location.column]
                            if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                                copy_input_array[butter_node.location.row][butter_node.location.column] = \
                                    copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                            # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                            butter_node = Node(Location(next_node.location.row, next_node.location.column))

                            map_array = x_locator(input_array, row, column)
                            map_array[robot_location.row][robot_location.column] = "r"
                            map_array[butter_node.location.row][butter_node.location.column] = "b"
                            map_printer(map_array)
                            butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

                    else:
                        butter_node.children.pop(index)


            else:
                if (butter_node.location.row == 0 and butter_node.location.column == 0) or (
                        butter_node.location.row == 0 and butter_node.location.column == column - 1) or (
                        butter_node.location.row == row - 1 and butter_node.location.column == 0) or (
                        butter_node.location.row == row - 1 and butter_node.location.column == column - 1):
                    robot_location = butter_node.location
                    path.append(Node(robot_location))
                    butter_path.append(next_node.location)
                    if input_array[next_node.location.row][next_node.location.column].find('p') != -1:
                        goal_finished = True
                        break
                    copy_input_array[butter_node.location.row][butter_node.location.column] = \
                        input_array[butter_node.location.row][butter_node.location.column]
                    if copy_input_array[butter_node.location.row][butter_node.location.column].find('b') != -1:
                        copy_input_array[butter_node.location.row][butter_node.location.column] = \
                            copy_input_array[butter_node.location.row][butter_node.location.column].rstrip('b')
                    # copy_input_array[next_node.location.row][next_node.location.column] = "x"
                    butter_node = Node(Location(next_node.location.row, next_node.location.column))

                    map_array = x_locator(input_array, row, column)
                    map_array[robot_location.row][robot_location.column] = "r"
                    map_array[butter_node.location.row][butter_node.location.column] = "b"
                    map_printer(map_array)
                    butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)
                else:
                    map_array = x_locator(input_array, row, column)
                    map_array[robot_location.row][robot_location.column] = "r"
                    map_array[butter_node.location.row][butter_node.location.column] = "b"
                    map_printer(map_array)
                    print("FAILURE")
                    break
            counter += 1
        if goal_finished:
            map_array = x_locator(input_array, row, column)
            map_array[robot_location.row][robot_location.column] = "r"
            map_array[butter_path[-1].row][butter_path[-1].column] = "b"
            map_printer(map_array)
            print("GOAL FOUND")
            print("=================")
            print("The robot path: ")
            for i in path:
                print(str(i.location.row) + ", " + str(i.location.column))

            print("=================")
            print("The butter path: ")
            for i in butter_path:
                print(str(i.row) + ", " + str(i.column))
            print("=================")
            input_array[first_butter_node.location.row][first_butter_node.location.column] = str(first_butter_node.cost)
            input_array[first_robot_location.row][first_robot_location.column] = input_array[first_robot_location.row][first_robot_location.column].rstrip("r")
            input_array[butter_path[-1].row][butter_path[-1].column] = "x"
            input_array[robot_location.row][robot_location.column] += "r"

        main_counter += 1

    finish_time = time.perf_counter()
    output_file_generator(opened_nodes, generated_nodes, butter_finding_part_depth, goal_finding_part_depth, cost, finish_time - start_time, input_file_name, "Bidirectional_BFS")

