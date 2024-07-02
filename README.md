# Knapsack Problem

The knapsack problem is a well-known decision problem where you need to select a subset of objects to maximize the overall value carried in a knapsack, given a weight constraint. Specifically, you have:

- A set of \( n \) objects, each with a specific value and weight.
- A maximum weight capacity \( w_{max} \) for the knapsack.

The goal is to select a subset of size \( s \leq n \) to maximize the total value without exceeding the weight capacity.

## Example Data Set

Below is an example data set for the knapsack problem:

| Item ID | Value | Weight |
|---------|-------|--------|
| 0       | 21    | 4      |
| 1       | 29    | 3      |
| 2       | 13    | 7      |
| 3       | 22    | 8      |
| 4       | 13    | 9      |
| 5       | 11    | 8      |
| 6       | 15    | 5      |
| 7       | 23    | 8      |
| 8       | 10    | 12     |
| 9       | 17    | 10     |

- **Capacity (\( w_{max} \))**: 25

## Solution Representation

In Python, a solution to this problem is represented as a list of boolean values of size \( n \). 

- A value of `True` at position \( i \) means that item \( i \) is included in the knapsack.
- A value of `False` at position \( i \) means that item \( i \) is not included in the knapsack.

The solution value is calculated as the sum of the values of all items included in the knapsack. In a feasible solution, the total weight of the selected items does not exceed the knapsack's capacity.

### Example Solution

For the provided data set, a possible solution could be:

\[ s = [True, True, False, True, False, False, False, True, False, False] \]

- **Selected Items**: Item 0, Item 1, Item 3, Item 7
- **Total Value**: 95
- **Total Weight**: 4 + 3 + 8 + 8 = 23 (which is within the capacity of 25)
