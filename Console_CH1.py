# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 09:50:26 2023

@author: Owner

"""

import random
import math
money = 1000
health = 10
hapiness =10

def CH_1():
    global money, hapiness, health
    
    count = 0
    
    while count < 7:
        if count == 0:
            print('MONDAY------------------------------------------------------')
        elif count == 1:
            print('TUESDAY-----------------------------------------------------')
        elif count == 2:
            print('WEDNESDAY---------------------------------------------------')
        elif count == 3:
            print('THURSDAY----------------------------------------------------')
        elif count == 4:
            print('FRIDAY------------------------------------------------------')
        elif count == 5:
            print('SATURDAY----------------------------------------------------')
        else:
            print('SUNDAY------------------------------------------------------')
            
        print('As a student, Sunny knew that there were scholarships, bursaries and grants at her post secondary school. Please help her to choose from one of the given options below. She will finish the chosen task by the end of the day and your health, finance and happiness level will vary accordingly. ')
        
        print('1. Apply for a scholarship') #1/10 chances to be picked. finance $1000-$3,500, happiness +1 if picked and hapiness -1 if not picked
        print('2. Eat out') #health +1, finance minus $30-$50, happiness +2
        print('3. Apply for a bursary') #1/5 chances to be picked. Finance $500-$1750, happiness +1 if picked and hapiness -1 if not picked
        print('4. Cook and eat at home') #health +2, finance minus $10 - $20, happiness +1
        print('5. Apply for a grant') #1/3 chances to be picked. Finance $200-$500 happiness +1 if picked and hapiness -1 if not picked
        
        print('Please enter a number from 1 to 5.')
        choice = input()
        choice = int(choice)
        while (choice>5 or choice<1):
            print('Please enter a number from 1 to 5 only.')
            choice = int (input())
        
        a = 0
        chance = random.randint(0, 100)
        if choice == 2:
            health +=1
            money -= random.randint(30, 50)
            hapiness +=2
        elif choice == 4:
            health +=2
            money -= random.randint(10, 20)
            hapiness +=1
        elif choice ==1: 
            if chance >= 90:
                a = random.randint(1000, 3500)
                hapiness += 1
        elif choice ==3: 
            if chance >=50:
                a = random.randint(500, 1750)
                hapiness += 1
        elif choice == 5:
            if chance >=30:
                a = random.randint(200, 500)
                hapiness += 1
        else:
            hapiness
            hapiness -=1 
            
        money += a
        
        if count == 6:
            print( 'Health: ', health, 'Hapiness:', hapiness, 'Money: ', money)
        count+=1
        print('\n')
        
    return 'Throughout last week, Sunny learned that it is not the best idea to rely solely on scholarships, bursaries or grants as there are a lot of competitors and the chances of getting selected is relatively small. In the last game, Scholarships had 1/10 chances to be awarded, bursaries had 1/5 chances and grants had 1/3 chances of being awarded. In the real world, however, the chances are much less. Thus, she decided to not only rely on scholarships, but to also find a job to earn a stable income. \n'

print(CH_1())