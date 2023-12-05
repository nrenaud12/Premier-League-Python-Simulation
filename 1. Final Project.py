#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import numpy as np


# In[5]:


teams_data = {
    "Arsenal": 0.7,
    "Aston Villa": 0.5,
    "Bournemouth": 0.3,
    "Brentford": 0.4,
    "Brighton": 0.5,
    "Burnley": 0.2,
    "Chelsea": 0.5,
    "Crystal Palace": 0.25,
    "Everton": 0.25,
    "Fulham": 0.2,
    "Liverpool": 0.7,
    "Luton Town": 0.2,
    "Manchester City": 0.75,
    "Manchester United": 0.5,
    "Newcastle": 0.7,
    "Nottingham Forest": 0.25,
    "Sheffield Utd": 0.2,
    "Tottenham": 0.7,
    "West Ham": 0.5,
    "Wolves": 0.4,
}

teams = list(teams_data.keys())


# In[6]:


def simulate_match(team1, team2):
    skill_diff = teams_data[team1] - teams_data[team2]
    win_probability = 1 / (1 + np.exp(-skill_diff / 0.1))
    
    goal_range = range(6) 
    home_goals = random.choices(goal_range, weights=[1 - win_probability] + [win_probability] * 5)[0]
    away_goals = random.choices(goal_range, weights=[1 - (1 - win_probability)] + [win_probability] * 5)[0]


    return home_goals, away_goals


# In[7]:


# Simulate a season with skill adjustments
def simulate_season():
    standings = {team: {"points": 0, "goal_difference": 0, "wins": 0, "draws": 0, "losses": 0} for team in teams}

    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                home_goals, away_goals = simulate_match(home_team, away_team)
                standings[home_team]["goal_difference"] += home_goals - away_goals
                standings[away_team]["goal_difference"] += away_goals - home_goals

                if home_goals > away_goals:
                    standings[home_team]["points"] += 3
                    standings[home_team]["wins"] += 1
                    standings[away_team]["losses"] += 1
                elif home_goals == away_goals:
                    standings[home_team]["points"] += 1
                    standings[away_team]["points"] += 1
                    standings[home_team]["draws"] += 1
                    standings[away_team]["draws"] += 1
                else:
                    standings[away_team]["points"] += 3
                    standings[home_team]["losses"] += 1
                    standings[away_team]["wins"] += 1

    return standings


# In[17]:


# Print final standings
def print_standings(standings):
    sorted_standings = sorted(standings.items(), key=lambda x: (x[1]["points"], x[1]["goal_difference"]), reverse=True)

    print("| TEAM                | POINTS | WINS | DRAWS | LOSSES | GOAL DIFFERENCE |")
    print("|---------------------|--------|------|-------|--------|-----------------|")

    for team, stats in sorted_standings:
        print(f"| {team}{' ' * (20- len(team))}|  {stats['points']}{' ' * (6 - len(str(stats['points'])))}|"
              f" {stats['wins']}{' ' * (4 - len(str(stats['wins'])))} |  {stats['draws']}{' ' * (5 - len(str(stats['draws'])))}|"
              f"  {stats['losses']}{' ' * (6 - len(str(stats['losses'])))}|  {stats['goal_difference']}{' ' * (15 - len(str(stats['goal_difference'])))}|")


# In[18]:


def print_results(standings):
    
    print("MATCH RESULTS:")
    for home_team in teams:
        print("")
        print("----------------------------------------")
        print(f"{home_team}'s home games: ")
        print("----------------------------------------")
        for away_team in teams:
            if home_team != away_team:
                home_goals, away_goals = simulate_match(home_team, away_team)
                print(f"{home_team} vs {away_team}: {home_goals} - {away_goals}")


# In[20]:


final_standings = simulate_season()
print_standings(final_standings)


# In[21]:


print_results(final_standings)

