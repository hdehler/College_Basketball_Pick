import pandas as pd
import sys

# Adjusted weights for different stats
STAT_WEIGHTS = {
    'FG%': 0.12,  # Shooting efficiency
    '3P%': 0.12,  # Three-point shooting efficiency
    'FT%': 0.08,  # Free-throw shooting efficiency
    '2P%': 0.08,  # Two-point shooting efficiency
    'TRB': 0.08,  # Total rebounds
    'ORB': 0.06,  # Offensive rebounds
    'DRB': 0.06,  # Defensive rebounds
    'AST': 0.08,  # Assists
    'STL': 0.06,  # Steals
    'BLK': 0.06,  # Blocks
    'TOV': 0.08,  # Turnovers
    'PF': 0.04,   # Personal fouls
    'PTS': 0.14,  # Points scored
    # Lesser emphasis on descriptive stats
    'G': 0.01,    # Games played
    'MP': 0.01,   # Minutes played
    'FG': 0.01,   # Field goals
    'FGA': 0.01,  # Field goal attempts
    '2P': 0.01,   # Two-points field goals
    '2PA': 0.01,  # Two-points field goal attempts
    '3P': 0.01,   # Three-points field goals
    '3PA': 0.01,  # Three-points field goal attempts
    'FT': 0.01,   # Free throws
    'FTA': 0.01   # Free throw attempts
}

HOME_COURT_ADVANTAGE = 4  # Slightly adjusted

def read_and_prepare_data(file_name):
    data = pd.read_csv(file_name)
    team_stats = data.iloc[1]
    return team_stats

def calculate_weighted_score(team_stats):
    weighted_score = 0
    for stat, weight in STAT_WEIGHTS.items():
        if stat in team_stats:
            stat_value = team_stats[stat]
            if isinstance(stat_value, str) and '%' in stat_value:
                value = float(stat_value.strip('%')) / 100
            else:
                value = float(stat_value)
            weighted_score += value * weight
    return weighted_score

def dynamic_home_court_advantage(home_stats, away_stats):
    # Example: Adjust based on team strength (e.g., points scored)
    home_advantage = 3
    if home_stats['PTS'] > away_stats['PTS']:
        home_advantage += 1  # Stronger home team gets more advantage
    else:
        home_advantage -= 1  # Weaker home team gets less advantage
    return home_advantage

def calculate_total_points(home_stats, away_stats):
    # Using average points scored and points allowed for estimation
    average_home_points = float(home_stats['PTS'])
    average_away_points = float(away_stats['PTS'])

    # Assuming 'Opponent PTS' represents the average points allowed by each team's defense
    home_points_allowed = float(home_stats['Opponent PTS']) if 'Opponent PTS' in home_stats else average_home_points
    away_points_allowed = float(away_stats['Opponent PTS']) if 'Opponent PTS' in away_stats else average_away_points

    # Estimate total points as the average of the points scored and points allowed by each team
    estimated_total_points = (average_home_points + average_away_points + home_points_allowed + away_points_allowed) / 2

    return round(estimated_total_points)

def calculate_points(home_stats, away_stats):
    home_court_advantage = dynamic_home_court_advantage(home_stats, away_stats)

    home_score = calculate_weighted_score(home_stats)
    away_score = calculate_weighted_score(away_stats)

    neutral_p = home_score - away_score
    point_diff = -(neutral_p + home_court_advantage)

    point_diff = round(point_diff * 2) / 2
    return "Home team", point_diff

# Read team stats
home_stats = read_and_prepare_data(sys.argv[1])
away_stats = read_and_prepare_data(sys.argv[2])

# Calculate point spread
favored_team, prediction_point_diff = calculate_points(home_stats, away_stats)
predicted_total_points = calculate_total_points(home_stats, away_stats)

print(f"Win margin: {favored_team} ({sys.argv[1]}) is predicted to win by {abs(prediction_point_diff)} points.")
print(f"Total Points: {predicted_total_points}")