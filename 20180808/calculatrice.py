'''
1 - Lire un fichier
dont le format est:
int;int;operation (+|-|*|/)

exemple:
1;1;+

2 - utiliser les informations fournies dans le fichier pour effectuer les operations arithmetiques définies


3 - Ecrire les résultats justes dans un fichier
sous le format:

L'addition de <premier nombre> avec <second nombre> est: <resultat>

4 - Ecrire les erreurs dans un autre fichier sous le format:
la ligne "a;1;e" contient 2 erreurs:
a n'est pas un chiffre
e n'est pas une operation

Il faut lire tout le fichier
Ecrire un fichier qui permet d'effectuer tous les tests
Utiliser des noms parlant
'''
import os
import csv
from fonction_calculs import operation, saisie_int, saisie_ope

def compute_from_file(input_filename):
    '''
    Read provided file name and execute operations in it
    '''
    with open(os.path.abspath(input_filename), newline='') as fd:
        for calcul in fd.read().splitlines():
            left, right, operand = calcul.split(';')
            print(left, right, operand)

if __name__ == '__main__':
    compute_from_file('test_input.csv')
