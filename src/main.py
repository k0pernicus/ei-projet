from lib.graph import Graph
from lib.node import Node
from lib.relation import Relation
from lib.rule import Rule

def test():

    # Création des noeuds
    uno = Node("uno")
    dos = Node("dos")
    tres = Node("tres")
    quatro = Node("quatro")

    # Création des relations
    r = Relation("R", directed = True)
    s = Relation("S", directed = True)
    t = Relation("T", directed = True)

    # Ajout des noeuds dans les relations, et création des arêtes
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

    # Création du graph, qui contient la liste des noeuds créés et la liste des relations utilisant les noeuds
    g = Graph("graph", [uno, dos, tres, quatro], [r, s, t])

    # Méthode permettant de sortir toutes les caractéristiques du graphe
    g.print_all()

    # Création des règles!
    # Définition d'une règle!
    pr_0 = Rule("pr_0", ["x", "y"], [(r, ("x", "z")), (s, ("z", "y"))])
    # Définition du goal, utilisant la règle pr_0!
    goal = Rule("Goal", ["x", "y"], [(pr_0, ("x","y"))], goal=True)

    # Ajout des règles dans une liste, afin de pouvoir la passer au graphe pour la résolution
    rules = [pr_0, goal]

    # Impression des règles
    print("Rules:")
    for r in rules:
        print("\t* {}".format(r))
    print("")

    # Résolution du problème
    solutions = g.resolve(rules)

    # Impression des solutions
    if len(solutions) != 0:
        print("Solutions:")
        for s in solutions:
            print("\t* ({0} - {1})".format(s[0].id, s[1].id))
    else:
        print("No solution!")

if __name__ == '__main__':
    test()
