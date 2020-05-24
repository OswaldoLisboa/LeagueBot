"""
Create the messages to be tweeted and modifies the json file after one season.
"""


import sys
import pandas as pd
import json
from helpers import create_league, run_league, generate_messages, generate_html, generate_path

def initialize_league(json_file):
    """
    Reads a json file and return two lists: one containing the dataframes of
    the teams in each division, and the other containing the fixtures of each division.
    """
    teams = {}
    fixtures = []
    for i in create_league.DIVISIONS.keys():
        te = create_league.df_creator(i, json_file)
        fx = create_league.fixture_maker(list(te.index))
        fx = run_league.generate_scores(fx)
        teams[create_league.DIVISIONS[i]] = te
        fixtures.append(fx)
    return teams, fixtures


def generate_schedule_promoted_relegated(teams, fixtures):
    """
    Creates a csv file containing the time, message and image for each tweet.
    It also returns two list of lists containing the promoted and relegated teams.
    """
    messages = pd.DataFrame(columns = ["TYPE", "DIV", "MD", "GM", "MSG", "HTML", "PATH", "TIMEDELTA", "SENT"])
    promotion = []
    relegation = []
    for i in range(len(create_league.DIVISIONS.keys())):
        for j in range(int(fixtures[i].tail(1)["Matchday"])):
            for k in range(len(teams[create_league.DIVISIONS[i+1]].index) // 2):
                match = fixtures[i].loc[(fixtures[i]["Matchday"] == j + 1) & (fixtures[i]["Match"] == k + 1)]
                match_msg = generate_messages.generate_match_msg(create_league.DIVISIONS[i+1], teams[create_league.DIVISIONS[i+1]], match, j+1, k+1)
                match_html = generate_html.generate_match_html(create_league.DIVISIONS[i+1], teams[create_league.DIVISIONS[i+1]], match, j+1, k+1)
                match_file_path = generate_path.generate_match_file_path(i+1, j+1, k+1, teams[create_league.DIVISIONS[i+1]], match)
                messages = messages.append({"TYPE":"1 - Match", "DIV":i+1, "MD":j+1, "GM":k+1,"MSG":match_msg, "HTML":match_html, "PATH":match_file_path, "TIMEDELTA":"{},{},{}".format(j, k*2, i*10), "SENT":False}, ignore_index=True)
            standings = run_league.generate_standings(j+1, fixtures[i], teams[create_league.DIVISIONS[i+1]])
            standings_msg = generate_messages.generate_standings_msg(create_league.DIVISIONS[i+1], j+1)
            standings_html = generate_html.generate_standings_html(standings)
            standings_file_path = generate_path.generate_standings_next_md_path("standings",i+1, j+1)
            messages = messages.append({"TYPE":"2 - Standings", "DIV":i+1, "MD":j+1, "GM":100,"MSG":standings_msg,"HTML":standings_html, "PATH":standings_file_path, "TIMEDELTA":"{},{},{}".format(j, 20, i*10), "SENT":False}, ignore_index=True)
            if (j + 1 != int(fixtures[i].tail(1)["Matchday"])):
                next_matchday = fixtures[i].loc[(fixtures[i]["Matchday"] == j + 2)].loc[:,["Match", "Home", "Away"]]
                next_matchday["-"] = "-"
                next_matchday = next_matchday[["Match", "Home", "-", "Away"]]
                next_matchday_msg = generate_messages.generate_next_matchday_msg(create_league.DIVISIONS[i+1], j+2)
                next_matchday_html = generate_html.generate_next_matchday_html(next_matchday)
                next_matchday_file_path = generate_path.generate_standings_next_md_path("next-matchday",i+1, j+1)
                messages = messages.append({"TYPE":"3 - Next Matchday", "DIV":i+1, "MD":j+1, "GM":100,"MSG":next_matchday_msg,"HTML":next_matchday_html,"PATH":next_matchday_file_path, "TIMEDELTA":"{},{},{}".format(j, 22, i*10), "SENT":False}, ignore_index=True)
        final_standings = run_league.generate_standings(j+1, fixtures[i], teams[create_league.DIVISIONS[i+1]])
        if i + 1 != len(create_league.DIVISIONS.keys()):
            relegated = teams[create_league.DIVISIONS[i+1]].loc[final_standings.tail(3).index]
            relegation.append(relegated)
            relegated_msg = generate_messages.generate_relegated_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i+2], relegated)
            relegated_html = generate_html.generate_relegated_html(create_league.DIVISIONS[i+2], relegated)
            relegated_file_path  = generate_path.generate_champion_promoted_relegated_path("relegated", i+1)
            messages = messages.append({"TYPE":"4 - Relegated", "DIV":i+1, "MD":100, "GM":100,"MSG":relegated_msg,"HTML":relegated_html,"PATH":relegated_file_path, "TIMEDELTA":"{},{},{}".format(38, i*1.5, 0), "SENT":False}, ignore_index=True)
        if i != 0:
            promoted = teams[create_league.DIVISIONS[i+1]].loc[final_standings.head(3).index]
            promotion.append(promoted)
            promoted_msg = generate_messages.generate_promoted_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i], promoted)
            promoted_html = generate_html.generate_promoted_html(create_league.DIVISIONS[i], promoted)
            promoted_file_path  = generate_path.generate_champion_promoted_relegated_path("promoted", i+1)
            messages = messages.append({"TYPE":"5 - Promoted", "DIV":i+1, "MD":100, "GM":100,"MSG":promoted_msg,"HTML":promoted_html,"PATH":promoted_file_path, "TIMEDELTA":"{},{},{}".format(38, 15+((i-1)*1.5), 0), "SENT":False}, ignore_index=True)
        champion = teams[create_league.DIVISIONS[i+1]].loc[final_standings.head(1).index[0]]
        champion_msg = generate_messages.generate_champion_msg(create_league.DIVISIONS[i+1], champion)
        champion_html = generate_html.generate_champion_html(create_league.DIVISIONS[i+1], champion)
        champion_file_path  = generate_path.generate_champion_promoted_relegated_path("champions", i+1)
        messages = messages.append({"TYPE":"6 - Champions", "DIV":i+1, "MD":100, "GM":100,"MSG":champion_msg,"HTML":champion_html,"PATH":champion_file_path, "TIMEDELTA":"{},{},{}".format(38, 30+(i*1.5), 0), "SENT":False}, ignore_index=True)
    messages = messages.sort_values(["MD", "GM", "TYPE", "DIV"], ascending=True)
    messages.to_csv("data/messages.csv", index=False)
    return promotion, relegation


