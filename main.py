from pulp import *

prob = LpProblem("The Miracle Worker", LpMaximize)

x = LpVariable("Medicine_1_units", 0, None, LpInteger)
y = LpVariable("Medicine_2_units", 0, None, LpInteger)

prob += 25*x + 20*y, "Health restored; to be maximized"

prob += 3*x + 4*y <= 25, "Herb A constraint"
prob += 2*x + y <= 10, "Herb B constraint"

prob.writeLP("MiracleWorker.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Total Health that can be restored = ", value(prob.objective))
