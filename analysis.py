import pandas as pd

# inferior = Bottom 11-17 from 25/26 + 3 promoted Championship teams
# superior = Top 1-10 from 25/26
inferior = ["Fulham", "Newcastle", "Everton", "Leeds", "Crystal Palace",
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

def mean_for_inferior(col1, col2):
    """
    Use this function to find the mean of a statistic in the context of unequal matchups.
    col1 and col2 should be the corresponding home and away columns.
    """
    values = []
    for index, row in unequal.iterrows():
        if row["HomeTeam"] in inferior:
            values.append(row[col1])
        else:
            values.append(row[col2])
    average = round(sum(values) / len(values), 2)
    return average

# Call the function to compute statistics
inferior_fouls = mean_for_inferior("HF","AF")
inferior_red_cards = mean_for_inferior("HR","AR")
inferior_yellow_cards = mean_for_inferior("HY","AY")

def control_mean(col1, col2):
    """
    Use this function to find the mean of a statistic in the context of equal matchups.
    This function will compute the control values.
    col1 and col2 should be the corresponding home and away columns.
    """
    values = []
    for index, row in equal.iterrows():
        if row["HomeTeam"] in inferior and row["AwayTeam"] in inferior:
            values.append(row[col1] + row[col2])
    average = round(sum(values) / len(values) / 2, 2)
    return average

# Call the function to compute statistics
control_fouls = control_mean("HF", "AF")
control_red_cards = control_mean("HR", "AR")
control_yellow_cards = control_mean("HY", "AY")

# Compute mean goals per match in the context of unequal matches
goals = []
for index, row in unequal.iterrows():
    goals.append(row["FTHG"] + row["FTAG"])
inferior_goals_per_game = round(sum(goals) / len(goals), 2)

# Compute mean total goals per match in the context of equal matches
goals = []
for index, row in equal.iterrows():
    if row["HomeTeam"] in inferior and row["AwayTeam"] in inferior:
        goals.append(row["FTHG"] + row["FTAG"])
control_goals_per_game = round(sum(goals) / len(goals), 2)

# Compute total shot accuracy over all games in the context of unequal matches
shots_taken = []
shots_on_target = []
for index, row in unequal.iterrows():
    if row["HomeTeam"] in inferior:
        shots_taken.append(row["HS"])
        shots_on_target.append(row["HST"])
    else:
        shots_taken.append(row["AS"])
        shots_on_target.append(row["AST"])
inferior_shot_quality = round(sum(shots_on_target) / sum(shots_taken), 4)

# Compute total shot accuracy over all games in the context of equal matches
shots_taken = []
shots_on_target = []
for index, row in equal.iterrows():
    if row["HomeTeam"] in inferior and row["AwayTeam"] in inferior:
        shots_taken.append(row["HS"])
        shots_taken.append(row["AS"])
        shots_on_target.append(row["HST"])
        shots_on_target.append(row["AST"])
control_shot_quality = round(sum(shots_on_target) / sum(shots_taken), 4)

print("Inferior fouls", inferior_fouls, "Control fouls", control_fouls, "Inferior red cards", inferior_red_cards,
      "Control red cards", control_red_cards, "Inferior yellow cards", inferior_yellow_cards,
      "Control yellow cards", control_yellow_cards, "Inferior goals per game", inferior_goals_per_game,
      "Control goals per game", control_goals_per_game, "Inferior shot quality",inferior_shot_quality,
      "Control shot quality",control_shot_quality)


# Investigates how accurate a team is on a match-per-match basis

"""
# Compute inferior team's shot quality against superior teams (Home Shots on Target/Home Shots)
shot_quality = []
for index, row in unequal.iterrows():
    if row["HomeTeam"] in inferior:
        shot_quality.append(row["HST"] / row["HS"])
    else:
        shot_quality.append(row["AST"] / row["AS"])
inferior_shot_quality = round(sum(shot_quality) / len(shot_quality), 4)

# Compute inferior team's shot quality against other inferior teams (Home Shots on Target/Home Shots)
shot_quality = []
for index, row in equal.iterrows():
    if row["HomeTeam"] in inferior and row["AwayTeam"] in inferior:
        shot_quality.append(row["HST"] / row["HS"])
        shot_quality.append(row["AST"] / row["AS"])
control_shot_quality = round(sum(shot_quality) / len(shot_quality), 4)
"""

# Prototype for mean_for_inferior and control_mean
"""
# Compute the average fouls commited by inferior teams on superior teams
inferior_fouls = []
    for index, row in unequal.iterrows():
        if row["HomeTeam"] in inferior:
            inferior_fouls.append(row["HF"])
        else:
            inferior_fouls.append(row["AF"])
    inferior_foul_average = round(sum(inferior_fouls) / len(inferior_fouls), 2)


# Compute the average fouls commited by inferior teams on inferior teams
equal_fouls = []
for index, row in equal.iterrows():
    if row["HomeTeam"] and row["AwayTeam"] in inferior:
        equal_fouls.append(row["AF"] + row["HF"])
foul_average = round(sum(equal_fouls) / len(equal_fouls) / 2, 2)

# Results
# print("Inferior teams average", inferior_foul_average, "fouls per game when playing superior teams,"
      # "compared to an average of", foul_average, "fouls per game when playing other inferior teams")

"""










