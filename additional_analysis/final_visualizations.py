
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv(Path(__file__).with_name("winning_strategies_data.csv"))

# Calculate averages by match outcome
averages = df.groupby("result")[
    ["xg", "xg_conceded", "shots_on_target", "fouls"]
].mean()

metrics = [
    ("xg", "Expected Goals Created"),
    ("xg_conceded", "Expected Goals Conceded"),
    ("shots_on_target", "Shots on Target"),
    ("fouls", "Fouls Committed")
]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

for ax, (column, title) in zip(axes.flat, metrics):
    values = [
        averages.loc["Avoided Defeat", column],
        averages.loc["Loss", column]
    ]

    bars = ax.bar(
        ["Win / Draw", "Loss"],
        values,
        color=["#3179c5", "#e0a04b"],
        width=0.55
    )

    ax.set_title(title, fontweight="bold")
    ax.set_ylim(0, max(values) * 1.25)
    ax.bar_label(bars, fmt="%.2f", padding=3)
    ax.spines[["top", "right"]].set_visible(False)

plt.suptitle(
    "How Lower-Ranked Teams Perform Against Stronger Opponents",
    fontsize=15,
    fontweight="bold"
)

plt.tight_layout()
plt.savefig(Path(__file__).with_name("winning_strategies.png"), dpi=300)
plt.show()
