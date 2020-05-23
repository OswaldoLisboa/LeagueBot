"""
Read a csv file and transform it into a DataFrame.
Then it reads through all rows of the dataframe and tweets its message and image
acording schedule.
"""


from src import twitter
import time
import sys
import datetime as dt
import pandas as pd


STARTTIME = dt.datetime.now()


def str_to_timedelta(str):
    """
    Convert a string formated as "day,hour,minute" to a datetime.timedelta object
    """
    td_list = str.split(",")

    days = float(td_list[0])
    hours = float(td_list[1])
    minutes = float(td_list[2])

    td = dt.timedelta(days=days, hours=hours, minutes=minutes)

    return td


if __name__ == "__main__":

    csv_file = sys.argv[1]

    schedule = pd.read_csv(csv_file)

    for i, row in schedule.iterrows():
        if row["SENT"] == False:
            row["TIMEDELTA"] = str_to_timedelta(row["TIMEDELTA"])
            while STARTTIME + row["TIMEDELTA"] > dt.datetime.now():
                time.sleep(30)
            twitter.tweet(row["MSG"], "{}.jpg".format(row["PATH"]))
            row["SENT"] = True
            schedule.iloc[i] = row
            schedule.to_csv("data/messages.csv")
            print("Just tweeted {}".format(row["PATH"]))
