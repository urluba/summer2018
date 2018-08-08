def saisie(_saisie):
    try:
        int(_saisie)
        return int(_saisie)
    except:
        print("La valeur {0} n'est pas un nombre".format(_saisie))
        return False

def operation(x,y, signe):
    if (saisie(x) != False) & (saisie(y) != False):
        if 'A' in signe:
            print(saisie(x) + saisie(y))
        if 'M' in signe:
            print(saisie(x) * saisie(y))

i = True
while i:
    a = raw_input("Q pour arreter, A pour addition, M pour multiplication: ")
    if 'Q' in a:
        i = False

    if ('A' in a) | ('M' in a):
        operation(raw_input("Saisir la premiere valeur: "), raw_input("Saisir la seconde valeur: "), a)