"""
Read a csv file with the infotmation of the teams and create a
json file with the information.
"""


import json
import sys
import pandas as pd
from src import create_league


if __name__ == "__main__":

    csv_file = sys.argv[1]
    json_file = csv_file.split(".")[0] + ".json"


    df = pd.read_csv(csv_file)
    teams = {}

    for i in range(1, len(create_league.DIVISIONS.keys()) + 1):
        teams[create_league.DIVISIONS[i]] = {}

    for i, row in df.iterrows():
        teams[create_league.DIVISIONS[row["Division"]]][row["Index"]] = {}
        teams[create_league.DIVISIONS[row["Division"]]][row["Index"]]["Name"] = row["Name"]
        teams[create_league.DIVISIONS[row["Division"]]][row["Index"]]["Twitter"] = row["Twitter"]
        teams[create_league.DIVISIONS[row["Division"]]][row["Index"]]["Crest"] = row["Crest"]

    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(teams, file, ensure_ascii=False)
