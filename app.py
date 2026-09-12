from datetime import date
import os

def assistant():
    print("RINDRA - ASSISTANTE IA")
    print()
    print(f"Date : {date.today()}")
    print()

    task = os.getenv("TASK", "")

    print("TÂCHE REÇUE :")
    print(task)
    print()

    if task == "Préparer la liste des tâches prioritaires du jour":
        resultat = """RINDRA - TÂCHES PRIORITAIRES DU JOUR

1. Vérifier les tâches importantes à accomplir aujourd'hui.
2. Traiter les tâches urgentes en premier.
3. Organiser les tâches restantes par ordre de priorité.
4. Prévoir les tâches à reporter si nécessaire.
"""

        with open("resultat.txt", "w", encoding="utf-8") as fichier:
            fichier.write(resultat)

        print("STATUT :")
        print("Liste des tâches prioritaires créée avec succès.")

    else:
        print("STATUT :")
        print("Tâche reçue mais non reconnue.")


if __name__ == "__main__":
    assistant()
