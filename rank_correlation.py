from scipy.stats import spearmanr

price = [15.5, 12, 9.5, 11, 0, 10, 10, 5, 8, 8.5, 0, 15, 0]
duration = [4.5, 3, 1, 2, 1.5, 2, 2.5, 2, 2, 1.5, 0.75, 2, 1.5]
appreciation = [5, 4, 3, 2, 3, 4, 1, 5, 4, 1, 3, 2, 5]

print("====================================================")
rho, _ = spearmanr(price, duration)
print("Price ranking and duration ranking's correlation coefficient is {}".format(rho))
if rho == 1:
    print("These rankings are same.")
else:
    print("These rankings are different.")
print()
print("====================================================")
rho, _ = spearmanr(price, appreciation)
print("Price ranking and appreciation ranking's correlation coefficient is {}".format(rho))
if rho == 1:
    print("These rankings are same.")
else:
    print("These rankings are different.")
print()
print("====================================================")
rho, _ = spearmanr(duration, appreciation)
print("Duration ranking and appreciation ranking's correlation coefficient is {}".format(rho))
if rho == 1:
    print("These rankings are same.")
else:
    print("These rankings are different.")
print()
print("====================================================")