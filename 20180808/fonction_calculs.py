import sys

def saisie_int(valeur=None, message='Entrer un nombre'):
    if not valeur:
        valeur = input(message)

    try:
        return int(valeur)
    except:
        raise TypeError('La valeur {} n\'est pas un nombre'.format(valeur))

def saisie_ope(operator=None, message='Entrer un operateur'):
    if not operator:
        operator = input(message).upper()

    if operator in ['+', '-', '*', '/']:
        return operator

    if operator == 'Q':
        sys.exit("Bye bye")

    raise ValueError('{} n\'est pas un operateur supporte'.format(valeur))

def operation(x, y, signe):
    if signe == '+':
        return x + y

    if signe == '*':
        return x * y

    if signe == '-':
        return x - y

    if signe == '/':
        return x - y

    raise ValueError('Unknown operation')

if __name__ == '__main__':
    while True:
        try:
            a = saisie_ope("Q pour arreter, A pour addition, M pour multiplication: ")
            operation(
                saisie_int("Saisir la premiere valeur: "),
                saisie_int("Saisir la seconde valeur: "),
                a
            )
        except TypeError as exception:
            print(exception)
        except ValueError as exception:
            print(exception)
