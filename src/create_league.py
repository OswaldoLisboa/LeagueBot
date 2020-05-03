import json
import pandas as pd
import numpy as np

DIVISIONS = {
    1:"1st Division",
    2:"2nd Division",
    3:"3rd Division",
    4:"4th Division",
    5:"5th Division",
    6:"6th Division",
    7:"7th Division",
    8:"8th Division",
    9:"9th Division",
    10:"10th Division",
    11:"11th Division"
}


def json_maker(csv_file, json_file):
    """
    Read a csv file with the infotmation of the teams and create a
    json file with the information.
    """
    df = pd.read_csv(csv_file)
    teams = {}

    for i in range(1, len(DIVISIONS.keys()) + 1):
        teams[DIVISIONS[i]] = {}

    for i, row in df.iterrows():
        teams[DIVISIONS[row["Division"]]][row["Code"]] = {}
        teams[DIVISIONS[row["Division"]]][row["Code"]]["Name"] = row["Name"]
        teams[DIVISIONS[row["Division"]]][row["Code"]]["Twitter"] = row["Twitter"]
        teams[DIVISIONS[row["Division"]]][row["Code"]]["Crest"] = row["Crest"]

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(teams, file, ensure_ascii=False)


def df_creator(div, json_file):
    """
    Read a json file and returns a dataframes containing the
    information about the teams of the division passed as argument.
    """
    with open(json_file, "r") as file:
        teams_dic = json.load(file)[DIVISIONS[div]]
        teams_df = pd.DataFrame(
            index=teams_dic.keys(),
            columns=["Name", "Twitter", "Crest"]
        )
        for i in teams_df.index.values:
            teams_df.loc[i]["Name"] = teams_dic[i]["Name"]
            teams_df.loc[i]["Twitter"] = teams_dic[i]["Twitter"]
            teams_df.loc[i]["Crest"] = teams_dic[i]["Crest"]
        return teams_df


def iterator_maker(teams):
    """
    Receives a list with the teams and returns an iterator with the iterator.
    This function was adapted from the user Makis posted on the following stack overflow question:
    https://stackoverflow.com/questions/1037057/how-to-automatically-generate-a-sports-league-iterator
    """
    iterators = []
    mid = int(len(teams) / 2)

    for i in range(len(teams)*2-2):
        # Fisrt half of the season
        if i < len(teams):
            l1 = teams[:mid]
            l2 = teams[mid:]
        # Second Half of the season
        else:
            l2 = teams[:mid]
            l1 = teams[mid:]
        l2.reverse()

        # Switch sides after each round
        if(i % 2 == 1):
            iterators = iterators + [ zip(l1, l2) ]
        else:
            iterators = iterators + [ zip(l2, l1) ]

        teams.insert(1, teams.pop())

    return iterators


def fixture_maker(teams):
    """
    Receives an iterator with the iterator and return a pandas DataFrame
    containing the matchday, the match number in the matchday, the home and away teams, the home and away
    scores (both initialize as 0) and the result (initially is an empty string)
    """
    iterators = iterator_maker(teams)
    fixture_list = []
    for i in range(len(iterators)):
        match = 1
        for j in iterators[i]:
            fixture_list.append([i+1, match, j[0], 0, 0, j[1], ""])
            match += 1

    fixture_df = pd.DataFrame.from_records(
        fixture_list,
        columns=["Matchday", "Match", "Home", "HScore", "AScore", "Away", "Result"]
        )
    return fixture_df
