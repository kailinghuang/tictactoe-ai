#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:23:10 2018

@author: yiqian
"""

from Board import  X, O, Empty, Dead, Row, Column, m

live_score = [0]         #huo
temp_live_score = 1
jump_score = [0, 0]      #tiao
temp_jump_score = 8
sleep_score = [0, 0]        #mian
temp_sleep_score = 6
sleep_jump_score = [0, 0]   #sleep jump
temp_sleep_jump_score = 4
dead_score = [0 for i in range(m)]     #dead
dead_jump_score = [0 for i in range(m-1)]

Max_score = pow(10, m-1)                               #100000...
Second_score = int(Max_score/10 - (Max_score/100))     #900..
Third_score = int(Max_score/10 - 5*(Max_score/100))    #500....

#live score
for i in range(m):
    live_score.append(temp_live_score)
    temp_live_score *= 10

#jump score
for i in range(m-2):
    jump_score.append(temp_jump_score)
    temp_jump_score *= 10
jump_score.append(Second_score)

#dead score
dead_score.append(Max_score)
    
#sleep score
for i in range(m-3):
    sleep_score.append(temp_sleep_score)
    temp_sleep_score *= 10
sleep_score.append(int(temp_jump_score/10))
sleep_score.append(Max_score)

#sleep jump score
for i in range(m-2):
    sleep_jump_score.append(temp_sleep_jump_score)
    temp_sleep_jump_score *= 10
sleep_jump_score.append(int(temp_jump_score/10))

#dead jump score
dead_jump_score.append(Third_score)
dead_jump_score.append(Third_score)





def evaluate(line):
    # Step 1: calculate the number of same
    item = [[line[0], 1, False]]
    index = 0
    for i in range(1, len(line)):
        if line[i] == item[index][0]:
            item[index][1] += 1
        else:
            index += 1
            item.append([line[i], 1, False])
    merge_item = [item[0]]
    
    # Step 2: combine
    i = 1
    while i<len(item)-1:
        player, player_num, _ = item[i]
        last_player, last_player_num, _ = item[i-1]
        after_player, after_player_num, _ = item[i+1]
        
        if player==Empty and player_num == 1 and last_player == after_player and last_player != Empty and last_player_num < (m-1) and after_player_num < (m-1):
            #exist Empty
            it = (last_player, last_player_num+after_player_num, True)
            if merge_item[-1][2] == False:
                merge_item.pop()
            else:
                merge_item.append((Empty, 1, False))
            merge_item.append(it)
            i+=2
        else:
            #no Empty
            merge_item.append(item[i])
            i += 1
    
    if i<len(item):
        merge_item.append(item[-1])
        
    merge_item = [(Dead, 1, False)] + merge_item + [(Dead, 1, False)]
        
    # Step 3: calculate score
    score = {X:[0, 0], O:[0, 0]}
    
    for i in range(1, len(merge_item)-1):
        player, player_num, flag = merge_item[i]
        last_player, last_player_num, last_flag = merge_item[i-1]
        after_player, after_player_num, after_flag = merge_item[i+1]
        
        if player == Empty:
            continue
        
        player_num = m if player_num >= m else player_num
        
        if flag == False and player_num >= m:
            # m in a line
            #print('m in line')
            score[player][0] += live_score[player_num]
        elif last_player == after_player == Empty:
            if flag == False:
                # live point
                #print('live')
                score[player][0] += live_score[player_num]
            else:
                # jump point
                #print('jump')
                score[player][0] += jump_score[player_num]
        elif ((last_player == Empty and after_player != player) or (last_player != player and after_player == Empty)):
            if flag == False:
                # sleep point
                #print('sleep')
                score[player][0] += sleep_score[player_num]
            else:
                # sleep jump point
                #print('sleep jump')
                score[player][0] += sleep_jump_score[player_num]
        else:
            if flag == False:
                # dead point
                #print('dead')
                score[player][0] += dead_score[player_num]
            else:
                # dead jump point
                #print('dead jump')
                score[player][0] += dead_jump_score[player_num]
    
    """
    print(len(merge_item))
    print(merge_item)
    print(live_score)
    print(jump_score)
    print(sleep_score)
    print(sleep_jump_score)
    print(dead_score)    
    print(dead_jump_score)
    print(score)
    """
    return score

if __name__ == '__main__':
    line = [0,0,  1, 1, 1, 1,  0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(line)
    score = evaluate(line)
    
    
