#!/usr/bin/env python3

import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

modes = ['random', 'reflect', 'repeat','cycle']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class Random_Player(Player):
    def move(self):
        return random.choice(moves)

class Reflect_Player(Player):
    def move(self):
        # print(f'The player mode is  {Player.move(self)} and the type: {type (Player.move(self))}')
        return Player.move(self)

class


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def intro():
    print("Here are the rules of the game: scissor cuts paper,paper "
          "covers rock, and rock crushes scissors.")
    print("Play either 'rock', 'paper', or 'scissors'")
    print("If you want to stop playing, enter a 'q'.")
    selected_mode = None
    while True:
        choice = input("Who would you like to play with? Please enter "
                       "'random', 'reflect', 'repeat', or 'cycle':")
        if choice in modes:
            selected_mode = select_mode(choice)
            break
        elif choice == 'q':
            print('Ok, bye!')
            exit()
        else:
            print('Sorry, not a valid choice. Try ')
    return selected_mode


def select_mode(mode):
    print('begin select_mode')
    if mode == 'random':
        return Random_Player
    elif mode == 'reflect':
        return Reflect_Player
    else:
        print('Sorry that mode is not implemented yet')
        exit()



class Game:
    print('inside GAAME CLASS')
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    opponent = intro()
    game = Game(Player(), opponent())
    game.play_game()