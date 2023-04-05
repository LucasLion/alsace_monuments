# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variables.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: llion <llion@student.42mulhouse.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 11:35:41 by llion             #+#    #+#              #
#    Updated: 2023/04/05 19:01:06 by llion            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd

AC = []
ED = []
KB = []
LM = []
MHC = []
PC = []
RRM = []
TG = []
UDAP = []

pers1 = pd.read_excel("personal_tabs/AC_BilanSanitaire.xlsx")
pers2 = pd.read_excel("personal_tabs/ED_BilanSanitaire.xlsx")
pers3 = pd.read_excel("personal_tabs/KB_BilanSanitaire.xlsx")
pers4 = pd.read_excel("personal_tabs/LM_BilanSanitaire.xlsx")
pers5 = pd.read_excel("personal_tabs/MHC_BilanSanitaire.xlsx")
pers6 = pd.read_excel("personal_tabs/PC_BilanSanitaire.xlsx")
pers7 = pd.read_excel("personal_tabs/RRM_BilanSanitaire.xlsx")
pers8 = pd.read_excel("personal_tabs/TG_BilanSanitaire.xlsx")
pers9 = pd.read_excel("personal_tabs/UDAP67_BilanSanitaire.xlsx")

tab1 = pd.read_excel("tabs/liste_up_immeubleLM.ods")
tab2 = pd.read_excel("tabs/liste_bilan_sanitaire.ods")
tab3 = pd.read_excel("tabs/georef-france-commune.ods")
tab4 = pd.read_excel("tabs/merimee-MH-valid.xlsx")

ids_1 = tab1["Id. AgrÉgée"]
ids_2 = tab2["Identifiant Agrégée"]
merimee_1 = tab1["Réf. Mérimée"]
merimee_2 = tab4["REF"]

#damages = tab2["Pourcentage de dégradation"]
coordinates = tab1["Coord. géographiques"]
names = tab1['Appellation']
#dates = tab2["Date du dernier état sanitaire d'Agrégée"]
commentaires = tab1["Commentaires"]
precisions = tab4["PPRO"]
code_commune = tab1["Code INSEE"]
nom_arrondissements = tab3["Nom Officiel Arrondissement départemental"]
adresses = tab1["Adresse"]
