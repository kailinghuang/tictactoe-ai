#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 20:29:16 2018

@author: yiqian
"""


X = 1
O = -1
Empty = 0
Dead = -2
Column = 15
Row = 15
m=7

class Error(Exception):
    def __init__(self, arg):
        self.args = arg

class BOARD():
    
    def __init__(self,  Column_Num, Row_Num, m_Num, plane=None):
        global Row, Column, m
        if plane==None:
            self.Board = [[Empty]*Column_Num for i in range(Row_Num)]
            Column = Column_Num
            Row = Row_Num
            m = m_Num
        else:
            self.Board = plane
            
    def get(self, x, y):
        if x<0 or x>=Row or y<0 or y>= Column:
            return Empty
        else:
            return self.Board[x][y]
        
    def move(self, x, y, player):
        if 0<=x<Row and 0<=y<Column:
            if self.Board[x][y]!=Empty:
                raise Error(['Error: The Place is not empty!'])
            self.Board[x][y] = player
        else:
            raise Error(['Error: Move beyond board:(%d, %d)'%(x, y)])
            
    def check(self, x, y, player):
        Check_Row = True
        Check_Column = True
        Check_Diagonal1 = True
        Check_Diagonal2 = True
        pos = self.Board[x][y]
        if pos == Empty:
            return False
        
        #check row
        for i in range(x-(m-1), x+m):
            Check_Row = True
            for j in range(m):
                if self.get(i+j, y)!=player:
                    Check_Row = False
            if Check_Row:
                return True
        
        #check column
        for i in range(y-(m-1), y+m):
            Check_Column = True
            for j in range(m):
                if self.get(x, i+j)!=player:
                    Check_Column = False
            if Check_Column:
                return True
        
        #check diagonal \
        k = y-m+1
        for i in range(x-(m-1), x+m):
            Check_Diagonal1 = True
            for j in range(m):
                if self.get(i+j, k+j)!=player:
                    Check_Diagonal1 = False
            if Check_Diagonal1:
                return True
            k+=1
        
        k = y+m-1
        for i in range(x-(m-1), x+m):
            Check_Diagonal2 = True
            for j in range(m):
                if self.get(i+j, k-j)!=player:
                    Check_Diagonal2 = False
            if Check_Diagonal2:
                return True
            k-=1
        
        return False
    
    def is_full(self):
        for i in range(Row):
            for j in range(Column):
                if self.Board[i][j]==Empty:
                    return False
        return True
    
    def display(self):
        for i in range(Row):
            temp = []
            for j in range(Column):
                if self.Board[i][j]==Empty:
                    temp1 = ' '
                elif self.Board[i][j] == X:
                    temp1 = 'X'
                else:
                    temp1 = 'O'
                temp.append(temp1)
            line = '%s|%s|'%(" ", '|'.join(temp))
            print(line)
            
if __name__ == '__main__':
    t = Board(15, 15, 5)
    Board()
    Board
    t.display()
"""
    j = 10
    for i in range(8, 8+5):
        t.move(i, j, X)
        print(t.check(i, j, X))
        j-=1
    t.display()
"""    
            
            
    