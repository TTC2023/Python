import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

commercials = pd.read_csv("super_bowl_project/super_bowl_csv/superbowl_commercials.csv")
# commercials.info()

# Which brand has had the most Super Bowl commercials? Do they have a distinct style?
# Bud Light has had the most commercials with 62. According to the data it seems they lean more towards "Funny" and "Shows Product Quickly".


brand_commercials = (
    commercials
    .groupby("Brand")
    .agg({"Brand": "count"})
)

bud_light_style = (
    commercials
    .query("Brand == 'Bud Light'")
    .agg({"Funny": "sum", "Shows Product Quickly": "sum", "Patriotic": "sum", "Celebrity": "sum", "Danger": "sum", "Uses Sex": "sum", "Animals": "sum"})
)

# Plotting
# (bud_light_style
#     .plot
#     .barh(
#         title="Bud Light Commercial Styles", 
#         xlabel="Style", 
#         ylabel="Count")
# )
# plt.show()

# How have different characteristics for commercials trended across time?
# The characteristic "Funny" has lost its appeal over time. It reached its peak in the 2000-2010 era. Quickly show products has been relatively consistent over the course of the data. The data shows Celebrity trending upwards over time.


commercials_over_time = (
    commercials
    .groupby("Year")
    .agg({"Funny": "sum", "Shows Product Quickly": "sum", "Patriotic": "sum", "Celebrity": "sum", "Danger": "sum", "Uses Sex": "sum", "Animals": "sum"})
    .sort_values("Year")
)
# print(commercials_over_time.head())

# (commercials_over_time
#     .plot
#     .line(
#         title="Commercial Styles Over Time",
#         xlabel="Year",
#         ylabel="Count",
#         legend=True
#     )
# )
# sns.despine()
# plt.show()

# print(commercials_over_time)

# Can you identify any patterns for the most successful commercials on YouTube? 
# For clarity I defined succcessful as most views. The data shows that the categories "Shows Product Quickly" and "Funny" have the most success on YT. They are clear outliers in the data.
funny_yt_views = (
    commercials
    .dropna(subset=['Youtube Views'])  
    .query("Funny == True")
    .groupby("Funny")
    .agg({"Youtube Views": "sum"})
)

quickly_yt_views = (
    commercials
    .dropna(subset=['Youtube Views']) 
    .query("`Shows Product Quickly` == True") 
    .groupby("Shows Product Quickly")
    .agg({"Youtube Views": "sum"})
)

patriotic_yt_views = (
    commercials
    .dropna(subset=['Youtube Views'])  
    .query("Patriotic == True")
    .groupby("Patriotic")
    .agg({"Youtube Views": "sum"})
)

danger_yt_views = (
    commercials
    .dropna(subset=['Youtube Views']) 
    .query("Danger == True") 
    .groupby("Danger")
    .agg({"Youtube Views": "sum"})
)

sex_yt_views = (
    commercials
    .dropna(subset=['Youtube Views'])  
    .query("`Uses Sex` == True")
    .groupby("Uses Sex")
    .agg({"Youtube Views": "sum"})
)

animals_yt_views = (
    commercials
    .dropna(subset=['Youtube Views']) 
    .query("Animals == True") 
    .groupby("Animals")
    .agg({"Youtube Views": "sum"})
)

celebrity_yt_views = (
    commercials
    .dropna(subset=['Youtube Views'])  
    .query("Celebrity == True")
    .groupby("Celebrity")
    .agg({"Youtube Views": "sum"})
)

combined_yt_df = (
    pd.concat([funny_yt_views, quickly_yt_views, patriotic_yt_views, danger_yt_views,
               sex_yt_views, animals_yt_views, celebrity_yt_views],
               keys=['Funny', 'Shows Product Quickly', 'Patriotic', 'Danger', 'Uses Sex', 'Animals', 'Celebrity'])
    .sort_values("Youtube Views", ascending=False)
)

# print(combined_yt_df)

# Which characteristics are paired most often? Can you find any unusual combinations?
# The most common pairs would be "Funny" and "Shows Product Quickly". An unusual combination that occurred often is Funny, Shows Product Quickly and Danger. 


characteristics_columns = ['Funny', 'Shows Product Quickly', 'Patriotic', 'Celebrity', 'Danger', 'Animals', 'Uses Sex']
commercials_bin = commercials[characteristics_columns].astype(int)

commercials_bin['Combination'] = commercials_bin.apply(lambda row: ''.join(row.astype(str)), axis=1)

combination_counts = commercials_bin['Combination'].value_counts().reset_index()
combination_counts.columns = ['Combination', 'Count']

print(combination_counts)