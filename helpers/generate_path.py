import pandas as pd


def generate_match_file_path(div, md, gm, teams, match):
    """
    Generate the route of the match image files.
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
    Generate the route of the next matchday image files.
    """
    file_path = "images/{}/DIV{}MD{}".format(
        folder,
        div,
        md
    )
    return file_path


def generate_champion_promoted_relegated_path(folder, div):
    """
    Generate the route of the champion, promoted or relegated teams image files.
    """
    file_path = "images/{}/DIV{}".format(
        folder,
        div
    )
    return file_path