def handle_promotion_delegation(teams):
    """
    Move the promoted teams to the upper divions and the relegated teams
    to the lower division.
    """
    for i in range(len(create_league.DIVISIONS.keys())):
        if i + 1 != len(create_league.DIVISIONS.keys()):
            teams[create_league.DIVISIONS[i+1]] = teams[create_league.DIVISIONS[i+1]].drop(relegation[i].index)
            teams[create_league.DIVISIONS[i+2]] = teams[create_league.DIVISIONS[i+2]].append(relegation[i])
        if i != 0:
            teams[create_league.DIVISIONS[i+1]] = teams[create_league.DIVISIONS[i+1]].drop(promotion[i-1].index)
            teams[create_league.DIVISIONS[i]] = teams[create_league.DIVISIONS[i]].append(promotion[i-1])
    return teams


def update_json(teams, json_file):
    """
    Update the json file after a season.
    """
    for i in create_league.DIVISIONS.keys():
        teams[create_league.DIVISIONS[i]] = json.loads(teams[create_league.DIVISIONS[i]].to_json(orient="index"))
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(teams, file, ensure_ascii=False)


if __name__ == "__main__":

    json_file = sys.argv[1]

    teams, fixtures = initialize_league(json_file)
    promotion, relegation = generate_schedule_promoted_relegated(teams, fixtures)
    teams = handle_promotion_delegation(teams)
    update_json(teams, json_file)
