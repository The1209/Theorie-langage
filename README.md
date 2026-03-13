Mini Interpréteur avec Fonctions — PLY (Python Lex Yacc)

1.  Présentation du projet

Ce projet implémente un mini langage de programmation interprété en
Python en utilisant la bibliothèque PLY (Python Lex Yacc).

PLY est une implémentation Python des outils classiques utilisés dans
les compilateurs : - Lex → analyse lexicale - Yacc → analyse syntaxique

L’objectif de ce projet est de comprendre comment fonctionne un
interpréteur en construisant les différentes étapes nécessaires : 1.
Analyse lexicale 2. Analyse syntaxique 3. Construction d’un AST
(Abstract Syntax Tree) 4. Exécution de cet AST

Le mini langage permet d’utiliser : - des variables - des opérations
mathématiques - des comparaisons - print - if / else - while - for -
fonctions - return

------------------------------------------------------------------------

2.  Fonctionnalités du langage

Variables Exemple : x = 5; y = 10;

Les variables sont stockées dans une table appelée : names = {}

------------------------------------------------------------------------

Opérations arithmétiques

Le langage supporte : + addition - soustraction * multiplication /
division

Exemple : x = 5 + 3; print(x);

Résultat : CALC> 8

------------------------------------------------------------------------

Comparaisons

Opérateurs disponibles : < inférieur > supérieur <= inférieur ou égal ==
égal

Exemple : if (x > 3){ print(x); };

------------------------------------------------------------------------

3.  Structures de contrôle

If / Else

if (x > 10){ print(x); } else{ print(0); };

------------------------------------------------------------------------

Boucle while

i = 0; while (i < 5){ print(i); i = i + 1; };

Résultat : CALC> 0 CALC> 1 CALC> 2 CALC> 3 CALC> 4

------------------------------------------------------------------------

Boucle for

for(i = 0; i < 5; i = i + 1){ print(i); };

------------------------------------------------------------------------

4.  Fonctions

Une des principales extensions de ce projet est l’ajout de fonctions.

Les fonctions permettent : - de structurer le code - de réutiliser des
calculs - de renvoyer des valeurs

------------------------------------------------------------------------

5.  Définition d’une fonction

Syntaxe :

func nom(param1, param2){ instructions return valeur; };

Exemple :

func carre(x){ return x * x; };

------------------------------------------------------------------------

6.  Appel de fonction

Une fonction peut être appelée comme une expression.

Exemple :

print(carre(5));

Résultat : CALC> 25

------------------------------------------------------------------------

7.  Fonction avec plusieurs paramètres

func add(a,b){ return a + b; };

print(add(2,3));

Résultat : CALC> 5

------------------------------------------------------------------------

8.  Représentation interne (AST)

Le programme est transformé en AST (Abstract Syntax Tree).

Chaque instruction est représentée par un tuple Python.

Exemple : x = 5 + 3;

AST : (‘assign’, ‘x’, (‘+’, 5, 3))

------------------------------------------------------------------------

9.  Table des fonctions

Les fonctions sont stockées dans :

functions = {}

Exemple : functions[“carre”] = ([“x”], bloc_ast)

------------------------------------------------------------------------

10. Appel de fonction : fonctionnement interne

Lorsqu’un appel de fonction est rencontré :

carre(5)

L’interpréteur effectue les étapes suivantes : 1. Vérifier que la
fonction existe 2. Récupérer ses paramètres 3. Évaluer les arguments 4.
Créer un environnement local 5. Exécuter le bloc de la fonction 6.
Récupérer la valeur de return

------------------------------------------------------------------------

11. Gestion du return

Le return doit : - arrêter immédiatement la fonction - renvoyer une
valeur

Pour cela on utilise une exception Python interne :

class ReturnValue(Exception): def init(self, value): self.value = value

Quand un return est rencontré : raise ReturnValue(valeur)

L’appel de fonction récupère ensuite cette valeur.

------------------------------------------------------------------------

12. Exemple complet

func carre(x){ return x * x; };

func add(a,b){ return a + b; };

print(carre(5)); print(add(2,3));

Résultat attendu :

CALC> 25 CALC> 5

------------------------------------------------------------------------


