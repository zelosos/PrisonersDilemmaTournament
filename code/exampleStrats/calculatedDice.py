import random

def strategy(history, memory):
  """
  Author: zelosos

  Lets write down some assumptions:
    - In a group most of the players will not be exploited.
    - Players will test, if they can exploit others.
    - Both cooperating for the hole time is best for both.

  With this said:
    - target should be: both coorperate for the hole time

  Improvements:
    - Later into the game it is beneficial to abuse the build up trust. So increase the cheat chance for longer games.
    - Maybe this could be improved by the weights of the score matrix, but I have to go to bed now.
  """
  # start with cooperate
  if len(history[1]) == 0:
    return 1, None
  
  played_rounds = len(history[1])
  got_wasted = len(history[1])-sum(history[1]) # how often we got cheated
  if random.uniform(0, 1) < got_wasted/played_rounds: # how often we got cheated determin how likely it is to cheat back
    return 0, None
  return 1, None
