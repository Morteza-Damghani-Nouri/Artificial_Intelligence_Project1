print("BUTTER FOUND")
        goal_finding_part_depth = 0
        butter_finding_part_depth = current_depth
        first_robot_location = robot_location
        copy_input_array = array_copier(input_array, row, column)
        robot_location = current_node.location
        goal_finished = False


        first_butter_node = butter_node
        butter_path = [butter_node.location]
        butter_node.children = goal_children_finder(copy_input_array, butter_node, row, column)

        counter = 1
        while True:
            # A number is chose for infinite loop handling
            if len(butter_node.children) != 0 and counter <= 10000000:
                next_node = butter_node.children[0]

                if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column - 1:
                    if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column + 1, row,
                                  column) and copy_input_array[butter_node.location.row][butter_node.location.column + 1] != "x":
                        local_goal_location = Location(butter_node.location.row, butter_node.location.column + 1)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = bidirectional_bfs_path_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
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
                            butter_node.children.pop(0)

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
                        butter_node.children.pop(0)

                if next_node.location.row == butter_node.location.row and next_node.location.column == butter_node.location.column + 1:

                    if does_exist(copy_input_array, butter_node.location.row, butter_node.location.column - 1, row,
                                  column) and copy_input_array[butter_node.location.row][butter_node.location.column - 1] != "x":
                        local_goal_location = Location(butter_node.location.row, butter_node.location.column - 1)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = bidirectional_bfs_path_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
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
                            butter_node.children.pop(0)

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
                        butter_node.children.pop(0)

                if next_node.location.row == butter_node.location.row - 1 and next_node.location.column == butter_node.location.column:
                    if does_exist(copy_input_array, butter_node.location.row + 1, butter_node.location.column, row,
                                  column) and copy_input_array[butter_node.location.row + 1][butter_node.location.column] != "x":
                        local_goal_location = Location(butter_node.location.row + 1, butter_node.location.column)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = bidirectional_bfs_path_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
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
                            butter_node.children.pop(0)

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
                        butter_node.children.pop(0)

                if next_node.location.row == butter_node.location.row + 1 and next_node.location.column == butter_node.location.column:
                    if does_exist(copy_input_array, butter_node.location.row - 1, butter_node.location.column, row,
                                  column) and copy_input_array[butter_node.location.row - 1][butter_node.location.column] != "x":
                        local_goal_location = Location(butter_node.location.row - 1, butter_node.location.column)
                        if robot_location.row != local_goal_location.row or robot_location.column != local_goal_location.column:
                            [failure_result, local_path, opened_nodes, generated_nodes, output_depth, output_cost] = bidirectional_bfs_path_finder(copy_input_array, row, column, robot_location, local_goal_location, opened_nodes, generated_nodes)
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
                            butter_node.children.pop(0)

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
                        butter_node.children.pop(0)


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
            print("The input array is: ")
            input_array[first_butter_node.location.row][first_butter_node.location.column] = str(first_butter_node.cost)
            input_array[first_robot_location.row][first_robot_location.column] = input_array[first_robot_location.row][first_robot_location.column].rstrip("r")
            input_array[butter_path[-1].row][butter_path[-1].column] = "x"
            input_array[robot_location.row][robot_location.column] += "r"
            map_printer(input_array)


    # This part of the code stops the timer
    finish_time = time.perf_counter()
    output_file_generator(opened_nodes, generated_nodes, butter_finding_part_depth, goal_finding_part_depth, cost, finish_time - start_time, input_file_name, "IDS")
