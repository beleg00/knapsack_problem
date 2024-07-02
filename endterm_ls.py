#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Local Search File
"""

import endterm_utils as u

def bi_swap_ls(s, values, weights, capacity):
    improve = True
    while improve:    
        t_value = u.calc_value(s, values)
        best_i = None
        best_j = None
        improve = False
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                if s[i] != s[j]:
                    s[i], s[j] = s[j], s[i] # exchanging the values at s[i] and s[j] (parallel)
                    new_w_value = u.calc_weight(s, weights)
                    if new_w_value <= capacity:
                        new_t_value = u.calc_value(s, values)
                        if new_t_value > t_value:
                            t_value = new_t_value
                            best_i = i
                            best_j = j
                    s[i], s[j] = s[j], s[i]
        
        if best_i != None:
            s[best_i], s[best_j] = s[best_j], s[best_i]
            improve = True
    return s

def fi_insert_ls(s, values, weights, capacity):
    improve = True
    while improve:    
        t_value = u.calc_value(s, values)
        improve = False
        i = 0
        while i < len(s): #(a) Write a condition for the while loop
            if not s[i]: #(b) Check if the item is available for being inserted in the Knapsack
                s[i] = True 
                new_weight = u.calc_weight(s, weights) #(c) Calculate the current weight in the Knapsack
                if new_weight > capacity: #(d) Check if the solution is infeasible
                    s[i] = False#(e) Change the solution back to its previous form
                else:
                    t_value += values[i] #(f) Update the value of the solution
                    improve = True
                    break 

            i += 1
    return s