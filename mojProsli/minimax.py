from tree import *
import random

positive_inifnity = float("infinity")
negative_infinity = float("-infinity")


class GameTable:

    def __init__(self):
        self._game_table = [["O", "-", "-", "O", "-", "-", "O"], ["|", "O", "-", "O", "-", "O", "|"],
                            ["|", "|", "O", "O", "O", "|", "|"], ["O", "O", "O", "*", "O", "O", "O"],
                            ["|", "|", "O", "O", "O", "|", "|"], ["|", "O", "-", "O", "-", "O", "|"],
                            ["O", "-", "-", "O", "-", "-", "O"]]

        self._row_length = 7
        self._column_length = 7
        self._pieces = []
        self._white_pieces_coordinates = []
        self._black_pieces_coordinates = []
        self._white_blocked_pieces = []
        self._black_blocked_pieces = []
        self._number_of_player_mills = 0
        self._number_of_opponent_mills = 0
        self._x_coordinate = None
        self._y_coordinate = None

        self._possible_mills = [["(0, 0)", "(0, 3)", "(0, 6)"], ["(0, 6)", "(3, 6)", "(6, 6)"],
                                ["(6, 0)", "(6, 3)", "(6, 6)"], ["(0, 0)", "(3, 0)", "(6, 0)"],
                                ["(1, 1)", "(1, 3)", "(1, 5)"], ["(1, 5)", "(3, 5)", "(5, 5)"],
                                ["(5, 1)", "(5, 3)", "(5, 5)"], ["(1, 1)", "(3, 1)", "(5, 1)"],
                                ["(2, 2)", "(2, 3)", "(2, 4)"], ["(2, 4)", "(3, 4)", "(4, 4)"],
                                ["(4, 2)", "(4, 3)", "(4, 4)"], ["(2, 2)", "(3, 2)", "(4, 2)"],
                                ["(3, 0)", "(3, 1)", "(3, 2)"], ["(3, 4)", "(3, 5)", "(3, 6)"],
                                ["(4, 3)", "(5, 3)", "(6, 3)"], ["(0, 3)", "(1, 3)", "(2, 3)"]]

        self._possible_double_mills = [["(0, 0)", "(0, 3)", "(0, 6)", "(3, 6)", "(6, 6)"],
                                       ["(0, 6)", "(3, 6)", "(6, 6)", "(6, 3)", "(6, 0)"],
                                       ["(6, 6)", "(6, 3)", "(6, 0)", "(3, 0)", "(0, 0)"],
                                       ["(6, 0)", "(3, 0)", "(0, 0)", "(0, 3)", "(0, 6)"],
                                       ["(1, 1)", "(1, 3)", "(1, 5)", "(3, 5)", "(5, 5)"],
                                       ["(1, 5)", "(3, 5)", "(5, 5)", "(5, 3)", "(5, 1)"],
                                       ["(5, 5)", "(5, 3)", "(5, 1)", "(3, 1)", "(1, 1)"],
                                       ["(5, 1)", "(3, 1)", "(1, 1)", "(1, 3)", "(1, 5)"],
                                       ["(2, 2)", "(2, 3)", "(2, 4)", "(3, 4)", "(4, 4)"],
                                       ["(2, 4)", "(3, 4)", "(4, 4)", "(4, 3)", "(4, 2)"],
                                       ["(4, 4)", "(4, 3)", "(4, 2)", "(3, 2)", "(2, 2)"],
                                       ["(4, 2)", "(3, 2)", "(2, 2)", "(2, 3)", "(2, 4)"],
                                       ["(0, 0)", "(0, 3)", "(0, 6)", "(1, 3)", "(2, 3)"],
                                       ["(0, 3)", "(1, 3)", "(2, 3)", "(1, 1)", "(1, 5)"],
                                       ["(0, 3)", "(1, 3)", "(2, 3)", "(2, 2)", "(2, 4)"],
                                       ["(3, 4)", "(3, 5)", "(3, 6)", "(0, 6)", "(6, 6)"],
                                       ["(1, 5)", "(3, 5)", "(5, 5)", "(3, 4)", "(3, 6)"],
                                       ["(2, 4)", "(3, 4)", "(4, 4)", "(3, 5)", "(3, 6)"],
                                       ["(6, 0)", "(6, 3)", "(6, 6)", "(5, 3)", "(4, 3)"],
                                       ["(5, 1)", "(5, 3)", "(5, 5)", "(4, 3)", "(6, 3)"],
                                       ["(4, 2)", "(4, 3)", "(4, 4)", "(5, 3)", "(6, 3)"],
                                       ["(0, 0)", "(3, 0)", "(6, 0)", "(3, 1)", "(3, 2)"],
                                       ["(3, 0)", "(3, 1)", "(3, 2)", "(1, 1)", "(5, 1)"],
                                       ["(3, 0)", "(3, 1)", "(3, 2)", "(2, 2)", "(4, 2)"]]

        self._possible_3_piece_configurations = [["(0, 0)", "(0, 3)", "(3, 0)"], ["(0, 0)", "(0, 3)", "(6, 0)"],
                                           ["(0, 0)", "(3, 0)", "(0, 6)"], ["(0, 0)", "(6, 0)", "(0, 6)"],
                                           ["(0, 3)", "(0, 6)", "(3, 6)"], ["(0, 3)", "(0, 6)", "(6, 6)"],
                                           ["(0, 0)", "(0, 6)", "(3, 6)"], ["(0, 0)", "(0, 6)", "(6, 6)"],
                                           ["(6, 6)", "(6, 3)", "(3, 6)"], ["(6, 0)", "(6, 6)", "(3, 6)"],
                                           ["(6, 3)", "(6, 6)", "(0, 6)"], ["(6, 0)", "(6, 6)", "(0, 6)"],
                                           ["(3, 0)", "(6, 0)", "(6, 3)"], ["(0, 0)", "(6, 0)", "(6, 3)"],
                                           ["(3, 0)", "(6, 0)", "(6, 6)"], ["(0, 0)", "(6, 0)", "(6, 6)"],
                                           ["(1, 1)", "(3, 1)", "(1, 3)"], ["(1, 1)", "(5, 1)", "(1, 3)"],
                                           ["(1, 1)", "(3, 1)", "(1, 5)"], ["(1, 1)", "(5, 1)", "(1, 5)"],
                                           ["(1, 3)", "(1, 5)", "(3, 5)"], ["(1, 3)", "(1, 5)", "(5, 5)"],
                                           ["(1, 1)", "(1, 5)", "(3, 5)"], ["(1, 1)", "(1, 5)", "(5, 5)"],
                                           ["(3, 5)", "(5, 5)", "(5, 3)"], ["(3, 5)", "(5, 5)", "(5, 1)"],
                                           ["(1, 5)", "(5, 5)", "(5, 3)"], ["(1, 5)", "(5, 5)", "(5, 1)"],
                                           ["(5, 3)", "(5, 1)", "(3, 1)"], ["(5, 3)", "(5, 1)", "(1, 1)"],
                                           ["(5, 5)", "(5, 1)", "(3, 1)"], ["(5, 5)", "(5, 1)", "(1, 1)"],
                                           ["(3, 2)", "(2, 2)", "(2, 3)"], ["(3, 2)", "(2, 2)", "(2, 4)"],
                                           ["(4, 2)", "(2, 2)", "(2, 3)"], ["(4, 2)", "(2, 2)", "(2, 4)"],
                                           ["(2, 3)", "(2, 4)", "(3, 4)"], ["(2, 3)", "(2, 4)", "(4, 4)"],
                                           ["(2, 2)", "(2, 4)", "(3, 4)"], ["(2, 2)", "(2, 4)", "(4, 4)"],
                                           ["(3, 4)", "(4, 4)", "(4, 3)"], ["(3, 4)", "(4, 4)", "(4, 2)"],
                                           ["(2, 4)", "(4, 4)", "(4, 3)"], ["(2, 4)", "(4, 4)", "(4, 2)"],
                                           ["(4, 3)", "(4, 2)", "(3, 2)"], ["(4, 3)", "(4, 2)", "(2, 2)"],
                                           ["(4, 4)", "(4, 2)", "(3, 2)"], ["(4, 4)", "(4, 2)", "(2, 2)"],
                                           ["(0, 0)", "(0, 3)", "(1, 3)"], ["(0, 3)", "(0, 6)", "(1, 3)"],
                                           ["(3, 0)", "(1, 3)", "(1, 1)"], ["(3, 0)", "(1, 3)", "(1, 5)"],
                                           ["(1, 1)", "(1, 3)", "(2, 3)"], ["(1, 3)", "(1, 5)", "(2, 3)"],
                                           ["(2, 2)", "(2, 3)", "(1, 3)"], ["(2, 3)", "(2, 4)", "(1, 3)"],
                                           ["(0, 6)", "(3, 6)", "(3, 5)"], ["(6, 6)", "(3, 6)", "(3, 5)"],
                                           ["(1, 5)", "(3, 5)", "(3, 6)"], ["(5, 5)", "(3, 5)", "(3, 6)"],
                                           ["(1, 5)", "(3, 5)", "(3, 4)"], ["(5, 5)", "(3, 5)", "(3, 4)"],
                                           ["(2, 4)", "(3, 4)", "(3, 5)"], ["(4, 4)", "(3, 4)", "(3, 5)"],
                                           ["(6, 0)", "(6, 3)", "(5, 3)"], ["(6, 6)", "(6, 3)", "(5, 3)"],
                                           ["(5, 1)", "(5, 3)", "(4, 3)"], ["(5, 5)", "(5, 3)", "(4, 3)"],
                                           ["(5, 1)", "(5, 3)", "(6, 3)"], ["(5, 5)", "(5, 3)", "(6, 3)"],
                                           ["(4, 2)", "(4, 3)", "(5, 3)"], ["(4, 4)", "(4, 3)", "(5, 3)"],
                                           ["(0, 0)", "(3, 0)", "(3, 1)"], ["(6, 0)", "(3, 0)", "(3, 1)"],
                                           ["(1, 1)", "(3, 1)", "(3, 0)"], ["(1, 1)", "(3, 1)", "(3, 2)"],
                                           ["(5, 1)", "(3, 1)", "(3, 0)"], ["(5, 1)", "(3, 1)", "(3, 2)"],
                                           ["(2, 2)", "(3, 2)", "(3, 1)"], ["(4, 2)", "(3, 2)", "(3, 1)"]]

        self._possible_2_piece_configurations = [["(0, 0)", "(0, 3)"], ["(0, 3)", "(0, 6)"], ["(0, 6)", "(3, 6)"],
                                           ["(3, 6)", "(6, 6)"], ["(6, 6)", "(3, 6)"], ["(3, 6)", "(0, 6)"],
                                           ["(0, 6)", "(0, 3)"], ["(0, 3)", "(0, 0)"], ["(1, 1)", "(1, 3)"],
                                           ["(1, 3)", "(1, 5)"], ["(1, 5)", "(3, 5)"], ["(3, 5)", "(5, 5)"],
                                           ["(5, 5)", "(5, 3)"], ["(5, 3)", "(5, 1)"], ["(5, 1)", "(3, 1)"],
                                           ["(3, 1)", "(1, 1)"], ["(2, 2)", "(2, 3)"], ["(2, 3)", "(2, 4)"],
                                           ["(2, 4)", "(3, 4)"], ["(3, 4)", "(4, 4)"], ["(4, 4)", "(4, 3)"],
                                           ["(4, 3)", "(4, 2)"], ["(4, 2)", "(3, 2)"], ["(3, 2)", "(2, 2)"],
                                           ["(0, 3)", "(1, 3)"], ["(1, 3)", "(2, 3)"], ["(3, 4)", "(3, 5)"],
                                           ["(3, 5)", "(3, 6)"], ["(4, 3)", "(5, 3)"], ["(5, 3)", "(6, 3)"],
                                           ["(0, 3)", "(1, 3)"], ["(1, 3)", "(2, 3)"], ["(0, 0)", "(0, 6)"],
                                           ["(0, 6)", "(6, 6)"], ["(6, 0)", "(6, 6)"], ["(0, 0)", "(6, 0)"],
                                           ["(1, 1)", "(1, 5)"], ["(1, 5)", "(5, 5)"], ["(5, 1)", "(5, 5)"],
                                           ["(1, 1)", "(5, 1)"], ["(2, 2)", "(2, 4)"], ["(2, 4)", "(4, 4)"],
                                           ["(4, 2)", "(4, 4)"], ["(2, 2)", "(4, 2)"], ["(3, 0)", "(3, 2)"],
                                           ["(3, 4)", "(3, 6)"], ["(4, 3)", "(6, 3)"], ["(0, 3)", "(2, 3)"]]

        self._neighbours_of_pieces = {"(0, 0)": ["(3, 0)", "(0, 3)"], "(0, 3)": ["(0, 0)", "(0, 6)", "(1, 3)"],
                        "(0, 6)": ["(0, 3)", "(3, 6)"], "(1, 1)": ["(1, 3)", "(3, 1)"],
                        "(1, 3)": ["(1, 1)", "(1, 5)", "(0, 3)", "(2, 3)"], "(1, 5)": ["(1, 3)", "(3, 5)"],
                        "(2, 2)": ["(2, 3)", "(3, 2)"], "(2, 3)": ["(2, 2)", "(2, 4)", "(1, 3)"],
                        "(2, 4)": ["(2, 3)", "(3, 4)"], "(3, 0)": ["(0, 0)", "(6, 0)", "(3, 1)"],
                        "(3, 1)": ["(3, 0)", "(3, 2)", "(1, 1)", "(5, 1)"], "(3, 2)": ["(2, 2)", "(4, 2)", "(3, 1)"],
                        "(3, 4)": ["(2, 4)", "(4, 4)", "(3, 5)"], "(3, 5)": ["(3, 4)", "(3, 6)", "(1, 5)", "(5, 5)"],
                        "(3, 6)": ["(3, 5)", "(0, 6)", "(6, 6)"], "(4, 2)": ["(3, 2)", "(4, 3)"],
                        "(4, 3)": ["(4, 2)", "(4, 4)", "(5, 3)"], "(4, 4)": ["(4, 3)", "(3, 4)"],
                        "(5, 1)": ["(3, 1)", "(5, 3)"], "(5, 3)": ["(5, 1)", "(5, 5)", "(4, 3)", "(6, 3)"],
                        "(5, 5)": ["(5, 3)", "(3, 5)"], "(6, 0)": ["(3, 0)", "(6, 3)"],
                        "(6, 3)": ["(6, 0)", "(6, 6)", "(5, 3)"], "(6, 6)": ["(6, 3)", "(3, 6)"]}

    def get_field(self, x, y):
        if x not in range(0, self._row_length) or y not in range(0, self._column_length):
            print("Date koordinate ne postoje!")

        elif self._game_table[x][y] not in ("B", "W", "O"):
            print("Na ovim koordinatama se ne nalazi nikakvo polje!")

        else:
            return self._game_table[x][y]

    def set_field(self, x, y, value):
        if x not in range(0, self._row_length) or y not in range(0, self._column_length):
            print("Date koordinate ne postoje!")

        elif value not in ("B", "W", "O"):
            print("Uneli ste lose karakter. Unesite W, B ili O")

        elif self._game_table[x][y] not in ("B", "W", "O"):
            print("Na ovim koordinatama se ne nalazi nikakvo polje!")

        else:
            if value == "W":
                white_coordinate = "(" + str(x) + "," + " " + str(y) + ")"
                self._white_pieces_coordinates.append(white_coordinate)
            elif value == "B":
                black_coordinate = "(" + str(x) + "," + " " + str(y) + ")"
                self._black_pieces_coordinates.append(black_coordinate)
            self._game_table[x][y] = value

    def get_possible_mills(self):
        return self._possible_mills

    def get_possible_double_mills(self):
        return self._possible_double_mills

    def get_possible_2_piece_configurations(self):
        return self._possible_2_piece_configurations

    def get_possible_3_piece_configurations(self):
        return self._possible_3_piece_configurations

    def get_neighbours_of_pieces(self):
        return self._neighbours_of_pieces

    def get_white_pieces_coordinates(self):
        return self._white_pieces_coordinates

    def get_black_pieces_coordinates(self):
        return self._black_pieces_coordinates

    def get_white_blocked_pieces(self):
        return self._white_blocked_pieces

    def get_black_blocked_pieces(self):
        return self._black_blocked_pieces

    def get_number_of_player_mills(self):
        return self._number_of_player_mills

    def set_number_of_player_mills(self, value):
        self._number_of_player_mills = value

    def get_number_of_opponent_mills(self):
        return self._number_of_opponent_mills

    def set_number_of_opponent_mills(self, value):
        self._number_of_opponent_mills = value

    def get_x_coordinate(self):
        return self._x_coordinate

    def get_y_coordinate(self):
        return self._y_coordinate

    def set_x_coordinate(self, value):
        self._x_coordinate = value

    def set_y_coordinate(self, value):
        self._y_coordinate = value

    def iterate(self):
        for row in self._game_table:
            for element in row:
                if element in ("W", "B"):
                    self._pieces.append(element)
        return self._pieces

    def print_table(self):
        print("     " + "0" + "1" + "2" + "3" + "4" + "5" + "6")
        print("")
        row_number = 0
        for row in self._game_table:
            print(str(row_number) + "    " + row[0] + row[1] + row[2] + row[3] + row[4] + row[5] + row[6])
            row_number += 1

    def dozvoljene_koordinate(self):

        print("\nDOZVOLJENE KOORDINATE:")
        print("\n(0, 0)  (0, 3)  (0, 6)  (1, 1)  (1, 3)  (1, 5)")
        print("\n(2, 2)  (2, 3)  (2, 4)  (3, 0)  (3, 1)  (3, 2)")
        print("\n(3, 4)  (3, 5)  (3, 6)  (4, 2)  (4, 3)  (4, 4)")
        print("\n(5, 1)  (5, 3)  (5, 5)  (6, 0)  (6, 3)  (6, 6)")

    def input(self):
        self._x_coordinate = int(input("\nUnesite x koordinatu: "))
        self._y_coordinate = int(input("Unesite y koordinatu: "))

    def maximizing_player(self):
        return True

    def game_over(self):
        return True


