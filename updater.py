# from src import twitter
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
    # print(td_list)

    days = float(td_list[0])
    hours = float(td_list[1])
    minutes = float(td_list[2])

    td = dt.timedelta(days=days, hours=hours, minutes=minutes)

    return td


def generate_images(row):
    """

    """
    html = "{}.html".format(row["PATH"])
    jpg = "{}.jpg".format(row["PATH"])

    with open(html, "w") as file:
        file.write('<meta charset="UTF-8">\n')
        file.write(row["HTML"])
        file.close()
    options = {'format': 'jpg', 'width': 1024, 'disable-smart-width': ''}
    imgkit.from_file(html, jpg, options=options)


if __name__ == "__main__":

    csv_file = sys.argv[1]

    schedule = pd.read_csv(csv_file)

    schedule["TIMEDELTA"] = schedule["TIMEDELTA"].apply(str_to_timedelta)

    for i, row in schedule.iterrows():
        if row["SENT"] == False:
            while STARTTIME + schedule.iloc[i]["TIMEDELTA"] > dt.datetime.now():
                time.sleep(30)
            generate_images(row)
            print(row["MSG"])
            # twitter.tweet(row["MSG"], row["IMG"])
            # row["SENT"] = True
            # schedule.iloc[i] = row
            # schedule.to_csv("schedule.csv")
