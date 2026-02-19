# Analyzing-TV-Data: Super Bowl Games, Viewership, and Halftime Shows

## Overview

This project explores the spectacle of the Super Bowl by analyzing three main aspects: the games themselves, television viewership and advertising, and the legendary halftime shows. Using data scraped from Wikipedia (covering all 52 Super Bowls through 2018), we combine pandas, matplotlib, and seaborn to answer questions such as:

- What were the most extreme game outcomes in Super Bowl history?
- How does the game's score affect TV viewership?
- How have viewership, TV ratings, and ad cost evolved over time?
- Who are the most prolific halftime show performers?
- Which halftime show acts performed the most songs?

## Datasets

The analysis uses three CSV files:

- `super_bowls.csv` — Game outcomes, teams, scores, venues, dates, and attendance.
- `tv.csv` — TV networks, US viewership, ratings, share, ad costs, and more.
- `halftime_musicians.csv` — Halftime show performers and number of songs performed.

Sample columns:
- `super_bowls.csv`: date, super_bowl, venue, city, state, attendance, team_winner, winning_pts, qb_winner_1, qb_winner_2, coach_winner, team_loser, losing_pts, qb_loser_1, qb_loser_2, coach_loser, combined_pts, difference_pts
- `tv.csv`: super_bowl, network, avg_us_viewers, total_us_viewers, rating_household, share_household, rating_18_49, share_18_49, ad_cost
- `halftime_musicians.csv`: super_bowl, musician, num_songs

## Analysis Steps

### 1. Data Loading and Inspection

- Data is loaded with pandas and visually inspected using `.head()` and `.info()`.
- Missing values in columns like `num_songs` and TV audience breakdowns are noted.

### 2. Combined Points & Point Difference

- A histogram of combined points reveals most Super Bowls are in the 40–50 point range, with outliers for high and low-scoring games.
- Extremes are highlighted (e.g., 75 points in 1995; 16 points in 2019).
- Another histogram shows most games are close, but there are notable blowouts and nail-biters.

### 3. Game Outcomes and Viewership

- The relationship between the game's point difference and TV household share is explored using a scatterplot/regression.
- Results suggest that viewers are less engaged during blowouts, but the effect is weak due to small sample size.

### 4. Viewership, Ratings, and Ad Cost Over Time

- Plots show that viewership rose before ad costs did, suggesting networks were slow to capitalize.
- Ad cost for a 30-second spot is now ~$5 million.

### 5. Halftime Shows: The Evolution

- Early halftime shows were dominated by marching bands and novelty acts.
- Michael Jackson’s Super Bowl XXVII performance in 1993 marked a turning point toward star-studded shows.

### 6. Halftime Show Performers

- The Grambling State University Tiger Marching Band holds the record for most appearances (6).
- Beyoncé, Justin Timberlake, Nelly, and Bruno Mars have each performed twice since 2000.

### 7. Most Songs Performed

- Non-band musicians are filtered and the number of songs per performance is visualized.
- Justin Timberlake (2018) performed the most songs in a single show (11), followed by Diana Ross (10 in 1996).

## Key Findings

- **Most Super Bowls are competitive**, but there have been both high-scoring shootouts and defensive slogs.
- **Blowouts may lead to lower viewership**, but most fans stick around for the halftime show and ads.
- **Viewership increases preceded ad cost spikes**—networks may have lagged in ad pricing.
- **Halftime shows evolved**: From marching bands and magic acts to global pop icons and multi-song medleys.
- **Justin Timberlake performed the most songs** in a single halftime show (11).

## Running This Project

1. Place the CSV files in a `datasets/` directory.
2. Run the Jupyter Notebook or Python script containing the analysis code.
3. Required libraries: `pandas`, `matplotlib`, `seaborn`.

```bash
pip install pandas matplotlib seaborn
```

## Example Code Snippet

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

super_bowls = pd.read_csv('datasets/super_bowls.csv')
tv = pd.read_csv('datasets/tv.csv')
halftime_musicians = pd.read_csv('datasets/halftime_musicians.csv')

plt.hist(super_bowls.combined_pts)
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()
```

## Acknowledgements

- Data: Wikipedia (scraped and cleaned for Super Bowls I–LII)
- Photo: "Left Shark Steals The Show", Katy Perry at Super Bowl XLIX by Huntley Paton (CC BY-SA 2.0)

---

**Author:**  
HarshShinde0