def number_of_pieces(pieces):
    num_white_pieces = 0
    num_black_pieces = 0
    for piece in pieces:
        if piece == "W":
            num_white_pieces += 1
        else:
            num_black_pieces += 1
    return num_white_pieces - num_black_pieces


def number_of_morisses(possible_mills, white_pieces_coordinates, black_pieces_coordinates):
    num_white_morisses = 0
    num_black_morisses = 0
    for i in possible_mills:
        if i[0] in white_pieces_coordinates and i[1] in white_pieces_coordinates and i[2] in white_pieces_coordinates:
            num_white_morisses += 1
        elif i[0] in black_pieces_coordinates and i[1] in black_pieces_coordinates and i[2] in black_pieces_coordinates:
            num_black_morisses += 1
    return num_white_morisses - num_black_morisses


def number_of_2_piece_configurations(possible_mills, white_pieces_coordinates, black_pieces_coordinates):
    num_white = 0
    num_black = 0
    for i in possible_mills:
        if not (i[0] in white_pieces_coordinates and i[1] in white_pieces_coordinates and i[2] in white_pieces_coordinates):
            if not (i[0] in black_pieces_coordinates or i[1] in black_pieces_coordinates or i[2] in black_pieces_coordinates):
                if i[0] in white_pieces_coordinates and i[1] in white_pieces_coordinates or i[1] in white_pieces_coordinates \
                and i[2] in white_pieces_coordinates or i[0] in white_pieces_coordinates and i[2] in white_pieces_coordinates:
                    num_white += 1
        if not (i[0] in black_pieces_coordinates and i[1] in black_pieces_coordinates and i[2] in black_pieces_coordinates):
            if not (i[0] in white_pieces_coordinates or i[1] in white_pieces_coordinates or i[2] in white_pieces_coordinates):
                if i[0] in black_pieces_coordinates and i[1] in black_pieces_coordinates or i[1] in black_pieces_coordinates \
                and i[2] in black_pieces_coordinates or i[0] in black_pieces_coordinates and i[2] in black_pieces_coordinates:
                    num_black += 1
    return num_white - num_black


