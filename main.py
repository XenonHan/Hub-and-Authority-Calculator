"""
Author: Xenon Han
Last modified date: 30/11/2021
"""
import numpy as np

# Give me the adjacency matrix first, from left to right, up to down, each separate by space
# Actually the hub matrix and the authority matrix is transport relation, but no sure which one the user want to use, so
# simple ask for all
hub_matrix = list(
    input("Give me the adjacency matrix for the hub, from left to right, up to down, each separate by space: ").split(
        " "))
authority_matrix = list(
    input(
        "Give me the adjacency matrix for the authority, from left to right, up to down, each separate by space: ").split(
        " "))
v = int(input("Input the number of vertices: "))
hub = [1] * v  # initialize to 1, you can change to other value
authority = [1] * v  # initialize to 1, you can change to other value

hub_matrix = list(map(float, hub_matrix))  # convert from string to float
authority_matrix = list(map(float, authority_matrix))  # convert from string to float

# transform the list the adjacency matrix
M = np.array(hub_matrix).reshape(v, int(len(hub_matrix) / v))
M_t = np.array(authority_matrix).reshape(v, int(len(authority_matrix) / v))

print("adjacency matrix for hub:\n", M)
print("\nadjacency matrix for authority:\n", M_t)

MM_t = np.dot(M, M_t)  # h = MM_T * h
M_tM = np.dot(M_t, M)  # a = M_tM * a
print("\nMM_t for hub:\n", MM_t)
print("\nM_tM for authority:\n", M_tM)

vector_sum = 0
iteration = 0
old_hub = hub
old_authority = authority

# calculate hub till convergence
while True:
    hub = np.dot(MM_t, hub)
    vector_sum = np.sum(hub, axis=0)
    hub = hub / vector_sum * v  # normalization
    if np.all(hub - old_hub < 0.00001):  # vector with 0's
        break
    print("\niteration", iteration, "hub value:\n", hub)
    old_hub = hub
    iteration += 1

print("Hub vector convergence at iteration", iteration, ", FINAL hub value:\n", hub)

# calculate authority till convergence
iteration = 0
while True:
    authority = np.dot(M_tM, authority)
    vector_sum = np.sum(authority, axis=0)
    authority = authority / vector_sum * v  # normalization
    if np.all(authority - old_authority < 0.00001):  # vector with 0's
        break
    print("\niteration", iteration, "authority value:\n", authority)
    old_authority = authority
    iteration += 1

print("Authority vector convergence at iteration", iteration, ", FINAL authority value:\n", authority)

np.set_printoptions(suppress=True)
print("\n\nNormalized Hub Weight: ", np.round(hub, 4))
print("Normalized Authority Weight: ", np.round(authority, 4))
