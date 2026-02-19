# Investigating-Netflix-Movies

## Overview

This project performs exploratory data analysis (EDA) on the Netflix Movies and TV Shows dataset, with a special focus on movies released in the 1990s. Using Python, pandas, and matplotlib, we analyze the characteristics of 90s movies available on Netflix to gain insights for a production company specializing in nostalgic styles.

## Dataset

The dataset used is `netflix_data.csv`, containing the following columns:

| Column         | Description                                  |
|----------------|----------------------------------------------|
| show_id        | The ID of the show                           |
| type           | Type of show (Movie/TV Show)                 |
| title          | Title of the show                            |
| director       | Director of the show                         |
| cast           | Cast of the show                             |
| country        | Country of origin                            |
| date_added     | Date added to Netflix                        |
| release_year   | Year of Netflix release                      |
| duration       | Duration of the show in minutes              |
| description    | Description of the show                      |
| genre          | Show genre                                   |

## Steps and Analysis

1. **Load Data**  
   The dataset is loaded using pandas:
   ```python
   import pandas as pd
   netflix_df = pd.read_csv("netflix_data.csv")
   ```

2. **Filter for 1990s Movies**  
   Select all movies released between 1990 and 1999:
   ```python
   import numpy as np
   ind_90s = np.logical_and(netflix_df["release_year"] >= 1990, netflix_df["release_year"] < 2000)
   netflix_df_90s = netflix_df[ind_90s]
   netflix_df_mov_90s = netflix_df_90s[netflix_df_90s["type"] == "Movie"]
   ```

3. **Analyze Duration Distribution**  
   Plot the distribution of movie durations for 90s movies:
   ```python
   import matplotlib.pyplot as plt
   dur_90s = netflix_df_mov_90s["duration"]
   plt.hist(dur_90s, bins=30)
   plt.xlabel("Duration")
   plt.ylabel("Frequency")
   plt.show()
   ```

4. **Most Common Duration**  
   Determine the mode (most common value) of movie durations:
   ```python
   duration = dur_90s.mode()[0]
   print(duration)  # Output: 94
   ```

5. **Action Movies with Short Durations**  
   Analyze how many action movies from the 1990s are shorter than 90 minutes:
   ```python
   action_mov_90s = netflix_df_mov_90s[netflix_df_mov_90s["genre"] == "Action"]
   action_mov_90s_dur = action_mov_90s["duration"]
   short_movie_count = sum(dur < 90 for dur in action_mov_90s_dur)
   print(short_movie_count)  # Output: 7
   ```

## Key Findings

- There are **183 movies** from the 1990s in the Netflix dataset.
- The **most common duration** for 90s movies on Netflix is **94 minutes**.
- There are **7 action movies** from the 1990s with a runtime of less than 90 minutes.

## How to Run

1. Place `netflix_data.csv` in your working directory.
2. Run the analysis scripts provided in a Jupyter Notebook or Python environment.
3. Install dependencies if needed:
   ```bash
   pip install pandas matplotlib numpy
   ```

## Further Exploration

- Explore trends by genre, director, or country.
- Compare 90s movies to other decades.
- Investigate cast and crew patterns for nostalgic or cult classics.

---

**Author:**  
HarshShinde0
