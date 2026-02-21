import pandas as pd 

data = {"Nom" : ["Tony", "Léo", "Alice"],
        "Age" : [23, 27, 39]
}

# Ici je créer ma DataFrame
df = pd.DataFrame(data, index = ["Employé 1", "Employé 2", "Employé 3"])

# Ajouter colonne
df["Job"] = ["Barman", "Serveur", "Responsable"]

# Ajouter une ligne
new_row = pd.DataFrame([{"Nom" : "Antoine", "Age" : 19, "Job" : "Serveur"}], index = ["Employé 4"])
df = pd.concat([df, new_row])

# Ajouter des lignes
new_rows = pd.DataFrame([{"Nom" : "Kim", "Age" : 25, "Job" : "Barman"},
                        {"Nom" : "Louis", "Age" : 31, "Job" : "Cuisinier"}], index = ["Employé 5", "Employé 6"])
df = pd.concat([df, new_rows])

print(df) # affichage de la DataFrame