def double_morris(possible_double_mills, white_pieces_coordinates, black_pieces_coordinates):
    num_white = 0
    num_black = 0
    for i in possible_double_mills:
        if i[0] in white_pieces_coordinates and i[1] in white_pieces_coordinates and i[2] in white_pieces_coordinates \
        and i[3] in white_pieces_coordinates and i[4] in white_pieces_coordinates:
            num_white += 1
        elif i[0] in black_pieces_coordinates and i[1] in black_pieces_coordinates and i[2] in black_pieces_coordinates\
             and i[3] in black_pieces_coordinates and i[4] in black_pieces_coordinates:
            num_black += 1
    return num_white - num_black


def number_of_3_piece_configurations(white_pieces_coordinates, black_pieces_coordinates, possible_2_piece_configurations, possible_mills):
    num_white = 0
    num_black = 0
    white_iterator = 0
    for i in range(0, len(white_pieces_coordinates)):
        for j in possible_3_piece_configurations:
            if white_pieces_coordinates[i] in j:
                if j[0] in white_pieces_coordinates and j[1] in white_pieces_coordinates and j[2] in white_pieces_coordinates:
                    white_iterator += 1
                if white_iterator == len(white_pieces_coordinates):
                    num_white += 1

    return num_white - num_black


def number_of_blocked_pieces(neighbours_of_pieces, white_pieces_coordinates, black_pieces_coordinates):
    num_white = 0
    num_black = 0
    for i in white_pieces_coordinates:
        if len(neighbours_of_pieces[i]) == 2:
            if (neighbours_of_pieces[i][0] in black_pieces_coordinates or neighbours_of_pieces[i][0] in white_pieces_coordinates) and\
                    (neighbours_of_pieces[i][1] in black_pieces_coordinates or neighbours_of_pieces[i][1] in white_pieces_coordinates):
                num_white += 1
                white_blocked_pieces.append(i)
        elif len(neighbours_of_pieces[i]) == 3:
            if (neighbours_of_pieces[i][0] in black_pieces_coordinates or neighbours_of_pieces[i][0] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][1] in black_pieces_coordinates or neighbours_of_pieces[i][1] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][2] in black_pieces_coordinates or neighbours_of_pieces[i][2] in white_pieces_coordinates):
                num_white += 1
                white_blocked_pieces.append(i)
        elif len(neighbours_of_pieces[i]) == 4:
            if (neighbours_of_pieces[i][0] in black_pieces_coordinates or neighbours_of_pieces[i][0] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][1] in black_pieces_coordinates or neighbours_of_pieces[i][1] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][2] in black_pieces_coordinates or neighbours_of_pieces[i][2] in white_pieces_coordinates) and\
                    (neighbours_of_pieces[i][3] in black_pieces_coordinates or neighbours_of_pieces[i][3] in white_pieces_coordinates):
                num_white += 1
                white_blocked_pieces.append(i)

    for i in black_pieces_coordinates:
        if len(neighbours_of_pieces[i]) == 2:
            if (neighbours_of_pieces[i][0] in black_pieces_coordinates or neighbours_of_pieces[i][0] in white_pieces_coordinates) and\
                    (neighbours_of_pieces[i][1] in black_pieces_coordinates or neighbours_of_pieces[i][1] in white_pieces_coordinates):
                num_black += 1
                black_blocked_pieces.append(i)

        elif len(neighbours_of_pieces[i]) == 3:
            if (neighbours_of_pieces[i][0] in black_pieces_coordinates or neighbours_of_pieces[i][0] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][1] in black_pieces_coordinates or neighbours_of_pieces[i][1] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][2] in black_pieces_coordinates or neighbours_of_pieces[i][2] in white_pieces_coordinates):
                num_black += 1
                black_blocked_pieces.append(i)

        elif len(neighbours_of_pieces[i]) == 4:
            if (neighbours_of_pieces[i][0] in black_pieces_coordinates or neighbours_of_pieces[i][0] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][1] in black_pieces_coordinates or neighbours_of_pieces[i][1] in white_pieces_coordinates) and \
                    (neighbours_of_pieces[i][2] in black_pieces_coordinates or neighbours_of_pieces[i][2] in white_pieces_coordinates) and\
                    (neighbours_of_pieces[i][3] in black_pieces_coordinates or neighbours_of_pieces[i][3] in white_pieces_coordinates):
                num_black += 1
                black_blocked_pieces.append(i)

    return num_black - num_white


