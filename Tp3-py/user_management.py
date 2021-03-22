#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script create a dictionary with user name and user statistics
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:
#               Objectifs :
#                               • Définition de 7 variables internes au programme
#                                   • 1 Dictionnaire contenant
#                                       • Toutes les informations utilisateurs
#                                       • Le nombre max d’utilisateur
#                                   • Message de la question pour le nom de famille
#                                   • Message de la question pour le prénom
#                                   • Message indiquant le bon chargement du fichier
#                                   • Message indiquant l’inexistence d’un fichier de sauvegarde
#                                   • Message indiquant la sauvegarde des utilisateurs
#                                   • Le nom du fichier de sauvegarde
#                                   • Utilisation de 9 fonctions permettant
#                                   • La modification du nombre maximum d’utilisateur
#                                   • La récupération du nombre maximum d’utilisateur
#                                   • L’ajout d’un nouvel utilisateur
#                                   • La récupération de la liste des utilisateurs enregistrés
#                                   • L’ajout des résultats d’une tentative d’un utilisateur
#                                   • Récupération de tous les résultats d’un utilisateur
#                                   • Récupération du nom complet d’un utilisateur
#                                   • Chargement des données utilisateurs depuis le fichier de sauvegarde
#                                   • Sauvegarde des données utilisateurs vers le fichier de sauvegarde
#
#                                   • Un programme de test dans le fichier qui permet de vérifier que les fonctions
#                                     réalisent leurs actions correctement avec le process suivant
#                                   • Récupération des anciennes statistiques
#                                   • Tentative de création de X utilisateurs(X étant le maximum d’utilisateur + 1)
#                                   • Gestion du nombre maximum d’utilisateur
#                                   • Affichage du nombre maximum en cours
#                                   • Tentative de modification à 1 utilisateur maximum
#                                   • Affichage du nombre maximum en cours
#                                   • Tentative de modification à 3 utilisateur maximum
#                                   • Affichage du nombre maximum en cours
#                                   • Ajout de statistiques aléatoires pour chaque utilisateur en mémoire
#                                   • Affichage de toutes les statistiques pour chaque utilisateur en mémoire
#                                   • Sauvegarde des statistiques
#
#                                   • Deux exécutions du programme ne produisent pas la même chose
#                                   • Exécution 1
#                                   • Recherche de fichier de sauvegarde inexistant
#                                   • Tentative de création de 3 utilisateurs
#                                   • Création de 2 utilisateurs
#                                   • Tentative de modification du nombre d’utilisateur
#                                   • Passage à 3 utilisateurs max
#                                   • Ajout de statistiques aléatoires sur les 2 utilisateurs existants
#                                   • Affichage des statistiques pour les 2 utilisateurs existants
#                                   • Sauvegarde des statistiques
#                                   • Exécution 2
#                                   • Recherche et chargement du fichier de sauvegarde existant
#                                   • Tentative de création de 4 utilisateurs
#                                   • Création de 1 utilisateur
#                                   • Tentative de modification du nombre d’utilisateur
#                                   • Ajout de statistiques aléatoires sur les 3 utilisateurs existants
#                                   • Affichage des statistiques pour les 3 utilisateurs existants
#                                   • Sauvegarde des statistiques
#
#
#
#               Contraintes :
#                                   • Les 7 variables globales doivent être initialisées dès
#                                     le début du programme et se nommer
#                                       • « all_users_information »
#                                       • « first_name_question »
#                                       • « last_name_question »
#                                       • « loading_success_message »
#                                       • « loading_failed_message »
#                                       • « saving_message »
#                                       • « statistic_file »
#                                   • Le fichier de sauvegarde doit être nommé « statistics.dat »
#                                   • Les 9 fonctions doivent être nommées
#                                       • « set_new_max_user »
#                                       • « get_max_user »
#                                       • « add_new_user »
#                                       • « get_list_of_users »
#                                       • « add_user_try_result »
#                                       • « get_user_statistics »
#                                       • « get_user_name »
#                                       • « load_statistics »
#                                       • « save_statistics »
#
#
#                                   • Fonction « set_new_max_user »
#                                       • Le nombre maximum d’utilisateur est mis à jour uniquement
#                                         dans le cas où il est supérieur au précédent
#
#                                   • Fonction « add_new_user »
#                                       • L’ajout d’utilisateur n’est possible que si le
#                                         nombre maximum n’est pas atteint
#                                       • Les informations de l’utilisateur sont associées à un identifiant unique
#                                       • L’ajout d’un utilisateur implique la création d’un dictionnaire dans le
#                                         dictionnaire principal « all_user_information » contenant:
#                                           • Clé « id_f_name » avec le prénom
#                                           • Clé « id_l_name » avec le nom de famille
#                                           • Clé « statistics » avec un dictionnaire vide pour les futures statistiques
#                                       • La fonction retourne un tuple avec
#                                         (Nouvel identifiant, Max user atteint ou pas)
#
#                                   • Fonction « get_list_of_users »
#                                       • Retourne une liste de tuples contenant
#                                         (Identifiant utilisateur, Nom complet utilisateur)
#                                       • Nom complet utilisateur veut dire « [Prénom] [Nom] »
#
#                                   • Fonction « add_user_try_result »
#                                       • Doit ajouter les statistiques suivantes à l’utilisateur donné
#                                           • Range min
#                                           • Range max
#                                           • Nombre de tentative
#                                       • La clé de l’événement est la date d’ajout au format ISO
#
#                                   • Fonction « get_user_name »
#                                       • Retourne le nom complet de l’utilisateur
#                                       • Nom complet utilisateur veut dire « [Prénom] [Nom] »
#
#                                   • Fonction « main » avec le programme de test
#                                       • Ne doit pas s’exécuter si le fichier est importé
#                                       • Toutes les affectations, modifications des variables internes
#                                         doivent utiliser les fonctions définies à cet effet
#                                       • Affichage et mise en forme
#                                       • La quasi-totalité de l’affichage avec mise en forme
#                                         faite avec des « print » doit-être contenue dans la fonction main
#                                       • Seul les affichages suivants sont fait dans les fonctions
#                                       • L’affichage des questions « Nom » / « Prénom»
#                                       • L’affichage du message de la réussite ou de l’impossibilité
#                                         du chargement (fichier de sauvegarde)
#                                       • L’affichage du message de la sauvegarde des statistiques
#
#
#
# Author:       LEJOSNE Florian
#
# Date:         2021.03.22
# ##############################################################################


