from PyQt6 import QtCore, QtGui, QtWidgets
import os, json, Saving
from EditWindow import Ui_Edit_Window

class Ui_Choose_to_edit(object):
    def loadJson(self):
        with open("config/SaveData.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def LoadItems(self):
        with open("config/SaveData.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            for task_name, task in item.get("Tasks", {}).items():
                list_item = QtWidgets.QListWidgetItem(task.get("Task Title"))
                self.Select_List.addItem(list_item)

    def selecting(self):
        selected_item = self.Select_List.currentItem()
        if selected_item:
            Ui_Edit_Window.openWindow(self, selected_item)
        else:
            QtWidgets.QMessageBox.warning(None, "Warnung")

    def SelectAndClose(self, choose_to_edit):
        choose_to_edit.close()
        self.selecting()
        

    def setupUi(self, Choose_to_edit):
        Choose_to_edit.setObjectName("Choose_to_edit")
        Choose_to_edit.resize(316, 578)
        self.Select_List = QtWidgets.QListWidget(parent=Choose_to_edit)
        self.Select_List.setGeometry(QtCore.QRect(10, 10, 291, 511))
        self.Select_List.setObjectName("Select_List")

        self.LoadItems()

        self.Select_List_Button = QtWidgets.QPushButton(parent=Choose_to_edit, clicked=lambda: self.SelectAndClose(Choose_to_edit))
        self.Select_List_Button.setGeometry(QtCore.QRect(90, 540, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Select_List_Button.setFont(font)
        self.Select_List_Button.setObjectName("Select_List_Button")

        self.retranslateUi(Choose_to_edit)
        QtCore.QMetaObject.connectSlotsByName(Choose_to_edit)

    def retranslateUi(self, Choose_to_edit):
        _translate = QtCore.QCoreApplication.translate
        Choose_to_edit.setWindowTitle(_translate("Choose_to_edit", "Dialog"))
        __sortingEnabled = self.Select_List.isSortingEnabled()
        self.Select_List.setSortingEnabled(False)
        self.Select_List.setSortingEnabled(__sortingEnabled)
        self.Select_List_Button.setText(_translate("Choose_to_edit", "Edit"))
