from analysis import (
    inferior_fouls,
    control_fouls,
    inferior_yellow_cards,
    control_yellow_cards,
    inferior_red_cards,
    control_red_cards,
    inferior_shot_quality,
    control_shot_quality
)

import matplotlib.pyplot as plt

metrics = ["Fouls", "Yellow Cards", "Red Cards", "Shot Accuracy (%)"]

# Define statistics corresponding to stronger and weaker
stronger = [
    inferior_fouls,
    inferior_yellow_cards,
    inferior_red_cards,
    inferior_shot_quality * 100
]

weaker = [
    control_fouls,
    control_yellow_cards,
    control_red_cards,
    control_shot_quality * 100
]

fig, axes = plt.subplots(2, 2, figsize=(11, 8))

for ax, name, a, b in zip(axes.flat, metrics, stronger, weaker):
    bars = ax.bar(
        ["Vs. Stronger", "Vs. Weaker"],
        [a, b],
        color=["#3179c5", "#e0a04b"],
        width=0.55
    )

    ax.set_title(name, fontweight="bold")
    ax.set_ylim(0, max(a, b) * 1.25)
    ax.bar_label(bars, fmt="%.2f", padding=3)
    ax.spines[["top", "right"]].set_visible(False)

plt.suptitle(
    "How Opponent Strength Affects Lower-Ranked Teams",
    fontsize=15,
    fontweight="bold"
)
plt.tight_layout()
plt.savefig("premier_league_analysis.png", dpi=300)
plt.show()