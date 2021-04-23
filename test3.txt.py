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
                                               generated_nodes)
        if not butter_finding_result:
            print("The butter path is: ")
            for i in robot_to_butter_path:
                print(str(i.location.row) + ", " + str(i.location.column))

        else:
            return 0

        input_array[butter_path[-1].row][butter_path[-1].column] = "x"
        input_array[robot_location.row][robot_location.column] += "r"
        statistic_list.append("GOAL FOUND")
        statistic_list.append(path)
        statistic_list.append(butter_finding_part_depth)
        statistic_list.append(goal_finding_part_depth)


    else:
        statistic_list.append("FAILURE")
        statistic_list.append(path)
        statistic_list.append(butter_finding_part_depth)
        statistic_list.append(goal_finding_part_depth)
