
import pandas as pd
from pathlib import Path

inferior = ["Fulham", "Newcastle", "Everton", "Leeds", "Crystal Palace",
            "Nott'm Forest", "Tottenham", "Ipswich", "Hull", "Coventry"]
superior = ["Arsenal", "Man City", "Liverpool", "Chelsea", "Bournemouth", "Sunderland",
            "Brighton", "Brentford", "Man United", "Aston Villa"]

df = pd.read_csv(Path(__file__).parent.parent / "E0.csv")

records = []

for _, row in df.iterrows():

    # Weaker team playing at home
    if row["HomeTeam"] in inferior and row["AwayTeam"] in superior:
        records.append({
            "team": row["HomeTeam"],
            "location": "Home",
            "result": "Avoided Defeat" if row["FTHG"] >= row["FTAG"] else "Loss",
            "shots": row["HS"],
            "shots_on_target": row["HST"],
            "shots_conceded": row["AS"],
            "goals_scored": row["FTHG"],
            "goals_conceded": row["FTAG"],
            "xg": row["HxG"],
            "xg_conceded": row["AxG"],
            "fouls": row["HF"],
            "corners": row["HC"]
        })

    # Weaker team playing away
    elif row["AwayTeam"] in inferior and row["HomeTeam"] in superior:
        records.append({
            "team": row["AwayTeam"],
            "location": "Away",
            "result": "Avoided Defeat" if row["FTAG"] >= row["FTHG"] else "Loss",
            "shots": row["AS"],
            "shots_on_target": row["AST"],
            "shots_conceded": row["HS"],
            "goals_scored": row["FTAG"],
            "goals_conceded": row["FTHG"],
            "xg": row["AxG"],
            "xg_conceded": row["HxG"],
            "fouls": row["AF"],
            "corners": row["AC"]
        })

data = pd.DataFrame(records)

# Calculate additional attacking statistics
data["shot_accuracy"] = (
    data["shots_on_target"] / data["shots"].replace(0, float("nan"))
)

data["xg_per_shot"] = (
    data["xg"] / data["shots"].replace(0, float("nan"))
)

# Compare performances
metrics = [
    "shots",
    "shots_on_target",
    "shots_conceded",
    "xg",
    "xg_conceded",
    "fouls",
    "corners",
    "shot_accuracy",
    "xg_per_shot"
]

print("\nWINNING STRATEGIES ANALYSIS")
print("\nNumber of matches:")
print(data["result"].value_counts())

print("\nAverage statistics by result:")
print(data.groupby("result")[metrics].mean().round(3).T)

# Save results for later visualizations
data.to_csv(Path(__file__).with_name("winning_strategies_data.csv"), index=False)


print("\nHOME VS AWAY PERFORMANCE")

print(data.groupby("location").agg(
    matches=("result", "size"),
    shots=("shots", "mean"),
    shots_conceded=("shots_conceded", "mean"),
    xg=("xg", "mean"),
    xg_conceded=("xg_conceded", "mean"),
    avoid_defeat_rate=("result", lambda x: (x == "Avoided Defeat").mean())
).round(3))