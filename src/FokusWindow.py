from PyQt6 import QtCore, QtGui, QtWidgets
import json


class Ui_Fokus_Window(object):
    def loadJson(self):
        with open("config/SaveData.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def loadFokusTasks(self):
        while self.FokusContainerLayout.count():
            child = self.FokusContainerLayout.takeAt(0)
            widget = child.widget()
            if widget:
                widget.deleteLater()

        today = QtCore.QDate.currentDate().toString("dd.MM.yyyy")

        fokus_tasks = []
        for item in self.loadJson():
            for task_name, task in item.get("Tasks", {}).items():
                if task.get("Task Fokus Date") == today:
                    fokus_tasks.append(task)

        if not fokus_tasks:
            empty = QtWidgets.QLabel("Keine Fokus Aufgaben für heute.")
            font = QtGui.QFont()
            font.setPointSize(12)
            empty.setFont(font)
            self.FokusContainerLayout.addWidget(empty)
            return

        for task in fokus_tasks:
            self.FokusContainerLayout.addWidget(self.createFokusCard(task))

    def createFokusCard(self, task):
        card = QtWidgets.QGroupBox()
        card.setTitle(task.get("Task Title", ""))
        font = QtGui.QFont()
        font.setPointSize(12)
        card.setFont(font)

        layout = QtWidgets.QVBoxLayout(card)

        prio = QtWidgets.QLabel("Priorität: " + task.get("Task Priority", ""))
        layout.addWidget(prio)

        beschreibung = QtWidgets.QLabel(task.get("Task Description", ""))
        beschreibung.setWordWrap(True)
        layout.addWidget(beschreibung)

        return card

    def setupUi(self, Fokus_Window):
        Fokus_Window.setObjectName("Fokus_Window")
        Fokus_Window.resize(429, 600)

        self.verticalLayout = QtWidgets.QVBoxLayout(Fokus_Window)

        self.FokusHeader = QtWidgets.QLabel(parent=Fokus_Window)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.FokusHeader.setFont(font)
        self.FokusHeader.setObjectName("FokusHeader")
        self.verticalLayout.addWidget(self.FokusHeader)

        self.FokusScrollArea = QtWidgets.QScrollArea(parent=Fokus_Window)
        self.FokusScrollArea.setWidgetResizable(True)
        self.FokusScrollArea.setObjectName("FokusScrollArea")

        self.FokusContainer = QtWidgets.QWidget()
        self.FokusContainer.setObjectName("FokusContainer")
        self.FokusContainerLayout = QtWidgets.QVBoxLayout(self.FokusContainer)
        self.FokusContainerLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.FokusScrollArea.setWidget(self.FokusContainer)

        self.verticalLayout.addWidget(self.FokusScrollArea)

        self.CloseButton = QtWidgets.QPushButton(parent=Fokus_Window, clicked=lambda: Fokus_Window.close())
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CloseButton.setFont(font)
        self.CloseButton.setObjectName("CloseButton")
        self.verticalLayout.addWidget(self.CloseButton)

        self.retranslateUi(Fokus_Window)
        QtCore.QMetaObject.connectSlotsByName(Fokus_Window)

        self.loadFokusTasks()

    def retranslateUi(self, Fokus_Window):
        _translate = QtCore.QCoreApplication.translate
        Fokus_Window.setWindowTitle(_translate("Fokus_Window", "Fokus"))
        self.FokusHeader.setText(_translate("Fokus_Window", "Fokus Aufgaben für heute:"))
        self.CloseButton.setText(_translate("Fokus_Window", "Schließen"))
