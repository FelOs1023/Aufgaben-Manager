import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import json, os

SaveData = "FokusProjekt/config/SaveData.json"

def AddSave(FullSaveData):
    print("Saving task...\n")

    if os.path.exists(SaveData):
        with open(SaveData, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = {}

    data.append(FullSaveData)

    print("Task saved\n")

    with open(SaveData, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)