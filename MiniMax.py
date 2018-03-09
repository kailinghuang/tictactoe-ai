#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 20:20:09 2018

@author: yiqian
"""

from Board import BOARD, Row, Column, m , X, O, Empty
from evaluate import evaluate, Max_score
from copy import deepcopy

class Node():
    def __init__(self, Board, deep, status):
        self.Board = Board
        self.status = status
        self.deep = deep
        self.Pos_i = -1
        self.Pos_j = -1
    
    def move(self, i, j, status):
        self.Board.move(i, j, status)
    

    # generate node    
    def traverse(self):
        for i in range(Row):
            for j in range(Column):
                if self.Board.Board[i][j] != Empty:
                    continue
                # jump, if there is no piece in two steps
                next_status = X^self.status^O    # exchange turn 
                new_node = Node(deepcopy(self.Board), self.deep-1, next_status)
                new_node.move(i, j, self.status)
                
                yield new_node, i, j
                
    def evaluateNega(self):
        return - self.evaluate()
    
    def evaluate(self):
        # get the status from 4 direction
        
        # Step 1:  get vector
        vecs = []
        # get row
        for i in range(Row):
            #print(self.Board.Board[i])
            vecs.append(self.Board.Board[i])
        # get column
        for j in range(Column):
            vecs.append([self.Board.Board[i][j] for i in range(Row)])
       
        # get diagonal \
        vecs.append([self.Board.Board[x][x] for x in range(Row)])
        for i in range(1, Row-m+1):
            vec = [self.Board.Board[x][x-i] for x in range(i, Row)]                  #lower diagonal
            vecs.append(vec)
            vec = [self.Board.Board[y-i][y] for y in range(i, Column)]         #upper diagonal
            vecs.append(vec)
        
        #get diagonal /
        for i in range(m-1, Row-1):
            vec = [self.Board.Board[x][i-x] for x in range(i, -1, -1)]          #upper diagonal
            vecs.append(vec)
            vec = [self.Board.Board[x][Column-x+Row-i-2] for x in range(Row-i-1, Row)]       #lower diagonal
            vecs.append(vec)
        
            
        # Step 2: calculate every vec, get sum
        
        board_score = 0
        for vec in vecs:
            score = evaluate(vec)
            if self.status == X:
                # last player is X, calculate O score
                board_score += score[O][0] - score[X][0] - score[X][1]
            else:
                # last player is O, calculate X score
                board_score += score[X][0] - score[O][0] - score[X][1]
                
        return board_score
    
def minMax(node):
    if node.deep <= 0:
        score = node.evaluateNega()
        return score
    score = -100000000
    for new_node, i, j in node.traverse():
        new_score = -minMax(new_node)
        if new_score > score:
            score = new_score
            node.Pos_i, node.Pos_j = i, j
    return score
    
def AlphaBeta(node, alpha =-Max_score, beta=Max_score):
    if node.deep <= 0:
        score = node.evaluateNega()
        return score
        
    for new_node, i, j in node.traverse():
        new_score = -AlphaBeta(new_node, -beta, -alpha)
        if new_score > beta:
            return beta
        if new_score > alpha:
            alpha = new_score
            node.Pos_i, node.Pos_j = i, j
    return alpha

if __name__ == '__main__':
    board = Board(15, 15, 5)
    node = Node(board, 10 , X)
    
    AlphaBeta(node)
        