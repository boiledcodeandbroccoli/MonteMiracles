#!/usr/bin/env python3.6
from collections import Counter
import random
import matplotlib.pyplot as plt

'''
This is my paper build
'''


num_iterations = 100000 # Number of times we want to do this
cards_seen = 7 # Always = 7 for an opening hand.

decklist = {'Plains': 2, 'Islands': 6, 'Blue_Fetches': 8, 'Arid_Mesa': 1, 'Tundra': 2, 'Cantrips':11, 'Others': 30} # Creating the decklist
deck = []
for card in decklist.keys():
    deck += [card] * decklist[card]

# Simulation loops

count_island_cantrip = 0 #counts how many times we have BASIC ISLANDS + 1 cantrip in our hand.
count_flood = 0 #counts how many times we have 4+ landers i.e, flooding
count_blue = 0 #counts all blue sources
count_no_lands = 0 #Should also calculate for zero landers bc that is also a mulligan. Also a 1 lander with zero cantrips. Should blue source be not accounting for Tundras?
count_no_cantrips = 0 # zero cantrips :(
cantrip_only = 0 #only the cantrip cartel.
good_lands_only = 0 #only Basic Islands + all the blue fetches.
count_all_lands = 0 #counts all lands in the deck.
count_island_only = 0 #for debugging purposes


for _ in range(num_iterations):
    draw = Counter(random.sample(deck, cards_seen)) 
    
''' 
draw function tells Python to randomly select 7 cards from the decklist, and count how many types of cards are in it.
random.sample(deck, cards_seen) takes a random saple of 'cards_seen' (the opening 7 card hand) from our created decklist.
The random 7 card sample gets fed into the 'Counter' function, which then gives a dictionary that is used to look up how many
of each card was in the given sample.
'''     
    count_island_cantrip += (min(draw['Islands'], 1) + min(draw['Cantrips'], 1) >= 2) # minimum of 1 Basic Island AND at least 1 Cantrip
    count_flood += (draw['Islands'] + draw['Blue_Fetches'] + draw['Plains'] + draw['Arid_Mesa'] + draw['Tundra'] >= 4) # drawing a 4 lander in the 7
    count_no_lands += (draw['Islands'] + draw['Blue_Fetches'] + draw['Arid_Mesa'] + draw['Tundra'] == 0) # the good ol' no lander
    count_no_cantrips += (draw['Cantrips'] == 0) # use this to calculate zero cantrips in the opener
    cantrip_only += (min(draw['Cantrips'], 1) >= 1) #drawing at least 1 cantrip
    good_lands_only += (min(draw['Islands'], 1) + min(draw['Blue_Fetches'], 1) >= 1) # minimum of having at least 1 land in your opener but no Tundra + no Mesa
    count_all_lands += (min(draw['Islands'], 1) + min(draw['Blue_Fetches'], 1) + min(draw['Arid_Mesa'], 1) + min(draw['Tundra'], 1) >=1) #trying to use this to tally up all blue sources with a minimum of 1 appearance in the hand
    count_island_only += (draw['Islands'] >= 1) 


# Printing results

for card, number in decklist.items():
    print(card + ': ' + str(number) + '\t', end='')
print()
print('Amount of times we hit BASIC ISLAND + 1 cantrip:                 \t' + str(round(count_island_cantrip / num_iterations,3)))
print('Amount of 4 land openers:                                        \t' + str(round(count_flood / num_iterations,3)))
print('Amount of times we hit Non-Wastable blue source + 1 cantrip:     \t' + str(round((cantrip_only / num_iterations) * (good_lands_only / num_iterations) ,3))) 
print('Amount of times we hit any blue source + 1 cantrip:              \t' + str(round((cantrip_only / num_iterations) * (count_all_lands / num_iterations) ,3))) 
print('Amount of ZERO land openers:                                     \t' + str(round(count_no_lands / num_iterations,3)))
print('Amount of ZERO cantrip opener:                                   \t' + str(round(count_no_cantrips / num_iterations,3)))

#debugging stuff
#print('Testing print of iterations  - only islands                      \t' + str(round(count_island_only,3)))
#print('Testing print of iterations  - only cantrips                     \t' + str(round(cantrip_only,3)))
