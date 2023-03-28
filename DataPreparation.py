import pandas as pd
import numpy as np

data = pd.read_csv("P:\Data Preparation Pandas\Data-preparariton-with-pandas\Data\games.csv")

#[20058 rows x 16 columns] originally

counts = data["opening_name"].value_counts()
to_remove = counts[counts < 3].index

notnull=data.dropna()
#print(notnull)
noduplicates= notnull.drop_duplicates(subset="id", keep=False)
#print(noduplicates)
lessthan4moves=noduplicates.drop(noduplicates[noduplicates['turns'] < 4].index, inplace = False)
#print(lessthan4moves)
lessthan3openings=lessthan4moves[~lessthan4moves.opening_name.isin(to_remove)]
print(lessthan3openings)
#print(lessthan3openings)

lessthan3openings.to_csv('P:\Data Preparation Pandas\Data-preparariton-with-pandas\Data\games_cleaned.csv', index=False)

