from scipy.optimize import fmin
import numpy as np


# 2. Demo2：多变量无约束优化问题(Scipy.optimize.brent)
# Rosenbrock 测试函数
def objf2(x):  # Rosenbrock benchmark function
    fx = sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)
    return fx


xIni = np.array([-2, -2])
xOpt = fmin(objf2, xIni)
print("xIni={:.4f},{:.4f}\tfxIni={:.4f}".format(xIni[0], xIni[1], objf2(xIni)))
print("xOpt={:.4f},{:.4f}\tfxOpt={:.4f}".format(xOpt[0], xOpt[1], objf2(xOpt)))
