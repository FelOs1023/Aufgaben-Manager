import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import json, os

SaveData = "config/SaveData.json"

def ensureSavedata():
    directory = os.path.dirname(SaveData)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(SaveData):
        with open(SaveData, "w", encoding="utf-8") as file:
            json.dump([{"Tasks": {}}], file, indent=4)

def AddSave(FullSaveData):
    print("Saving task...\n")

    ensureSavedata()

    with open(SaveData, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not data:
        data.append({"Tasks": {}})
    elif "Tasks" not in data[0]:
        data[0]["Tasks"] = {}

    existing_numbers = [
        int(key.removeprefix("Task"))
        for key in data[0]["Tasks"]
        if key.removeprefix("Task").isdigit()
    ]
    next_number = max(existing_numbers, default=0) + 1
    task_key = f"Task{next_number}"
    data[0]["Tasks"][task_key] = FullSaveData

    print("Task saved\n")

    with open(SaveData, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


