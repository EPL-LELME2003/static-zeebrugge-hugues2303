import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()

# Define model parameters
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define model variables
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory('/Users/huguesc/Documents/UCL/2024-2025/M1Q2/LELME2003_project_energy')
#sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################

print("test1")
print("test2")