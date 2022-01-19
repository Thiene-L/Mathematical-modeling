from scipy.optimize import minimize
import numpy as np


# 4. Demo4：约束非线性规划问题(Scipy.optimize.minimize)
def objF4(x):  # 定义目标函数
    a, b, c, d = 1, 2, 3, 8
    fx = a * x[0] ** 2 + b * x[1] ** 2 + c * x[2] ** 2 + d
    return fx


# 定义约束条件函数
def constraint1(x):  # 不等式约束 f(x)>=0
    return x[0] ** 2 - x[1] + x[2] ** 2


def constraint2(x):  # 不等式约束 转换为标准形式
    return -(x[0] + x[1] ** 2 + x[2] ** 3 - 20)


def constraint3(x):  # 等式约束
    return -x[0] - x[1] ** 2 + 2


def constraint4(x):  # 等式约束
    return x[1] + 2 * x[2] ** 2 - 3


# 定义边界约束
b = (0.0, None)
bnds = (b, b, b)

# 定义约束条件
con1 = {'type': 'ineq', 'fun': constraint1}
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'eq', 'fun': constraint3}
con4 = {'type': 'eq', 'fun': constraint4}
cons = ([con1, con2, con3, con4])  # 3个约束条件

# 求解优化问题
x0 = np.array([1., 2., 3.])  # 定义搜索的初值
res = minimize(objF4, x0, method='SLSQP', bounds=bnds, constraints=cons)

print("Optimization problem (res):\t{}".format(res.message))  # 优化是否成功
print("xOpt = {}".format(res.x))  # 自变量的优化值
print("min f(x) = {:.4f}".format(res.fun))  # 目标函数的优化值
