class Graph:

  def __init__(self):
    self.adj_list = {}
    self.node_count = 0
    self.edge_count = 0

  def __str__(self):
    res = "Nodes: " + str(self.node_count) + "\Edges: " + str(
      self.edge_count) + "\n\n" + "Graph: " + "\n"

    for key in self.adj_list:
      res += str(key) + ": " + str(self.adj_list[key]) + "\n"

    return res

  def add_node(self, node):
    if node in self.adj_list:
      print(f"WARN: Node {node} already exists.")
      return
    self.adj_list[node] = []
    self.node_count += 1

  def add_edge(self, node1, node2):
    try:
      self.adj_list[node1].append(node2)
      self.edge_count += 1
    except KeyError as e:
      print(f"ERROR: Node {e} does not exist in the graph")

  def add_nodes(self, nodes):
    for item in nodes:
      self.add_node(item)

  def add_two_way_edge(self, node1, node2):
    self.add_edge(node1, node2)
    self.add_edge(node2, node1)

  def remove_node(self, node):
    for neighbor in self.adj_list:
      if node in self.adj_list[neighbor]:
        self.adj_list[neighbor].remove(node)
        self.edge_count -= 1
    self.adj_list.pop(node)
    self.node_count -= 1

  def remove_edge(self, node1, node2):
    try:
      self.adj_list[node1].remove(node2)
      self.edge_count -= 1
    except KeyError as e:
      print(f"Node {e} does not exist")
    except ValueError as e:
      print(f"WARN: Edge {node1} -> {node2} does not exist")

  def degree_out(self, node):
    return len(self.adj_list[node])

  def degree_in(self, node):
    count = 0
    for neighbor in self.adj_list:
      if node in self.adj_list[neighbor]:
        count += 1

    return count

  def highest_degree_out(self):
    highest = -1
    for node in self.adj_list:
      if self.degree_out(node) > highest:
        highest = len(self.adj_list[node])
        name = node
    return name, highest

  def highest_degree_in(self):
    highest = float("-inf")
    for node in self.adj_list:
      if self.degree_in(node) > highest:
        highest = self.degree_in(node)
    return highest

  def density(self):
    return self.edge_count / self.node_count * (self.node_count - 1)

  def is_complete(self):
    total_edges = 2**(self.node_count - 1) * self.node_count
    if self.edge_count == total_edges or self.density() == 1:
      return True
    return False

  def is_directed(self):
    for node in self.adj_list:
      for neighbor in self.adj_list[node]:
        if node in self.adj_list[neighbor]:
          flag = False
        else:
          flag = True
          return flag

    return flag

  def there_is_edge(self, node1, node2):
    if node1 in self.adj_list[node2]:
      flag = True
    else:
      flag = False

    return flag

  def neighbors(self, node):
    list = []
    for neighbor in self.adj_list[node]:
      list.append(neighbor)

    return list

  def is_regular(self):
    first_node = list(self.adj_list)[0]

    degree_first_node = self.degree_out(first_node)

    for node in self.adj_list:
      if self.degree_out(node) != degree_first_node:
        return False
    return True

  def is_subgraph_of(self, graph):
    for node in self.adj_list:
      if node not in graph.adj_list:
        return False
      for neighbor in self.adj_list[node]:
        if neighbor not in graph.adj_list[node]:
          return False
    return True

  def is_valid_walk(self, walk):  # recebe um vetor nós
    i = 0
    while (i < len(walk) - 1):
      if not self.there_is_edge(walk[i + 1], walk[i]):
        return False
      i += 1

    return True

  def is_valid_trail(self, trail):
    i = 0
    trails = []
    while (i < len(trail) - 1):
      if not self.there_is_edge(trail[i + 1], trail[i]):
        return False
      else:
        trails += (trail[i + 1], trail[i])
      i += 1

    j = 0
    c = 1
    while (j < len(trails) - 1):
      node_pair = 0
      for node in trails[j]:
        while (c < len(trails)):
          if node in trails[c]:
            node_pair += 1
          if (node_pair == 1):
            return False
          c += 1

    return True
  
  def width_search(self, s):
    desc = []

    for node in self.adj_list:
      desc.append(0)

    queue = []
    queue.append(s)
    res = []
    res.append(s)
    desc[s] = 1

    while (len(queue) != 0):
      u = queue[0]
      queue.pop(0)
      for node in self.adj_list[u]:
        if (desc[node] == 0):
          queue.append(node)
          res.append(node)
          desc[node] = 1

    return res
  
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
  
  def width_search_rec(self, o, m, nodes):
    nodes = []
    nodes[o] = m

    for node in self.adj_list[o]:
      if nodes[node] == 0:
        self.width_search_rec(node, m, nodes)
  
  def nodes_connected(self):
    for i in range(self.node_count):
      nodes = [0]

    m = 0

    for n in range(len(self.adj_list)):
      if nodes[n] == 0:
        m += 1
        self.width_search_rec(n, m, nodes)
    
    return nodes

  def degree_out_higher_three(self):
    highest = []
    for node in self.adj_list:
      count = 0
      for ng in self.adj_list[node]:
        count += 1
      if count > 3:
        highest.append(node)

    return highest
