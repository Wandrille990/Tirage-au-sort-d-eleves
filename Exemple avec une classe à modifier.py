from random import shuffle

choisir_classe = str(input("Avec quelle classe êtes vous actuellement ? (ex: 1s4) : "))

# 1er S4

if choisir_classe == "1s4":
    # LISTE DES ELEVES QUI VONT POSER LES QUESTIONS

    classe_interrogatrice = [
        "Atilla",
        "Axel",
        "Cédric",
        "Chamsdine",
        "Chloé",
        "Coline",
        "Eléana",
        "Flavie",
        "Florian",
        "Gabriel",
        "Guillaume",
        "Inês",
        "Jéléna",
        "Justine",
        "Laudy",
        "Lison",
        "Margot",
        "Marine",
        "Marko",
        "Rémy",
        "Romain",
        "Sofiane",
        "Thomas",
        "Wandrille",
    ]

    # LISTE DES ELEVES QUI VONT REPONDRENT AUX QUESTIONS

    classe_interroge = [
        "Atilla",
        "Axel",
        "Cédric",
        "Chamsdine",
        "Chloé",
        "Coline",
        "Eléana",
        "Flavie",
        "Florian",
        "Gabriel",
        "Guillaume",
        "Inês",
        "Jéléna",
        "Justine",
        "Laudy",
        "Lison",
        "Margot",
        "Marine",
        "Marko",
        "Rémy",
        "Romain",
        "Sofiane",
        "Thomas",
        "Wandrille",
    ]

try:

    shuffle(classe_interrogatrice)

    print("")

    try:
        print(classe_interrogatrice[0])
        print(classe_interrogatrice[1])
        print(classe_interrogatrice[2])
    except IndexError:
        print("")
        print("ERREUR : Il reste moins de 3 personnes qui peuvent poser les questions.")
        print(
            "Veuillez réinitialiser les listes d'élèves en retirant les '#' devant les prénoms et relancer le programme.")
        print(
            "Gardez les personnes déjà sélectionnées pour poser les questions et rajouter y les premières désignées une fois le programme réinitialisé et relancer.")
        print(
            "Vous pourrez ensuite à nouveau mettre les '#' devant les personnes choisies comme précedemment, jusqu'à ce que ce message d'erreur arrive à nouveau.")
        print("")

    shuffle(classe_interroge)

    if classe_interrogatrice[0] in classe_interroge:
        classe_interroge.remove(classe_interrogatrice[0])

    if classe_interrogatrice[1] in classe_interroge:
        classe_interroge.remove(classe_interrogatrice[1])

    if classe_interrogatrice[2] in classe_interroge:
        classe_interroge.remove(classe_interrogatrice[2])

    print('')
    print("Vont interroger :")
    print('')

    try:
        print(classe_interroge[0])
        print(classe_interroge[1])
        print(classe_interroge[2])
    except IndexError:
        print("")
        print(
            "ERREUR : Un ou plusieurs élèves qui posent les questions sont les mêmes que ceux qui peuvent y répondre, il n'a plus de possibilités.")
        print(
            "Veuillez réinitialiser les listes d'élèves en retirant les '#' devant les prénoms et relancer le programme.")
        print(
            "Gardez les personnes déjà sélectionnées pour poser ou répondre aux questions et rajoutez y les premières désignées un fois le programme réinitialisé et relancer.")
        print(
            "Vous pourrez ensuite à nouveau mettre les '#' devant les personnes choisies comme précedemment, jusqu'a ce que ce message d'erreur arrive à nouveau.")
        print("")

except NameError:
    print('')
    print("La classe que vous avez appelé n'éxiste pas.")
    print("Relancer le programme en vous assurant de ne pas vous tromper dans l'appel de la classe voulue.")

# créé par Wandrille Legras
