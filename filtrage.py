import pandas as pd
df = pd.read_csv("exemple-importation.csv")

tall_pokemon = df[df["Height"] >= 2]

print(tall_pokemon)