from datetime import datetime


def creer_liste_taches():
    date = datetime.now().strftime("%d/%m/%Y")

    taches = [
        "Vérifier les nouvelles tâches",
        "Traiter les tâches prioritaires",
        "Préparer les réponses",
        "Vérifier les tâches terminées"
    ]

    contenu = f"RINDRA - LISTE DES TÂCHES\n"
    contenu += f"Date : {date}\n\n"

    for numero, tache in enumerate(taches, 1):
        contenu += f"{numero}. {tache}\n"

    with open("taches.txt", "w", encoding="utf-8") as fichier:
        fichier.write(contenu)

    print("================================")
    print("RINDRA - AUTOMATISATION")
    print("================================")
    print(contenu)
    print("Le fichier taches.txt a été créé.")


if __name__ == "__main__":
    creer_liste_taches()
