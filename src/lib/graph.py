class Graph(object):
    """
        A Graph object is labeled by an id, and contains a list of Nodes objects and a dictionary of edges.
        The graph can be directed or not directed -> the configuration will be interfered on the dictionary of edges.
        The default graph is not directed.
    """
    def __init__(self, arg, directed = False):
        super(Graph, self).__init__()
        self.arg = arg
        self.nodes = []
        self.edges = {}
        self.directed = False

    def set_id(self, new_id):
        """
            Method to modify the id of the object.
        """
        self.id = new_id

    def add_node(self, node):
        """
            Method to add a Node object in the list of nodes.
            If the node is already in the list, a simple message error will be display.
        """
        if not node in self.nodes:
            self.nodes.append(node)
        else:
            print("ERROR: This node already exists!")

    def add_target(self, source, target):
        """
            Method to add a target to a source node.
        """
        if not source in self.edges:
            self.edges[source] = []
        self.edges[source].append(target)

    def add_edge(self, edge):
        """
            Method to add an edge in the object.
            The source node of the edge will be the target node of a new edge, and will be added in the dictionary of edges if the graph is not directed!
            If the source node or the target node is not in the list of Nodes objects, or if the edge is already in the base of graph, a simple message error will be display.
        """
        source_node = edge[0]
        target_node = edge[1]
        if (source_node in self.nodes) and (target_node in self.nodes):
            if not edge in self.edges:
                self.add_target(source_node, target_node)
                if not self.directed:
                    self.add_target(target_node, source_node)
            else:
                print("ERROR: This edge already exists!")
        else:
            print("ERROR: You can't create an edge with non-initialized nodes. Please to add edges with existing nodes, contained in the list of this object!")
