def afficher_menu():
    print("================================")
    print("   RINDRA - ASSISTANTE IA")
    print("================================")
    print("1. Afficher un message")
    print("2. Quitter")


def assistant():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            message = input("Quel message voulez-vous afficher ? ")
            print("\nAssistant :", message)

        elif choix == "2":
            print("À bientôt !")
            break

        else:
            print("Option invalide. Réessayez.")


if __name__ == "__main__":
    assistant()
