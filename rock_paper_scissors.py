#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
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

    player_name = False
    if not player_name:
       player_name = input('Please enter player\'s name: ')


        # print("Game over!")
        print('Here are the rules:')
        print('To stop playing enter z')
        control = input('Who would you like to play with?')
        throw = input('What would you like to throw?')
        while throw.lower() != 'z':

            print ('inside the game!')
            


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
