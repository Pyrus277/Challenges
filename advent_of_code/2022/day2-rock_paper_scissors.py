# AOC Day 2 - Rock Paper Scissors

'''
Procedure:
0. Read in data and put it into a structure
1. Calculate the base score total based on what was selected:
    x = 1, y = 2, z = 3
2. Calculate the outcome score total based on opponent's move:
    A: x = 3, y = 6, z = 0 
    B: x = 0, y = 3, z = 6
    C: x = 6, y = 0, z = 3
3. Sum these two totals for the answer
'''
import pandas as pd
df = pd.read_csv('day2.txt', delimiter=' ', 
                 header=None, names=['opponent','you'])
# Part 1
# Integers in the dictionary maps the constant value score component for the move,
# and then the round outcome score component like (constant + round)
score_dict = {'A':{'X':1+3,'Y':2+6,'Z':3+0},'B':{'X':1+0,'Y':2+3,'Z':3+6},
              'C':{'X':1+6,'Y':2+0,'Z':3+3}}
def score(opp, you):
    return score_dict[opp][you]

df['score'] = df.apply(lambda x: score(x.opponent, x.you), axis =1) 

print(df.score.sum())


# Part 2
# Integers in the dictionary maps the constant value score for the round outcome,
# and then the move score component, like (round + constant)
score_dict_2 = {'A':{'X':0+3,'Y':3+1,'Z':6+2},'B':{'X':0+1,'Y':3+2,'Z':6+3},
                'C':{'X':0+2,'Y':3+3,'Z':6+1}}
def score_2(opp, you):
    return score_dict_2[opp][you]

df['score'] = df.apply(lambda x: score_2(x.opponent, x.you), axis =1) 

print(df.score.sum())





