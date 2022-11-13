# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:         :+:        #
#                                                     +:+ +:+         +:+      #
#    By: noil </var/spool/mail/noil>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/28 16:55:24 by noil              #+#    #+#              #
#    Updated: 2022/11/13 18:55:19 by llion         ##########  ###########     #
#                                                                              #
# **************************************************************************** #

from functions import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

for i in range(len(names)):
    id = get_id(i)
    merimee = get_merimee(i)
    
    matched_index = match_ids(id)
    matched_merimee = match_merimee(merimee)

    nom_arrondissement = get_arrondissement(int(code_commune[i]))
    name = get_name(i)
    coor_x = get_coor_x(i)
    coor_y = get_coor_y(i)
    status = get_status(matched_index)
    damages = get_damages(i)
    commentaire = get_comments(i)
    adresse = get_address(i)
    if adresse == None:
        adresse = "Non Renseigné"

    if matched_merimee == None:
        precision = "Non Renseigné"
    else:
        precision = get_precision(matched_merimee)
    date = get_date(i)

    monument = (id, name, nom_arrondissement, coor_x, coor_y, status, damages, commentaire, precision, date)

    match monument[2]:
        case "Altkirch":
            altkirch.append(monument)
        case "Colmar-Ribeauvillé":
            colmar_ribeauville.append(monument)
        case "Haguenau-Wissembourg":
            haguenau_wissembourg.append(monument)
        case "Molsheim":
            molsheim.append(monument)
        case "Mulhouse":
            mulhouse.append(monument)
        case "Saverne":
            saverne.append(monument)
        case "Sélestat-Erstein":
            selestat_erstein.append(monument)
        case "Strasbourg":
            strasbourg.append(monument)
        case "Thann-Guebwiller":
            thann_guebwiller.append(monument)

    monuments.append(monument)

columns = ['ID', 'Nom', 'Arrondissemnt', 'Coor_x', 'Coor_y', 'Status', 'Dommages', 'Commentaire', 'Précision', 'Date']

df_altkirch = pd.DataFrame(altkirch, columns = columns)
print(df_altkirch)
df_colmar_ribeauville = pd.DataFrame(colmar_ribeauville, columns = columns)
df_haguenau_wissembourg = pd.DataFrame(haguenau_wissembourg, columns = columns)
df_molsheim = pd.DataFrame(molsheim, columns = columns)
df_mulhouse = pd.DataFrame(mulhouse, columns = columns)
df_saverne = pd.DataFrame(saverne, columns = columns) 
df_selestat_erstein = pd.DataFrame(selestat_erstein, columns = columns)
df_strasbourg = pd.DataFrame(strasbourg, columns = columns)
df_thann_guebwiller = pd.DataFrame(thann_guebwiller, columns = columns)


df_altkirch.to_csv(f'{BASE_DIR}/calques/Altkirch.csv', index = False)
df_colmar_ribeauville.to_csv(f'{BASE_DIR}/calques/Colmar-Ribeauvillé.csv', index = False)
df_haguenau_wissembourg.to_csv(f'{BASE_DIR}/calques/Haguenau-Wissembourg.csv', index = False)
df_molsheim.to_csv(f'{BASE_DIR}/calques/Molsheim.csv', index = False)
df_mulhouse.to_csv(f'{BASE_DIR}/calques/Mulhouse.csv', index = False)
df_saverne.to_csv(f'{BASE_DIR}/calques/Saverne.csv', index = False)
df_selestat_erstein.to_csv(f'{BASE_DIR}/calques/Sélestat-Erstein.csv', index = False)
df_strasbourg.to_csv(f'{BASE_DIR}/calques/Strasbourg.csv', index = False)
df_thann_guebwiller.to_csv(f'{BASE_DIR}/calques/Thann-Guebwiller.csv', index = False)
print(f"fichiers crées")

