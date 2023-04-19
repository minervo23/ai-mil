# Gesamtes Mühle-Spiel mit Methoden

class MuehleSpiel:
    def __init__(self):
        # Der Konstruktor der Klasse initialisiert das Spielbrett als 3x3-Liste von '-'-Zeichen, eine leere Liste
        # von Spielsteinen, den aktuellen Spieler (initial auf 'X') und das Spielende (initial auf False).

        self.spielbrett = [['-' for i in range(3)] for j in range(3)]
        self.spielsteine = []
        self.spielende = False
        self.aktueller_spieler = 'X'

    def spielstein_setzen(self, position):
        #  Diese Methode setzt einen Spielstein auf das Spielbrett an einer bestimmten Position, die als Argument übergeben wird.
        # Wenn der Zug gültig ist, wird der Spielstein zur Liste der Spielsteine hinzugefügt und der nächste Spieler ist an
        # der Reihe. Wenn der Spielstein eine Mühle bildet, erhält der aktuelle Spieler einen Zusatzzug.

        if self.spielbrett[position[0]][position[1]] == '-':
            self.spielbrett[position[0]][position[1]] = self.aktueller_spieler
            spielstein = Spielstein(self.aktueller_spieler, position)
            self.spielsteine.append(spielstein)
            if self.spielstein_bildet_muehle(spielstein):
                self.aktueller_spieler_erhaelt_zusatzzug()
            else:
                self.naechster_spieler()
        else:
            print('Ungültiger Zug')

    def naechster_spieler(self):
        # naechster_spieler: Diese Methode wechselt den aktuellen Spieler.

        if self.aktueller_spieler == 'X':
            self.aktueller_spieler = 'O'
        else:
            self.aktueller_spieler = 'X'

    def spielstein_bildet_muehle(self, spielstein):
        # Diese Methode prüft, ob ein gegebener Spielstein eine Mühle bildet. Diese Methode ist derzeit immer auf False gesetzt
        # und muss noch implementiert werden.
        # Prüfen, ob der Spielstein eine Mühle bildet

        return False

    def beste_zug(self):
        # Diese Methode berechnet den besten Zug für den Computer-Spieler basierend auf der aktuellen Spielposition.
        # Diese Methode ist derzeit nicht implementiert
        # Berechnen Sie den besten Zug basierend auf der aktuellen Spielposition

        return (0, 0)


    def spielen(self):
        # Diese Methode ist die Hauptschleife des Spiels. Sie wechselt zwischen den Spielern (einer menschlicher Spieler und
        # einem Computer-Spieler) und fordert die Eingabe des Spielers oder führt den besten Zug des Computers aus.

        while not self.spielende:
            if self.aktueller_spieler == 'X':
                # Spieler X ist ein Mensch und gibt den Zug ein
                position = input('Spieler X, geben Sie Ihre Position ein: ')
                position = tuple(map(int, position.split(',')))
                self.spielstein_setzen(position)
            else:
                # Spieler O ist der Roboter und wählt den besten Zug
                position = self

board = [['-', '-', '-'] for i in range(3)]

def display_board(board):
    for row in board:
        print(row)

def make_move(board, player):
    # Diese Funktion erlaubt einem Spieler, seinen Spielstein auf dem Spielbrett zu platzieren.
    valid_move = False # Gültiger Zug wird initial auf False gesetzt.
    while not valid_move: # Schleife läuft, bis ein gültiger Zug gemacht wurde.
        position = input("Player " + player + ", make your move (row,column): ") # Spieler gibt seine Position ein.
        row, column = position.split(',') # Position wird geteilt.
        row, column = int(row)-1, int(column)-1 # Position wird in Zahlen umgewandelt.
        if board[row][column] == '-': # Prüft, ob das Feld frei ist.
            valid_move = True # Zug ist gültig.
            board[row][column] = player # Spielstein wird auf das Feld gesetzt.
        else:
            print("Invalid move, try again.") # Zug ist ungültig.
    return board # Gibt das aktualisierte Spielbrett zurück.

def check_mill(board, player):
    # Diese Funktion prüft, ob ein Spieler eine Mühle hat, also ob er drei Spielsteine in einer Reihe,
    # Spalte oder Diagonale hat.
    mill = False # Mühle wird initial auf False gesetzt.
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            mill = True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            mill = True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        mill = True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        mill = True
    return mill # Gibt zurück, ob der Spieler eine Mühle hat.

def main():
    # Diese Funktion steuert den Spielablauf. Sie zeigt das Spielbrett an, lässt abwechselnd Spieler
    # ihre Züge machen und prüft, ob ein Spieler gewonnen hat.

    display_board(board) # Das Spielbrett wird angezeigt.
    players = ['X', 'O'] # Die Spieler werden definiert.
    current_player = players[0] # Der aktuelle Spieler wird initialisiert.
    while True: # Die Schleife läuft, bis das Spiel beendet ist.
        board = make_move(board, current_player) # Der aktuelle Spieler macht einen Zug.
        display_board(board) # Das Spielbrett wird aktualisiert.
        if check_mill(board, current_player): # Die Funktion prüft, ob der Spieler eine Mühle hat.
            print("Player " + current_player + " wins!") # Der Spieler hat gewonnen.
            break # Die Schleife wird beendet.
        if current_player == players[0]: # Wechselt den aktuellen Spieler.
            current_player = players[1]
        else:
            current_player = players[0]

if __name__ == "__main__":
    main()
