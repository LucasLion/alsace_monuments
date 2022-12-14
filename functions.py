# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    functions.py                                       :+:         :+:        #
#                                                     +:+ +:+         +:+      #
#    By: llion <llion@student.42mulhouse.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 11:31:27 by llion             #+#    #+#              #
#    Updated: 2022/11/13 18:08:29 by llion         ##########  ###########     #
#                                                                              #
# **************************************************************************** #

from variables import *

def match_ids(id):
    for i in range(len(tab2)):
        try:
            if id == ids_2[i]:
                return i
        except:
            raise Exception(f"ID {id} not found")
            
def match_merimee(merimee):
    for i in range(len(tab4)):
        try:
            if merimee == merimee_2[i]:
                return i
        except:
            raise Exception(f"ID {id} not found")

def get_arrondissement(code):
    for i in range(len(tab3["Code Officiel Commune"])):
        #print(f"code",code)
        #print(f"code tab",tab3['Code Officiel Commune'][i])
        #print(nom_arrondissements[i])
        #print(i)
        if code == tab3["Code Officiel Commune"][i]:
            return nom_arrondissements[i]

def get_id(index):
    id = ids_1[index]
    return id

def get_merimee(index):
    merimee = merimee_1[index]
    return merimee

def get_name(index):
    name = names[index]
    return name

def get_coor_x(index):
    if type(coordinates[index]) is not float:
        co = coordinates[index].split(";")
        coor_x = (co[1].replace(",", "."))
    return coor_x

def get_coor_y(index):
    if type(coordinates[index]) is not float:
        co = coordinates[index].split(";")
        coor_y = (co[2].replace(",", "."))
    return coor_y

def get_status(index):
    if tab2["Dernier ??tat sanitaire d'Agr??g??e"][index]:
        status = tab2["Dernier ??tat sanitaire d'Agr??g??e"][index]
    else:
        status = "Non renseign??"
    return status

def get_damages(index):
    damage = damages[index]
    return damage

def get_comments(index):

    if commentaires[index] == None:
        commentaire = "None"
    else:
        commentaire = commentaires[index]
    return commentaire

def get_address(index):
    if adresses[index] == None:
        address = "Non Renseing??"
    else:
        address = adresses[index]
    return address

def get_precision(index):
    if precisions[index] == None:
        precision = "Non Renseign??"
    else:
        precision = precisions[index]
    return precision

def get_date(index):
    if tab2["Dernier ??tat sanitaire d'Agr??g??e"][index]:
        date = tab2["Date du dernier ??tat sanitaire d'Agr??g??e"][index]
    else:
        date = "Non renseign??"
    return date
