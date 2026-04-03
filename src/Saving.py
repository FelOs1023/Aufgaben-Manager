import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import json, os

SaveData = "config/SaveData.json"

def AddSave(FullSaveData):
    print("Saving task...\n")

    if os.path.exists(SaveData):
        with open(SaveData, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []

    if not data:
        data.append({"Tasks": {}})
    elif "Tasks" not in data[0]:
        data[0]["Tasks"] = {}

    task_key = f"Task{len(data[0]['Tasks']) + 1}"
    data[0]["Tasks"][task_key] = FullSaveData

    print("Task saved\n")

    with open(SaveData, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def loadSave():
    try:
        with open(SaveData, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Fehler beim Laden: {e}")
        return []
