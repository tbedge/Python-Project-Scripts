# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:59:04 2019

@author: trevo
"""

#Tic Tac Toe Game

#Player X goes 1st, then player O goes 2nd
#Game Board
board = {"A": ["A1","A2","A3"], 
         "B": ["B1","B2","B3"],
         "C": ["C1","C2","C3"]}

def show():
    print("---------------------------------------")
    print(board["A"][0],"|",board["B"][0],"|",board["C"][0])
    print('------------')
    print(board["A"][1],"|",board["B"][1],"|",board["C"][1])
    print('------------')
    print(board["A"][2],"|",board["B"][2],"|",board["C"][2])

show()
turncount = 0
xturns = 0
running = True
while running:
    if turncount % 2 == 1:
        data = input("Player O, choose your position: ")
        if data[0] not in board:
            print()
            print("Invalid position")
            continue
        if int(data[1]) != 1 and int(data[1]) != 2 and int(data[1]) != 3:
            print()
            print("Invalid position")
            continue
        if board[data[0]][int(data[1]) - 1] == "X" or board[data[0]][int(data[1]) - 1] == "O":
            print()
            print("Invalid position")
            continue
        board[data[0]][int(data[1]) - 1] = "O"   
    else:
        data = input("Player X, choose your position: ")
        if data[0] not in board:
            print()
            print("Invalid position")
            continue
        if int(data[1]) != 1 and int(data[1]) != 2 and int(data[1]) != 3:
            print()
            print("Invalid position")
            continue
        if board[data[0]][int(data[1]) - 1] == "X" or board[data[0]][int(data[1]) - 1] == "O":
            print()
            print("Invalid position")
            continue
        board[data[0]][int(data[1]) - 1] = "X"
        xturns = xturns + 1
    print()
    print()
    show()
    if xturns >= 3:
        if board["A"][0] == board["B"][1] == board["C"][2] == "X":
            print("Player X Wins!!!")
            break
        elif board["A"][2] == board["B"][1] == board["C"][0] == "X":
            print("Player X Wins!!!")
            break
        elif board["A"][0] == board["B"][1] == board["C"][2] == "O":
            print("Player O Wins!!!")
            break
        elif board["A"][2] == board["B"][1] == board["C"][0] == "O":
            print("Player O Wins!!!")
            break
        for win in board.keys():
            if board[win][0] == board[win][1] == board[win][2]:
                print("Player " + board[win][0] + " Wins!!!")
                running = False
                break
        for i in range(0, 3):
            if board["A"][i] == board["B"][i] == board["C"][i]:
                print("Player " + board["A"][i] + " Wins!!!")
                running = False
                break          
    if running == False:
        break
    turncount = turncount + 1
    if turncount == 9:
        print("Players have tied!!!")
        break