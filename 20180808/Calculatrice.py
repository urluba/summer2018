fichier = open("calcul.txt", "w")
fichier.write(raw_input("Saisir la premiere valeur: "))
fichier.write("\n")
fichier.write(raw_input("Saisir la seconde valeur: "))
fichier.write("\n")
fichier.write(raw_input("Saisir le signe operatoire: "))
fichier.close()   

fichier = open("calcul.txt", "r")
x = fichier.readline()
y = fichier.readline()
s = fichier.readline()
print x
print y
print s
fichier.close()