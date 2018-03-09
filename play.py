#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 14:22:31 2018

@author: yiqian
"""
from P2P import P2P
from Board import BOARD, X, O, Empty
from MiniMax import Node, minMax, AlphaBeta
TeamId="1070"
GameId="1171"


        
def searchNum(input):
    help = '"move"'
    index = 0
    for i in range(10, len(input)):
        if input[i:i+6]==help[:]:
            index = i+8
            break
    num1,num2 = "", ""
    index2 = 0
    for i in range(index, len(input)):
        if input[i]==',':
            num1 = input[index:i]
            index2 = i+1
        if input[i]=='"':
            num2 = input[index2:i]
            break
    
    return int(num1), int(num2)

def play():
    global m, n
    global TeamId, GameId
    
    """
    print('input n')
    n = int(input())
    print('input m')
    m = int(input())
    """
    n = 15
    m = 7
    board = BOARD(n, n, m)
    board.display()
    
    side = True
    new = False
    print('please choose side: x or o')
    choose = input()
    if choose=='x':
        side = True
        status = X
    else:
        side = False
        status = O
        
    deep = 2
    
    if side:
        #print('your turn ' + str(status) + 'input x and y')
        response=P2P.GetMoveList(GameId,1)
        team=response.text[53:57]
        if team!=TeamId:
            x, y = searchNum(str(response.text))
            #x = int(input())
            #y = int(input())
            #side = not side
            new = True
        board.move(x, y, X)
        board.move(int(n/2+1), int(n/2+1), O)
        x, y =int(n/2+1) ,int(n/2+1)
        move=str(x)+','+str(y)
        P2P.MakeMove(TeamId,move,GameId)
        board.display()
        new = not new

    else:
        node = Node(board, deep, status)
        print('wait AI...')
        print('AI done')
        x, y =int(n/2-1) ,int(n/2+1)
        move=str(x)+','+str(y)
        P2P.MakeMove(TeamId,move,GameId)
        print(x, y, status)
        side = not side
        board.move(x, y, status)
        board.display()
        status = X^status^O
        #new = not new
        
        
    
    
    while True:
        
        if side:
            #print('your turn ' + str(status) + 'input x and y')
            response=P2P.GetMoveList(GameId,1)
            team=response.text[53:57]
            if team!=TeamId:
                x, y = searchNum(str(response.text))
                #x = int(input())
                #y = int(input())
                side = not side
                new = True
        else:
            node = Node(board, deep, status)
            print('wait AI...')
            score = AlphaBeta(node)
            print('AI done')
            x, y = node.Pos_i, node.Pos_j
            move=str(x)+','+str(y)
            P2P.MakeMove(TeamId,move,GameId)
            print(x, y, status)
            side = not side
            new = True
        
        
        if new:
            board.move(x, y, status)
            board.display()
        
            if board.check(x, y, status):
                if status == X:
                    print ('X win!')
                    break
                else:
                    print ('O win!')
                    break
            elif board.is_full():
                print ('draw game!')
                break
            else:
                status = X^status^O
                new = not new
                print('your turn ' + str(status) + ' input x and y')

if __name__=='__main__':
    P2P=P2P()
    play()