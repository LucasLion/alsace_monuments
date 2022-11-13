# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: noil </var/spool/mail/noil>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/10/28 16:55:24 by noil              #+#    #+#              #
#    Updated: 2022/11/12 11:32:26 by llion            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functions import *

print(f"len tab3: {len(tab3)}")


for i in range(len(names)):
    tab2_index = match_ids(id)

    id = get_id(i)
    nom_arrondissement = get_arrondissement(int(code_commune[i]))
    name = get_name(i)
    coor_x = get_coor_x(i)
    coor_y = get_coor_y(i)
    status = get_status(tab2_index)
    damages = get_damages(i)
    commentaire = get_comments(i)
    precision = get_precision(i)
    date = get_date(i)

    monument = (id, name, nom_arrondissement, coor_x, coor_y, status, damage, commentaire, precision, date)

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

columns = ['id', 'name', 'Arrondissemnt', 'Coor_x', 'Coor_y', 'Status', 'Dommages', 'Commentaire', 'Précision', 'Date']

df_altkirch = pd.DataFrame(altkirch, columns = columns)
df_colmar_ribeauville = pd.DataFrame(colmar_ribeauville, columns = columns)
df_haguenau_wissembourg = pd.DataFrame(haguenau_wissembourg, columns = columns)
df_molsheim = pd.DataFrame(molsheim, columns = columns)
df_mulhouse = pd.DataFrame(mulhouse, columns = columns)
df_saverne = pd.DataFrame(saverne, columns = columns)
df_selestat_erstein = pd.DataFrame(selestat_erstein, columns = columns)
df_strasbourg = pd.DataFrame(strasbourg, columns = columns)
df_thann_guebwiller = pd.DataFrame(thann_guebwiller, columns = columns)


df_altkirch.to_csv('/home/noil/code/python/monuments3/calques/Altkirch.csv')
df_colmar_ribeauville.to_csv('/home/noil/code/python/monuments3/calques/Colmar-Ribeauvillé.csv')
df_haguenau_wissembourg.to_csv('/home/noil/code/python/monuments3/calques/Haguenau-Wissembourg.csv')
df_molsheim.to_csv('/home/noil/code/python/monuments3/calques/Molsheim.csv')
df_mulhouse.to_csv('/home/noil/code/python/monuments3/calques/Mulhouse.csv')
df_saverne.to_csv('/home/noil/code/python/monuments3/calques/Saverne.csv')
df_selestat_erstein.to_csv('/home/noil/code/python/monuments3/calques/Sélestat-Erstein.csv')
df_strasbourg.to_csv('/home/noil/code/python/monuments3/calques/Strasbourg.csv')
df_thann_guebwiller.to_csv('/home/noil/code/python/monuments3/calques/Thann-Guebwiller.csv')
