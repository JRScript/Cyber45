__author__= "Jithin Raj"

import requests
import json
import pandas as pd
import csv
import tkinter as tk
import time
from tkinter import simpledialog

def cyber():
    year = e1.get()
    month = e2.get()
    code = open('api.txt', 'r')
    api = code.read()
    response = requests.get("https://www.cyber45.com/_functions/myAPIaccess/"+api+"/"+year+"/"+month)
    result = response.json()
    res = open('result.json', 'w+')
    json.dump(result, res)
    code.close()
    res.close()
    data = pd.read_json('result.json')
    columns = []
    all_rows = []
    for items in data["items"]:
        row = ["" for col in columns]
        for key, value in items.items():
            try:
                index = columns.index(key)
            except ValueError: 
                columns.append(key)
                row.append("")
                index = len(columns) - 1
            row[index] = value
        all_rows.append(row)

    with open("IOC "+ time.strftime("%m%d%Y-%H%M%S") +".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile) 
        writer.writerow(columns) # first row is the headers
        writer.writerows(all_rows)# then, the rows
    print("Successfully generated the IOC file for the Month", month, year)

master = tk.Tk()
master.title("IOC Finder")
master.geometry("250x90+600+300")

tk.Label(master, text="Year").grid(row=0)
tk.Label(master, text="Month").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Find IOC ', command=cyber).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=1, sticky=tk.W, pady=4)

tk.mainloop()
