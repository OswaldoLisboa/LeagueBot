import pandas as pd


def generate_match_file_path(div, md, gm, teams, match):
    """

    """
    file_path = "images/matches/DIV{}MD{}GM{} - {} vs {}".format(
        div,
        md,
        gm,
        teams.loc[match["Home"]]["Name"].iloc[0],
        teams.loc[match["Away"]]["Name"].iloc[0]
    )
    return file_path


def generate_standings_next_md_path(folder, div, md):
    """

    """
    file_path = "images/{}/DIV{}MD{}".format(
        folder,
        div,
        md
    )
    return file_path


def generate_champion_promoted_relegated_path(folder, div):
    """

    """
    file_path = "images/{}/DIV{}".format(
        folder,
        div
    )
    return file_path
