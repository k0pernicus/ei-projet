class Rule(object):
    """
        A Rule object is an object which contains some variables (max. 2), and 2 entries.
        These entries (in_v, out_v) are linked by a relation.
    """
    def __init__(self, relation_rule, parameters, relations, goal = False):
        super(Rule, self).__init__()
        self.relation_rule = relation_rule
        self.parameters = parameters
        # Relations : [(ma_relation, (x,y)), ...]
        self.relations = relations
        self.goal = goal

    def is_goal(self):
        return self.goal

    def __str__(self):
        parameters = ""
        for i, p in enumerate(self.parameters):
            if not i == len(self.parameters) - 1:
                parameters += "{0}, ".format(p)
            else:
                parameters += "{0}".format(p)
        relations = ""
        for r in self.relations:
            relations += "{0}({1},{2}) ".format(r[0].id, r[1][0], r[1][1])
        return "{0}({1}) :- {2}".format(self.relation_rule, parameters, relations)