def winning_configuration(white_pieces_coordinates, black_pieces_coordinates, white_blocked_pieces, black_blocked_pieces):
    if len(black_pieces_coordinates) == 2:
        return 1
    elif len(black_blocked_pieces) == len(black_pieces_coordinates):
        return 1
    elif len(white_pieces_coordinates) == 2:
        return -1
    elif len(white_blocked_pieces) == len(white_pieces_coordinates):
        return -1
    elif len(white_pieces_coordinates) == len(black_pieces_coordinates) == 3:
        return 0


def closed_morris(possible_mills, white_pieces_coordinates, black_pieces_coordinates):
    num_white_mills = 0
    num_black_mills = 0
    for i in possible_mills:
        if i[0] in white_pieces_coordinates and i[1] in white_pieces_coordinates and i[2] in white_pieces_coordinates:
            num_white_mills += 1
        elif i[0] in black_pieces_coordinates and i[1] in black_pieces_coordinates and i[2] in black_pieces_coordinates:
            num_black_mills += 1

    if g.get_number_of_player_mills() != num_white_mills:
        g.set_number_of_player_mills(num_white_mills)
        return 1
    if g.get_number_of_opponent_mills() != num_black_mills:
        print(g.get_number_of_opponent_mills())
        g.set_number_of_opponent_mills(num_black_mills)
        print(g.get_number_of_opponent_mills())
        return -1
    g.set_number_of_player_mills(num_white_mills)
    g.set_number_of_opponent_mills(num_black_mills)
    return 0


