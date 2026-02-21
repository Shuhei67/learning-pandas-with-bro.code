# importe pandas et surnomme "pd"
import pandas as pd 

#________________LES SERIES___________________
#_____________________________________________

# dictionnaire avec des valeur
calories = {"Day 1" : 1750,
            "Day 2" : 2100,
            "Day 3" : 1700}

# pd.Series() demande a pandas de créer une serie avec les valeur du dictionnaire
series = pd.Series(calories)

print(series) # affiche ma série
print("-" * 50) # séparation éstéthique
print(series[series >= 2000]) # ici par exemple je vérifie si la diet à été respecter
print("-" * 50)

# en gros serie = juste une colonne, qui a plusieurs formeront une dataFrame


#______________LES DATAFRAMES_________________
#_____________________________________________


data = {"Nom" : ["Tony", "Léo", "Alice"],
        "Age" : [23, 27, 39]
}

# Ici je créer ma DataFrame
df = pd.DataFrame(data, index = ["Employé 1", "Employé 2", "Employé 3"])

# Ajouter colonne
df["Job"] = ["Barman", "Serveur", "Responsable"]

# Ajouter une ligne
new_row = pd.DataFrame([{"Nom" : "Antoine", "Age" : 19, "Job" : "Serveur"}], index = ["Employé 4"])
df = pd.concat([df, new_row]) # Formule pour concaténer la dataframe avec la nouvelle ligne

# Ajouter des lignes
new_rows = pd.DataFrame([{"Nom" : "Kim", "Age" : 25, "Job" : "Barman"},
                        {"Nom" : "Louis", "Age" : 31, "Job" : "Cuisinier"}], index = ["Employé 5", "Employé 6"])
df = pd.concat([df, new_rows]) # comme pour avant mais au pluriel ptdrrrr

print(df) # affichage de la DataFrame