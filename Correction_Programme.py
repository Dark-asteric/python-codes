#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# =============================================================================
#                                 CORRECTION

# Programme permettant d'afficher les positions successives du skieur, le plan
# incliné et les vecteurs vitesse toutes les 2 positions successives

# Questions B/
# Compléter les lignes 25 à 43.
# Question C/
# Supprimer les guillemets des lignes 44 et 55.

# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from math import tan, pi

# Définition du plan incliné NE PAS MODIFIER ==================================
x = np.linspace(0,120,20)
y = tan(-35*pi/180)*x

# Demander d'entrer le nombre de positions successives N à représenter=========
N = int(input('Nombre de positions à représenter N= '))

# Demander d'entrer l'intervalle de temps ∆t (en s) entre 2 positions successives
Delta_t = float(input('∆t (en s) entre deux positions successives, ∆t= '))

# Définir les coordonnées des positions successives du skieur==================
t = np.linspace(0,(N-1)*Delta_t,N) # Domaine des dates (en s)
xs = 23*t                          # Domaine des abscisses (en m)
ys = -4.9*t**2                     # Domaine des ordonnées (en m)

# Figure représentant les positions successives du skieur et le plan incliné===
plt.figure('Saut à ski')      # Nommer la figure
plt.title('Positions successives du skieur') # Donner un nom au graphe
plt.xlabel('x (en m)')        # Nommer l'axe des abscisses
plt.ylabel('y (en m)')        # Nommer l'axe des ordonnées
plt.plot(xs,ys,'r+-',lw=0.5)  # Tracer les posisions du skieur
plt.plot(x,y,'b-',lw=0.5)     # Tracer le plan incliné en bleu
plt.axis('equal')             # Imposer un repère orthonormé

# Tracé des vecteurs vitesse toutes les 2 positions============================
# e est un facteur d'échelle pour la représentation du vecteur vitesse
e=float(input('Valeur e du facteur d échelle des vecteurs vitesse (0.1 à 0.5), e= '))

for i in range(0,N-1,2):
    plt.arrow(xs[i], ys[i],
              e*(xs[i+1]-xs[i])/(t[i+1]-t[i]),
              e*(ys[i+1]-ys[i])/(t[i+1]-t[i]),
              width=0.5, color='c', length_includes_head="true")

plt.show()                    # Afficher la figure




