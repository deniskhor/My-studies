import pandas as pd

df = pd.read_csv('learn/pokemon.csv')

# 1. Drop irrelevant columns

df = df.dropna(subset=['Type2'])

print(df.to_string())