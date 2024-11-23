def find_path(start, end, graph):

    """

    Finds the path from the start to the end node in the graph.



    Args:

        start: The starting node.

        end: The end node.

        graph: The graph represented as a dictionary.



    Returns:

        A list of nodes representing the path, or None if no path is found.

    """



    

    



def main():

    

    graph = {

        1: [(2, 1)],

        2: [(1, 0), (3, 1)],

        
    }



    start = 1 

    end = 14  



    path = find_path(start, end, graph)

    if path:

        print("Path:", path)

    else:

        print("No path found.")




if name == "main":

    main()