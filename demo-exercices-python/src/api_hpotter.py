#Test Api du site hp-api.onrender.com/api/characters/house
# Importation des modules
import requests
import json
from PIL import Image
from io import BytesIO
from colorama import Fore, Back, Style, init

# Fonction pour récupérer les données de l'API
def get_api_data(url):
    response = requests.get(url)
    return response.json()

# Fonction pour afficher les données de l'API
def display_api_data(data):
    for item in data:
        if item['house'] == 'Gryffindor':
            print(item['name'], item['house'], item['patronus'])
            #affiche l'image du personnage dans la console en ascii art
            if item['image']:
                image_to_ascii(item['image'])

# Fonction pour enregistrer les données de l'API dans un fichier JSON
def save_api_data(data):
    with open('api_data.json', 'w') as f:
        json.dump(data, f)

# Fonction pour charger les données de l'API depuis un fichier JSON
def load_api_data():
    with open('api_data.json', 'r') as f:
        return json.load(f)

def image_to_ascii(image_url):
    # Télécharger l'image depuis le lien
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Convertir l'image en ASCII art
    ascii_art = convert_to_ascii(image)

    # Afficher l'ASCII art dans la console
    print(ascii_art)

def convert_to_ascii(image, width=100):
    # Redimensionner l'image tout en maintenant le rapport hauteur/largeur
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio)
    resized_image = image.resize((width, new_height))

    # Convertir l'image en niveaux de gris
    grayscale_image = resized_image.convert("L")

    # Définir les caractères ASCII pour la conversion
    ascii_chars = "@%#*+=-:. "

    # Convertir chaque pixel en caractère ASCII
    ascii_str = ""
    for pixel_value in grayscale_image.getdata():
        # Assurer que l'index est dans la plage valide
        index = min(pixel_value // 25, len(ascii_chars) - 1)
        ascii_str += ascii_chars[index]

    # Diviser la chaîne ASCII en lignes pour l'affichage
    lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]
    return "\n".join(lines)

def image_to_colored_ascii(image_url):
    # Télécharger l'image depuis le lien
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Convertir l'image en ASCII art coloré
    colored_ascii_art = convert_to_colored_ascii(image)

    # Afficher l'ASCII art coloré dans la console
    print(colored_ascii_art)

def convert_to_colored_ascii(image, width=100):
    # Redimensionner l'image tout en maintenant le rapport hauteur/largeur
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio)
    resized_image = image.resize((width, new_height))

    # Convertir l'image en niveaux de gris
    grayscale_image = resized_image.convert("L")

    # Définir les caractères ASCII et les couleurs pour la conversion
    ascii_chars = "@%#*+=-:. "
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

    # Convertir chaque pixel en caractère ASCII avec couleur
    colored_ascii_str = ""
    for pixel_value in grayscale_image.getdata():
        # Assurer que l'index est dans la plage valide
        index = min(pixel_value // 25, len(ascii_chars) - 1)
        char = ascii_chars[index]

        # Choix aléatoire d'une couleur parmi la liste
        color = colors[index % len(colors)]

        # Ajouter le caractère coloré à la chaîne résultante
        colored_ascii_str += f"{color}{char}"

    # Diviser la chaîne ASCII colorée en lignes pour l'affichage
    lines = [colored_ascii_str[i:i + width] for i in range(0, len(colored_ascii_str), width)]
    return "\n".join(lines)


# Fonction principale
def main():
    init(autoreset=True)
    # Récupération des données de l'API
    url = 'https://hp-api.onrender.com/api/characters/'
    data = get_api_data(url)

    # Affichage des données de l'API
    display_api_data(data)

    # Enregistrement des données de l'API dans un fichier JSON
    save_api_data(data)

    # Chargement des données de l'API depuis un fichier JSON
    data = load_api_data()

    # Affichage des données de l'API
    display_api_data(data)

# Appel de la fonction principale
if __name__ == '__main__':
    main()

#Fin du programme
