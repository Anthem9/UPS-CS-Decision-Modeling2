\* How_to_visit_Paris? *\
Maximize
OBJ: AC_l'Avenue_des_Champs_Elysées + AT_l'Arc_de_triomphe
 + BS_la_Basilique_de_Sacré_Coeur + CA_les_Catacombes
 + CN_la_Cathédrale_Notre_Dame_de_Paris + CP_le_Centre_Pompidou
 + JT_le_Jardin_des_tuileries + ML_Le_Musée_du_louvre + MO_le_Musée_d'Orsay
 + PC_La_Place_de_la_Concorde + SC_la_Sainte_Chapelle + TE_La_Tour_Eiffel
 + TM_la_Tour_Montparnasse
Subject To
Money_constraint: 9.5 AT_l'Arc_de_triomphe + 8 BS_la_Basilique_de_Sacré_Coeur
 + 10 CA_les_Catacombes + 5 CN_la_Cathédrale_Notre_Dame_de_Paris
 + 10 CP_le_Centre_Pompidou + 12 ML_Le_Musée_du_louvre
 + 11 MO_le_Musée_d'Orsay + 8.5 SC_la_Sainte_Chapelle + 15.5 TE_La_Tour_Eiffel
 + 15 TM_la_Tour_Montparnasse <= 65
Preference1: CN_la_Cathédrale_Notre_Dame_de_Paris - SC_la_Sainte_Chapelle = 0
Time_constraint: 1.5 AC_l'Avenue_des_Champs_Elysées + AT_l'Arc_de_triomphe
 + 2 BS_la_Basilique_de_Sacré_Coeur + 2 CA_les_Catacombes
 + 2 CN_la_Cathédrale_Notre_Dame_de_Paris + 2.5 CP_le_Centre_Pompidou
 + 1.5 JT_le_Jardin_des_tuileries + 3 ML_Le_Musée_du_louvre
 + 2 MO_le_Musée_d'Orsay + 0.75 PC_La_Place_de_la_Concorde
 + 1.5 SC_la_Sainte_Chapelle + 4.5 TE_La_Tour_Eiffel
 + 2 TM_la_Tour_Montparnasse <= 12
Binaries
AC_l'Avenue_des_Champs_Elysées
AT_l'Arc_de_triomphe
BS_la_Basilique_de_Sacré_Coeur
CA_les_Catacombes
CN_la_Cathédrale_Notre_Dame_de_Paris
CP_le_Centre_Pompidou
JT_le_Jardin_des_tuileries
ML_Le_Musée_du_louvre
MO_le_Musée_d'Orsay
PC_La_Place_de_la_Concorde
SC_la_Sainte_Chapelle
TE_La_Tour_Eiffel
TM_la_Tour_Montparnasse
End
