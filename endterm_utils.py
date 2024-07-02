#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Useful Functions File
"""

import random

def create_data(n):
    weights = []
    values = []
    for i in range(n):
        weights.append((random.randint(3, 30)))
        
    for i in range(n):
        values.append((random.randint(20, 200))) 

    return values, weights

def calc_value(solution, values):
    total_value = 0
    for i in range(len(solution)):
        if solution[i]:
            total_value += values[i]
    return total_value

def calc_weight(solution, weights):
    total_weight = 0
    for i in range(len(solution)):
        if solution[i]:
            total_weight += weights[i]
    return total_weight


def print_sol(solution, weights, values, capacity):
    print("The current objects in the knapsack are: ")
    for i in range(len(solution)):
        if solution[i]:
            print(i, end  = " ")
    print()
    total_value = calc_value(solution, values)
    print("Current total value:", total_value)
    total_weight = calc_weight(solution, weights)
    if total_weight <= capacity:
        print("This is a feasible solution with a total weight of " + str(total_weight) + ".")
    else:
        print("Knapsack capacity exceeded. This is not a fesible solution.")