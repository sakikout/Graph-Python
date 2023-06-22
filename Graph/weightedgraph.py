class WeightedGraph:

    def __init__(self):
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    def __str__(self):
        res = "Nodes: " + str(self.node_count) + "\nEdges: " + str(
            self.edge_count) + "\n\n" + "Graph: " + "\n"

        for key in self.adj_list:
            res += str(key) + ": " + str(self.adj_list[key]) + "\n"

        return res

    def add_node(self, node):
        if node in self.adj_list:
            print(f"WARN: Node {node} already exists.")
            return
        self.adj_list[node] = {}
        self.node_count += 1

    def add_nodes(self, nodes):
        for n in nodes:
            self.add_node(n)

    def add_edge(self, node1, node2, w):
        try:
            self.adj_list[node1][node2] = w
            self.edge_count += 1
        except KeyError as e:
            print(f"ERROR: Node {e} does not exist in the graph")

    def add_two_way_edge(self, node1, node2, w):
        self.add_edge(node1, node2, w)
        self.add_edge(node2, node1, w)

    def remove_node(self, node):
        for n in self.adj_list:
            if node in self.adj_list[n]:
                self.remove_edge(n, node)

        for nd in self.adj_list[node]:
            self.remove_edge(node, nd)

        self.adj_list.pop(node)
        self.node_count -= 1

    def remove_edge(self, node1, node2):
        try:
            self.adj_list[node1].pop(node2)
            self.edge_count -= 1

        except KeyError as e:
            print(f"WARN: Node {e} does not exist.")
        except ValueError:
            print(f"WARN: Edge {node1} -> {node2} does not exist.")

    def degree_out(self, node):
        return len(self.adj_list[node])

    def degree_in(self, node):
        count = 0
        for neighbor in self.adj_list:
            if node in self.adj_list[neighbor]:
                count += 1

        return count
    
    def get_weight_edge(self, node1, node2):
        return float(self.adj_list[node1][node2])
    
    def neighbours(self, node):
        return self.adj_list[node]
    
    def get_higher_weight_edge(self, node):
        ng = self.neighbours(node)
        higher = -9999

        for nd in ng:
            if ng[nd] > higher:
                higher = ng[nd]
                node = nd

        return node
    
    def depth_search(self, s):
        desc = []

        for node in self.adj_list:
            desc.append(0)
            
        S = [s]
        R = [s]
        desc[s] = 1

        while len(S) != 0:
            u = S[-1]
            unstack = True

            if (len(self.adj_list[u]) == 0):
                break

            for n in self.adj_list[u]:
                if desc[n] == 0:
                    unstack = False
                    S.append(n)
                    R.append(n)
                    desc[n] = 1
                   
                    break
                
            if unstack:
                S.pop()
        return R
    
    def best_way(self, s, d):
        visited = set()
        return self.depth_search_recursive(s, d, visited)

    
    def depth_search_recursive(self, node, destination, visited):
        visited.add(node)

        if node == destination:
            return [node]

        for neighbor in self.adj_list[node]:
            if neighbor not in visited:
                path = self.depth_search_recursive(neighbor, destination, visited)
                if path is not None:
                    return [node] + path

        return None
