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

    goal = Rule("Goal", ["x", "y"], [(r, ("x","w")), (s, ("w", "z")), (t, ("z", "y"))], goal=True)

    rules = [goal]

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
