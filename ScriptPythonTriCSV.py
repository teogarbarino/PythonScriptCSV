import csv

def supprimer_lignes_sans_region(fichier_csv, region_cible):
    """Supprime les lignes d'un fichier CSV ne contenant pas la région cible.

    Args:
        fichier_csv (str): Nom du fichier CSV.
        region_cible (str): Chaîne de caractères à rechercher dans les lignes.
    """

    lignes_a_garder = []
    ligne_num = 1

    with open(fichier_csv, 'r', encoding='utf-8') as csvfile:
        lecteur = csv.reader(csvfile)
        for ligne in lecteur:
            if region_cible in ' '.join(ligne):
                lignes_a_garder.append(ligne)
            ligne_num += 1

    with open(fichier_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(lignes_a_garder)
        print("Fichier mis à jour avec succès.")

# Exemple d'utilisation
fichier = "Donnees-detaillees-au-logement-du-repertoire-des-logements-locatifs-des-bailleurs-sociau.2023-01.csv"
region = "Provence-Alpes-Côte d'Azur"
supprimer_lignes_sans_region(fichier, region)