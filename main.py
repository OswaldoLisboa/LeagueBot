import sys
import pandas as pd
from src import create_league, run_league, generate_messages

if __name__ == "__main__":

    csv_file = sys.argv[1]
    json_file = csv_file.split(".")[0] + ".json"

    create_league.json_maker(csv_file, json_file)
    teams = []
    fixtures = []
    for i in create_league.DIVISIONS.keys():
        te = create_league.df_creator(i, json_file)
        fx = create_league.fixture_maker(list(te.index))
        fx = run_league.generate_scores(fx)
        teams.append(te)
        fixtures.append(fx)

    messages = pd.DataFrame(columns = ["TYPE", "DIV", "MD", "GM", "MSG"])
    for i in range(len(create_league.DIVISIONS.keys())):
        for j in range(int(fixtures[i].tail(1)["Matchday"])):
            for k in range(len(teams[i].index) // 2):
                match = fixtures[i].loc[(fixtures[i]["Matchday"] == j + 1) & (fixtures[i]["Match"] == k + 1)]
                match_msg = generate_messages.generate_match_msg(create_league.DIVISIONS[i+1], teams[i], match, j+1, k+1)
                # messages = messages.append({"TYPE":"1 - Match", "DIV":i+1, "MD":j+1, "GM":k+1,"MSG":match_msg}, ignore_index=True)
                # print(generate_messages.generate_match_msg(create_league.DIVISIONS[i+1], teams[i], match, j+1, k+1))
                if (k + 1 != len(teams[i].index) // 2):
                    next_match = fixtures[i].loc[(fixtures[i]["Matchday"] == j + 1) & (fixtures[i]["Match"] == k + 2)]
                    next_match_msg = generate_messages.generate_next_match_msg(create_league.DIVISIONS[i+1], teams[i], next_match, j+1, k+1)
                    # messages = messages.append({"TYPE":"2 - Next Match", "DIV":i+1, "MD":j+1, "GM":k+1,"MSG":next_match_msg}, ignore_index=True)
                    # print(generate_messages.generate_next_match_msg(create_league.DIVISIONS[i+1], teams[i], next_match, j+1, k+1))
            standings_msg = generate_messages.generate_standings_msg(create_league.DIVISIONS[i+1], j+1)
            # messages = messages.append({"TYPE":"3 - Standings", "DIV":i+1, "MD":j+1, "GM":100,"MSG":standings_msg}, ignore_index=True)
            # print(generate_messages.generate_standings_msg(create_league.DIVISIONS[i+1], j+1))
            if (j + 1 != int(fixtures[i].tail(1)["Matchday"])):
                next_matchday_msg = generate_messages.generate_next_matchday_msg(create_league.DIVISIONS[i+1], j+2)
                # messages = messages.append({"TYPE":"4 - Next Matchday", "DIV":i+1, "MD":j+1, "GM":100,"MSG":next_matchday_msg}, ignore_index=True)
                # print(generate_messages.generate_next_matchday_msg(create_league.DIVISIONS[i+1], j+2))
        final_standings = run_league.generate_standings(j+1, fixtures[i], teams[i])
        if i + 1 != len(create_league.DIVISIONS.keys()):
            relegated = teams[i].loc[final_standings.tail(3).index]
            relegated_msg = generate_messages.generate_relegated_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i+2], relegated)
            messages = messages.append({"TYPE":"5 - Relegated", "DIV":i+1, "MD":j+1, "GM":100,"MSG":relegated_msg}, ignore_index=True)
            # print(generate_messages.generate_relegated_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i+2], relegated))
        if i != 0:
            promoted = teams[i].loc[final_standings.head(3).index]
            promoted_msg = generate_messages.generate_promoted_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i], promoted)
            messages = messages.append({"TYPE":"6 - Promoted", "DIV":i+1, "MD":j+1, "GM":100,"MSG":promoted_msg}, ignore_index=True)
            # print(generate_messages.generate_promoted_msg(create_league.DIVISIONS[i+1], create_league.DIVISIONS[i], promoted))
        champion = teams[i].loc[final_standings.head(1).index[0]]
        champion_msg = generate_messages.generate_champion_msg(create_league.DIVISIONS[i+1], champion)
        messages = messages.append({"TYPE":"7 - Champions", "DIV":i+1, "MD":j+1, "GM":100,"MSG":champion_msg}, ignore_index=True)
        # print(generate_messages.generate_champion_msg(create_league.DIVISIONS[i+1], champion))
    messages = messages.sort_values(["MD", "GM", "DIV", "TYPE"], ascending=True)
    messages.to_csv("data/messages.csv", index=False)
