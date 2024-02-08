import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

athlete_events = pd.read_csv("olympics/olympics_csv/athlete_events.csv")
country_def = pd.read_csv("olympics/olympics_csv/country_definitions.csv")
# print(athlete_events.info())
# print(country_def.head())

# Analyze and visualize the % of athletes who were female over time.
# The percentage of femail athletes has grown significantly

# Assuming you have a DataFrame named athlete_events
female_ath = (
    athlete_events
    .query("Sex=='F' | Sex=='M'")
    .groupby("Year")
    .agg({"Sex": lambda n: round((n == 'F').mean(),2) * 100})
    .rename(columns={"Sex": "Percentage_Female"})
)

(female_ath
    .plot
    .line(
        title="Percentage of Female Athletes",
        xlabel="Year",
        ylabel="Percentage",
        legend=None
    )
)

# plt.show()


# print(female_ath)

# Compare and contrast the summer and the winter games...

# How many athletes compete? Summer: 222552, Winter: 48564
# How many countries compete? Summer: 1157, Winter: 221
# How many events are there? Summer: 52, Winter: 17

summer_games = (
    athlete_events
    .query("Season == 'Summer'" )
    .agg(total_events=('Sport', 'nunique'))
)

winter_games = (
    athlete_events
    .query("Season == 'Winter'" )
    .agg(total_events=('Sport', 'nunique'))
)

# print(summer_games, "Summer Games")
# print(winter_games, "Winter Games")

# Analyze and visualize country-level trends...
# Which countries send the most athletes to the olympics? US = 17847, France = 11988, Great Britain = 11404
# Do they also tend to win the most medals? For the most part, this statement holds true. The US, France, and GB all come in the top five for most medals of all time.
# How have these trends changed over time? The US has been on time throughout time. However, Great Britain and France reached on all time high in the late 1800s to early 1900's. They slumped in the middle 20th century, but are making a comeback in recent history.

ath_by_country = (
    athlete_events
    .query("Team == 'United States' | Team =='Great Britain' | Team =='France'")
    .dropna(subset=["Medal"])
    .groupby(["Team","Year"])
    .agg({"Name":"count"})
    .sort_values(by=["Year","Name"], ascending=False)
)

print(ath_by_country.head())

# Pivot the DataFrame
ath_by_country_pivot = (
    ath_by_country
    .pivot_table(
        index='Year', columns='Team', values='Name')
    )

# Plot the pivoted DataFrame
(ath_by_country_pivot
    .plot
    .line(
        title="Medal Wins By Country", xlabel="Year", ylabel="Wins"
        )
)



plt.show()