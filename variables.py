# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    variables.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: llion <llion@student.42mulhouse.fr>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/11/12 11:35:41 by llion             #+#    #+#              #
#    Updated: 2022/11/13 14:30:28 by llion            ###   ########.fr        #
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
print(tab2["Dernier État sanitaire d'Agrégée"])
tab3 = pd.read_excel("tabs/georef-france-commune.ods")

ids_1 = tab1["Id. AgrÉgée"]
ids_2 = tab2["Identifiant Agrégée"]
damages = tab2["Pourcentage de dégradation"]
coordinates = tab1["Coord. géographiques"]
names = tab1['Appellation']
dates = tab2["Date du dernier état sanitaire d'Agrégée"]
commentaires = tab1["Commentaires"]
precisions = tab1["Précision protection"]
code_commune = tab1["Code INSEE"]
nom_arrondissements = tab3["Nom Officiel Arrondissement départemental"]
