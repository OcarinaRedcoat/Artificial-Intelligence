#Bernardo Faria numero 87636 ------ Ricardo Caetano numero 87699 ---- Grupo 20 Taguspark
import math
import pickle
import time
import itertools
from copy import deepcopy

class Node:
    def __init__(self, parent, node, transport, tickets):
        self.parent = parent
        self.node = node
        self.transport = transport
        self.tickets = tickets
        self.gScore = 0
        self.hScore = 0
        self.fScore = 0

    def f():
        self.fScore = self.hScore + self.gScore

class SearchProblem:
  def __init__(self, goal, model, auxheur=[]):
    self.goal = goal
    self.model = model
    self.auxheur = auxheur

    self.openSet = list()

  def search(self, init, limitexp=2000, limitdepth=10, tickets=[math.inf, math.inf, math.inf], anyorder = False):

    H=[0]*114

    H[1] = [
        math.inf,0,1,2,3,2,1,2,2,3,4,4,4,3,4,5,6,5,6,4,4,3,2,4,5,5,4,5,5,5,4,6,6,6,6,5,5,5,4,3,3,4,4,5,5,6,5,6,7,6,7,6,5,4,3,2,3,3,3,4,4,5,6,6,6,6,7,6,6,5,6,4,3,4,4,4,4,4,5,4,4,4,5,5,5,6,5,5,5,5,5,5,4,4,5,4,5,4,5,6,5,6,7,7,7,6,7,6,6,4,5,5,5,5,         ]

    H[2] = [
        math.inf,1,0,1,2,3,2,1,2,3,4,4,4,3,4,5,6,5,6,4,3,2,2,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,2,3,3,4,5,5,6,5,6,7,6,7,6,5,3,4,3,4,4,4,5,5,6,7,6,6,6,7,6,6,5,7,5,4,5,5,5,5,5,6,5,5,5,6,6,6,6,6,6,6,6,6,6,5,5,6,5,6,5,6,7,6,6,7,7,7,6,7,6,7,5,6,6,6,6,         ]

    H[3] = [
        math.inf,2,1,0,1,3,2,2,1,2,3,3,3,2,3,4,5,4,5,3,3,2,3,3,4,4,3,4,4,4,3,5,5,5,5,4,4,4,3,3,2,3,3,4,4,5,4,5,6,5,6,5,4,3,4,3,3,4,4,4,4,5,6,5,5,5,6,5,5,4,6,4,3,4,5,4,4,4,5,4,4,4,5,5,5,5,5,5,5,5,5,5,4,4,5,4,5,4,5,6,5,5,6,6,6,5,6,5,6,4,5,5,5,5,         ]

    H[4] = [
        math.inf,3,2,1,0,4,3,3,2,1,2,2,3,3,4,5,6,5,6,4,2,3,4,3,3,4,4,5,5,5,4,6,6,6,6,5,5,3,2,4,3,3,4,5,5,6,5,6,7,6,7,6,5,3,4,4,4,5,5,5,5,6,7,6,6,6,7,6,6,5,7,5,4,5,6,5,5,5,6,5,5,5,6,6,6,6,6,6,6,6,6,6,5,5,6,5,6,5,6,7,6,6,7,7,7,6,7,6,7,5,6,6,6,6,         ]

    H[5] = [
        math.inf,2,3,3,4,0,1,2,2,3,4,4,4,3,4,5,6,5,6,4,3,3,2,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,1,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,3,2,2,2,3,2,3,3,4,4,4,5,4,4,4,4,4,3,2,2,3,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,3,         ]

    H[6] = [
        math.inf,1,2,2,3,1,0,1,1,2,3,3,3,2,3,4,5,4,5,3,3,2,1,3,4,4,3,4,4,4,3,5,5,5,5,4,4,4,3,2,2,3,3,4,4,5,4,5,6,5,6,5,4,3,2,1,2,2,2,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,3,3,3,3,4,3,3,3,4,4,4,5,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[7] = [
        math.inf,2,1,2,3,2,1,0,1,2,3,3,3,2,3,4,5,4,5,3,2,1,1,2,3,4,3,4,4,4,3,5,5,5,5,4,4,3,2,1,2,2,3,4,4,5,4,5,6,5,6,5,4,2,3,2,3,3,3,4,4,5,6,5,5,5,6,5,5,4,6,4,3,4,4,4,4,4,5,4,4,4,5,5,5,5,5,5,5,5,5,5,4,4,5,4,5,4,5,6,5,5,6,6,6,5,6,5,6,4,5,5,5,5,         ]

    H[8] = [
        math.inf,2,2,1,2,2,1,1,0,1,2,2,2,1,2,3,4,3,4,2,2,1,2,2,3,3,2,3,3,3,2,4,4,4,4,3,3,3,2,2,1,2,2,3,3,4,3,4,5,4,5,4,3,2,3,2,2,3,3,3,3,4,5,4,4,4,5,4,4,3,5,3,2,3,4,3,3,3,4,3,3,3,4,4,4,4,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,4,5,5,5,4,5,4,5,3,4,4,4,4,         ]

    H[9] = [
        math.inf,3,3,2,1,3,2,2,1,0,1,1,2,2,3,4,5,4,5,3,1,2,3,2,2,3,3,4,4,4,3,5,5,5,5,4,4,2,1,3,2,2,3,4,4,5,4,5,6,5,6,5,4,2,3,3,3,4,4,4,4,5,6,5,5,5,6,5,5,4,6,4,3,4,5,4,4,4,5,4,4,4,5,5,5,5,5,5,5,5,5,5,4,4,5,4,5,4,5,6,5,5,6,6,6,5,6,5,6,4,5,5,5,5,         ]

    H[10] = [
        math.inf,4,4,3,2,4,3,3,2,1,0,1,2,2,3,4,5,4,5,3,2,3,4,3,1,4,3,4,4,4,3,5,5,5,5,4,4,3,2,4,3,3,3,4,4,5,4,5,6,5,6,5,4,3,4,4,4,5,5,5,4,5,6,5,5,5,6,5,5,4,6,5,4,5,6,5,5,5,6,5,5,5,6,5,6,5,6,6,6,6,6,6,5,5,6,5,6,5,6,6,5,5,6,6,6,5,6,5,6,5,6,6,6,6,         ]

    H[11] = [
        math.inf,4,4,3,2,4,3,3,2,1,1,0,1,1,2,3,4,3,4,2,2,2,3,2,1,3,2,3,3,3,2,4,4,4,4,3,3,2,1,3,2,2,2,3,3,4,3,4,5,4,5,4,3,2,3,3,3,4,4,4,3,4,5,4,4,4,5,4,4,3,5,4,3,4,5,4,4,4,5,4,4,4,5,4,5,4,5,5,5,5,5,5,4,4,5,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[12] = [
        math.inf,4,4,3,3,4,3,3,2,2,2,1,0,1,2,3,4,3,4,2,3,3,4,3,2,2,2,3,3,3,2,4,4,4,4,3,3,1,2,4,2,3,2,3,3,4,3,4,5,4,5,4,3,3,4,3,3,4,4,4,3,4,5,4,4,4,5,4,4,3,5,4,3,4,5,4,4,4,5,4,4,4,5,4,5,4,5,5,5,5,5,5,4,4,5,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[13] = [
        math.inf,3,3,2,3,3,2,2,1,2,2,1,1,0,1,2,3,2,3,1,2,2,3,2,2,2,1,2,2,2,1,3,3,3,3,2,2,2,2,3,1,2,1,2,2,3,2,3,4,3,4,3,2,2,3,2,2,3,3,3,2,3,4,3,3,3,4,3,3,2,4,3,2,3,4,3,3,3,4,3,3,3,4,3,4,3,4,4,4,4,4,4,3,3,4,3,4,3,4,4,3,3,4,4,4,3,4,3,4,3,4,4,4,4,         ]

    H[14] = [
        math.inf,4,4,3,4,4,3,3,2,3,3,2,2,1,0,1,4,3,4,2,3,3,4,3,3,3,2,3,2,3,2,4,4,4,4,3,3,3,3,4,2,3,2,3,3,3,3,4,5,4,4,4,3,3,4,3,3,4,4,4,3,4,5,4,4,4,5,4,4,3,5,4,3,4,5,4,4,4,5,4,4,4,5,4,5,4,5,5,5,5,5,5,4,4,5,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[15] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,1,0,5,4,3,3,4,4,5,4,4,3,2,2,1,4,3,3,3,3,3,2,3,4,4,5,3,4,3,4,3,2,3,3,4,4,3,4,4,4,5,4,4,5,5,5,4,4,4,3,4,4,5,4,5,4,4,5,4,5,6,5,5,5,6,5,5,5,6,5,4,5,5,6,6,6,6,6,5,5,6,5,6,5,6,5,5,5,6,5,6,5,6,5,6,5,6,6,6,6,         ]

    H[16] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,5,0,1,2,4,5,5,6,5,5,5,4,5,4,1,2,3,3,3,4,3,5,5,5,6,4,5,4,4,4,3,2,3,4,3,4,5,4,5,5,5,5,6,5,4,3,4,5,4,4,4,5,4,4,3,5,4,4,5,6,6,6,6,7,6,5,5,5,4,5,4,5,5,6,6,6,6,6,6,7,5,6,5,5,5,4,4,5,5,5,4,5,4,5,4,6,6,6,6,         ]

    H[17] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,4,1,0,1,3,4,4,5,4,4,4,3,4,3,2,1,2,2,2,3,2,4,4,4,5,3,4,3,3,4,3,2,3,3,3,4,4,3,4,4,4,4,5,4,3,2,3,4,3,3,3,4,3,3,2,4,3,3,4,5,5,5,5,6,5,4,4,4,3,4,3,4,4,5,5,5,5,5,5,6,4,5,4,4,4,3,3,4,4,4,3,4,3,4,3,5,5,5,5,         ]

    H[18] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,3,2,1,0,4,5,5,6,5,5,4,3,3,2,3,2,1,1,1,2,1,4,5,5,6,4,5,4,4,4,3,3,2,2,4,4,5,4,5,5,5,5,6,5,4,3,4,5,4,4,3,3,2,3,3,5,4,4,5,6,6,6,6,7,6,5,5,5,4,5,4,5,5,6,6,6,6,6,6,7,5,6,5,5,5,4,4,4,3,4,3,4,4,5,4,6,6,6,6,         ]

    H[19] = [
        math.inf,4,4,3,4,4,3,3,2,3,3,2,2,1,2,3,4,3,4,0,3,3,4,3,3,3,2,1,2,3,2,4,4,4,4,3,3,3,3,4,2,3,2,3,3,3,3,4,5,4,4,4,3,3,4,3,3,4,4,4,3,4,5,4,4,4,5,4,4,3,5,4,3,4,5,4,4,4,5,4,4,4,5,4,5,4,5,5,5,5,5,5,4,4,5,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[20] = [
        math.inf,4,3,3,2,3,3,2,2,1,2,2,3,2,3,4,5,4,5,3,0,1,2,1,2,3,3,4,4,4,3,5,5,5,5,4,3,2,1,2,1,1,2,3,4,5,4,5,6,5,6,5,3,1,2,2,2,3,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,4,3,3,3,4,3,3,3,4,4,4,5,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[21] = [
        math.inf,3,2,2,3,3,2,1,1,2,3,2,3,2,3,4,5,4,5,3,1,0,1,1,2,3,3,4,4,4,3,5,5,5,5,4,3,2,1,1,1,1,2,3,4,5,4,5,6,5,6,5,3,1,2,2,2,3,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,4,3,3,3,4,3,3,3,4,4,4,5,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[22] = [
        math.inf,2,2,3,4,2,1,1,2,3,4,3,4,3,4,5,6,5,6,4,2,1,0,2,3,4,4,5,5,5,4,6,6,6,6,5,4,3,2,1,2,2,3,4,5,6,5,6,7,6,7,6,4,2,3,2,3,3,3,4,4,5,6,6,6,6,7,6,6,5,6,4,3,4,4,4,4,4,5,4,4,4,5,5,5,6,5,5,5,5,5,5,4,4,5,4,5,4,5,6,5,6,7,7,7,6,7,6,6,4,5,5,5,5,         ]

    H[23] = [
        math.inf,4,3,3,3,3,3,2,2,2,3,2,3,2,3,4,5,4,5,3,1,1,2,0,2,3,3,4,4,4,3,5,5,5,5,4,3,2,1,1,1,1,2,3,4,5,4,5,6,5,6,5,3,1,2,2,2,3,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,4,3,3,3,4,3,3,3,4,4,4,5,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[24] = [
        math.inf,5,4,4,3,4,4,3,3,2,1,1,2,2,3,4,5,4,5,3,2,2,3,2,0,3,3,4,4,4,3,5,5,5,5,4,4,2,1,3,2,2,3,4,4,5,4,5,6,5,6,5,4,2,3,3,3,4,4,4,4,5,6,5,5,5,6,5,5,4,6,4,3,4,5,4,4,4,5,4,4,4,5,5,5,5,5,5,5,5,5,5,4,4,5,4,5,4,5,6,5,5,6,6,6,5,6,5,6,4,5,5,5,5,         ]

    H[25] = [
        math.inf,5,5,4,4,5,4,4,3,3,4,3,2,2,3,3,5,4,4,3,3,3,4,3,3,0,1,2,2,4,3,4,4,4,4,3,2,1,2,4,3,3,2,3,2,3,4,4,5,5,4,3,3,3,4,4,4,5,5,4,3,3,4,4,5,5,6,5,5,4,5,4,4,5,6,5,5,5,6,5,5,5,5,4,4,5,5,5,6,6,6,6,5,5,6,5,6,5,6,6,5,5,6,6,6,5,6,5,6,5,6,6,6,6,         ]

    H[26] = [
        math.inf,4,4,3,4,4,3,3,2,3,3,2,2,1,2,2,4,3,3,2,3,3,4,3,3,1,0,1,1,3,2,3,3,3,3,2,1,2,3,4,2,3,2,2,1,2,3,3,4,4,3,2,3,3,4,3,3,4,4,4,3,2,3,3,4,4,5,4,4,3,4,4,3,4,5,4,4,4,5,4,4,4,5,4,3,4,4,5,5,5,5,5,4,4,5,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[27] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,2,5,4,3,1,4,4,5,4,4,2,1,0,1,4,3,3,3,3,3,2,2,3,4,5,3,4,3,3,2,2,3,3,4,4,3,3,4,4,5,4,4,5,5,5,4,3,4,3,4,4,5,4,5,4,4,5,4,5,6,5,5,5,6,5,5,5,6,5,4,5,5,6,6,6,6,6,5,5,6,5,6,5,6,5,5,5,6,5,6,5,6,5,6,5,6,6,6,6,         ]

    H[28] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,2,1,4,3,2,2,4,4,5,4,4,2,1,1,0,3,2,2,2,2,2,1,2,3,4,5,3,4,3,3,2,1,2,2,3,3,2,3,4,4,5,4,4,5,5,4,3,3,3,2,3,3,4,3,4,3,3,4,4,5,6,5,5,5,6,5,5,5,5,4,3,4,4,5,6,6,6,6,5,5,6,5,6,5,5,4,4,4,5,4,5,4,5,4,5,4,6,6,6,6,         ]

    H[29] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,4,1,2,3,3,4,4,5,4,4,4,3,4,3,0,1,3,3,3,3,2,4,4,4,5,3,4,3,3,3,2,1,2,3,2,3,4,3,4,4,4,4,5,4,3,2,3,4,3,3,3,4,3,3,2,4,3,3,4,5,5,5,5,6,5,4,4,4,3,4,3,4,4,5,5,5,5,5,5,6,4,5,4,4,4,3,3,4,4,4,3,4,3,4,3,5,5,5,5,         ]

    H[30] = [
        math.inf,4,4,3,4,4,3,3,2,3,3,2,2,1,2,3,2,1,2,2,3,3,4,3,3,3,2,3,2,1,0,2,2,2,2,1,3,3,3,4,2,3,2,2,3,2,1,2,3,2,3,3,2,3,3,3,3,4,3,2,1,2,3,2,2,2,3,2,2,1,3,2,2,3,4,4,4,4,5,4,3,3,3,2,3,2,3,3,4,4,4,4,4,4,5,3,4,3,3,3,2,2,3,3,3,2,3,2,3,2,4,4,4,4,         ]

    H[31] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,3,3,2,1,4,5,5,6,5,5,4,3,3,2,3,2,0,1,2,2,1,4,5,5,6,4,5,4,4,4,3,3,2,3,4,4,5,4,5,5,5,5,6,5,4,3,4,5,4,4,3,4,3,4,3,5,4,4,5,6,6,6,6,7,6,5,5,5,4,5,4,5,5,6,6,6,6,6,6,7,5,6,5,5,5,4,4,5,4,5,4,5,4,5,4,6,6,6,6,         ]

    H[32] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,3,3,2,1,4,5,5,6,5,5,4,3,3,2,3,2,1,0,1,2,1,4,5,5,6,4,5,4,4,4,3,3,2,2,4,4,5,4,5,5,5,5,6,5,4,3,4,5,4,4,3,3,2,3,3,5,4,4,5,6,6,6,6,7,6,5,5,5,4,5,4,5,5,6,6,6,6,6,6,7,5,6,5,5,5,4,4,4,3,4,3,4,4,5,4,6,6,6,6,         ]

    H[33] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,3,3,2,1,4,5,5,6,5,5,4,3,3,2,3,2,2,1,0,1,1,4,5,5,6,4,5,4,4,4,3,3,2,1,3,4,4,4,5,5,5,5,6,5,4,3,4,4,3,3,2,2,1,2,2,4,4,4,5,6,6,6,6,7,6,5,5,5,4,4,3,4,5,5,6,6,6,6,6,7,5,5,4,4,4,3,3,3,2,3,2,3,3,4,3,5,5,6,6,         ]

    H[34] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,3,4,3,2,4,5,5,6,5,5,4,3,3,2,3,2,2,2,1,0,1,4,5,5,6,4,5,4,4,4,3,3,2,2,4,4,5,4,5,5,5,5,6,5,4,3,4,5,4,4,3,3,2,3,3,5,4,4,5,6,6,6,6,7,6,5,5,5,4,5,4,5,5,6,6,6,6,6,6,7,5,6,5,5,5,4,4,4,3,4,3,4,4,5,4,6,6,6,6,         ]

    H[35] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,2,3,2,1,3,4,4,5,4,4,3,2,2,1,2,1,1,1,1,1,0,3,4,4,5,3,4,3,3,3,2,2,1,2,3,3,4,3,4,4,4,4,5,4,3,2,3,4,3,3,2,3,2,3,2,4,3,3,4,5,5,5,5,6,5,4,4,4,3,4,3,4,4,5,5,5,5,5,5,6,4,5,4,4,4,3,3,4,3,4,3,4,3,4,3,5,5,5,5,         ]

    H[36] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,3,5,4,4,3,3,3,4,3,4,2,1,2,2,4,3,4,4,4,4,3,0,2,3,4,3,2,1,1,1,2,3,3,4,4,3,2,2,2,3,4,4,5,4,3,2,2,3,3,4,4,5,4,4,3,4,3,3,4,5,5,5,5,6,5,4,4,4,3,3,4,4,4,5,5,5,5,5,5,6,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[37] = [
        math.inf,5,4,4,3,4,4,3,3,2,3,2,1,2,3,4,5,4,5,3,2,2,3,2,2,1,2,3,3,4,3,5,5,5,5,4,2,0,1,3,2,2,1,2,3,4,4,5,6,5,5,4,2,2,3,3,3,4,4,3,2,3,4,4,4,4,5,4,4,3,5,3,3,4,5,4,4,4,5,4,4,4,4,3,4,4,5,4,5,5,5,5,4,4,5,4,5,4,5,5,4,4,5,5,5,4,5,4,5,4,5,5,5,5,         ]

    H[38] = [
        math.inf,4,3,3,2,3,3,2,2,1,2,1,2,2,3,4,5,4,5,3,1,1,2,1,1,2,3,4,4,4,3,5,5,5,5,4,3,1,0,2,1,1,2,3,4,5,4,5,6,5,6,5,3,1,2,2,2,3,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,4,3,3,3,4,3,3,3,4,4,4,5,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[39] = [
        math.inf,3,2,3,4,3,2,1,2,3,4,3,4,3,4,5,6,5,6,4,2,1,1,1,3,4,4,5,5,5,4,6,6,6,6,5,4,3,2,0,2,2,3,4,5,6,5,6,7,6,6,6,4,2,2,1,2,3,2,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,3,3,3,3,4,3,3,3,4,4,4,5,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[40] = [
        math.inf,3,3,2,3,2,2,2,1,2,3,2,2,1,2,3,4,3,4,2,1,1,2,1,2,3,2,3,3,3,2,4,4,4,4,3,3,2,1,2,0,1,2,3,3,4,3,4,5,4,5,4,3,1,2,1,1,2,2,2,2,3,4,4,4,4,5,4,4,3,4,2,1,2,3,2,2,2,3,2,2,2,3,3,3,4,3,3,3,3,3,3,2,2,3,2,3,2,3,4,3,4,5,5,5,4,5,4,4,2,3,3,3,3,         ]

    H[41] = [
        math.inf,4,3,3,3,3,3,2,2,2,3,2,3,2,3,4,5,4,5,3,1,1,2,1,2,3,3,4,4,4,3,5,5,5,5,4,2,2,1,2,1,0,1,2,3,4,4,5,6,5,5,4,2,1,2,2,2,3,3,3,2,3,4,4,4,4,5,4,4,3,5,3,2,3,4,3,3,3,4,3,3,3,4,3,4,4,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,4,5,5,5,4,5,4,5,3,4,4,4,4,         ]

    H[42] = [
        math.inf,4,4,3,4,4,3,3,2,3,3,2,2,1,2,3,4,3,4,2,2,2,3,2,3,2,2,3,3,3,2,4,4,4,4,3,1,1,2,3,2,1,0,1,2,3,3,4,5,4,4,3,1,1,2,3,3,4,3,2,1,2,3,3,3,3,4,3,3,2,4,2,2,3,4,4,4,4,5,4,3,3,3,2,3,3,4,3,4,4,4,4,4,4,5,3,4,3,4,4,3,3,4,4,4,3,4,3,4,3,4,4,4,4,         ]

    H[43] = [
        math.inf,5,5,4,5,4,4,4,3,4,4,3,3,2,3,4,4,3,4,3,3,3,4,3,4,3,2,3,3,3,2,4,4,4,4,3,1,2,3,4,3,2,1,0,1,2,3,3,4,4,3,2,2,2,3,3,3,4,3,2,1,2,3,3,3,3,4,3,3,2,4,2,2,3,4,4,4,4,5,4,3,3,3,2,3,3,4,3,4,4,4,4,4,4,5,3,4,3,4,4,3,3,4,4,4,3,4,3,4,3,4,4,4,4,         ]

    H[44] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,3,4,4,4,3,4,4,5,4,4,2,1,2,2,3,3,4,4,4,4,3,1,3,4,5,3,3,2,1,0,1,2,2,3,3,2,1,3,3,4,4,4,5,4,3,2,1,2,2,3,3,4,4,4,3,3,3,3,4,5,5,5,5,6,5,4,4,4,3,2,4,3,4,5,5,5,5,5,5,6,4,5,4,4,4,4,4,5,5,5,4,5,4,5,3,5,5,5,5,         ]

    H[45] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,3,2,3,3,3,3,5,5,6,5,5,3,2,2,1,2,2,3,3,3,3,2,2,4,5,6,4,4,3,2,1,0,1,1,2,2,1,2,4,4,5,5,5,6,5,4,3,2,2,1,2,2,3,3,3,2,2,4,4,5,6,6,6,6,7,6,5,5,4,3,2,3,3,4,5,6,6,6,6,6,7,5,5,4,4,3,3,3,4,4,4,3,4,3,4,3,5,5,6,6,         ]

    H[46] = [
        math.inf,5,5,4,5,5,4,4,3,4,4,3,3,2,3,3,2,2,3,3,4,4,5,4,4,4,3,3,2,1,1,3,3,3,3,2,3,4,4,5,3,4,3,3,2,1,0,1,2,1,2,3,3,4,4,4,4,5,4,3,2,3,3,2,2,2,3,3,3,2,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,3,4,4,5,5,5,5,5,5,6,4,5,4,4,4,3,3,4,4,4,3,4,3,4,3,5,5,5,5,         ]

    H[47] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,3,3,3,2,4,5,5,6,5,5,4,3,3,2,2,2,2,2,2,2,1,3,5,5,6,4,5,4,3,2,1,1,0,1,2,2,3,4,5,5,5,5,6,5,4,3,3,3,2,2,1,2,2,3,2,3,4,4,5,6,6,6,6,7,6,5,5,5,4,3,3,4,5,5,6,6,6,6,6,7,5,5,4,4,4,3,3,4,3,3,3,4,3,4,3,5,5,6,6,         ]

    H[48] = [
        math.inf,7,7,6,7,7,6,6,5,6,6,5,5,4,5,4,4,3,2,5,6,6,7,6,6,5,4,4,3,3,3,3,2,1,2,2,4,6,6,7,5,6,5,4,3,2,2,1,0,3,3,4,5,6,6,6,6,7,6,5,4,4,4,3,3,2,1,2,3,3,4,5,5,6,7,7,7,7,8,7,6,6,6,5,4,4,5,6,6,7,7,7,7,7,8,6,6,5,5,5,4,4,4,3,2,3,4,4,5,4,6,6,7,7,         ]

    H[49] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,4,3,3,4,4,5,5,6,5,5,5,4,4,3,2,2,4,4,3,4,3,4,5,5,6,4,5,4,4,3,2,1,2,3,0,1,2,4,5,5,5,5,6,5,4,3,3,2,1,1,1,2,2,2,2,2,4,4,5,6,6,6,6,7,6,5,5,4,3,2,3,3,4,5,6,6,6,6,6,7,5,5,4,4,3,3,3,3,3,3,3,4,3,4,3,5,5,6,6,         ]

    H[50] = [
        math.inf,7,7,6,7,6,6,6,5,6,6,5,5,4,4,3,4,4,4,4,6,6,7,6,6,4,3,3,2,3,3,4,4,4,4,3,3,5,6,6,5,5,4,3,2,1,2,2,3,1,0,1,4,5,5,5,5,6,5,4,3,3,2,1,2,2,3,3,3,2,2,4,4,5,6,6,6,6,7,6,5,5,4,3,2,3,3,4,5,6,6,6,6,6,7,5,5,4,4,3,3,3,4,4,4,3,4,3,4,3,5,5,6,6,         ]

    H[51] = [
        math.inf,6,6,5,6,6,5,5,4,5,5,4,4,3,4,4,5,4,5,4,5,5,6,5,5,3,2,3,3,4,3,5,5,4,5,4,2,4,5,6,4,4,3,2,1,2,3,3,4,2,1,0,4,4,5,5,5,6,5,4,3,2,1,1,2,3,4,3,3,2,2,4,4,5,6,6,6,6,7,6,5,5,4,3,2,3,3,4,5,6,6,6,6,6,7,5,5,4,4,3,3,3,4,4,4,3,4,3,4,3,5,5,6,6,         ]

    H[52] = [
        math.inf,5,5,4,5,4,4,4,3,4,4,3,3,2,3,4,4,3,4,3,3,3,4,3,4,3,3,4,4,3,2,4,4,4,4,3,2,2,3,4,3,2,1,2,3,4,3,4,5,4,4,4,0,2,3,3,3,4,3,2,1,2,3,3,3,3,4,3,3,2,4,2,2,3,4,4,4,4,5,4,3,3,3,2,3,3,4,3,4,4,4,4,4,4,5,3,4,3,4,4,3,3,4,4,4,3,4,3,4,3,4,4,4,4,         ]

    H[53] = [
        math.inf,4,3,3,3,3,3,2,2,2,3,2,3,2,3,4,5,4,5,3,1,1,2,1,2,3,3,4,4,4,3,5,5,5,5,4,2,2,1,2,1,1,1,2,3,4,4,5,6,5,5,4,2,0,1,2,2,3,3,2,2,3,4,4,4,4,5,4,4,3,5,3,2,3,4,3,3,3,4,3,3,3,4,3,4,4,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,4,5,5,5,4,5,4,5,3,4,4,4,4,         ]

    H[54] = [
        math.inf,3,4,4,4,3,2,3,3,3,4,3,4,3,4,5,5,4,5,4,2,2,3,2,3,4,4,5,5,4,3,5,5,5,5,4,3,3,2,2,2,2,2,3,4,5,4,5,6,5,5,5,3,1,0,1,2,3,2,1,2,3,4,4,4,4,5,4,4,3,5,2,2,3,3,3,3,3,4,3,3,3,3,3,4,4,4,4,4,4,4,4,3,3,4,3,4,3,4,5,4,4,5,5,5,4,5,4,5,3,4,4,4,4,         ]

    H[55] = [
        math.inf,2,3,3,4,2,1,2,2,3,4,3,3,2,3,4,5,4,5,3,2,2,2,2,3,4,3,4,4,4,3,5,5,5,5,4,4,3,2,1,1,2,3,3,4,5,4,5,6,5,5,5,3,2,1,0,1,2,1,2,2,3,4,4,4,4,5,4,4,3,4,2,1,2,2,2,2,2,3,2,2,2,3,3,3,4,3,3,3,3,3,3,2,2,3,2,3,2,3,4,3,4,5,5,5,4,5,4,4,2,3,3,3,3,         ]

    H[56] = [
        math.inf,3,4,3,4,1,2,3,2,3,4,3,3,2,3,4,5,4,5,3,2,2,3,2,3,4,3,4,4,4,3,5,5,5,5,4,4,3,2,2,1,2,3,3,4,5,4,5,6,5,5,5,3,2,2,1,0,1,2,2,2,3,4,4,4,4,5,4,4,3,4,2,1,2,2,1,1,1,2,1,2,2,3,3,3,4,3,3,3,3,3,2,1,1,2,2,3,2,3,4,3,4,5,5,5,4,5,4,4,2,3,3,3,2,         ]

    H[57] = [
        math.inf,3,4,4,5,1,2,3,3,4,5,4,4,3,4,5,6,5,6,4,3,3,3,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,0,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,3,2,2,2,3,2,3,3,4,4,4,5,4,4,4,4,4,3,2,2,3,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,3,         ]

    H[58] = [
        math.inf,3,4,4,5,3,2,3,3,4,5,4,4,3,4,5,5,4,5,4,3,3,3,3,4,5,4,5,5,4,3,5,5,5,5,4,4,4,3,2,2,3,3,3,4,5,4,5,6,5,5,5,3,3,2,1,2,3,0,2,2,3,4,4,4,4,5,4,4,3,4,2,1,1,1,2,3,3,4,2,2,2,3,3,3,4,3,3,3,3,3,3,3,3,4,2,3,2,3,4,3,4,5,5,5,4,5,4,4,2,3,3,3,3,         ]

    H[59] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,4,3,4,4,3,3,4,3,4,4,4,5,4,3,2,4,4,4,4,3,3,3,3,3,2,3,2,2,3,4,3,4,5,4,4,4,2,2,1,2,2,3,2,0,1,2,3,3,3,3,4,3,3,2,4,1,1,2,3,3,3,3,4,3,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,2,3,2,3,4,3,3,4,4,4,3,4,3,4,2,3,3,3,3,         ]

    H[60] = [
        math.inf,4,5,4,5,3,3,4,3,4,4,3,3,2,3,4,3,2,3,3,3,3,4,3,4,3,3,4,3,2,1,3,3,3,3,2,2,2,3,3,2,2,1,1,2,3,2,3,4,3,3,3,1,2,2,2,2,3,2,1,0,1,2,2,2,2,3,2,2,1,3,1,1,2,3,3,3,3,4,3,2,2,2,1,2,2,3,2,3,3,3,3,3,3,4,2,3,2,3,3,2,2,3,3,3,2,3,2,3,2,3,3,3,3,         ]

    H[61] = [
        math.inf,5,6,5,6,4,4,5,4,5,5,4,4,3,4,4,4,3,4,4,4,4,5,4,5,3,2,3,3,3,2,4,4,4,4,3,2,3,4,4,3,3,2,2,1,2,3,3,4,3,3,2,2,3,3,3,3,4,3,2,1,0,1,2,3,3,4,3,3,2,2,2,2,3,4,4,4,4,5,4,3,3,3,2,1,3,2,3,4,4,4,4,4,4,5,3,4,3,3,3,3,3,4,4,4,3,4,3,4,2,4,4,4,4,         ]

    H[62] = [
        math.inf,6,7,6,7,5,5,6,5,6,6,5,5,4,5,4,5,4,5,5,5,5,6,5,6,4,3,4,3,4,3,5,5,4,5,4,3,4,5,5,4,4,3,3,2,2,3,3,4,2,2,1,3,4,4,4,4,5,4,3,2,1,0,1,2,3,4,3,3,2,1,3,3,4,5,5,5,5,6,5,4,4,4,3,2,3,3,4,5,5,5,5,5,5,6,4,5,4,3,2,3,3,4,4,4,3,4,3,3,3,5,5,5,5,         ]

    H[63] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,3,4,3,4,4,5,5,6,5,5,4,3,3,2,3,2,4,4,3,4,3,3,4,5,5,4,4,3,3,2,1,2,2,3,1,1,1,3,4,4,4,4,5,4,3,2,2,1,0,1,2,3,2,2,1,1,3,3,4,5,5,5,5,6,5,4,4,3,2,1,2,2,3,4,5,5,5,5,5,6,4,4,3,3,2,2,2,3,3,3,2,3,2,3,2,4,4,5,5,         ]

    H[64] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,4,4,3,4,4,5,5,6,5,5,5,4,4,3,3,2,4,4,3,4,3,4,4,5,5,4,4,3,3,3,2,2,2,3,1,2,2,3,4,4,4,4,5,4,3,2,3,2,1,0,1,2,2,1,1,2,3,3,4,5,5,5,5,6,5,4,4,4,3,2,2,3,4,4,5,5,5,5,5,6,4,4,3,3,3,2,2,2,3,3,2,3,2,3,2,4,4,5,5,         ]

    H[65] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,4,4,3,3,4,5,5,6,5,5,5,4,4,3,3,2,3,3,2,3,2,4,4,5,5,4,4,3,3,3,2,2,1,2,1,2,3,3,4,4,4,4,5,4,3,2,3,3,2,1,0,1,1,2,1,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,2,3,4,4,5,5,5,5,5,6,4,4,3,3,3,2,2,3,2,2,2,3,2,3,2,4,4,5,5,         ]

    H[66] = [
        math.inf,7,7,6,7,6,6,6,5,6,6,5,5,4,5,5,5,4,3,5,6,6,7,6,6,6,5,5,4,4,3,4,3,2,3,3,5,5,6,6,5,5,4,4,4,3,3,2,1,2,3,4,4,5,5,5,5,6,5,4,3,4,4,3,2,1,0,2,3,2,4,4,4,5,6,6,6,6,7,6,5,5,5,4,4,3,4,5,5,6,6,6,6,6,7,5,5,4,4,4,3,3,4,3,1,2,3,3,4,3,5,5,6,6,         ]

    H[67] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,4,4,3,2,4,5,5,6,5,5,5,4,4,3,3,2,3,2,1,2,2,4,4,5,5,4,4,3,3,4,3,3,2,2,2,3,3,3,4,4,4,4,5,4,3,2,3,3,2,2,1,2,0,1,1,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,2,3,4,4,5,5,5,5,5,6,4,4,3,3,3,2,2,2,1,2,1,2,2,3,2,4,4,5,5,         ]

    H[68] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,5,4,3,3,4,5,5,6,5,5,5,4,5,4,3,2,4,3,2,3,3,4,4,5,5,4,4,3,3,4,3,3,3,3,2,3,3,3,4,4,4,4,5,4,3,2,3,3,2,1,2,3,1,0,1,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,2,3,4,4,5,5,5,5,5,6,4,4,3,3,3,2,2,1,2,3,2,2,2,3,2,4,4,5,5,         ]

    H[69] = [
        math.inf,5,5,4,5,4,4,4,3,4,4,3,3,2,3,4,3,2,3,3,4,4,5,4,4,4,3,4,3,2,1,3,3,2,3,2,3,3,4,4,3,3,2,2,3,2,2,2,3,2,2,2,2,3,3,3,3,4,3,2,1,2,2,1,1,1,2,1,1,0,2,2,2,3,4,4,4,4,5,4,3,3,3,2,2,1,2,3,3,4,4,4,4,4,5,3,3,2,2,2,1,1,2,2,2,1,2,1,2,1,3,3,4,4,         ]

    H[70] = [
        math.inf,6,7,6,7,5,5,6,5,6,6,5,5,4,5,4,5,4,5,5,5,5,6,5,6,5,4,4,3,4,3,5,5,4,5,4,4,5,5,5,4,5,4,4,3,2,3,3,4,2,2,2,4,5,5,4,4,5,4,4,3,2,1,1,2,3,4,3,3,2,0,3,3,4,5,5,5,5,6,5,4,4,3,2,1,2,2,3,4,5,5,5,5,5,6,4,4,3,2,1,3,3,4,4,4,3,4,3,2,2,4,4,5,5,         ]

    H[71] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,4,3,4,4,3,3,4,3,4,4,4,5,4,3,2,4,4,4,4,3,3,3,3,3,2,3,2,2,3,4,3,4,5,4,4,4,2,3,2,2,2,3,2,1,1,2,3,3,3,3,4,3,3,2,3,0,1,2,3,3,3,3,4,3,2,2,1,1,2,3,3,2,2,3,3,3,3,3,4,2,3,2,3,4,3,3,4,4,4,3,4,3,4,2,3,3,3,3,         ]

    H[72] = [
        math.inf,3,4,3,4,2,2,3,2,3,4,3,3,2,3,4,4,3,4,3,2,2,3,2,3,4,3,4,4,3,2,4,4,4,4,3,3,3,2,2,1,2,2,2,3,4,3,4,5,4,4,4,2,2,2,1,1,2,1,1,1,2,3,3,3,3,4,3,3,2,3,1,0,1,2,2,2,2,3,2,1,1,2,2,2,3,2,2,2,2,2,2,2,2,3,1,2,1,2,3,2,3,4,4,4,3,4,3,3,1,2,2,2,2,         ]

    H[73] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,5,4,5,4,3,3,4,3,4,5,4,5,5,4,3,5,5,5,5,4,4,4,3,3,2,3,3,3,4,5,4,5,6,5,5,5,3,3,3,2,2,3,1,2,2,3,4,4,4,4,5,4,4,3,4,2,1,0,1,2,3,3,3,1,1,2,3,3,3,4,3,3,3,2,2,2,2,3,3,2,3,2,3,4,3,4,5,5,5,4,5,4,4,2,3,3,3,3,         ]

    H[74] = [
        math.inf,4,5,5,6,3,3,4,4,5,6,5,5,4,5,6,6,5,6,5,4,4,4,4,5,6,5,6,6,5,4,6,6,6,6,5,5,5,4,3,3,4,4,4,5,6,5,6,7,6,6,6,4,4,3,2,2,3,1,3,3,4,5,5,5,5,6,5,5,4,5,3,2,1,0,1,2,3,3,2,2,3,4,4,4,5,4,4,4,3,3,3,3,3,4,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,4,         ]

    H[75] = [
        math.inf,4,5,4,5,2,3,4,3,4,5,4,4,3,4,5,6,5,6,4,3,3,4,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,2,2,3,3,4,5,5,5,5,6,5,5,4,5,3,2,2,1,0,1,2,2,1,3,3,4,4,4,5,4,4,4,4,3,2,2,2,3,2,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,3,3,3,         ]

    H[76] = [
        math.inf,4,5,4,5,2,3,4,3,4,5,4,4,3,4,5,6,5,6,4,3,3,4,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,2,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,2,1,0,2,1,2,3,3,4,4,4,5,4,4,4,4,4,3,2,2,3,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,3,         ]

    H[77] = [
        math.inf,4,5,4,5,2,3,4,3,4,5,4,4,3,4,5,6,5,6,4,3,3,4,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,2,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,3,2,2,0,1,2,3,3,4,4,4,5,4,4,4,4,4,3,2,2,3,3,4,3,4,5,4,5,6,6,6,5,6,5,5,3,4,4,4,3,         ]

    H[78] = [
        math.inf,5,6,5,6,3,4,5,4,5,6,5,5,4,5,6,7,6,7,5,4,4,5,4,5,6,5,6,6,6,5,7,7,7,7,6,6,5,4,4,3,4,5,5,6,7,6,7,8,7,7,7,5,4,4,3,2,3,4,4,4,5,6,6,6,6,7,6,6,5,6,4,3,3,3,2,1,1,0,2,4,4,5,5,5,6,5,5,5,4,4,3,1,1,2,3,5,4,5,6,5,6,7,7,7,6,7,6,6,4,4,3,3,2,         ]

    H[79] = [
        math.inf,4,5,4,5,2,3,4,3,4,5,4,4,3,4,5,6,5,6,4,3,3,4,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,2,2,3,3,4,5,5,5,5,6,5,5,4,5,3,2,1,2,1,2,2,2,0,2,3,4,4,4,5,4,4,4,3,2,1,1,2,2,1,4,3,4,5,4,5,6,6,6,5,6,5,5,3,3,2,2,2,         ]

    H[80] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,5,4,5,4,3,3,4,3,4,5,4,5,5,4,3,5,5,5,5,4,4,4,3,3,2,3,3,3,4,5,4,5,6,5,5,5,3,3,3,2,2,3,2,2,2,3,4,4,4,4,5,4,4,3,4,2,1,1,2,3,3,3,4,2,0,2,3,3,3,4,3,3,3,1,1,2,3,3,4,2,2,2,3,4,3,4,5,5,5,4,5,4,4,2,3,2,3,3,         ]

    H[81] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,5,4,5,4,3,3,4,3,4,5,4,5,5,4,3,5,5,5,5,4,4,4,3,3,2,3,3,3,4,5,4,5,6,5,5,5,3,3,3,2,2,3,2,2,2,3,4,4,4,4,5,4,4,3,4,2,1,2,3,3,3,3,4,3,2,0,1,2,3,4,3,3,1,1,2,3,3,3,4,2,2,2,3,4,3,4,5,5,5,4,5,4,4,2,3,2,3,3,         ]

    H[82] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,5,4,5,5,4,4,5,4,5,5,5,6,5,4,3,5,5,5,5,4,4,4,4,4,3,4,3,3,4,4,4,5,6,4,4,4,3,4,3,3,3,4,3,2,2,3,4,3,4,4,5,4,4,3,3,1,2,3,4,4,4,4,5,4,3,1,0,1,2,4,3,2,1,2,3,4,4,4,5,3,3,2,4,4,4,4,5,5,5,4,5,4,5,3,3,3,4,4,         ]

    H[83] = [
        math.inf,5,6,5,6,4,4,5,4,5,5,4,4,3,4,5,4,3,4,4,4,4,5,4,5,4,4,5,4,3,2,4,4,4,4,3,3,3,4,4,3,3,2,2,3,3,3,4,5,3,3,3,2,3,3,3,3,4,3,2,1,2,3,2,3,3,4,3,3,2,2,1,2,3,4,4,4,4,5,4,3,2,1,0,1,3,2,1,2,3,3,4,4,4,4,3,2,1,3,3,3,3,4,4,4,3,4,3,4,2,2,2,3,3,         ]

    H[84] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,4,5,4,5,5,4,4,5,4,5,4,3,4,3,4,3,5,5,4,5,4,3,4,4,4,3,4,3,3,2,2,3,3,4,2,2,2,3,4,4,3,3,4,3,3,2,1,2,1,2,3,4,3,3,2,1,2,2,3,4,4,4,4,5,4,3,3,2,1,0,3,1,2,3,4,4,4,4,4,5,3,3,2,2,2,2,3,4,4,4,3,4,3,3,1,3,3,4,4,         ]

    H[85] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,5,4,3,4,4,5,5,6,5,5,5,4,5,4,3,2,4,4,3,4,3,4,4,5,5,4,4,3,3,4,3,3,3,4,3,3,3,3,4,4,4,4,5,4,3,2,3,3,2,2,2,3,2,2,1,2,3,3,4,5,5,5,5,6,5,4,4,4,3,3,0,2,4,4,5,5,5,5,5,6,4,4,3,2,1,1,2,3,3,3,2,3,2,2,2,4,4,5,5,         ]

    H[86] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,5,5,4,5,5,4,4,5,4,5,5,4,5,4,4,3,5,5,4,5,4,4,5,4,4,3,4,4,4,3,3,4,4,5,3,3,3,4,4,4,3,3,4,3,3,3,2,3,2,3,3,4,3,3,2,2,3,2,3,4,4,4,4,5,4,3,3,3,2,1,2,0,3,3,4,4,4,4,4,5,3,3,2,2,1,2,3,4,4,4,3,4,3,2,1,3,3,4,4,         ]

    H[87] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,5,4,5,5,4,4,5,4,5,5,5,6,5,4,3,5,5,5,5,4,4,4,4,4,3,4,3,3,4,4,4,5,6,4,4,4,3,4,4,3,3,4,3,3,2,3,4,3,4,4,5,4,4,3,3,2,2,3,4,4,4,4,5,4,3,3,2,1,2,4,3,0,2,3,3,4,4,4,4,3,2,1,3,4,3,4,5,5,5,4,5,4,4,2,2,2,3,3,         ]

    H[88] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,5,6,5,5,5,4,4,3,4,4,4,5,5,5,5,6,5,5,5,4,4,4,3,3,4,3,3,3,4,5,4,4,4,5,4,4,3,4,2,2,3,4,4,4,4,5,4,3,1,1,2,3,4,3,2,0,2,3,4,4,4,4,3,2,1,3,4,3,4,5,5,5,4,5,4,4,2,2,2,3,3,         ]

    H[89] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,6,6,5,5,5,4,4,3,4,4,4,5,6,5,6,7,6,6,6,4,4,4,3,3,4,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,2,3,4,4,4,4,3,1,1,2,3,4,5,4,3,2,0,1,2,3,3,3,2,1,2,4,5,4,5,6,6,6,5,6,5,5,3,2,1,2,2,         ]

    H[90] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,6,6,5,5,5,4,4,3,4,4,4,5,6,5,6,7,6,6,6,4,4,4,3,3,4,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,2,3,3,4,4,4,2,1,2,3,3,4,5,4,3,3,1,0,1,3,3,3,1,2,2,4,5,4,5,6,6,6,5,6,5,5,3,2,1,2,2,         ]

    H[91] = [
        math.inf,5,6,5,6,3,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,6,6,5,5,5,4,4,3,4,4,4,5,6,5,6,7,6,6,6,4,4,4,3,2,3,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,2,3,2,3,3,3,1,2,3,4,4,4,5,4,4,4,2,1,0,2,3,3,1,3,3,4,5,4,5,6,6,6,5,6,5,5,3,3,2,2,2,         ]

    H[92] = [
        math.inf,4,5,4,5,2,3,4,3,4,5,4,4,3,4,5,6,5,6,4,3,3,4,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,2,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,2,3,2,2,2,1,1,3,3,4,4,4,5,4,4,4,3,3,2,0,1,1,2,4,3,4,5,4,5,6,6,6,5,6,5,5,3,3,2,2,1,         ]

    H[93] = [
        math.inf,4,5,4,5,2,3,4,3,4,5,4,4,3,4,5,6,5,6,4,3,3,4,3,4,5,4,5,5,5,4,6,6,6,6,5,5,4,3,3,2,3,4,4,5,6,5,6,7,6,6,6,4,3,3,2,1,2,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,3,2,2,2,1,2,3,3,4,4,4,5,4,4,4,3,3,3,1,0,1,2,4,3,4,5,4,5,6,6,6,5,6,5,5,3,3,2,2,1,         ]

    H[94] = [
        math.inf,5,6,5,6,3,4,5,4,5,6,5,5,4,5,6,7,6,7,5,4,4,5,4,5,6,5,6,6,6,5,7,7,7,7,6,6,5,4,4,3,4,5,5,6,7,6,7,8,7,7,7,5,4,4,3,2,3,4,4,4,5,6,6,6,6,7,6,6,5,6,4,3,3,4,3,3,3,2,2,4,4,5,4,5,6,5,4,4,3,3,3,1,1,0,2,4,3,5,6,5,6,7,7,7,6,7,6,6,4,3,2,2,1,         ]

    H[95] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,5,4,5,4,3,3,4,3,4,5,4,5,5,4,3,5,5,5,5,4,4,4,3,3,2,3,3,3,4,5,4,5,6,5,5,5,3,3,3,2,2,3,2,2,2,3,4,4,4,4,5,4,4,3,4,2,1,2,3,2,3,3,3,1,2,2,3,3,3,4,3,3,3,2,1,1,2,2,2,0,3,2,3,4,3,4,5,5,5,4,5,4,4,2,2,1,1,1,         ]

    H[96] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,5,6,5,5,5,4,4,3,4,4,4,5,5,5,5,6,5,5,5,4,4,4,3,3,4,3,3,3,4,5,4,4,4,5,4,4,3,4,3,2,3,4,4,4,4,5,4,2,2,3,2,3,4,3,2,2,1,2,3,4,4,4,3,0,1,3,4,3,4,5,5,5,4,5,4,4,2,1,2,3,3,         ]

    H[97] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,5,4,5,4,3,3,4,3,4,5,4,5,5,4,3,5,5,4,5,4,4,4,3,3,2,3,3,3,4,4,4,4,5,4,4,4,3,3,3,2,2,3,2,2,2,3,4,3,3,3,4,3,3,2,3,2,1,2,3,3,3,3,4,3,2,2,2,1,2,3,2,1,1,2,2,3,3,3,3,2,1,0,2,3,2,3,4,4,4,3,4,3,3,1,1,1,2,2,         ]

    H[98] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,5,4,5,5,4,4,5,4,5,6,5,6,5,4,3,5,5,4,5,4,5,5,4,4,3,4,4,4,4,4,4,4,5,4,4,4,4,4,4,3,3,4,3,3,3,3,3,3,3,3,4,3,3,2,2,3,2,3,4,4,4,4,5,4,3,3,4,3,2,2,2,3,3,4,4,4,4,4,5,3,3,2,0,1,2,3,4,4,4,3,3,2,1,1,3,3,4,4,         ]

    H[99] = [
        math.inf,6,7,6,7,5,5,6,5,6,6,5,5,4,5,5,5,4,5,5,5,5,6,5,6,6,5,5,4,4,3,5,5,4,5,4,5,5,5,5,4,5,4,4,4,3,4,4,5,3,3,3,4,5,5,4,4,5,4,4,3,3,2,2,3,3,4,3,3,2,1,4,3,4,5,5,5,5,6,5,4,4,4,3,2,1,1,4,4,5,5,5,5,5,6,4,4,3,1,0,2,3,4,4,4,3,3,2,1,2,4,4,5,5,         ]

    H[100] = [
        math.inf,5,6,5,6,4,4,5,4,5,5,4,4,3,4,5,4,3,4,4,4,4,5,4,5,5,4,5,4,3,2,4,4,3,4,3,4,4,4,4,3,4,3,3,4,3,3,3,4,3,3,3,3,4,4,3,3,4,3,3,2,3,3,2,2,2,3,2,2,1,3,3,2,3,4,4,4,4,5,4,3,3,4,3,2,1,2,3,3,4,4,4,4,4,5,3,3,2,2,2,0,1,2,3,3,2,3,2,1,1,3,3,4,4,         ]

    H[101] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,5,4,3,4,4,5,5,6,5,5,5,4,5,4,3,2,4,4,3,4,3,4,4,5,5,4,4,3,3,4,3,3,3,4,3,3,3,3,4,4,4,4,5,4,3,2,3,3,2,2,2,3,2,2,1,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,2,3,4,4,5,5,5,5,5,6,4,4,3,3,3,1,0,1,2,3,2,2,1,2,2,4,4,5,5,         ]

    H[102] = [
        math.inf,7,7,6,7,6,6,6,5,6,6,5,5,4,5,6,5,4,4,5,6,6,7,6,6,6,5,6,5,4,3,5,4,3,4,4,5,5,6,6,5,5,4,4,5,4,4,4,4,3,4,4,4,5,5,5,5,6,5,4,3,4,4,3,2,3,4,2,1,2,4,4,4,5,6,6,6,6,7,6,5,5,5,4,4,3,4,5,5,6,6,6,6,6,7,5,5,4,4,4,2,1,0,1,3,2,1,2,3,3,5,5,6,6,         ]

    H[103] = [
        math.inf,7,7,6,7,6,6,6,5,6,6,5,5,4,5,5,5,4,3,5,6,6,7,6,6,6,5,5,4,4,3,4,3,2,3,3,5,5,6,6,5,5,4,4,5,4,4,3,3,3,4,4,4,5,5,5,5,6,5,4,3,4,4,3,3,2,3,1,2,2,4,4,4,5,6,6,6,6,7,6,5,5,5,4,4,3,4,5,5,6,6,6,6,6,7,5,5,4,4,4,3,2,1,0,2,1,2,2,3,3,5,5,6,6,         ]

    H[104] = [
        math.inf,7,7,6,7,6,6,6,5,6,6,5,5,4,5,6,5,4,4,5,6,6,7,6,6,6,5,6,5,4,3,5,4,3,4,4,5,5,6,6,5,5,4,4,5,4,4,3,2,3,4,4,4,5,5,5,5,6,5,4,3,4,4,3,3,2,1,2,3,2,4,4,4,5,6,6,6,6,7,6,5,5,5,4,4,3,4,5,5,6,6,6,6,6,7,5,5,4,4,4,3,3,3,2,0,1,2,2,3,3,5,5,6,6,         ]

    H[105] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,5,4,3,3,4,5,5,6,5,5,5,4,5,4,3,2,4,3,2,3,3,4,4,5,5,4,4,3,3,4,3,3,3,3,3,3,3,3,4,4,4,4,5,4,3,2,3,3,2,2,2,2,1,2,1,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,2,3,4,4,5,5,5,5,5,6,4,4,3,3,3,2,2,2,1,1,0,1,1,2,2,4,4,5,5,         ]

    H[106] = [
        math.inf,7,7,6,7,6,6,6,5,6,6,5,5,4,5,6,5,4,4,5,6,6,7,6,6,6,5,6,5,4,3,5,4,3,4,4,5,5,6,6,5,5,4,4,5,4,4,4,4,4,4,4,4,5,5,5,5,6,5,4,3,4,4,3,3,3,3,2,2,2,4,4,4,5,6,6,6,6,7,6,5,5,5,4,4,3,4,5,5,6,6,6,6,6,7,5,5,4,3,3,3,2,1,2,2,1,0,1,2,3,5,5,6,6,         ]

    H[107] = [
        math.inf,6,6,5,6,5,5,5,4,5,5,4,4,3,4,5,4,3,4,4,5,5,6,5,5,5,4,5,4,3,2,4,4,3,4,3,4,4,5,5,4,4,3,3,4,3,3,3,4,3,3,3,3,4,4,4,4,5,4,3,2,3,3,2,2,2,3,2,2,1,3,3,3,4,5,5,5,5,6,5,4,4,4,3,3,2,3,4,4,5,5,5,5,5,6,4,4,3,2,2,2,1,2,2,2,1,1,0,1,2,4,4,5,5,         ]

    H[108] = [
        math.inf,6,7,6,7,5,5,6,5,6,6,5,5,4,5,6,5,4,5,5,5,5,6,5,6,6,5,6,5,4,3,5,5,4,5,4,5,5,5,5,4,5,4,4,5,4,4,4,5,4,4,4,4,5,5,4,4,5,4,4,3,4,3,3,3,3,4,3,3,2,2,4,3,4,5,5,5,5,6,5,4,4,5,4,3,2,2,4,4,5,5,5,5,5,6,4,4,3,1,1,1,2,3,3,3,2,2,1,0,2,4,4,5,5,         ]

    H[109] = [
        math.inf,4,5,4,5,3,3,4,3,4,5,4,4,3,4,5,4,3,4,4,3,3,4,3,4,5,4,5,4,3,2,4,4,3,4,3,4,4,3,3,2,3,3,3,3,3,3,3,4,3,3,3,3,3,3,2,2,3,2,2,2,2,3,2,2,2,3,2,2,1,2,2,1,2,3,3,3,3,4,3,2,2,3,2,1,2,1,2,2,3,3,3,3,3,4,2,2,1,1,2,1,2,3,3,3,2,3,2,2,0,2,2,3,3,         ]

    H[110] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,5,6,5,5,5,4,4,3,4,4,4,5,5,5,5,6,5,5,5,4,4,4,3,3,4,3,3,3,4,5,4,4,4,5,4,4,3,4,3,2,3,4,4,4,4,4,3,3,3,3,2,3,4,3,2,2,2,2,3,3,3,3,2,1,1,3,4,3,4,5,5,5,4,5,4,4,2,0,1,2,2,         ]

    H[111] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,5,6,5,5,5,4,4,3,4,4,4,5,5,5,5,6,5,5,5,4,4,4,3,3,4,3,3,3,4,5,4,4,4,5,4,4,3,4,3,2,3,4,3,4,4,3,2,2,2,3,2,3,4,3,2,2,1,1,2,2,2,2,1,2,1,3,4,3,4,5,5,5,4,5,4,4,2,1,0,1,1,         ]

    H[112] = [
        math.inf,5,6,5,6,4,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,5,6,6,5,4,6,6,6,6,5,5,5,4,4,3,4,4,4,5,6,5,6,7,6,6,6,4,4,4,3,3,4,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,4,3,4,4,3,2,3,3,4,3,4,5,4,3,3,2,2,2,2,2,2,1,3,2,4,5,4,5,6,6,6,5,6,5,5,3,2,1,0,1,         ]

    H[113] = [
        math.inf,5,6,5,6,3,4,5,4,5,6,5,5,4,5,6,6,5,6,5,4,4,5,4,5,6,5,6,6,5,4,6,6,6,6,5,5,5,4,4,3,4,4,4,5,6,5,6,7,6,6,6,4,4,4,3,2,3,3,3,3,4,5,5,5,5,6,5,5,4,5,3,2,3,4,3,3,3,2,2,3,3,4,3,4,5,4,3,3,2,2,2,1,1,1,1,3,2,4,5,4,5,6,6,6,5,6,5,5,3,2,1,1,0,         ]


    def heuristic(node, destiny):
        return math.sqrt(((destiny[0]-node[0])**2)+((destiny[1]-node[1])**2))

    def total_cost(node, goal, agent):
        # return self.gScore[agent].get(node, math.inf) + H[node][goal]
        return H[node][goal]


    def is_goal(node):
        return node == self.goal

    def getKey(node):
        return node.fScore


    def verifica_posicoes(current):
        if (len(init) == 1):
            return True
        elif (current[0] == current[1]):
            return False
        elif (current[1] == current[2]):
            return False
        elif (current[0] == current[2]):
            return False
        else:
            return True


    def reconstruct_path(current):
        result = []

        while current.parent != None:
            result.append([current.transport, current.node])
            current = current.parent
        result.append([[], current.node])

        return result[::-1]



    def check_tickets(current, neighbor):

        tickets = deepcopy(current)

        for i in range(len(neighbor)):

            if (neighbor[i] == 0):
                tickets[0] -= 1

            elif (neighbor[i] == 1):
                tickets[1] -= 1

            elif (neighbor[i] == 2):
                tickets[2] -= 1

        return tickets





    if (len(init) == 1):
        iterations = H[init[0]][self.goal[0]]
        init_node = Node(None, init, [[]], tickets)
    elif (len(init) == 3):
        iterations = max(H[init[0]][self.goal[0]], H[init[1]][self.goal[1]], H[init[2]][self.goal[2]])
        init_node = Node(None, [init[0], init[1], init[2]], [[], [], []], tickets)




    init_node.hScore = iterations

    self.openSet = [init_node]



    while self.openSet != []:

        self.openSet = sorted(self.openSet, key=getKey)
        current = self.openSet[0]

        self.openSet.remove(current)


        # for i in range(len(init)):


        if (is_goal(current.node)):

            result = reconstruct_path(current)
            return result



        lst_neighbor = list()
        for i in range(len (init)):
            lst_neighbor_aux = []
            for neighbor in self.model[current.node[i]]:
                lst_neighbor_aux.append(neighbor)

            lst_neighbor.append(lst_neighbor_aux)


        if (len(init) == 3):
            lst_neighbor = list(itertools.product(lst_neighbor[0],lst_neighbor[1],lst_neighbor[2]))
        else:
            lst_neighbor = lst_neighbor[0]

        for c_neighbor in lst_neighbor:
            if (len(init) == 3):

                if (not verifica_posicoes([c_neighbor[0][1], c_neighbor[1][1], c_neighbor[2][1]])):
                    continue


                new_tickets = check_tickets(current.tickets, [c_neighbor[0][0],c_neighbor[1][0],c_neighbor[2][0]])
                if (new_tickets[0] < 0 or new_tickets[1] < 0 or new_tickets[2] < 0):

                    continue


                new_node = Node(current, [c_neighbor[0][1],c_neighbor[1][1],c_neighbor[2][1]], [c_neighbor[0][0],c_neighbor[1][0],c_neighbor[2][0]], new_tickets)

                new_node.hScore = max(H[new_node.node[0]][self.goal[0]], H[new_node.node[1]][self.goal[1]], H[new_node.node[2]][self.goal[2]])

                new_node.gScore += 1

                new_node.fScore = new_node.gScore + new_node.hScore

                if new_node not in self.openSet:
                    self.openSet.append(new_node)
                else:
                    for i in self.openSet:
                        if (new_node.node == i.node):
                            i.parent = new_node.parent
                            i.transport = new_node.transport
                            i.tickets = new_node.tickets
                            i.hScore = new_node.hScore
                            i.gScore = new_node.gScore
                            i.fScore = new_node.fScore

            else:


                new_tickets = check_tickets(current.tickets, [c_neighbor[0]])
                if (new_tickets[0] < 0 or new_tickets[1] < 0 or new_tickets[2] < 0):

                    continue

                new_node = Node(current, [c_neighbor[1]], [c_neighbor[0]], new_tickets)

                new_node.hScore = H[new_node.node[0]][self.goal[0]]

                new_node.gScore += 1

                new_node.fScore = new_node.gScore + new_node.hScore

                if new_node not in self.openSet:
                    self.openSet.append(new_node)
                else:
                    for i in self.openSet:
                        if (new_node.node == i.node):
                            i.parent = new_node.parent
                            i.transport = new_node.transport
                            i.tickets = new_node.tickets
                            i.hScore = new_node.hScore
                            i.gScore = new_node.gScore
                            i.fScore = new_node.fScore

    return []