# ==============================================================================
# IMPORTS
# ==============================================================================

import ast
import finder_management

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================


all_users_information = {}
first_name_question = "| What is the first name of the user: "
last_name_question = "| What is the last name of the user: "
loading_success_message = "| Users statistics loaded!"
loading_failed_message = "| No previous statistics to load..."
saving_message = "| Users statistics saved!"
statistic_file = "statistics.dat"
user_number = 0


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def load_statistics():
    """
    This function retrieves data from the statistic_file to the all_the_users_information

    :return: None
    """
    # Importing variable from global scope
    global all_users_information
    global statistic_file
    global user_number
    # Sequential control structure
    try:
        with open(statistic_file, "r") as file:
            # Loading variable from file
            all_users_information = ast.literal_eval(file.read())
            # Displaying variable
            finder_management.printer_top()
            print(loading_success_message)
            finder_management.printer_end()
    except IOError:
        # Displaying variable
        finder_management.printer_top()
        print(loading_failed_message)
        finder_management.printer_end()


def save_statistics():
    """
    This function saves statistics from the all_the_users_information dictionary to the statistic_file

    :return: None
    """
    # Importing variable from global scope
    global all_users_information
    # Open, Write and Close inside file statistics.dat
    file = open(statistic_file, "w")
    file.write(str(all_users_information))
    file.close()
    # Displaying variable
    finder_management.printer_top()
    print(saving_message)
    finder_management.printer_end()


def add_new_user():
    """
    This function adds a new dictionary with the id of the all_users_information
    with the get_user_name function

    :return: None
    """

    for user_id in range(user_number, all_users_information["data"]["user_required"]):
        # Iterative control structure
        if user_id >= all_users_information["data"]["user_max"]:
            # Displaying string
            finder_management.printer_top()
            print("| => Maximum number of user have been reached <=")
            # Calling function
            finder_management.printer_end()
        else:
            # Calling function
            all_users_information[user_id] = get_user_name()
            all_users_information[user_id]["stats"] = {}
            # Displaying variable
            print("| New user '{0} {1}' have been created\n| Default statistics set to '{2}'".format(
                all_users_information[user_id]["id_f_name"],
                all_users_information[user_id]["id_l_name"],
                all_users_information[user_id]["stats"]
            ))
            # Calling function
            finder_management.printer_end()


def get_user_name():
    """
    This function returns a dictionary corresponding to a name with two strings inputted by the user

    :return: user_name
    """
    # Define dictionary
    finder_management.printer_top()
    user_data = dict({
        "id_f_name": input("| What is the first name of the user: "),
        "id_l_name": input("| What is the last name of the user: ")
    })
    # Returning list
    return user_data


def set_max_user(new_user_max):
    """
    This function overwrites the value for the "user_max" key in the all_users_information dictionary

    :param new_user_max: Number - The new number corresponding to the new maximum amount of users
    :return: None
    """
    # Defining variable
    last_user_max = all_users_information["data"]["user_max"]
    # Displaying variable
    finder_management.printer_top()
    print("| Previous maximum of users: '{0}'".format(
        last_user_max
    ))
    # Redefining variable
    all_users_information["data"]["user_max"] = new_user_max
    print("| New maximum of users: '{0}'\n"
          "| Last maximum of users: '{1}'".format(new_user_max, last_user_max))
    finder_management.printer_end()


# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':
    load_statistics()
    # Calling function
    add_new_user()
    # Calling function
    set_max_user(3)
    # Redefining value
    all_users_information["data"]["user_required"] = 4
    # Calling function
    save_statistics()
