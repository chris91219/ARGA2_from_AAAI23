from task import *
import sys
import json


def solve_task_id(task_file, task_type="training", possible_abstractions=[], possible_transformations=[], solution_prefix=""):
    """
    solves a given task and saves the solution to a file
    """
    if task_type == "training":
        data_path = "dataset/training/"
    else:
        data_path = "dataset/evaluation/"
    task = Task(data_path + task_file,possible_abstractions,possible_transformations)

    abstraction, solution_apply_call, error, train_error, solving_time, nodes_explored = task.solve(
        shared_frontier=True, time_limit=1800, do_constraint_acquisition=True, save_images=True)

    solution = {"abstraction": abstraction, "apply_call": solution_apply_call, "train_error": train_error,
                "test_error": error, "time": solving_time, "nodes_explored": nodes_explored}
    if error == 0:
        with open('solutions/correct/{}/solutions_{}_{}'.format(task_type, solution_prefix, task_file), 'w') as fp:
            json.dump(solution, fp)
    else:
        with open('solutions/incorrect/{}/solutions_{}_{}'.format(task_type, solution_prefix, task_file), 'w') as fp:
            json.dump(solution, fp)
    print(solution)


if __name__ == "__main__":

    # example tasks:
    # recolor task: d2abd087.json
    # dynamic recolor task: ddf7fa4f.json
    # movement task: 3906de3d.json
    # augmentation task: d43fd935.json

    """
    task_file = str(sys.argv[1])
    task_type = str(sys.argv[2])
    solve_task_id(task_file, task_type)
    """
    # Subset
    possible_abstractions=["ccgbr"]
    possible_transformations = {        
        "ccgbr": ["update_color"],
    }

    # Re-order
    possible_abstractions=["ccgbr", "na", "nbccg", "ccgbr2", "ccg", "mcccg", "lrg", "nbvcg"]
    possible_transformations = {        
        "nbccg": ["update_color", "move_node", "extend_node", "move_node_max", "fill_rectangle", "hollow_rectangle",
                  "add_border", "insert", "mirror", "flip", "rotate_node", "remove_node"],
        "nbvcg": ["update_color", "move_node", "extend_node", "move_node_max", "remove_node"],
        "nbhcg": ["update_color", "move_node", "extend_node", "move_node_max", "remove_node"],
        "ccgbr": ["update_color", "remove_node"],
        "ccgbr2": ["update_color", "remove_node"],
        "ccg": ["update_color", "remove_node"],
        "mcccg": ["move_node", "move_node_max", "rotate_node", "fill_rectangle", "add_border", "insert", "mirror",
                  "flip", "remove_node"],
        "na": ["flip", "rotate_node"],
        "lrg": ["update_color", "move_node", "extend_node", "move_node_max"] 
    }

    #solve_task_id("00d62c1b.json", "training", possible_abstractions, possible_transformations,solution_prefix="reorder")

    solve_task_id("00d62c1b.json", "training",solution_prefix="full_list_with_acl")

