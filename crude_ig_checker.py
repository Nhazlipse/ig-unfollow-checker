import tkinter as tk
import json
import os

from tkinter import *
from tkinter import filedialog

followersArray = []
followingArray = []

root = tk.Tk()
root.title("Crude IG Unfollow Checker")
root.minsize(400, 200)

uFrame = Frame(root)
uFrame.pack()

uFrame.columnconfigure(0,weight=2, uniform='second')
uFrame.columnconfigure(1,weight=2, uniform='second')


def uploadAction(column, row, event=None):
    filepath = filedialog.askopenfilename()
    with open(filepath, 'r') as file:
        data = json.load(file)
        filename = os.path.basename(filepath)
        print(filename)
        if filename == "following.json":
            i = 0
            for x in data['relationships_following']:
                name = data['relationships_following'][i]['string_list_data'][0]['value']
                i += 1
                followingArray.append(name)
            print(followingArray)
        else:
            i = 0
            for x in data:
                name = data[i]['string_list_data'][0]['value']
                i += 1
                followersArray.append(name)
            print(followersArray)
    print('Selected:', filename)
    filepath = tk.Label(uFrame, text=filename)
    filepath.grid(row=row, column=column)


def analyseFiles():

    # Find values only in array A
    noFollow = [value for value in followingArray if value not in followersArray]
    # Find values only in array B
    onlyFollower = [value for value in followersArray if value not in followingArray]

    with open("not_following_you_back.txt", "w") as f:
        for line in noFollow:
            f.write(f"{line}\n")
    with open("you_dont_follow.txt", "w") as f1:
        for line in onlyFollower:
            f1.write(f"{line}\n")

    noFLabel = tk.Label(root, text="Files generated in folder")
    noFLabel.pack()


ub1 = tk.Button(uFrame, text='Select File', command=lambda: uploadAction(0, 3))
ub1.grid(row=2, column=0)
ul1 = tk.Label(uFrame, text="Following.json file:")
ul1.grid(row=1, column=0)

ub2 = tk.Button(uFrame, text='Select File', command=lambda: uploadAction(1, 3))
ub2.grid(row=2, column=1)
ul2 = tk.Label(uFrame, text="Followers.json file:")
ul2.grid(row=1, column=1)

contb = tk.Button(root, text='Analyse', command=analyseFiles)
contb.pack()
root.mainloop()