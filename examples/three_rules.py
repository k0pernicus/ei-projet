from lib.graph import Graph
from lib.node import Node
from lib.relation import Relation
from lib.rule import Rule

def test():

    uno = Node("uno")
    dos = Node("dos")
    tres = Node("tres")
    quatro = Node("quatro")

    r = Relation("R", directed = True)
    s = Relation("S", directed = True)
    t = Relation("T", directed = True)

    r.add_node(uno)
    r.add_node(dos)
    r.add_node(quatro)
    r.add_edge((uno, dos))
    r.add_edge((quatro, dos))

    s.add_node(dos)
    s.add_node(tres)
    s.add_edge((dos, tres))

    t.add_node(tres)
    t.add_node(quatro)
    t.add_node(uno)
    t.add_edge((tres, quatro))
    t.add_edge((quatro, uno))

    g = Graph("graph", [uno, dos, tres, quatro], [r, s, t])

    g.print_all()

    pr_0 = Rule("pr_0", ["x", "y"], [(r, ("x", "y"))])
    pr_1 = Rule("pr_1", ["x", "y"], [(s, ("x", "y"))])
    pr_2 = Rule("pr_2", ["x", "y"], [(t, ("x", "y"))])

    goal = Rule("Goal", ["x", "y"], [(pr_0, ("x","w")), (pr_1, ("w","z")), (pr_2, ("z","y"))], goal=True)

    rules = [pr_0, pr_1, pr_2, goal]

    print("Rules:")
    for r in rules:
        print("\t* {}".format(r))

    print("")

    solutions = g.resolve(rules)
    if len(solutions) != 0:
        print("Solutions:")
        for s in solutions:
            print("\t* ({0} - {1})".format(s[0].id, s[1].id))
    else:
        print("No solution!")

if __name__ == '__main__':
    test()
