class Node(object):
    """
        A Node object is labeled by an id, and some attributes.
        These attributes are represented with a dictionary.
    """
    def __init__(self, id):
        super(Node, self).__init__()
        self.id = id
        self.attributes = {}

    def set_id(self, new_id):
        """
            Method to modify the id of the object.
        """
        self.id = new_id

    def add_attribute(self, attribute_id, value_id):
        """
            Method to add an attribute to an existing node.
            This attribute is labeled by an id, and have a single value
        """
        self.attributes[attribute_id] = value_id

    def remove_attribute(self, attribute_id):
        """
            Method to remove an existing attribute.
            If this one does not exists, a simple message error will be display.
        """
        try:
            self.attributes.remove(attribute_id)
        except Exception as e:
            print("ERROR: Canno't remove {0} from the object {1} : {2}".format(attribute_id, self.id, e))
