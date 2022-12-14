# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variables.py                                       :+:         :+:        #
#                                                     +:+ +:+         +:+      #
#    By: llion <llion@student.42mulhouse.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 11:35:41 by llion             #+#    #+#              #
#    Updated: 2022/11/13 18:15:06 by llion         ##########  ###########     #
#                                                                              #
# **************************************************************************** #

import pandas as pd

monuments = []
altkirch = []
colmar_ribeauville = []
haguenau_wissembourg = []
molsheim = []
mulhouse = []
saverne = []
selestat_erstein = []
strasbourg = []
thann_guebwiller = []

tab1 = pd.read_excel("tabs/liste_up_immeubleLM.ods")
tab2 = pd.read_excel("tabs/liste_bilan_sanitaire.ods")
tab3 = pd.read_excel("tabs/georef-france-commune.ods")
tab4 = pd.read_excel("tabs/merimee-MH-valid.xlsx")
#tab4 = pd.read_csv('tabs/merimee-MH-valid.ods', encoding='latin-1', error_bad_lines = False)

ids_1 = tab1["Id. AgrÉgée"]
ids_2 = tab2["Identifiant Agrégée"]
merimee_1 = tab1["Réf. Mérimée"]
merimee_2 = tab4["REF"]

damages = tab2["Pourcentage de dégradation"]
coordinates = tab1["Coord. géographiques"]
names = tab1['Appellation']
dates = tab2["Date du dernier état sanitaire d'Agrégée"]
commentaires = tab1["Commentaires"]
precisions = tab4["PPRO"]
code_commune = tab1["Code INSEE"]
nom_arrondissements = tab3["Nom Officiel Arrondissement départemental"]
adresses = tab1["Adresse"]
