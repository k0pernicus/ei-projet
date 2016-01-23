class Relation(object):
    """
        A Relation object is labeled by an id, and contains a list of Nodes objects and a dictionary of edges.
        The relation can be directed or not directed -> the configuration will be interfered on the dictionary of edges.
        The default relation is not directed.
    """
    def __init__(self, id, directed = False):
        super(Relation, self).__init__()
        self.id = id
        self.nodes = []
        self.edges = {}
        self.directed = directed

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

    def remove_node(self, node):
        """
            Methode to remove a node.
        """
        try:
            self.nodes.remove(node)
            # Remove the edge with target 'node'
            self.edges.pop(node, None)
            if not self.directed:
                for source in self.edges:
                    if node in self.edges[source]:
                        self.edges[source].remove(node)
        except Exception as e:
            print("ERROR: Canno't remove node {} from the list of nodes in Relation {1} : {2}".format(node, self.id, e))

    def add_edge(self, edge):
        """
            Method to add an edge in the object.
            The source node of the edge will be the target node of a new edge, and will be added in the dictionary of edges if the relation is not directed!
            If the source node or the target node is not in the list of Nodes objects, or if the edge is already in the base of relation, a simple message error will be display.
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

    def print_nodes(self):
        """
            Method to print nodes for the current Relation object.
        """
        print("\t* Nodes: ", end="")
        for n in self.nodes:
            print("{0}, ".format(n.id), end="")
        print("")

    def print_edges(self):
        """
            Method to print edges for the current Relation object.
        """
        print("\t* Edges: ", end="")
        for source_node in self.edges:
            for target_node in self.edges[source_node]:
                print("{0}->{1} | ".format(source_node.id, target_node.id), end="")
        print("")
