"""
Usage:
        tictac start
        tictac start [option] [value]

        options:
                -n    (Number of players)
                -r    (Number of rounds)
                -d    (Wait time in seconds)
"""
# Author:	Adeoti Warith Adetayo
# Program:	TIC-TAC-TOE Game
# Date:	        August 18, 2020
#The Tic-Tac-Toe Game

import random
import time
from os import system
from string import ascii_uppercase
from platform import system as ostype
import sys


playerType = {'1':'Computer', '2':'Human'}
WAIT_TIME = 3
DELAY_TIME = 1


#Function Clear Screen
def clear_screen():
        if ostype() == 'Linux' or ostype() == 'Darwin':
                system('clear')
        elif ostype() == 'Windows':
                system('cls')

class Player:
        def __init__(self, playerType, alias, playerCap=1):
                self.name = alias
                self.playerType = playerType
                self.playerCap = playerCap
                self.score = 0

        def move(self):
                aSpace = tic_tac.THE_BOARD.availableSpace()
                if self.playerType == playerType['1']:
                        move = self.computerMove(aSpace)
                else:
                        while True:
                                move = input()
                                if move in aSpace:
                                        break
                                elif move in GameBoard.moveNumbers:
                                        print('Space is filled')
                                else:
                                        print(f'Invalid input (Choose {", ".join(aSpace[0:-1])} or {aSpace[-1]})')
                return move

        def computerMove(self, space):
                time.sleep(WAIT_TIME)
                if self.playerCap == 1:
                        rn = random.randrange(0, len(space))
                        return space[rn]
                board_copy = GameBoard()
                board_copy.board = dict(tic_tac.THE_BOARD.board)
                for player in self.playerAlias():
                        for i in space:
                                board_copy.update(i, player)
                                if board_copy.checkWinnings():
                                        return i
                                board_copy.update(i, " ")
                rn = random.randrange(0, len(space))
                return space[rn]

        def updateScore(self):
                self.score += 1

        def playerAlias(self):
                alias = [self.name]
                return alias + [i.name for i in tic_tac.players.values() if i.name != self.name]


class GameBoard:
        moveNumbers = ('1', '2', '3', '4', '5', '6', '7', '8' '9')
        def __init__(self):
                self.board =    {       'top-L':' ', 'top-M':' ', 'top-R':' ',
                                        'mid-L':' ', 'mid-M':' ', 'mid-R':' ',
                                        'low-L':' ', 'low-M':' ', 'low-R':' '   }

                self.core =     {       '1':'top-L', '2':'top-M', '3':'top-R',
                                        '4':'mid-L', '5':'mid-M', '6':'mid-R',
                                        '7':'low-L', '8':'low-M', '9':'low-R'   }
        def print_board(self):
                print("    " + self.board['top-L'] + "    " + '|' + "    " + self.board['top-M'] + "    " + '|' + "    " + self.board['top-R'] + "    ")
                print("---------" + '*' + "---------" + '*' + "---------")
                print("    " + self.board['mid-L'] + "    " + '|' + "    " + self.board['mid-M'] + "    " + '|' + "    " + self.board['mid-R'] + "    ")
                print("---------" + '*' + "---------" + '*' + "---------")
                print("    " + self.board['low-L'] + "    " + '|' + "    " + self.board['low-M'] + "    " + '|' + "    " + self.board['low-R'] + "    ")

        def update(self, num, alias):
                #To add place new alias in any position on the board
                self.board[self.core[num]] = alias

        def space(self):
                return self.board.values()

        def availableSpace(self):
                """aSpace = []
                for i in range(1, 10):
                        if self.board[self.core[str(i)]] == ' ':
                                aSpace.append(str(i))
                return aSpace"""
                return [str(i) for i in range(1, 10) if self.board[self.core[str(i)]] == ' ']

        def clean(self):
                self.__init__()

        def checkWinnings(self):
                return  (self.board['top-L'] == self.board['top-M'] == self.board['top-R'] != ' ') or \
                        (self.board['mid-L'] == self.board['mid-M'] == self.board['mid-R'] != ' ') or \
                        (self.board['low-L'] == self.board['low-M'] == self.board['low-R'] != ' ') or \
                        \
                        (self.board['top-L'] == self.board['mid-L'] == self.board['low-L'] != ' ') or \
                        (self.board['top-M'] == self.board['mid-M'] == self.board['low-M'] != ' ') or \
                        (self.board['top-R'] == self.board['mid-R'] == self.board['low-R'] != ' ') or \
                        \
                        (self.board['top-L'] == self.board['mid-M'] == self.board['low-R'] != ' ') or \
                        (self.board['top-R'] == self.board['mid-M'] == self.board['low-L'] != ' ') 


