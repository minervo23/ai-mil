import random

class Mill:
    def __init__(self):
        # Spielbrett initialisieren
        self.board = [['_', '_', '_'] for _ in range(3)]
        # Spieler X beginnt
        self.player = 'X'
        # Positions-Diagramm
        self.positions = {'a1': [0, 0], 'a2': [0, 1], 'a3': [0, 2],
                          'b1': [1, 0], 'b2': [1, 1], 'b3': [1, 2],
                          'c1': [2, 0], 'c2': [2, 1], 'c3': [2, 2]}
        # Anzahl der Züge auf 0 setzen
        self.moves = 0
        # Spiel-Status: noch nicht beendet
        self.gameover = False

    def print_board(self):
        # Funktion, um das Spielbrett auf der Konsole auszugeben
        print('\n'.join([' '.join(row) for row in self.board]))

    def place(self, position):
        # Überprüfen, ob die Position auf dem Spielbrett frei ist
        if self.board[self.positions[position][0]][self.positions[position][1]] == '_':
            # Platzieren des Spielers auf der Position
            self.board[self.positions[position][0]][self.positions[position][1]] = self.player
            # Anzahl der Züge erhöhen
            self.moves += 1
            # Überprüfen, ob das Spiel gewonnen wurde
            self.check_win()
            # Wenn das Spiel noch nicht gewonnen wurde, wechsle den Spieler
            if not self.gameover:
                self.switch_player()
        else:
            print('Ungültiger Zug')

    def switch_player(self):
        # Wechselt den aktuellen Spieler
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'

    def check_win(self):
        # horizontale Gewinnbedingungen prüfen
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0] != '_':
                self.gameover = True
                print(f'{self.board[i][0]} hat gewonnen!')
        # vertikale Gewinnbedingungen prüfen
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] != '_':
                self.gameover = True
                print(f'{self.board[0][i]} hat gewonnen!')
        # diagonale Gewinnbedingungen prüfen
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != '_':
            self.gameover = True
            print(f'{self.board[0][0]} hat gewonnen!')
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != '_':
            self.gameover = True
            print(f'{self.board[0][2]} hat gewonnen!')
        # Unentschieden prüfen
        if self.moves == 9 and not self.gameover:
            self.gameover = True
            print('Unentschieden!')

    # Definition einer Funktion, die einen Zug für den Computer ausführt
    def ai_move(self):
        # Liste aller gültigen Züge initialisieren
        valid_moves = []
        # Iterieren über alle Positionen auf dem Brett
        for position, coords in self.positions.items():
            # Wenn die Position leer ist, füge sie zu den gültigen Zügen hinzu
            if self.board[coords[0]][coords[1]] == '_':
                valid_moves.append(position)
        # Wenn es gültige Züge gibt, wähle zufällig einen Zug aus der Liste aus
        if valid_moves:
            position = random.choice(valid_moves)
            self.place(position)
        # Wenn es keine gültigen Züge gibt, beende das Spiel
        else:
            print('Tie game')
            self.gameover = True

    # Definition eines Tic Tac Toe Spiels in Python

    # Initialisieren des Spielbretts als eine 3x3 Matrix
    board = [[' ', ' ', ' '] for i in range(3)]

    # Funktion zur Ausgabe des aktuellen Spielstands auf der Konsole
    def print_board(board):
        print("   0   1   2")  # Spaltenüberschriften
        for i in range(3):
            print(i, board[i][0], '|', board[i][1], '|', board[i][2])  # Zeile mit Werten und Trennlinien
            if i != 2:
                print("  -----------")  # Trennlinie zwischen Zeilen

    # Funktion, die prüft, ob das Spiel vorbei ist (Gewinner oder Unentschieden)
    def game_over(board):
        # Überprüfen auf Gewinnbedingungen in horizontalen Reihen
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return True
        # Überprüfen auf Gewinnbedingungen in vertikalen Reihen
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return True
        # Überprüfen auf Gewinnbedingungen in diagonalen Reihen
        if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
            return True
        # Überprüfen auf Unentschieden
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    return False
        return True

    # Funktion, die den Zug des Spielers durch Eingabe von Zeile und Spalte erhält und ausführt
    def player_move(board, player):
        while True:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That space is already taken. Try again.")

    # Funktion, um einen Zug für den Computer auszuführen
    def computer_move(board, computer, player):
        # Überprüfen Sie, ob der Computer in einem Zug gewinnen kann
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = computer
                    if game_over(board):
                        return
                    else:
                        board[i][j] = ' '
        # Überprüfen Sie, ob der Spieler in einem Zug gewinnen kann
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = player
                    if game_over(board):
                        board[i][j] = computer
                        return
                    else:
                        board[i][j] = ' '
        # Falls keine der obigen Bedingungen zutrifft, wählen Sie ein beliebiges freies Feld
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if board[row][col] == ' ':
                board[row][col] = computer
                return

    # Das Spiel startet hier
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    player = input("Enter your name: ")
    computer = "X" if player == "O" else ""

