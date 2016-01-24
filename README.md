# ei-projet
Projet d'Extraction d'Information

# Auteur
Carette Antonin (antonin.carette[at]etudiant[dot]univ-lille1[dot]fr)

# Langage de programmation
Python3 (version 4)

# Exemple

Sur un schéma tel que

```
uno -> dos (R)
dos -> tres (S)
tres -> quatro (T)
quatro -> dos (R)
quatro -> uno (T)
```


et une règle **GOAL** permettant de trouver tous les chemins empruntants les relations *r*, *s* et *t*

```goal = Rule("Goal", ["x", "y"], [(r, ("x","w")), (s, ("w", "z")), (t, ("z", "y"))], goal=True)```

nous obtenons au final...

```
Graph "graph"
* Nodes:
	 uno
	 dos
	 tres
	 quatro

* Relations:
	Relation "R"
	############
	* Nodes: uno, dos, quatro,
	* Edges: uno->dos | quatro->dos |

	Relation "S"
	############
	* Nodes: dos, tres,
	* Edges: dos->tres |

	Relation "T"
	############
	* Nodes: tres, quatro, uno,
	* Edges: quatro->uno | tres->quatro |

Solutions: * uno - quatro
           * quatro - quatro
```

À noter que la règle **GOAL** peut aussi s'écrire:

```
pr_0 = Rule("pr_0", ["x", "y"], [(r, ("x", "z")), (s, ("z", "y"))])
goal = Rule("Goal", ["x", "y"], [(pr_0, ("x","y"))], goal=True)
```

Dans ce cas, la règle **GOAL** va aller chercher la règle **pr_0** qui va définir ce qu'elle veut dans les relations du graph.
