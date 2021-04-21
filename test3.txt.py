top_current_node.children = butter_children_finder(input_array, top_current_node, row, column)

            bottom_current_node.children = butter_children_finder(input_array, bottom_current_node, row, column)

            [is_connected_result, top_connected_node, bottom_connected_node] = is_connected(top_current_node.children,
                                                                                            bottom_current_node.children)
            if is_connected_result:
                goal_found = True
                break


            else:
                [top_current_node, top_index] = first_children_finder(top_current_node.children)

                [bottom_current_node, bottom_index] = first_children_finder(bottom_current_node.children)