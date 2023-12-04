def compter_caracteres_recursif(phrase):
    # Cas de base : la phrase est vide
    if not phrase:
        return 0
    # Cas récursif : ajouter 1 pour le premier caractère et appeler la fonction pour le reste de la phrase
    else:
        return 1 + compter_caracteres_recursif(phrase[1:])


# Exemple d'utilisation
phrase_exemple = "Ceci est une phrase de test."
nombre_caracteres = compter_caracteres_recursif(phrase_exemple)

print(f"La phrase '{phrase_exemple}' a {nombre_caracteres} caractères.")
