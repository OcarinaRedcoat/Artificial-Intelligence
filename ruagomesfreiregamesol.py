import math
import pickle
import time
from copy import deepcopy


class SearchProblem:
  def __init__(self, goal, model, auxheur=[]):
    self.goal = goal #obejtivo
    self.model = model #grafo com as transicoes entre localizacoes
    self.auxheur = auxheur

    self.g_agent1 = 0
    self.g_agent2 = 0
    self.g_agent3 = 0

    self.queue = []
  def search(self, init, limitexp=2000, limitdepth=10, tickets=[math.inf, math.inf, math.inf]):
    def cost(agent): # agent represents the index, agent 1 is index 0, 2 is index 1 and 3 is index 2
    #TODO: fix this fuction
        if (agent == 0):
            self.g_agent1 += 1
            return self.g_agent1
        elif (agent == 1):
            self.g_agent2 += 1
            return self.g_agent2
        else:
            self.g_agent3 += 1
            return self.g_agent3

    def heuristic(node, destiny):  #send the tupple of coords of the nodes in auxheur
        return math.sqrt(((destiny[0]-node[0])**2)+((destiny[1]-node[1])**2))

    def total_cost(node, agent): # function f that reperesent g + h
        return heuristic(self.auxheur[node-1] , self.auxheur[self.goal[agent]-1])

    def is_goal(node):
        return node == self.goal[0]

    def successors(node):
        succ = deepcopy(self.model[node])
        for i in range (len(succ)):
            cost = total_cost(succ[i][1], 0)
            succ[i].append(cost)
            self.queue.append(succ[i])
        return succ


    shortest_path = [[[], init]]

    if(is_goal(init)):
        return shortest_path


    for i in range (len(init)):
        successors(init[i])

    while (is_goal(shortest_path[-1][1][0])==False):
        smallest_cost_node = []
        for i in range (len(self.queue)):
            if (i == 0):
                smallest_cost_node = [self.queue[i][0], self.queue[i][1], self.queue[i][2]]
            else:
                if (smallest_cost_node[2] > self.queue[i][2]):
                    smallest_cost_node[0] = self.queue[i][0]
                    smallest_cost_node[1] = self.queue[i][1]
                    smallest_cost_node[2] = self.queue[i][2]


        next_node = [[smallest_cost_node[0]], [smallest_cost_node[1]]]
        shortest_path.append(next_node)
        successors(next_node[1][0])

        print(shortest_path)

    return shortest_path