class Minimax:
    pass

# def minimax(node, depth, alpha, beta, maximizingPlayer):
#     if depth == 0 or game_over() in node:
#         return static_evaluation_of_node
#
#     if maximizing_player:
#         maxEval = negative_infinity
#         for child in node:
#             eval = minimax(child, depth - 1, alpha, beta, false)
#             maxEval = max(maxEval, eval)
#             alpha = max(alpha, eval)
#             if beta <= alpha:
#                 break
#         return maxEval
#
#     else:
#         minEval = positive_infinity
#         for child in node:
#             eval = minimax(child, depth - 1, alpha, beta, true)
#             minEval = min(minEval, eval)
#             beta = min(beta, eval)
#             if beta <= alpha
#                 break
#         return minEval




if __name__ == '__main__':
    g = GameTable()
    g.set_field(0, 0, "W")
    g.set_field(0, 3, "W")
    g.set_field(3, 0, "W")
    #g.set_field(0, 6, "W")
    #g.set_field(6, 0, "W")
    #g.set_field(6, 6, "W")
    g.print_table()
    pieces = g.iterate()
    possible_mills = g.get_possible_mills()
    possible_double_mills = g.get_possible_double_mills()
    possible_2_piece_configurations = g.get_possible_2_piece_configurations()
    possible_3_piece_configurations = g.get_possible_3_piece_configurations()
    neighbours_of_pieces = g.get_neighbours_of_pieces()
    white_pieces_coordinates = g.get_white_pieces_coordinates()
    black_pieces_coordinates = g.get_black_pieces_coordinates()
    white_blocked_pieces = g.get_white_blocked_pieces()
    black_blocked_pieces = g.get_black_blocked_pieces()
    number_of_player_mills = g.get_number_of_player_mills()
    number_of_opponent_mills = g.get_number_of_player_mills()
    number_of_3_piece_configurations(white_pieces_coordinates, black_pieces_coordinates, possible_3_piece_configurations, possible_double_mills)
    number_of_blocked_pieces(neighbours_of_pieces, white_pieces_coordinates, black_pieces_coordinates)
    winning_configuration(white_pieces_coordinates, black_pieces_coordinates, white_blocked_pieces, black_blocked_pieces)
    closed_morris(possible_mills, white_pieces_coordinates, black_pieces_coordinates)










