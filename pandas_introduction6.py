# groupby method

from gapminder import gapminder
df = gapminder
print(df.head())

avg_life_exp_by_year = df.groupby('year').lifeExp.mean()
print(avg_life_exp_by_year)


