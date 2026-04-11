# Aufgaben-Manager
Ein kleines Programm in welchem man am Ende Aufgaben erstellen, bearbeiten, Löschen und generell ansehen kann.
Die Informationen sollen lokal in einer JSON gespeichert werden.

Eine Aufgabe kann die folgenden Informationen halten:
- Titel/Namen der Aufgabe
- Eine Beschreibung der Aufgabe, welche auch länger sein kann
- Ein geplantes Enddatum wann die Aufgabe erledigt werden soll
- Ein Fokus Datum für die Fokus Funktion, welches nur gespeichert wird wenn man dieses via checkbox bestätigt
- Eine Prioritäts angabe, welche die Aufgabe in Priorität Hoch, Mittel, Niedrig einordnet
- Einen Aktuellen Status, welches anzeigt ob die Aufgabe schon in Bearbeitung, Fertig oder noch zu machen ist

# Fertige Features
Das Erstellen von Aufgaben ist möglich. Die Eingegebenen Daten werden erfolgreich in der vorgesehenen JSON formatiert gespeichert.

# Features in Bearbeitung
Das Editieren von Aufgaben soll die Informationen in die Felder einsetzen und änderbar machen. Beim speichern soll dann der angegebene Datensatz geändert werden statt das ein komplett neuer Datensatz erstellt wird. 

Das Auswähl Fenster soll alle gespeicherten Aufgaben beinhalten und diese anzeigen. Die ausgewählte Aufgabe wird dann in das Edit Fenster gesetzt und kann von dort bearbeitet, gelöscht oder einfach nur angeguckt werden. 

Das Löschen soll möglich sein im Bearbeitungsfenster und den ausgewählten Datensatz komplett aus dem Speicher entfernen.

Das Fokus Fenster soll eine Aufgabe für einen bestimmten Tag fokussieren. Wenn beim erstellen einer Aufgabe ein Fokusdatum angegeben wurde wird an diesem Datum die Aufgabe automatisch im Fokus Fenster auftauchen. 