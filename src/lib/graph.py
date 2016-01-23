class Graph(object):
    """
        A Graph object is an object which represents a simple graph.
        The Graph object contains a list of Node objects, and a list of Relation objects.
    """
    def __init__(self, id, nodes, relations):
        super(Graph, self).__init__()
        self.id = id
        self.nodes = nodes
        self.relations = relations

    def add_relation(self, relation):
        """
            Method to add a Relation object in the Graph object.
        """
        if not relation in self.relations:
            self.relations.append(relation)

    def remove_relation(self, relation):
        """
            Method to remove a Relation object.
            If this object is not contained in the relations list, the method display a simple message error.
        """
        try:
            self.relations.remove(relation)
        except:
            print("ERROR: The relation {0} does not exists for the graph {1}".format(relation.id, self.id))

    def get_relations(self):
        """
            Method to get relations from the graph.
            This method returns an empty list if it does not contains any Relation object.
        """
        return [relation.id for relation in self.relations]

    def print_nodes(self):
        """
            Method to print nodes contains in the Graph object.
        """
        print("* Nodes:")
        for n in self.nodes:
            print("\t {0}".format(n.id))

    def print_relations(self):
        """
            Method to print edges contains in the Graph object.
        """
        print("* Relations:")
        for r in self.relations:
            print("\tRelation \"{0}\"".format(r.id))
            print("\t", end="")
            print("#"*len("Relation \"{0}\"".format(r.id)))
            r.print_nodes()
            r.print_edges()
            print("")

    def print_all(self):
        """
            Method to print nodes and edges.
        """
        print("Graph \"{0}\"".format(self.id))
        self.print_nodes()
        self.print_relations()
