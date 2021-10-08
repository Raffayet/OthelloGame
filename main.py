from tree import *
import random
import sys
from hashmap import HashMap
import os
os.system("cls")

positive_inifnity = float("infinity")
negative_infinity = float("-infinity")


def introduction():
    print()
    print("          OTHELLO / REVERSI")
    print()
    print("Discs can be placed only on the fields labeled as '$'\n")
    print("If you want to quit the game, just type in 'q'\n")


class GameTable:

    def __init__(self):
        self._game_table = [["*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"],
                            ["*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "W", "B", "*", "*", "*"],
                            ["*", "*", "*", "B", "W", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"],
                            ["*", "*", "*", "*", "*", "*", "*", "*"], ["*", "*", "*", "*", "*", "*", "*", "*"]]

        self._row_length = 8
        self._column_length = 8
        self._pieces = []
        self._table_characters = []
        self._number_of_black_discs = 2
        self._number_of_white_discs = 2
        self._allowed_input_values = ['1', '2', '3', '4', '5', '6', '7', '8', 'q']
        self._white_pieces_coordinates = []
        self._black_pieces_coordinates = []
        self._white_blocked_pieces = []
        self._black_blocked_pieces = []
        self._number_of_player_mills = 7
        self._number_of_opponent_mills = 0
        self._map = HashMap(self._row_length * self._column_length)

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

    def fill_hashmap(self):
        self.fill_table_characters()
        map_key = 1
        for i in range(self._row_length * self._column_length):
            self._map.add(map_key, self._table_characters[i])
            map_key += 1

    def print_hashmap(self):
        for i in range(self._row_length * self._column_length):
            print(self._map[i])

    def fill_table_characters(self):
        for i in range(self._row_length):
            for j in range(self._column_length):
                self._table_characters.append(self._game_table[i][j])

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

    def set_new_table(self, x_coordinate, y_coordinate, new_value):
        self._game_table[int(x_coordinate) - 1][int(y_coordinate) - 1] = new_value
        self.fill_hashmap()

    def iterate(self):
        for row in self._game_table:
            for element in row:
                if element in ("W", "B"):
                    self._pieces.append(element)
        return self._pieces

    def print_table(self):
        self.display_score()
        LINE = '  \u001b[32m +---+---+---+---+---+---+---+---+'
        print('    \u001b[34m 1   2   3   4   5   6   7   8')
        print(LINE)
        for i in range(self._row_length):
            print("\u001b[34m", i+1, end=' ')
            for j in range(self._column_length):
                if self._game_table[i][j] == 'W':
                    print('\u001b[32m| %s' % ("\u001b[37m" + self._game_table[i][j]), end=' ')
                elif self._game_table[i][j] == 'B':
                    print('\u001b[32m| %s' % ("\u001b[30;1m" + self._game_table[i][j]), end=' ')
                elif self._game_table[i][j] == '$':
                    print('\u001b[32m| %s' % ("\u001b[31;1m" + self._game_table[i][j]), end=' ')
                else:
                    print('\u001b[32m| %s' % ("\u001b[32m" + self._game_table[i][j]), end=' ')
            print('|')
            print(LINE)

    def display_score(self):
        print("\n\u001b[30;1m BLACK: " + "\u001b[30;1m" + str(self._number_of_black_discs) + "                   " +
              "\u001b[37mWHITE: " + str(self._number_of_white_discs) +"\n")

    def get_input(self):
        return self._x_coordinate, self._y_coordinate

    def maximizing_player(self):
        return True

    def is_game_over(self):
        if self._number_of_black_discs == 0:
            print("\n\nGAME OVER! WHITE WINS!\n\n")
        if self._number_of_white_discs == 0:
            print("\n\nGAME OVER! BLACK WINS!\n\n")
        if self._number_of_black_discs + self._number_of_white_discs == 64:
            if self._number_of_black_discs > self._number_of_white_discs:
                print("\n\nGAME OVER! BLACK WINS!\n\n")
            elif self._number_of_white_discs > self._number_of_black_discs:
                print("\n\nGAME OVER! WHITE WINS!\n\n")
            else:
                print("\n\nGAME OVER! IT'S A DRAW!\n\n")

    def import_input_coordinations(self):

        x_coord = input("\nType in row number: ")
        if x_coord == 'q':
            sys.exit()

        while x_coord not in self._allowed_input_values:
            print("Invalid input. Type in 1-8.")
            x_coord = input("\nType in row number: ")
            if x_coord == 'q':
                sys.exit()

        y_coord = input("\nType in column number: ")
        if y_coord == 'q':
            sys.exit()

        while y_coord not in self._allowed_input_values:
            print("Invalid input. Type in 1-8.")
            y_coord = input("\nType in column number: ")
            if y_coord == 'q':
                sys.exit()

        return x_coord, y_coord

    def check_input_coordinations(self, player_color):

        x_coord, y_coord = self.import_input_coordinations()

        while self._game_table[int(x_coord) - 1][int(y_coord) - 1] != '*' and self._game_table[int(x_coord) - 1][int(y_coord) - 1] != '$':
            print("There already exist a disc. Try with other positions.\n")
            x_coord, y_coord = self.import_input_coordinations()

        while player_color == 'black' and self._game_table[int(x_coord) - 1][int(y_coord) - 1] != '$':
            print("Not a valid move. You can only move to '$' positions.\n")
            x_coord, y_coord = self.import_input_coordinations()

        if player_color == 'black':
            self.set_new_table(x_coord, y_coord, 'B')

        elif player_color == 'white':
            self.set_new_table(x_coord, y_coord, 'W')

        if player_color == 'white':
            self.mark_allowed_fields_white()

        self.mark_allowed_fields()

    def player_turn(self):
        print("\nBlack turn.\n")
        self.check_input_coordinations('black')
        self.refresh_score()
        self.print_table()

    def bot_turn(self):
        print("\nWhite turn.\n")
        self.check_input_coordinations('white')
        self.refresh_score()
        self.print_table()

    def refresh_score(self):
        self._number_of_white_discs, self._number_of_black_discs = 0, 0

        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'B':
                    self._number_of_black_discs += 1
                elif self._game_table[i][j] == 'W':
                    self._number_of_white_discs += 1

    def change_disc_color(self, x_to_be_changed, y_to_be_changed):
        for i in range(self._row_length):
            for j in range(self._column_length):
                for k in range(len(x_to_be_changed)):
                    if i == x_to_be_changed[k] and j == y_to_be_changed[k]:
                        if self._game_table[i][j] == 'B':
                            self._game_table[i][j] = 'W'
                        else:
                            self._game_table[i][j] = 'B'
                        if self._game_table[i+1][j] == '$':
                            self._game_table[i+1][j] = '*'
                        if self._game_table[i][j+1] == '$':
                            self._game_table[i][j+1] = '*'
                        if self._game_table[i-1][j] == '$':
                            self._game_table[i-1][j] = '*'
                        if self._game_table[i][j-1] == '$':
                            self._game_table[i][j-1] = '*'
                        if self._game_table[i+1][j+1] == '$':
                            self._game_table[i+1][j+1] = '*'
                        if self._game_table[i-1][j-1] == '$':
                            self._game_table[i-1][j-1] = '*'
                        if self._game_table[i+1][j-1] == '$':
                            self._game_table[i+1][j-1] = '*'
                        if self._game_table[i-1][j+1] == '$':
                            self._game_table[i-1][j+1] = '*'

    def mark_allowed_fields(self):      #strane sveta sam izabrao kako bih napravio jednostavnu
                                                                    # analogiju za iteraciju u 8 pravaca
                                                                    #svaka crna figura moze da se krece samo u tim osama,
                                                                    #i cilj nam je da iteriramo
                                                                    #kroz te ose da bi videli ima li usput nekih belih figura

        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'B':
                    north_x, north_y = self.iterate_north(i, j)

                    if north_x != None and north_y != None and self._game_table[north_x][north_y] != 'B':

                        self._game_table[north_x][north_y] = '$'

                    south_x, south_y = self.iterate_south(i, j)

                    if south_x != None and south_y != None and self._game_table[south_x][south_y] != 'B':

                        self._game_table[south_x][south_y] = '$'

                    east_x, east_y = self.iterate_east(i, j)

                    if east_x != None and east_y != None and self._game_table[east_x][east_y] != 'B':
                        self._game_table[east_x][east_y] = '$'

                    west_x, west_y = self.iterate_west(i, j)

                    if west_x != None and west_y != None and self._game_table[west_x][west_y] != 'B':
                        self._game_table[west_x][west_y] = '$'

                    south_east_x, south_east_y = self.iterate_south_east(i, j)

                    if south_east_x != None and south_east_y != None and self._game_table[south_east_x][south_east_y] != 'B':
                        self._game_table[south_east_x][south_east_y] = '$'

                    south_west_x, south_west_y = self.iterate_south_west(i, j)

                    if south_west_x != None and south_west_y != None and self._game_table[south_west_x][
                        south_west_y] != 'B':
                        self._game_table[south_west_x][south_west_y] = '$'

                    north_west_x, north_west_y = self.iterate_north_west(i, j)

                    if north_west_x != None and north_west_y != None and self._game_table[north_west_x][
                        north_west_y] != 'B':
                        self._game_table[north_west_x][north_west_y] = '$'

                    north_east_x, north_east_y = self.iterate_north_east(i, j)

                    if north_east_x != None and north_east_y != None and self._game_table[north_east_x][
                        north_east_y] != 'B':
                        self._game_table[north_east_x][north_east_y] = '$'

    def mark_allowed_fields_white(self):
        for i in range(self._row_length):
            for j in range(self._column_length):
                if self._game_table[i][j] == 'W':
                    north_x, north_y = self.iterate_north_white(i, j)

                    if north_x != None and north_y != None and self._game_table[north_x][north_y] != 'W':
                        self._game_table[north_x][north_y] = '*'

                    south_x, south_y = self.iterate_south_white(i, j)

                    if south_x != None and south_y != None and self._game_table[south_x][south_y] != 'W':
                        self._game_table[south_x][south_y] = '*'

                    east_x, east_y = self.iterate_east_white(i, j)

                    if east_x != None and east_y != None and self._game_table[east_x][east_y] != 'W':
                        self._game_table[east_x][east_y] = '*'

                    west_x, west_y = self.iterate_west_white(i, j)

                    if west_x != None and west_y != None and self._game_table[west_x][west_y] != 'W':
                        self._game_table[west_x][west_y] = '*'

                    south_east_x, south_east_y = self.iterate_south_east_white(i, j)

                    if south_east_x != None and south_east_y != None and self._game_table[south_east_x][south_east_y] != 'W':
                        self._game_table[south_east_x][south_east_y] = '*'

                    south_west_x, south_west_y = self.iterate_south_west_white(i, j)

                    if south_west_x != None and south_west_y != None and self._game_table[south_west_x][south_west_y] != 'W':
                        self._game_table[south_west_x][south_west_y] = '*'

                    north_west_x, north_west_y = self.iterate_north_west_white(i, j)

                    if north_west_x != None and north_west_y != None and self._game_table[north_west_x][north_west_y] != 'W':
                        self._game_table[north_west_x][north_west_y] = '*'

                    north_east_x, north_east_y = self.iterate_north_east_white(i, j)

                    if north_east_x != None and north_east_y != None and self._game_table[north_east_x][north_east_y] != 'W':
                        self._game_table[north_east_x][north_east_y] = '*'

    def iterate_north(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []            # lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []            # lista mogucih y koordinata za promenu boja diska
        target_x_coord = None
        if disc_x_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord] == 'W':
                for i in reversed(range(disc_x_coord)):
                    if self._game_table[i][disc_y_coord] == 'W':

                        while self._game_table[i][disc_y_coord] == 'W':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            i -= 1
                        if i < 0:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'B':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord

    def iterate_north_white(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []  # lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []  # lista mogucih y koordinata za promenu boja diska
        target_x_coord = None
        if disc_x_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord] == 'B':
                for i in reversed(range(disc_x_coord)):
                    if self._game_table[i][disc_y_coord] == 'B':

                        while self._game_table[i][disc_y_coord] == 'B':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            i -= 1
                        if i < 0:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'W':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord

    def iterate_south(self, disc_x_coord, disc_y_coord):
        target_x_coord = None
        x_to_be_changed = []        #lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []        #lista mogucih y koordinata za promenu boja diska
        if disc_x_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord] == 'W':
                for i in range(disc_x_coord, self._row_length):
                    if self._game_table[i][disc_y_coord] == 'W':
                        while self._game_table[i][disc_y_coord] == 'W':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            i += 1
                        if i > 7:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'B':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord

    def iterate_south_white(self, disc_x_coord, disc_y_coord):
        target_x_coord = None
        x_to_be_changed = []        #lista mogucih x koordinata za promenu boja diska (kada crni okruze beli disk, on menja boju)
        y_to_be_changed = []        #lista mogucih y koordinata za promenu boja diska
        if disc_x_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord] == 'B':
                for i in range(disc_x_coord, self._row_length):
                    if self._game_table[i][disc_y_coord] == 'B':
                        while self._game_table[i][disc_y_coord] == 'B':
                            x_to_be_changed.append(i)
                            y_to_be_changed.append(disc_y_coord)
                            i += 1
                        if i > 7:
                            target_x_coord = None
                        else:
                            target_x_coord = i

                        if self._game_table[i][disc_y_coord] == 'W':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, disc_y_coord

    def iterate_east(self, disc_x_coord, disc_y_coord):
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 7:
            if self._game_table[disc_x_coord][disc_y_coord + 1] == 'W':
                for j in range(disc_y_coord, self._column_length):
                    if self._game_table[disc_x_coord][j] == 'W':
                        while self._game_table[disc_x_coord][j] == 'W':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            j += 1
                            if j > 7:
                                target_y_coord = None
                                return disc_x_coord, target_y_coord
                            else:
                                target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'B':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord

    def iterate_east_white(self, disc_x_coord, disc_y_coord):
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 7:
            if self._game_table[disc_x_coord][disc_y_coord + 1] == 'B':
                for j in range(disc_y_coord, self._column_length):
                    if self._game_table[disc_x_coord][j] == 'B':
                        while self._game_table[disc_x_coord][j] == 'B':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            j += 1
                            if j > 7:
                                target_y_coord = None
                                return disc_x_coord, target_y_coord
                            else:
                                target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'W':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord

    def iterate_west(self, disc_x_coord, disc_y_coord):
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 0:
            if self._game_table[disc_x_coord][disc_y_coord - 1] == 'W':
                for j in reversed(range(disc_y_coord)):
                    if self._game_table[disc_x_coord][j] == 'W':
                        while self._game_table[disc_x_coord][j] == 'W':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            j -= 1
                        if j < 0:
                            target_y_coord = None
                        else:
                            target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'B':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord

    def iterate_west_white(self, disc_x_coord, disc_y_coord):
        target_y_coord = None
        x_to_be_changed = []
        y_to_be_changed = []
        if disc_y_coord != 0:
            if self._game_table[disc_x_coord][disc_y_coord - 1] == 'B':
                for j in reversed(range(disc_y_coord)):
                    if self._game_table[disc_x_coord][j] == 'B':
                        while self._game_table[disc_x_coord][j] == 'B':
                            x_to_be_changed.append(disc_x_coord)
                            y_to_be_changed.append(j)
                            j -= 1
                        if j < 0:
                            target_y_coord = None
                        else:
                            target_y_coord = j

                        if self._game_table[disc_x_coord][j] == 'W':
                            self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return disc_x_coord, target_y_coord

    def iterate_south_east(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord + 1] == 'W':
                disc_x_coord += 1
                disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord += 1
                    disc_y_coord += 1
                if disc_x_coord > 7 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_south_east_white(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 7:
            if self._game_table[disc_x_coord + 1][disc_y_coord + 1] == 'B':
                disc_x_coord += 1
                disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord += 1
                    disc_y_coord += 1
                if disc_x_coord > 7 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_north_east(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 7:
            if self._game_table[disc_x_coord - 1][disc_y_coord + 1] == 'W':
                disc_x_coord -= 1
                disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord -= 1
                    disc_y_coord += 1
                if disc_x_coord < 0 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_north_east_white(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 7:
            if self._game_table[disc_x_coord - 1][disc_y_coord + 1] == 'B':
                disc_x_coord -= 1
                disc_y_coord += 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord -= 1
                    disc_y_coord += 1
                if disc_x_coord < 0 or disc_y_coord > 7:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_north_west(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord - 1] == 'W':
                disc_x_coord -= 1
                disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord -= 1
                    disc_y_coord -= 1
                if disc_x_coord < 0 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_north_west_white(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 0 and disc_y_coord != 0:
            if self._game_table[disc_x_coord - 1][disc_y_coord - 1] == 'B':
                disc_x_coord -= 1
                disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord -= 1
                    disc_y_coord -= 1
                if disc_x_coord < 0 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_south_west(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 0:
            if self._game_table[disc_x_coord + 1][disc_y_coord - 1] == 'W':
                disc_x_coord += 1
                disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord += 1
                    disc_y_coord -= 1
                if disc_x_coord > 7 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def iterate_south_west_white(self, disc_x_coord, disc_y_coord):
        x_to_be_changed = []
        y_to_be_changed = []
        target_x_coord = None
        target_y_coord = None
        if disc_x_coord != 7 and disc_y_coord != 0:
            if self._game_table[disc_x_coord + 1][disc_y_coord - 1] == 'B':
                disc_x_coord += 1
                disc_y_coord -= 1
                while self._game_table[disc_x_coord][disc_y_coord] == 'B':
                    x_to_be_changed.append(disc_x_coord)
                    y_to_be_changed.append(disc_y_coord)
                    disc_x_coord += 1
                    disc_y_coord -= 1
                if disc_x_coord > 7 or disc_y_coord < 0:
                    target_x_coord = None
                    target_y_coord = None
                else:
                    target_x_coord = disc_x_coord
                    target_y_coord = disc_y_coord
                if self._game_table[disc_x_coord][disc_y_coord] == 'W':
                    self.change_disc_color(x_to_be_changed, y_to_be_changed)

        return target_x_coord, target_y_coord

    def delete_allowed_fields(self):
        for i in range(self._row_length):
            for j in range (self._column_length):
                if self._game_table[i][j] == '$':
                    self._game_table[i][j] = '*'


if __name__ == '__main__':
    introduction()
    g = GameTable()
    g.fill_hashmap()
    g.mark_allowed_fields()
    g.print_table()

    while True:
        g.is_game_over()
        g.player_turn()
        g.delete_allowed_fields()
        g.is_game_over()
        g.bot_turn()