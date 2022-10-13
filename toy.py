from pulp import *

prob = LpProblem("ToyProblem", LpMaximize)

x = LpVariable("Toy_A_units", 0, None, LpInteger)
y = LpVariable("Toy_B_units", 0, None, LpInteger)

prob += 25*x + 20*y, "Total profit; to be maximized"

prob += 5*x + 5*y <= 9*60, "Time constraint"
prob += 20*x + 12*y <= 2000, "Resource constraint"

prob.writeLP("ToyProblem.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Profit that can be earned = ", value(prob.objective))
