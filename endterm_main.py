#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import endterm_utils as u
import endterm_construction as c
import endterm_ls as ls
import time

# Random seed, do not change
random.seed(20240626)

# Data for the Review questions
n = 100
capacity = 200

v, w = u.create_data(n)

total_time = 0
# Call the construction and local search functions
start = time.time()
solution = c.random_construction(n, capacity, v, w)
total_time += time.time() - start

# Uncomment the next lines to print the current knapsack problem solution
print("-" * 20)
print("Initial solution: ")
u.print_sol(solution, w, v, capacity)
print("Total time:", total_time, "seconds")

start = time.time()
new_solution_swap = ls.bi_swap_ls(solution, v, w, capacity)
total_time_swap = total_time + time.time() - start

# Uncomment the next lines to print the current knapsack problem solution
print("-" * 20)
print("After Local Search: ")
u.print_sol(new_solution_swap, w, v, capacity)
print("Swap BI running time:", time.time() - start, "seconds")
print("Total time:", total_time_swap, "seconds")

start = time.time()
new_solution_insert = ls.fi_insert_ls(new_solution_swap, v, w, capacity)
total_time_insert = total_time_swap + time.time() - start

# Uncomment the next lines to print the current knapsack problem solution
print("-" * 20)
print("After Local Search 2: ")
u.print_sol(new_solution_insert, w, v, capacity)
print("Insert FI running time:", time.time() - start, "seconds")
print("Total time:", total_time_insert, "seconds")
print("-" * 20)

# Write code to 
# 1. Generate N initial solutions using the sequential random heuristic
# 2. Call the swap local search and then the insert local search to improve them
# 3. Store the best solution and the best cost found so far
N = 10
best_solution = None
best_value = 0

for _ in range(N):
    solution = c.sequential_random(n, capacity, v, w)
    solution = ls.bi_swap_ls(solution, v, w, capacity)
    solution = ls.fi_insert_ls(solution, v, w, capacity)
    total_value = u.calc_value(solution, v)
    if total_value > best_value:
        best_value = total_value
        best_solution = solution

print("-" * 20)
print('Best of', N, 'trials:')
u.print_sol(best_solution, w, v, capacity)
print("-" * 20)







