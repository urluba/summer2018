import sys

def saisie_int(valeur=None, message='Entrer un nombre'):
    if valeur is None:
        valeur = input(message)

    try:
        return int(valeur)
    except:
        raise TypeError('La valeur {} n\'est pas un nombre'.format(valeur))

def saisie_ope(operator=None, message='Entrer un operateur'):
    if operator is None:
        operator = input(message).upper()

    if operator in ['+', '-', '*', '/']:
        return operator

    if operator == 'Q':
        sys.exit("Bye bye")

    raise ValueError('{} n\'est pas un operateur supporte'.format(operator))

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
            a = saisie_ope(None, "Q pour arreter, + pour addition, * pour multiplication...: ")
            print(operation(
                saisie_int(None, "Saisir la premiere valeur: "),
                saisie_int(None, "Saisir la seconde valeur: "),
                a
            ))
        except TypeError as exception:
            print(exception)
        except ValueError as exception:
            print(exception)