class GamePlay:
        def __init__(self, numberOfPlayers=2, numberOfRounds=None):
                self.playerNumbers = numberOfPlayers
                self.numberOfRounds = numberOfRounds
                self.round = 0
                if self.playerNumbers > 3:
                        raise ValueError ('Number of possible players exceeded')
                self.players = {}
                self.validAlias = list(ascii_uppercase)


                for i in range(self.playerNumbers):
                        print('Player ' + str(i+1) + ': Choose Player Type')
                        print('1. Computer Player\n2. Human Player')
                        while True:
                                userIn = input()
                                if userIn == '1' or userIn == '2':
                                        break
                                else:
                                        print('Invalid input: (Choose 1 or 2 for player type)')
                        if userIn == '1':
                                rn = random.randrange(len(self.validAlias))
                                alias = self.validAlias[rn]
                                print("Choose Difficulty Level for your Computer Player")
                                print("1. Dumb\n2. Smart")
                                while True:
                                        userIn2 = input()
                                        if userIn2 in ("1", "2"):
                                                playerCap = int(userIn2)
                                                break
                                        else:
                                                print('Invalid input: (Choose 1 or 2 for Difficulty Level)')
                        else:
                                print('Choose an alias: ', end='')
                                while True:
                                        alias = input().upper()
                                        if alias in self.validAlias:
                                                break
                                        elif alias in ascii_uppercase:
                                                print('Alias Taken!!!')
                                        else:
                                                print('Invalid Alias: Choose(A - Z)')
                                playerCap = None
                        self.validAlias.remove(alias)
                        self.players[i+1] = Player(playerType[userIn], alias, playerCap)
                        setattr(self.players[i+1], 'playerNum', i+1)
                        print(self.players[i+1].playerType + ': ' + self.players[i+1].name)
                        print('\n')
                print('\n\n')
                for i, j in self.players.items():
                        print(f'Player {i} ({j.playerType}): \t{j.name}')
                print('\n\n')
                self.THE_BOARD = GameBoard()

        def instruction(self):
                print('Welcome to Tic-Tac-Toe\n')
                for i in range(1,10):
                        self.THE_BOARD.update(str(i), str(i))
                self.THE_BOARD.print_board()
                print('To play, choose number (1 - 9) to move your alias to\nthe corresponding space on the board\n')
                self.THE_BOARD.clean()
                print('\n\n')
                print('Press Enter to start')
                input()
        
        def winner(self):
                highest_score = max([player.score for player in self.players.values()])
                if highest_score == 0:
                        return []
                winners = [player for player in self.players.values() if player.score == highest_score]
                return winners
        
        def printWinnerLeaderBoard(self):
                winner = self.winner()
                w_msg = 'Winners' if len(winner) > 1 else 'Winner'
                print(f"\nThe {w_msg} for this game")
                print('-' * len(f"\nThe {w_msg} for this game"))
                for player in winner:
                        print(f'Player {player.playerNum} ({player.name})\tTotal Winnings: {player.score}\t({player.playerType} Player)')
                if len(winner) == self.playerNumbers:
                        print('\t' + '-' * len("|A tie Game!!!|"))
                        print('\t|A tie Game!!!|')
                        print('\t' + '-' * len("|A tie Game!!!|"))
                print("\n\nThanks for playing, Bye!!!")
        
        def gameStart(self):
                for i in range(5,-1,-1):
                        clear_screen()
                        print('GAME WILL START IN' + '.' * (6-i))
                        print(i)
                        time.sleep(DELAY_TIME)
                time.sleep(DELAY_TIME)

        def mainStart(self):
                #self.gameStart()
                clear_screen()

                self.round += 1
                print(f"ROUND {self.round}\n")

                print('The Board\n')
                self.THE_BOARD.print_board()
                print()

                player = 1
                while ' ' in self.THE_BOARD.space():
                        if player > len(self.players):
                                player = 1
                        currentPlayer = self.players[player]
                        print(f'Player {player} ({currentPlayer.name}) : move your alias')
                        move  = currentPlayer.move()
                        self.THE_BOARD.update(move, currentPlayer.name)
                        print()
                        self.THE_BOARD.print_board()
                        if self.THE_BOARD.checkWinnings():
                                print('\nWe have a winner for this round!!!')
                                print(f"Player {player}:", currentPlayer.name)
                                currentPlayer.updateScore()
                                print("\n")
                                break
                        player += 1
                        print('\n\n')
                if not self.THE_BOARD.checkWinnings():
                        print("A Tie: No winner in this round")
                        print("\n")
                
                msg = 'Round'
                if self.round > 1:
                        msg += 's'
                print(f'Winning Streaks\t({msg}: {self.round})')
                print('-' * len(f'Winning Streaks\t({msg}: {self.round})'))
                for i, player in self.players.items():
                        print(f'Player {i} ({player.name})\tScore: {player.score}\t({player.playerType})')
                print('\n\n')
                
                if self.numberOfRounds:
                        if self.round == self.numberOfRounds:
                                self.printWinnerLeaderBoard()
                        else:
                                self.THE_BOARD.clean()
                                self.mainStart()
                else:  
                        print('1. Go another\n2. Quit Game')
                        userIn = input()
                        if userIn == '1' or userIn == '':
                                self.THE_BOARD.clean()
                                self.mainStart()
                        elif userIn == '2':
                                self.printWinnerLeaderBoard()

        def play(self):
                self.instruction()
                self.gameStart()
                self.mainStart()

