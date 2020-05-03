import sys
import pandas as pd
import json
from src import create_league, run_league, generate_messages

def initialize_league(json_file):
    """

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

    """
    messages = pd.DataFrame(columns = ["TYPE", "DIV", "MD", "GM", "MSG"])
    promotion = []
    relegation = []
    for i in range(len(create_league.DIVISIONS.keys())):
        for j in range(int(fixtures[i].tail(1)["Matchday"])):
            for k in range(len(teams[create_league.DIVISIONS[i+1]].index) // 2):
                match = fixtures[i].loc[(fixtures[i]["Matchday"] == j + 1) & (fixtures[i]["Match"] == k + 1)]
                match_msg = generate_messages.generate_match_msg(create_league.DIVISIONS[i+1], teams[create_league.DIVISIONS[i+1]], match, j+1, k+1)
                messages = messages.append({"TYPE":"1 - Match", "DIV":i+1, "MD":j+1, "GM":k+1,"MSG":match_msg}, ignore_index=True)
            standings_msg = generate_messages.generate_standings_msg(create_league.DIVISIONS[i+1], j+1)
            messages = messages.append({"TYPE":"2 - Standings", "DIV":i+1, "MD":j+1, "GM":100,"MSG":standings_msg}, ignore_index=True)
            if (j + 1 != int(fixtures[i].tail(1)["Matchday"])):
                next_matchday_msg = generate_messages.generate_next_matchday_msg(create_league.DIVISIONS[i+1], j+2)
                messages = messages.append({"TYPE":"3 - Next Matchday", "DIV":i+1, "MD":j+1, "GM":100,"MSG":next_matchday_msg}, ignore_index=True)

        final_standings = run_league.generate_standings(j+1, fixtures[i], teams[create_league.DIVISIONS[i+1]])
        if i + 1 != len(create_league.DIVISIONS.keys()):
            relegated = teams[create_league.DIVISIONS[i+1]].loc[final_standings.tail(3).index]
            relegation.append(relegated)
            relegated_msg = generate_messages.generate_relegated_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i+2], relegated)
            messages = messages.append({"TYPE":"4 - Relegated", "DIV":i+1, "MD":100, "GM":100,"MSG":relegated_msg}, ignore_index=True)
        if i != 0:
            promoted = teams[create_league.DIVISIONS[i+1]].loc[final_standings.head(3).index]
            promotion.append(promoted)
            promoted_msg = generate_messages.generate_promoted_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i], promoted)
            messages = messages.append({"TYPE":"5 - Promoted", "DIV":i+1, "MD":100, "GM":100,"MSG":promoted_msg}, ignore_index=True)
        champion = teams[create_league.DIVISIONS[i+1]].loc[final_standings.head(1).index[0]]
        champion_msg = generate_messages.generate_champion_msg(create_league.DIVISIONS[i+1], champion)
        messages = messages.append({"TYPE":"6 - Champions", "DIV":i+1, "MD":100, "GM":100,"MSG":champion_msg}, ignore_index=True)
    messages = messages.sort_values(["MD", "GM", "TYPE", "DIV"], ascending=True)
    messages.to_csv("data/messages.csv", index=False)
    return promotion, relegation


def handle_promotion_delegation(teams):
    """

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
