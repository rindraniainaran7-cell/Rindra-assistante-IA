import os
from datetime import datetime


def executer_tache():
    tache = os.getenv("TASK", "Préparer la liste des tâches du jour")
    date = datetime.now().strftime("%d/%m/%Y")

    resultat = f"""RINDRA - ASSISTANTE IA
Date : {date}

TÂCHE REÇUE :
{tache}

STATUT :
Tâche reçue et traitée avec succès.
"""

    with open("resultat.txt", "w", encoding="utf-8") as fichier:
        fichier.write(resultat)

    print(resultat)
    print("Le fichier resultat.txt a été créé.")


if __name__ == "__main__":
    executer_tache()
