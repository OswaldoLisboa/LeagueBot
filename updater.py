from src import twitter
import time
import sys
import imgkit
import pandas as pd
import datetime as dt


STARTTIME = dt.datetime.now()


def str_to_timedelta(str):
    """

    """
    td_list = str.split(",")

    days = float(td_list[0])
    hours = float(td_list[1])
    minutes = float(td_list[2])

    td = dt.timedelta(days=days, hours=hours, minutes=minutes)

    return td


def generate_images(row):
    """

    """
    jpg = "{}.jpg".format(row["PATH"])

    options = {'format': 'jpg', 'width': 1024, 'disable-smart-width': ''}
    imgkit.from_string(row["HTML"], jpg, options=options)


if __name__ == "__main__":

    csv_file = sys.argv[1]

    schedule = pd.read_csv(csv_file)

    schedule["TIMEDELTA"] = schedule["TIMEDELTA"].apply(str_to_timedelta)

    for i, row in schedule.iterrows():
        if row["SENT"] == False:
            while STARTTIME + schedule.iloc[i]["TIMEDELTA"] > dt.datetime.now():
                time.sleep(30)
            generate_images(row)
            twitter.tweet(row["MSG"], row["IMG"])
            row["SENT"] = True
            schedule.iloc[i] = row
            schedule.to_csv("schedule.csv")
