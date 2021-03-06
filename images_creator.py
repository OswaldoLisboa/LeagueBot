"""
Read a csv file and transform it into a DataFrame.
Then use the html code (in form of a string) inside each cell to create an image.
"""


import sys
import os
import imgkit
import pandas as pd


def generate_images(row):
    """
    Create a html file with the code passed as argument, then convert it into
    a jpg file
    """
    html = "{}.html".format(row["PATH"])
    jpg = "{}.jpg".format(row["PATH"])

    with open(html, "w") as file:
        file.write(row["HTML"])
        file.close()
    options = {'format': 'jpg', 'width': 1024}
    imgkit.from_file(html, jpg, options=options)
    print("Just created {}.jpg".format(row["PATH"]))
    os.system("rm -f {}.html".format(row["PATH"]))


if __name__ == "__main__":

    csv_file = sys.argv[1]

    schedule = pd.read_csv(csv_file)

    for i, row in schedule.iterrows():
        if not os.path.isfile("{}.jpg".format(row["PATH"])):
            generate_images(row)
