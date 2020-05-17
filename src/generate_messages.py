import pandas as pd

def generate_match_msg(division, teams, match, matchday, match_number):
    """
    Generate a string containing the match info.
    """
    match_msg = ""
    match_msg += "{} - Matchday {} - Game {}\n\n".format(
        division,
        matchday,
        match_number
    )
    match_msg += "{} {} - {} {}\n\n".format(
        teams.loc[match["Home"]]["Twitter"].iloc[0],
        match["HScore"].iloc[0],
        match["AScore"].iloc[0],
        teams.loc[match["Away"]]["Twitter"].iloc[0]
    )
    match_msg += "#{} #{} #{} #WorldNationsLeagueSimulator".format(
        teams.loc[match["Home"]]["Name"].iloc[0].replace(" ", "").replace(".", "").replace("'", ""),
        teams.loc[match["Away"]]["Name"].iloc[0].replace(" ", "").replace(".", "").replace("'", ""),
        division.replace(" ", "")
    )

    return match_msg


def generate_standings_msg(division, matchday):
    """
    Generate a string that will be tweeted along with the standings image.
    """
    standings_msg = "Standings\n\n{} - Matchday {}\n\n#WorldNationsLeagueSimulator #{}".format(
        division,
        matchday,
        division.replace(" ", "")
    )

    return standings_msg


def generate_next_matchday_msg(division, next_matchday):
    """
    Generate a string that will be tweeted along with the next matchday image.
    """
    next_matchday_msg = "Next Matchday:\n\n{} - Matchday {}\n\n#WorldNationsLeagueSimulator #{}".format(
        division,
        next_matchday,
        division.replace(" ", "")
    )

    return next_matchday_msg


def generate_champion_msg(division, champion):
    """
    Generate a string that will be tweeted along with the champion image of every division.
    """
    champion_msg = "And the winner of the {} is ...\n\n{}!!!\n\nCongratulations.\n\n#{} #{} #WorldNationsLeagueSimulator".format(
        division,
        champion["Twitter"],
        champion["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        division.replace(" ", "")
    )
    return champion_msg


def generate_promoted_msg(promoted_from, promoted_to, promoted_teams):
    """
    Generate a string that will be tweeted along with the promoted image of every division.
    """
    promoted_msg = "The teams promoted to the {} are ...\n\n{}\n{}\n{}\n\nCongratulations!!!\n\n#{} #{} #{} #{} #WorldNationsLeagueSimulator".format(
        promoted_to,
        promoted_teams.iloc[0]["Twitter"],
        promoted_teams.iloc[1]["Twitter"],
        promoted_teams.iloc[2]["Twitter"],
        promoted_teams.iloc[0]["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        promoted_teams.iloc[1]["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        promoted_teams.iloc[2]["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        promoted_from.replace(" ", "")
    )
    return promoted_msg


def generate_relegated_msg(relegated_from, relegated_to, relegated_teams):
    """
    Generate a string that will be tweeted along with the relegated image of every division.
    """
    relegated_msg = "The teams relegated to the {} are ...\n\n{}\n{}\n{}\n\nBetter luck next time.\n\n#{} #{} #{} #{} #WorldNationsLeagueSimulator".format(
        relegated_to,
        relegated_teams.iloc[0]["Twitter"],
        relegated_teams.iloc[1]["Twitter"],
        relegated_teams.iloc[2]["Twitter"],
        relegated_teams.iloc[0]["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        relegated_teams.iloc[1]["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        relegated_teams.iloc[2]["Name"].replace(" ", "").replace(".", "").replace("'", ""),
        relegated_from.replace(" ", "")
    )
    return relegated_msg
