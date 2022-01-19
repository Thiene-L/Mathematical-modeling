from scipy.optimize import minimize
import numpy as np


# 3. Demo3：多变量边界约束优化问题(Scipy.optimize.minimize)
# 定义目标函数
def objf3(x):  # Rosenbrock 测试函数
    fx = sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)
    return fx


# 定义边界约束（优化变量的上下限）
b0 = (0.0, None)  # 0.0 <= x[0] <= Inf
b1 = (0.0, 10.0)  # 0.0 <= x[1] <= 10.0
b2 = (-5.0, 100.)  # -5.0 <= x[2] <= 100.0
bnds = (b0, b1, b2)  # 边界约束

# 优化计算
xIni = np.array([1., 2., 3.])
resRosen = minimize(objf3, xIni, method='SLSQP', bounds=bnds)
xOpt = resRosen.x

print("xOpt = {:.4f}, {:.4f}, {:.4f}".format(xOpt[0], xOpt[1], xOpt[2]))
print("min f(x) = {:.4f}".format(objf3(xOpt)))