def main():
        print("TIC-TAC-TOE")
        print("\n")
        arg = sys.argv[1:]
        
        if len(arg) > 0:
                if arg[0] == "--usage":
                        print(__doc__)
                        raise SystemExit
                elif arg[0] == "start":
                        # Options
                        # -n    Number of players
                        # -r    Number of rounds
                        # -d    Wait time in seconds
                        arg = arg[1:]

                        if len(arg) == 0:
                                gamePlayArgs = (2,)
                        else:
                                validOptions = {"-n":"Number of Player", "-r":"Number of Rounds", "-d": "Wait Time"}
                                options = [option for option in arg if option.startswith("-")]
                                values = [value for value in arg if value not in options]
                                if len(options) > 3 or len(options) != len(values):
                                        print("Invalid Arguments")
                                        print(__doc__)
                                        raise SystemExit
                                optionValue = {options[i]:values[i] for i in range(len(options)) if options[i] in validOptions}
                                if len(optionValue) == 0:
                                        print("Invalid Arguments")
                                        print(__doc__)
                                        raise SystemExit
                                uValues = []
                                for option in validOptions:
                                        value = optionValue.get(option)
                                        if value != None:
                                                try:
                                                        value = int(value)
                                                except:
                                                        print(f"({value}) <-- Invalid value for " + validOptions[option])
                                                        raise SystemExit
                                        uValues.append(value)
                                if uValues[0] == None:
                                        uValues[0] = 2
                                if uValues[2] != None and uValues[2] >= 0:
                                        global WAIT_TIME
                                        WAIT_TIME = uValues[2]
                                gamePlayArgs = tuple(uValues[:2])
                else:
                        print(f"({arg[0]}) Invalid Option")
                        raise SystemExit
        else:
                print(__doc__)
                raise SystemExit 
        global tic_tac      
        tic_tac = GamePlay(*gamePlayArgs)
        tic_tac.play()

if __name__ == "__main__":
        try:
                main()
        except KeyboardInterrupt:
                print("\nQuiting Program!!!")
