#def erreur_nombre("calcul.txt", "erreur.txt"):
#    fs = open("calcul.txt", "r")
#    fd = open("erreur.txt", "w")
#    fd.write(raw_input("La valeur {0} n'est pas un nombre".format(_saisie)))
#    fs.close()
#    fd.close()

def saisie(_saisie):
    try:
        int(_saisie)
        return int(_saisie)
    except:
        print("La valeur {0} n'est pas un nombre".format(_saisie))
        return False

def saisie2(_saisie2):
    if ('+' in s) | ('-' in s) | ('*' in s) | ('/' in s):
        _saisie2 = True
    else:
        _saisie2 = False

def operation(x,y, s):
    if (saisie(x) != False) & (saisie(y) != False) & (saisie2 != False):
        if '+' in s:
            print(saisie(x) + saisie(y))
        if '-' in s:
            print(saisie(x) - saisie(y))
        if '*' in s:
            print(saisie(x) * saisie(y))
        if '/' in s:
            print(saisie(x) / saisie(y))

fichier = open("calcul.txt", "w")
fichier.write(raw_input("Saisir la premiere valeur: "))
fichier.write("\n")
fichier.write(raw_input("Saisir la seconde valeur: "))
fichier.write("\n")
fichier.write(raw_input("Saisir le signe operatoire (+;-;*;/): "))
fichier.close()   

fichier = open("calcul.txt", "r")
x = fichier.readline()
y = fichier.readline()
s = fichier.readline()
fichier.close()

i = True
while i:
    if ('+' in s) | ('-' in s) | ('*' in s) | ('/' in s):
        operation(x,y, s)
        break