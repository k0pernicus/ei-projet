# ei-projet
Projet d'Extraction d'Information

# Auteur
Carette Antonin (antonin.carette[at]etudiant[dot]univ-lille1[dot]fr)

# Langage de programmation
Python3 (version 4)

# Utilisation

Des objets Python sont à votre disposition pour créer votre propre graphe, et vos propres règles.  
Vous pouvez ainsi créer des noeuds (Node) et des relations entre ces derniers (Relation), afin de pouvoir importer le tout dans un graphe (Graph).  
Après, il vous sera demandé d'ajouter des règles (Rule - avec une règle **GOAL**) et de demander à résoudre le problème de **GOAL** dans le graphe que vous souhaitez.

Un exemple documenté est présent dans ```src/main.py```.
Trois exemples sont à votre disposition, afin de voir la syntaxe des objets, conçu dans le même modèle que l'exemple ci-dessous (dans le dossier ```examples```).  
Aussi, les objets et leur documentation sont à votre disposition dans le sous-module ```lib``` de ```src```.

Pour l'exécution:
*	créez votre modèle et vos règles dans un fichier ```mon_modele.py```,
*	résolvez le avec ```python3.4 mon_modele.py```.

Pour tester, vous pouvez très bien utiliser un exemple contenu dans le dossier ```examples```, comme par exemple:
*	```cd src && cp ../examples/three_rules.py ./```
*	```python3.4 three_rules.py```

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

```
goal = Rule("Goal", ["x", "y"], [(r, ("x","w")), (s, ("w", "z")), (t, ("z", "y"))], goal=True)
```

(ici, les atomes ne seront pas parsées par le programme - ainsi, une suite r(x,y) s(y,z) sera perçu comme une suite de règles!), nous obtenons en sortie

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
