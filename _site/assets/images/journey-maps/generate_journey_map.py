import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import textwrap

# Journey stages data
stages = ["Awareness", "Onboarding", "Daily Use", "Appointment\nBooking"]
emotions = [2, 3.5, 4.5, 4]  # Emotional score: 1=frustrated, 5=delighted

actions = [
    "Discovers app via doctor,\nfamily, or app store search\nafter missing a dose",
    "Downloads app, opens it,\nconfigures global reminder\npreferences in minimal setup",
    "Receives reminders, confirms\nmedication taken, checks\nupcoming appointments",
    "Creates appointment event\nusing visual selectors,\nfills in essential details",
]

thoughts = [
    '"Will this app be\neasy enough for me?"',
    '"This setup is quick,\nI only set reminders once"',
    '"The reminder went off\nright on time"',
    '"No more double-booking\nor forgetting specialists"',
]

pain_points = [
    "Handwritten notes get lost,\ntoo many tools, low\nmotivation to search",
    "Unfamiliar screens may\nintimidate low-tech users,\nintegration concerns",
    "Notifications dismissed on\nbad days, hard to respond\nduring busy hours",
    "Past double-bookings,\nneed for straightforward\ninput fields",
]

opportunities = [
    "Simple app store listing,\naccessibility-focused\nmarketing",
    "One-screen onboarding,\nlarge inputs, brief\nwalkthrough",
    "Persistent reminders,\none-tap confirmation,\nvisual progress summary",
    "Visual selectors,\nconflict detection,\nunified calendar view",
]

# Color palette
bg_color = "#1a1a2e"
card_color = "#16213e"
accent_color = "#0f3460"
line_color = "#e94560"
text_color = "#eaeaea"
highlight_color = "#e94560"
stage_colors = ["#e94560", "#f5a623", "#7ed957", "#53a8e2"]

fig, axes = plt.subplots(2, 1, figsize=(18, 16), gridspec_kw={"height_ratios": [1, 3]})
fig.patch.set_facecolor(bg_color)

# --- Top: Emotion curve ---
ax1 = axes[0]
ax1.set_facecolor(bg_color)

x = np.arange(len(stages))
x_smooth = np.linspace(0, len(stages) - 1, 200)
from numpy.polynomial.polynomial import Polynomial
coeffs = np.polyfit(x, emotions, 3)
y_smooth = np.polyval(coeffs, x_smooth)

ax1.fill_between(x_smooth, y_smooth, alpha=0.15, color=line_color)
ax1.plot(x_smooth, y_smooth, color=line_color, linewidth=3, zorder=3)
ax1.scatter(x, emotions, color=line_color, s=120, zorder=4, edgecolors="white", linewidths=2)

emotion_labels = ["Frustrated", "Cautiously\nOptimistic", "Confident", "Reassured"]
for i, (xi, yi, label) in enumerate(zip(x, emotions, emotion_labels)):
    ax1.annotate(label, (xi, yi), textcoords="offset points", xytext=(0, 18),
                 ha="center", fontsize=9, color=text_color, fontweight="bold")

ax1.set_xticks(x)
ax1.set_xticklabels(stages, fontsize=12, fontweight="bold", color=text_color)
ax1.set_yticks([1, 2, 3, 4, 5])
ax1.set_yticklabels(["Low", "", "Neutral", "", "High"], fontsize=9, color="#888")
ax1.set_ylim(0.5, 5.5)
ax1.set_xlim(-0.5, len(stages) - 0.5)
ax1.set_title("User Emotional Journey", fontsize=16, fontweight="bold", color=text_color, pad=15)
ax1.spines[:].set_visible(False)
ax1.tick_params(axis="both", length=0)
ax1.grid(axis="y", color="#333", linestyle="--", alpha=0.4)

# --- Bottom: Detail cards ---
ax2 = axes[1]
ax2.set_facecolor(bg_color)
# Offset columns to the right — just enough to fit the labels
col_offset = 0.55
ax2.set_xlim(-0.95, len(stages) - 1 + col_offset + 0.55)
ax2.set_ylim(-0.5, 5.2)
ax2.axis("off")

row_labels = ["Actions", "Thoughts", "Pain Points", "Opportunities"]
row_data = [actions, thoughts, pain_points, opportunities]
row_icons = ["\u25B6", "\u25CF", "\u25B2", "\u2605"]
row_colors = ["#53a8e2", "#f5a623", "#e94560", "#7ed957"]

card_height = 0.95
card_width = 0.85
y_start = 4.8
row_gap = 0.35

for row_idx, (label, data, icon, color) in enumerate(zip(row_labels, row_data, row_icons, row_colors)):
    y_pos = y_start - row_idx * (card_height + row_gap)
    # Row label outside the grid on the left
    ax2.text(-0.65, y_pos - card_height / 2, f"{icon} {label}", fontsize=11, fontweight="bold",
             color=color, va="center", ha="left")

    for col_idx, text in enumerate(data):
        x_pos = col_idx + col_offset
        rect = mpatches.FancyBboxPatch(
            (x_pos - card_width / 2, y_pos - card_height),
            card_width, card_height,
            boxstyle="round,pad=0.05",
            facecolor=card_color,
            edgecolor=color,
            linewidth=1.2,
            alpha=0.85,
        )
        ax2.add_patch(rect)
        ax2.text(x_pos, y_pos - card_height / 2, text,
                 fontsize=9.5, color=text_color, ha="center", va="center",
                 linespacing=1.4)

# Stage column headers
for i, (stage, color) in enumerate(zip(stages, stage_colors)):
    ax2.text(i + col_offset, y_start + 0.15, stage.replace("\n", " "), fontsize=12, fontweight="bold",
             color=color, ha="center", va="bottom")

plt.tight_layout(pad=1.5)
plt.savefig(
    "/Users/sergioabreo/studio code/pergioa.github.io/assets/images/journey-maps/journey-map.png",
    dpi=200,
    bbox_inches="tight",
    facecolor=bg_color,
)
print("Journey map saved successfully!")
