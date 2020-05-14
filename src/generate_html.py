from templates import match_template, champion_template, promoted_template, relegated_template, standing_template, next_matchday_template


def generate_match_html(division, teams, match, matchday, match_number):
    """

    """
    html = match_template.template.format(
        division=division,
        matchday=matchday,
        game=match_number,
        home_name=teams.loc[match["Home"]]["Name"].iloc[0],
        home_crest=teams.loc[match["Home"]]["Crest"].iloc[0],
        home_score=match["HScore"].iloc[0],
        home_twitter=teams.loc[match["Home"]]["Twitter"].iloc[0],
        away_score=match["AScore"].iloc[0],
        away_name=teams.loc[match["Away"]]["Name"].iloc[0],
        away_crest=teams.loc[match["Away"]]["Crest"].iloc[0],
        away_twitter=teams.loc[match["Away"]]["Twitter"].iloc[0]
    )
    return html


def generate_standings_html(standings):
    """

    """
    html = standing_template.template.format(
        body = standings.to_html(index=True)
    )
    return html


def generate_next_matchday_html(next_matchday):
    """

    """
    html = next_matchday_template.template.format(
        body = next_matchday.to_html(index=False)
    )
    return html

def generate_champion_html(division, champion):
    """

    """
    html = champion_template.template.format(
        division=division,
        champion_name=champion["Name"],
        champion_crest=champion["Crest"],
        champion_twitter=champion["Twitter"]
    )

    return html


def generate_promoted_html(promoted_to, promoted_teams):
    """

    """
    html = promoted_template.template.format(
        division=promoted_to,
        promoted1_crest_file=promoted_teams.iloc[0]["Crest"],
        promoted2_crest_file=promoted_teams.iloc[1]["Crest"],
        promoted3_crest_file=promoted_teams.iloc[2]["Crest"],
        promoted1_name=promoted_teams.iloc[0]["Name"],
        promoted2_name=promoted_teams.iloc[1]["Name"],
        promoted3_name=promoted_teams.iloc[2]["Name"],
        promoted1_twitter=promoted_teams.iloc[0]["Twitter"],
        promoted2_twitter=promoted_teams.iloc[1]["Twitter"],
        promoted3_twitter=promoted_teams.iloc[2]["Twitter"],
    )
    return html


def generate_relegated_html(relegated_to, relegated_teams):
    """

    """
    html = relegated_template.template.format(
        division=relegated_to,
        relegated1_crest_file=relegated_teams.iloc[0]["Crest"],
        relegated2_crest_file=relegated_teams.iloc[1]["Crest"],
        relegated3_crest_file=relegated_teams.iloc[2]["Crest"],
        relegated1_name=relegated_teams.iloc[0]["Name"],
        relegated2_name=relegated_teams.iloc[1]["Name"],
        relegated3_name=relegated_teams.iloc[2]["Name"],
        relegated1_twitter=relegated_teams.iloc[0]["Twitter"],
        relegated2_twitter=relegated_teams.iloc[1]["Twitter"],
        relegated3_twitter=relegated_teams.iloc[2]["Twitter"],
    )
    return html
