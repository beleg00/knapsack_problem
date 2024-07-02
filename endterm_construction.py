#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Construction Heuristics File
"""
import random

def random_construction(n, c, values, weights):
    candidates = []
    for i in range(n):
        candidates.append(i)
    random.shuffle(candidates)
    t_weight = 0
    solution = [False]*n
    i = 0
    stop = False
    while not stop:
        cand = candidates[i]
        if t_weight + weights[cand] <= c:
            solution[cand] = True
            t_weight += weights[cand]
        else:
            stop = True
        i+=1
        
    return solution

def sequential_random(n, c, values, weights):
    solution = [False] * n
    t_weight = 0
    candidates = list(range(n))
    
    # Place n/10 random items
    random.shuffle(candidates)
    for i in range(n // 10):
        if t_weight + weights[candidates[i]] <= c:
            solution[candidates[i]] = True
            t_weight += weights[candidates[i]]
    
    # Add remaining items sequentially
    for i in range(n):
        if t_weight + weights[i] <= c and not solution[i]:
            solution[i] = True
            t_weight += weights[i]
    
    return solution
        