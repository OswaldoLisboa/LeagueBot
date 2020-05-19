from src import twitter
import time
import sys
import imgkit
import pandas as pd
import datetime as dt

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


def generate_images(row):
    """
    Create a html file with the code passed as argument, then convert it into
    a jpg file and returns the jpg file roue.
    """
    html = "{}.html".format(row["PATH"])
    jpg = "{}.jpg".format(row["PATH"])

    with open(html, "w") as file:
        file.write(row["HTML"])
        file.close()
    options = {'format': 'jpg', 'width': 1024}
    imgkit.from_file(html, jpg, options=options)

    return jpg


if __name__ == "__main__":

    csv_file = sys.argv[1]

    schedule = pd.read_csv(csv_file)

    for i, row in schedule.iterrows():
        if row["SENT"] == False:
            row["TIMEDELTA"] = str_to_timedelta(row["TIMEDELTA"])
            while STARTTIME + row["TIMEDELTA"] > dt.datetime.now():
                time.sleep(30)
            image = generate_images(row)
            twitter.tweet(row["MSG"], image)
            row["SENT"] = True
            schedule.iloc[i] = row
            schedule.to_csv("data/messages.csv")
