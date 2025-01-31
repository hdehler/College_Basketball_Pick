# College Basketball Prediction Model

## Overview
This project is a **College Basketball Prediction Model** that estimates the point spread and total points for a game based on team statistics. The model applies weighted scoring for various performance metrics and accounts for home-court advantage.

## How It Works
1. The program takes two CSV files as input: **home.csv** and **away.csv**.
2. These CSV files must contain team statistics copied from **Sports Reference**.
3. The script calculates a **weighted score** for each team based on various statistical categories.
4. It then adjusts for **home-court advantage** dynamically based on team strength.
5. Finally, it predicts:
   - **Point spread** (how much the home team is expected to win or lose by)
   - **Total points** (the expected combined score of both teams)

## Getting the Data
To fill out `home.csv` and `away.csv`, follow these **not-at-all-extravagant** (but actually easy) steps:

1. Go to [Sports Reference](https://www.sports-reference.com/cbb/).
2. Search for the team you want to analyze.
3. Click on **Roster & Stats**.
4. Scroll down to **Team and Opponent Stats**.
5. Hover over **Share & Export** and select **Get as CSV**.
6. Copy everything **except the ranks**.
7. Paste it into either `home.csv` or `away.csv`, depending on whether the team is playing at home or away.

## Usage
Run the script using the following command:

```sh
python3 cbbPick2.py home.csv away.csv
```

### Example Output:
```
Win margin: Home team (home.csv) is predicted to win by 5.5 points.
Total Points: 145
```

## How It Works (Under the Hood)
The script uses a **weighted formula** for various stats, prioritizing field goal percentage, rebounds, assists, and other key metrics. It then applies a **dynamic home-court advantage adjustment**, making minor tweaks based on team strength.

## Adjusted Weights for Stats
| Stat | Weight |
|------|--------|
| FG% | 0.12 |
| 3P% | 0.12 |
| FT% | 0.08 |
| 2P% | 0.08 |
| TRB | 0.08 |
| ORB | 0.06 |
| DRB | 0.06 |
| AST | 0.08 |
| STL | 0.06 |
| BLK | 0.06 |
| TOV | 0.08 |
| PF  | 0.04 |
| PTS | 0.14 |

## Dependencies
- Python 3
- Pandas (`pip install pandas`)

## Future Improvements
- Automate the CSV data retrieval process.
- Implement machine learning for better predictions.
- Improve home-court advantage adjustments.

## Notes
Yes, manually copying stats into CSV files might seem excessive... but hey, it's not that bad! Plus, it gets you hands-on experience with **real data**. 

Enjoy predicting college basketball games! 🏀

