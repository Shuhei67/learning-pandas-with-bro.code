import pandas as pd

# _________IMPORTATION DE FICHIER CSV OU JSON _____________
#__________________________________________________________

# On stock le contenue de notre fichier .csv dans la variable "df" qui sera notre DataFrame
# Si ça avait été au format .json c'est pareil, juste remplacer par .json
df = pd.read_csv("exemple-importation.csv", index_col="Name") # en ajoutant index_col="Name", je remplace les index (0,1,2,3,...) par les noms 


# ______________________SELECTION__________________________
#__________________________________________________________

# Sélection par colonne
# print(df["Type1"]) # ici j'affiche uniquement les Type1
# print(df["Height"]) # ici j'affiche uniquement la taille
# print(df[["No", "Type1", "Height", "Weight"]]) # La je séléctionne plusieurs critère


# Sélection par ligne
print(df.loc["Mewtwo"])
print(df.loc["Mewtwo", ["Height", "Weight"]]) # pour ajouter des critères