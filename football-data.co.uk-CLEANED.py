from email.quoprimime import unquote

import pandas as pd

# inferior = Bottom 11-17 from 25/26 + 3 promoted Championship teams
# superior = Top 1-10 from 25/26
inferior = ["Fullham", "Newcastle", "Everton", "Leeds", " Crystal Palace",
            "Nott'm Forest", "Tottenham", "Ipswich", "Hull", "Coventry"]
superior = ["Arsenal", "Man City", "Liverpool", "Chelsea", "Bournemouth", "Sunderland",
            "Brighton", "Brentford", "Man United", "Aston Villa"]

# Save the entirety of useful data in "df"
original = pd.read_csv("E0.csv")
df = original[["HomeTeam", "AwayTeam", "HF", "AF","HY","AY",
               "HR","AR","HS","AS","HST","AST","FTHG","FTAG"]]

# Create two lists: one where equally matched teams play each other, and one where matches are unequal
unequal = []
equal = []
for index, row in df.iterrows():
    if row["HomeTeam"] in superior and row["AwayTeam"] in inferior or row["HomeTeam"] in inferior and row["AwayTeam"] in superior:
       unequal.append(index)
    else:
        equal.append(index)

unequal = df.loc[unequal].reset_index(drop=True)
equal = df.loc[equal].reset_index(drop=True)

# Compute statistics that say something about how teams play when they aren't on equal footing

# Compute the average fouls commited by inferior teams on superior teams
inferior_fouls = []
for index, row in unequal.iterrows():
    if row["HomeTeam"] in inferior:
        inferior_fouls.append(row["HF"])
    else:
        inferior_fouls.append(row["AF"])
inferior_foul_average = round(sum(inferior_fouls) / len(inferior_fouls), 2)

# Compute the average fouls commited on average
equal_fouls = []
for index, row in df.iterrows():
    total_fouls = row["HF"] + row["AF"]
    equal_fouls.append(total_fouls)
foul_average = round(sum(equal_fouls) / len(equal_fouls) / 2, 2)

# Results
print("Inferior teams average", inferior_foul_average, "fouls per game, compared to an average of", foul_average, "fouls per game")










