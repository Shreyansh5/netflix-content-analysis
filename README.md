# Netflix Content Analysis

An exploratory data analysis of 8,807 Netflix titles using Python,
Pandas, Seaborn, Matplotlib, and MySQL.

## Objective

The goal of this project was to explore Netflix's content catalog
and identify patterns in content types, countries, genres, ratings,
release years, content acquisition, movie durations, and TV show
seasons.

## Tools Used

- Python
- Pandas
- Seaborn
- Matplotlib
- MySQL

## Analysis

The project answers the following questions:

1. What is the distribution of Movies vs TV Shows?
2. Which countries contribute the most content?
3. Which directors have the most titles?
4. What are the most common genres?
5. Which months see the most content additions?
6. Which release years have the most content?
7. How have Movies and TV Shows changed over time?
8. What are the most common content ratings?
9. How has Netflix's content acquisition changed over time?
10. What are the typical movie durations and number of TV show seasons?

## Key Insights

- Movies account for approximately 69.6% of the catalog, while TV Shows account for approximately 30.4%.
- The United States is the largest content contributor, followed by India and the United Kingdom.
- Drama, international content, and comedy are among the most represented categories.
- July has the highest number of content additions in the dataset.
- Netflix's catalog is heavily concentrated around relatively recent releases, particularly the late 2010s.
- Movies remain dominant, while TV Shows show substantial growth over time.
- TV-MA and TV-14 are among the most common content ratings.
- Netflix experienced significant catalog expansion during the late 2010s.
- Most movies fall within the typical feature-film runtime range of roughly 90–120 minutes.
- Most TV Shows have relatively few seasons, with 1–2 seasons being particularly common.

## Project Structure

```text
netflix_project/
│
├── data/
│   └── netflix_titles.csv
│
├── python/
│   └── netflix_analysis.py
│
├── sql/
│   └── netflix_analysis.sql
│
├── insights.txt
└── README.md