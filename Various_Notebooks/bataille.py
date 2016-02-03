# -*- coding: utf-8 -*-
"""
Jeu de la bataille

@author: JH218595
"""

import matplotlib.pyplot as plt
import numpy as np

def new_card_set():
    '''
    Creates an returns a brand new card set.
    '''
    cards = []
    cards_nb = list(range(9,15)) # 
    cards_sym= list(['P', 'C', 'Q', 'T'])
    for nb in cards_nb:
        for sym in cards_sym:
            cards.append((nb, sym))
    return cards
    
def sort_cards(cards):   
        '''
        Creates two card sets A and B from a new card set
        '''    
        from numpy.random import randint
        A = []
        B = []
        while len(cards) != 0: # tant que le paquet n'est pas vide on distribue
            A.append(cards.pop(randint(low=0, high=len(cards))))
            B.append(cards.pop(randint(low=0, high=len(cards))))
        return A, B

def play_bataille(A,B):
    '''
    Joue à la bataille et retourne l'évolution du nombre de cartes par joueur
    au cours d'une partie.
    '''
    manche_A = []
    manche_B = []
    
    taille_A = []
    taille_B = []
    
    continuer = True
    
    while continuer:
        taille_A.append(len(A))
        taille_B.append(len(B))
    
#        if len(taille_B)>100: # trop de manche, on arrête la partie 
#            continuer = False
        if len(A) == 0:
            #print('### B gagne la partie ###')
            continuer = False
        elif len(B) == 0:
            #print('### A gagne la partie ###')
            continuer = False
        else:
            manche_A.append(A.pop())
            manche_B.append(B.pop())
            
            if manche_A[-1][0] == manche_B[-1][0]:
                #print('Bataille !!')
                pass
            elif manche_A[-1][0] > manche_B[-1][0]:
                #print('A remporte la manche')
                A = manche_A + manche_B + A
                manche_A.clear()
                manche_B.clear()
            else:
                #print('B remporte la manche')
                B = manche_B + manche_A + B
                manche_A.clear()
                manche_B.clear()

    return taille_A, taille_B
                
cards = new_card_set()
A, B = sort_cards(cards)
taille_A, taille_B = play_bataille(A, B)
                
plt.figure(1)
plt.clf()
plt.plot(taille_A, lw=2)
plt.plot(taille_B, lw=2)  
plt.xlabel('Nombre de manches')
plt.grid(True)          

# fait un nombre N de partie et affiche les statistiques
def play_N_batailles(N):
    nb_manches = []
    for idx in range(N):
        cards = new_card_set()
        A, B = sort_cards(cards)
        taille_A, taille_B = play_bataille(A, B)
        nb_manches.append(len(taille_A))
    return nb_manches

N = 10000
nb_manches = np.array(play_N_batailles(N))


plt.figure(2)
plt.hist(nb_manches, bins=500, color='b', alpha=0.5)

from scipy.stats import gamma 

params = gamma.fit(nb_manches)

x = np.arange(1, N)
#plt.figure(3)
plt.plot(x, 2*N*gamma.pdf(x, *params[:-2], loc=params[-2], scale=params[-1]),
                          lw=2, color='r')
plt.xlim(0, 300)