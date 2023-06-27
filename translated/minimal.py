import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.interpolate import interp1d

from quadpoints import quadpoints

EXPN  = 10
MMAX  = 10
NM    = 100
TBAR  = 25
SIGMA = 0.25
Y     = 1
R     = 0.05
DF    = 0.95

quadp, quadw = quadpoints(EXPN, 0, 1)
quadstnorm = norm.ppf(quadp, 0, 1)
savingsgrid = np.array([list(np.linspace(0, MMAX, NM))]) # This nesting enables a (1,100) rather than (100,) shape so we can multiply it as a matrix.
policy = np.array([{"w": [0, 100], "c": [0, 100]} for _ in range(25)])
for i in range(23, 0, -1):
    w1 = Y + np.matmul(np.exp(quadstnorm * SIGMA) * (1 + R), savingsgrid)
    c1 = np.interp(w1, policy[i+1]["w"], policy[i+1]["c"])
    rhs = np.matmul(np.transpose(quadw), (1./c1))
    policy[i]["c"] = np.insert(1./(DF * (1 + R) * rhs), 0, 0)
    policy[i]["w"] = np.insert(savingsgrid + policy[i]["c"][1:], 0, 0)

for val in policy:
    plt.plot(list(val["w"]), list(val["c"]))

plt.xlim(0, MMAX)
plt.ylim(0, MMAX)
plt.xlabel("Wealth")
plt.ylabel("Optimal consumption")
plt.title("Optimal consumption rules by age")
plt.show()