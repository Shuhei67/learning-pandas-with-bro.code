# importe panda et surnomme pd
import pandas as pd

# dictionnaire avec des valeur
calories = {"Day 1" : 1750,
            "Day 2" : 2100,
            "Day 3" : 1700}

# pd.Series() demande a pandas de créer une serie
# Avec les valeur du dictionnaire ci - dessus
# Qui sera stocker dans la variable series
series = pd.Series(calories)

print(series) # affiche ma série
print("-" * 50) # juste séparation éstéthique
print(series[series >= 2000]) # ici par exemple je vérifie si la diet à été respecter