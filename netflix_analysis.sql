-- Netflix Content Analysis

USE netflix;

-- Q1: Movies vs TV Shows

SELECT 
    type,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY type
ORDER BY total_titles DESC;

-- Q2: Top 10 Countries by Number of Titles

SELECT
    country,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE country IS NOT NULL
  AND TRIM(country) <> ''
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;

-- Q3: Top 10 Directors by Number of Titles

SELECT
    director,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE director IS NOT NULL
  AND TRIM(director) <> ''
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;

-- Q4: Most Common Genre Combinations

SELECT
    listed_in AS genre,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE listed_in IS NOT NULL
  AND TRIM(listed_in) <> ''
GROUP BY listed_in
ORDER BY total_titles DESC
LIMIT 10;

-- Q5: Content by Release Year

SELECT
    release_year,
    COUNT(*) AS total_titles
FROM netflix_titles
GROUP BY release_year
ORDER BY release_year;


-- Q6: Most Common Netflix Ratings

SELECT
    rating,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE rating IS NOT NULL
  AND TRIM(rating) <> ''
GROUP BY rating
ORDER BY total_titles DESC
LIMIT 10;


-- Q7: Netflix Content Added by Year

SELECT
    YEAR(STR_TO_DATE(date_added, '%M %e, %Y')) AS added_year,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE date_added IS NOT NULL
  AND TRIM(date_added) <> ''
GROUP BY YEAR(STR_TO_DATE(date_added, '%M %e, %Y'))
ORDER BY added_year;

-- Q8: Average Movie Duration

SELECT
    AVG(
        CAST(
            REPLACE(duration, ' min', '')
            AS DECIMAL(10,2)
        )
    ) AS average_movie_duration
FROM netflix_titles
WHERE type = 'Movie'
  AND duration IS NOT NULL;
  
  
 -- Q9: Average Number of Seasons for TV Shows

SELECT
    AVG(
        CAST(
            REPLACE(
                REPLACE(duration, ' Seasons', ''),
                ' Season', ''
            ) AS DECIMAL(10,2)
        )
    ) AS average_seasons
FROM netflix_titles
WHERE type = 'TV Show'
  AND duration IS NOT NULL;
  
  
  -- Q10: Netflix Content Added by Month

SELECT
    MONTHNAME(STR_TO_DATE(date_added, '%M %e, %Y')) AS added_month,
    COUNT(*) AS total_titles
FROM netflix_titles
WHERE date_added IS NOT NULL
  AND TRIM(date_added) <> ''
GROUP BY MONTH(STR_TO_DATE(date_added, '%M %e, %Y')),
         MONTHNAME(STR_TO_DATE(date_added, '%M %e, %Y'))
ORDER BY total_titles DESC;