import random
import pandas as pd

HOME_SCORES = [0] * 245 + [1] * 379 + [2] * 219 + [3] * 95 + [4] * 47 + [5] * 8 + [6] * 4 + [7] * 2 + [8] * 1
AWAY_SCORES = [0] * 379 + [1] * 395 + [2] * 168 + [3] * 40 + [4] * 11 + [5] * 5 + [6] * 1 + [7] * 1

def match():
    """
    Simulates a match generating two random numbers inside two lists
    (one for the home team and other for the away team). The home and away scores
    probabilities are based on the scores of the 2019 brazillian league
    (with a few modifications).
    """
    home_score = random.choice(HOME_SCORES)
    away_score = random.choice(AWAY_SCORES)
    return home_score, away_score


def generate_scores(fixture):
    """
    Creates three lists containing the home and away goals of the league,
    as well as the results of the match ("h" for a home win, "a" for a away win
    and "d" for a draw"). Then asigns thes list to its correspondent column
    in the dataframe.
    """
    home_goals = []
    away_goals = []
    results = []
    for i in range(len(fixture.index)):
        h, a = match()
        home_goals.append(h)
        away_goals.append(a)
        if h > a:
            results.append("h")
        elif a > h:
            results.append("a")
        else:
            results.append("d")
    fixture["HScore"] = home_goals
    fixture["AScore"] = away_goals
    fixture["Result"] = results
    return fixture


def generate_standings(matchday, fixture, teams):
    """
    Generate a dataframe with the standing of the matchday passed as argument.
    It also sorts the dataframes.
    """
    standings = pd.DataFrame(
        index=teams.index,
        columns=["PTS", "PLD", "W", "D", "L", "GF", "GA", "GD"]
    )
    for i, row in standings.iterrows():
        home_games = fixture[(fixture["Matchday"] <= matchday) & (fixture["Home"] == i)]
        away_games = fixture[(fixture["Matchday"] <= matchday) & (fixture["Away"] == i)]
        row["W"] = (home_games["Result"] == "h").sum() + (away_games["Result"] == "a").sum()
        row["D"] = (home_games["Result"] == "d").sum() + (away_games["Result"] == "d").sum()
        row["L"] = (home_games["Result"] == "a").sum() + (away_games["Result"] == "h").sum()
        row["GF"] = home_games["HScore"].sum() + away_games["AScore"].sum()
        row["GA"] = home_games["AScore"].sum() + away_games["HScore"].sum()
        row["PTS"] = row["W"]*3 + row["D"]
        row["GD"] = row["GF"] - row["GA"]
        row["PLD"] = row["W"] + row["D"] + row["L"]
    standings =  standings.sort_values(["PTS", "GD", "GF"], ascending=False)
    return standings
