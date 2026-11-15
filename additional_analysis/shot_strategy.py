
import pandas as pd
from pathlib import Path

# Load match data
file = Path(__file__).with_name("winning_strategies_data.csv")
df = pd.read_csv(file)

# Calculate points earned in each match
# Win = 3, Draw = 1, Loss = 0
df["points"] = 0

df.loc[df["goals_scored"] == df["goals_conceded"], "points"] = 1
df.loc[df["goals_scored"] > df["goals_conceded"], "points"] = 3

print("SHOT STRATEGY ANALYSIS")
print("Number of matches:", len(df))

# Compare teams taking more versus fewer shots
median_shots = df["shots"].median()

df["shot_volume"] = "Low Volume"
df.loc[df["shots"] > median_shots, "shot_volume"] = "High Volume"

print("\nLOW VS HIGH SHOT VOLUME")
print(df.groupby("shot_volume").agg(
    matches=("points", "size"),
    average_points=("points", "mean"),
    average_xg_per_shot=("xg_per_shot", "mean"),
    average_goals=("goals_scored", "mean")
).round(3))

# Compare teams creating higher versus lower quality chances
median_quality = df["xg_per_shot"].median()

df["shot_quality"] = "Low Quality"
df.loc[df["xg_per_shot"] > median_quality, "shot_quality"] = "High Quality"

print("\nLOW VS HIGH SHOT QUALITY")
print(df.groupby("shot_quality").agg(
    matches=("points", "size"),
    average_shots=("shots", "mean"),
    average_points=("points", "mean"),
    average_goals=("goals_scored", "mean")
).round(3))

# Compare shot quantity and quality together
print("\nSHOT QUALITY VS QUANTITY")
print(df.groupby(["shot_volume", "shot_quality"]).agg(
    matches=("points", "size"),
    average_points=("points", "mean"),
    average_goals=("goals_scored", "mean")
).round(3))
