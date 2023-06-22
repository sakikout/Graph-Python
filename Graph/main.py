from graph import Graph
from weightedgraph import WeightedGraph

gp = Graph()
wg = WeightedGraph()

def set_graph_UI(graph : Graph):
    print("Enter the nodes of the Graph\nType -99999 to stop: ")

    node = 1
    node2 = 1
    i = 0

    while (int(node) != -99999):
        node = input(f"Node {i}: ")
        graph.add_node(node)
        i += 1

    print("Enter the edges in the graph\nType -99999 to stop: ")
    while(int(node) != -99999 or int(node2) != -99999):
        node = input(f"\nNode 1: ")
        if int(node) == -99999:
            break
        node2 = input(f"Node 2: ")
        graph.add_edge(node, node2)


def set_weighted_graph_UI( graph : WeightedGraph):
    print("Enter the nodes of the Graph\nType -99999 to stop: ")

    node = 1
    node2 = 1
    i = 0

    while (int(node) != -99999):
        node = input(f"Node {i}: ")
        graph.add_node(node)
        i += 1

    print("Enter the edges in the graph\nType -99999 to stop: ")
    while(int(node) != -99999 or int(node2) != -99999):
        node = input(f"\nNode 1: ")
        if int(node) == -99999:
            break
        node2 = input(f"Node 2: ")
        weight = input(f"Weight: ")
        weight = int(weight)
        graph.add_edge(node, node2, weight)

def UI(gp : Graph, wg : WeightedGraph):
    print("--------------- GRAPH PROGRAM ------------------")
    print("Wellcome! In this program, we will provide some basic operations with graph for you.\nFirst, we must create a graph. You can choose between:\n1 - Graph\n2 - Weighted Graph\n0 - Leave\nAnswer: ")
    resp = input("")
    resp = int(resp)

    while(resp != 1 or resp != 2):
        if resp == 1:
            set_graph_UI(gp)
            print("Here is your graph: ")
            print(gp.__str__())
            break
          
    
        elif resp == 2:
            set_weighted_graph_UI(wg)
            print("Here is your graph: ")
            print(wg.__str__())
            break
           
        elif resp == 0:
            print("Finalizing. Leaving the UI...")
            return

        else:
            print("Invalid answer. Try Again.")
            

    print("Now that you have a beautiful graph, let's try some operations!")
    answer = -1

    if (resp == 1):
        while(answer != 0):
            print("--------------- DISPONIBLE OPERATIONS --------------")
            print("1 - Remove node\n2 - Remove edge\n3 - Add node\n4 - Add edge\n5 - Degree in\n6 - Degree out\n7 - Density\n8 - Width Search\n9 - Depth Search\n0 - Leave\n")
            answer = input("Answer: ")
            answer = int(answer)

            if answer == 1:
                node = input("Node to delete: ")
                gp.remove_node(node)
                break
            
            elif answer == 2:
                node = input("Node 1: ")
                node2 = input("Node 2: ")
                gp.remove_edge(node, node2)
                break
            
            elif answer == 3:
                node = input("Node to add: ")
                gp.add_node(node)
                break

            elif answer == 4:
                node = input("Node 1: ")
                node2 = input("Node 2: ")
                gp.add_edge(node, node2)
                break

            elif answer == 5:
                node = input("Node: ")
                print(f"Degree in from node {node}: {str(gp.degree_in(node))}")
                break

            elif answer == 6:
                node = input("Node: ")
                print(f"Degree out from node {node}: {str(gp.degree_out(node))}")
                break

            elif answer == 7:
                print(f"Density of the graph: {str(gp.density())}")
                break

            elif answer == 8:
                o = input("Node to start search: ")
                print(f"Width search from {o}:\n{gp.width_search(o)}")
                break

            elif answer == 9:
                o = input("Node to start search: ")
                print(f"Depth search from {o}:\n{gp.depth_search(o)}")
                break

            elif answer == 0:
                print("Finalizing the UI...")
                return

            else:
                print("Invalid answer. Try again.")
                break

        print(gp.__str__())

    elif (resp == 2):
        while(answer != 0):
            print("--------------- DISPONIBLE OPERATIONS --------------")
            print("1 - Remove node\n2 - Remove edge\n3 - Add node\n4 - Add edge\n0 - Leave\n")
            answer = input("Answer: ")
            answer = int(answer)

            if answer == 1:
                node = input("Node to delete: ")
                wg.remove_node(node)
                break
            
            elif answer == 2:
                node = input("Node 1: ")
                node2 = input("Node 2: ")
                wg.remove_edge(node, node2)
                break
            
            elif answer == 3:
                node = input("Node to add: ")
                wg.add_node(node)
                break

            elif answer == 4:
                node = input("Node 1: ")
                node2 = input("Node 2: ")
                weight = input("Weight: ")
                weight = int(weight)
                wg.add_edge(node, node2, weight)
                break

            elif answer == 0:
                print("Finalizing the UI...")
                return

            else:
                print("Invalid answer. Try again.")
                break

        print(wg.__str__())
        

# ----------------------------------- MAIN --------------------------------------- #

## UI(gp, wg)

graph = WeightedGraph()
nodes = [0, 1, 2, 3, 4, 5]
graph.add_nodes(nodes)

graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 3)
graph.add_two_way_edge(1, 2, 6)
graph.add_edge(2, 3, 5)
graph.add_edge(2, 4, 2)
graph.add_edge(3, 4, 7)
graph.add_edge(3, 0, 1)
graph.add_edge(5, 0, 5)
graph.add_edge(5, 3, 3)

print(graph.__str__())

print(graph.depth_search(2))
print(graph.best_way(5, 4))