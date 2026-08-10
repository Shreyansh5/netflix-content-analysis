import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




df = pd.read_csv("netflix_titles.csv")



# Data exploration

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())



# DATA CLEANING


print("Duplicates:", df.duplicated().sum())

df["date_added"] = pd.to_datetime(
    df["date_added"],
    format="mixed",
    errors="coerce"
)



# Movies vs TV Shows


type_counts = df["type"].value_counts()
print(type_counts)

type_percentage = df["type"].value_counts(normalize=True) * 100
print(type_percentage)



sns.countplot(data=df, x="type")
plt.title("Netflix Content: Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")
plt.tight_layout()

plt.show()


# Top countries

top_countries = (df["country"].value_counts().head(10))
sns.barplot(x=top_countries.values, y= top_countries.index)
plt.title("Top 10 countries by Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.show()


# Top directors

director_df = df.dropna(subset=["director"])
top_directors= director_df["director"].value_counts().head(10)
sns.barplot(
    x= top_directors.values , y= top_directors.index
)
plt.title("Top 10 Directors by Number of Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Director")
plt.tight_layout()
plt.show()


# Top genres

top_genres = (df["listed_in"].str.split(", ").explode().value_counts().head(10))

sns.barplot(
    y= top_genres.index, x= top_genres.values
)
plt.title("Top genres in Netflix")
plt.ylabel("Genre")
plt.xlabel("Number of Titles")
plt.tight_layout()
plt.show()

# Month vs Content

months = df["date_added"].dt.month_name().value_counts()
sns.barplot(
    x= months.values, y = months.index
)
plt.title("Netflix content added by Month")
plt.xlabel("Number of Titles")
plt.ylabel("Month")
plt.tight_layout()
plt.show()


# Release year

yearly_content = df["release_year"].value_counts().sort_index()

sns.lineplot(
    x=yearly_content.index,
    y=yearly_content.values
)

plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()


# Movie vs Tv shows trend line

content_by_year= df.groupby(["release_year","type"]).size().unstack()

sns.lineplot(data=content_by_year)

plt.title("Movies vs TV Shows by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()


# Rating

ratings = df["rating"].value_counts().head(10)

sns.barplot(
    x= ratings.values, y= ratings.index
)

plt.title("Top 10 Netflix Content Ratings")
plt.xlabel("Number of Titles")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()


# Netflix's content library over time

added_year = df.groupby(df["date_added"].dt.year).size()

sns.lineplot(
    data = added_year
)

plt.title("Netflix's content acquisition over years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()


# Common Movie Duration

movies = df[df["type"] == "Movie"].copy()

durations = pd.to_numeric(
    movies["duration"]
    .str.replace(" min", "", regex=False),errors="coerce"
)

print("Average movie duration:", durations.mean())
print("Median movie duration:", durations.median())

sns.histplot(
    data=durations,
    bins=30
)

plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.show()


# TV Show Season Analysis

tv_shows = df[df["type"] == "TV Show"].copy()

seasons = pd.to_numeric(
    tv_shows["duration"]
    .str.replace(" Season", "", regex=False)
    .str.replace("s", "", regex=False), errors= "coerce"
)

print("Average number of seasons:", seasons.mean())
print("Median number of seasons:", seasons.median())

sns.histplot(
    data=seasons,
    bins=10
)

plt.title("Distribution of TV Show Seasons")
plt.xlabel("Number of Seasons")
plt.ylabel("Number of TV Shows")
plt.tight_layout()
plt.show()