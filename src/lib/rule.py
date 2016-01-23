class Rule(object):
    """
        A Rule object is an object which contains some variables (max. 2), and 2 entries.
        These entries (in_v, out_v) are linked by a relation.
    """
    def __init__(self, relation_rule, in_v, out_v):
        super(Rule, self).__init__()
        self.relation_rule = relation_rule
        self.in_v = in_v
        self.out_v = out_v
