import matplotlib.pyplot as plt
import pandas as pd

players = ["Bob", "David", "Zelda", "Link", "Mario"]
# Scores for each player in three rounds
scores = [
    [12, 15, 10],   # Bob
    [20, 18, 25],   # David
    [17, 22, 19],   # Zelda
    [10, 10, 12],   # Link
    [25, 24, 23]    # Mario
]

# Step 1: Calculate totals and means
player_data = []
for i, s in enumerate(scores, start=1):
    total = sum(s)
    mean = total / len(s)
    highest = max(s)
    players = ["Bob", "David", "Zelda", "Link", "Mario"]
    player_data.append({
        "Player": players[i - 1],
        "Total": total,
        "Mean": round(mean, 2),
        "Highest Round Score": highest
    })

# Step 2: Sort by total score (descending)
ranked = sorted(player_data, key=lambda x: x["Total"], reverse=True)

# Step 3: Display rankings
print("Final Rankings:\n")
for rank, pdata in enumerate(ranked, start=1):
    print(f"{rank}. {pdata['Player']} | Total: {pdata['Total']} | Mean: {pdata['Mean']} | Highest Round: {pdata['Highest Round Score']}")

    names = [pdata["Player"] for pdata in ranked]
    scores = [pdata["Total"] for pdata in ranked]

# Step 4: Prepare data for plotting
totals = [pdata["Total"] for pdata in ranked]
names = [pdata["Player"] for pdata in ranked]

# Step 5: Plotting the results
plt.style.use('ggplot')  # Use a ggplot style for better aesthetics

# Create a bar chart
plt.figure(figsize=(8, 5))
plt.bar(names, totals, color="skyblue", edgecolor="black")

# Add labels and title
plt.xlabel("Players")
plt.ylabel("Total Score")
plt.title("Scoreboard Overview")
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

# Bold the Player title in the chart
plt.xlabel("Players", fontweight="bold")
plt.ylabel("Total Score", fontstyle="italic")
plt.title("Scoreboard Overview", fontweight="bold")

# Rounds (x-axis)
rounds = [1, 2, 3]

# Create figure
plt.figure(figsize=(10, 6))

# Plot each player's scores
# Use the original scores list for per-player round scores
original_scores = [
    [12, 15, 10],   # Bob
    [20, 18, 25],   # David
    [17, 22, 19],   # Zelda
    [10, 10, 12],   # Link
    [25, 24, 23]    # Mario
]
for name, player_scores in zip(names, original_scores):
    plt.plot(rounds, player_scores, marker="o", label=name)

# Labels and styling
plt.title("Player Performance Over 3 Rounds")
plt.xlabel("Round Number")
plt.ylabel("Score")
plt.xticks(rounds)
plt.legend(title="Players")
plt.grid(True, linestyle="--", alpha=0.6)

# Display the chart
plt.tight_layout()
plt.show()

# Create a DataFrame from the ranked player data
df = pd.DataFrame(ranked)

# Display the DataFrame
print(df.to_string(index=False)) 
