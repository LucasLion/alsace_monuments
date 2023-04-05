# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: noil </var/spool/mail/noil>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/28 16:55:24 by noil              #+#    #+#              #
#    Updated: 2023/04/05 19:20:08 by llion            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functions import *
from pathlib import Path

def parse_for_one_person(tab, return_list):
    for i in range(len(tab)):
        id = get_id(i)
        merimee = get_merimee(i)
        matched_index = match_ids(id)
        matched_merimee = match_merimee(merimee)
        nom_arrondissement = get_arrondissement(int(code_commune[i]))
        name = get_name(i)
        coor_x = get_coor_x(i)
        coor_y = get_coor_y(i)
        status = get_status(matched_index)
        damages = get_damages(i, tab)
        commentaire = get_comments(i)
        adresse = get_address(i)
        if adresse == None:
            adresse = "Non Renseigné"

        if matched_merimee == None:
            precision = "Non Renseigné"
        else:
            precision = get_precision(matched_merimee)
        date = get_date(i, tab)

        monument = (id, name, nom_arrondissement, coor_x, coor_y, status, damages, commentaire, precision, date)
        return_list.append(monument)
    return (return_list)

def create_csv(list, name):
    columns = ['ID', 'Nom', 'Arrondissemnt', 'Coor_x', 'Coor_y', 'Status', 'Dommages', 'Commentaire', 'Précision', 'Date']
    frame = pd.DataFrame(list, columns=columns)
    frame.to_csv(name, index=False)

def main():
    BASE_DIR = Path(__file__).resolve().parent

    list_AC = parse_for_one_person(pers1, AC)
    create_csv(list_AC, BASE_DIR / 'calques_personels/AC.csv')
    list_ED = parse_for_one_person(pers2, ED)
    create_csv(list_ED, BASE_DIR / 'calques_personels/ED.csv')
    list_KB = parse_for_one_person(pers3, KB)
    create_csv(list_KB, BASE_DIR / 'calques_personels/KB.csv')
    list_LM = parse_for_one_person(pers4, LM)
    create_csv(list_LM, BASE_DIR / 'calques_personels/LM.csv')
    list_MHC = parse_for_one_person(pers5, MHC)
    create_csv(list_MHC, BASE_DIR / 'calques_personels/MHC.csv')
    list_PC = parse_for_one_person(pers6, PC)
    create_csv(list_PC, BASE_DIR / 'calques_personels/PC.csv')
    list_RRM = parse_for_one_person(pers7, RRM)
    create_csv(list_RRM, BASE_DIR / 'calques_personels/RRM.csv')
    list_TG = parse_for_one_person(pers8, TG)
    create_csv(list_TG, BASE_DIR / 'calques_personels/TG.csv')
    list_UDAP = parse_for_one_person(pers9, UDAP)
    create_csv(list_UDAP, BASE_DIR / 'calques_personels/UDAP.csv')
    print(f"fichiers créés dans le dossier calques_personels")

if __name__ == "__main__":
    main()
