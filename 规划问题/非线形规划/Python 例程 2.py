from scipy.optimize import minimize
import numpy as np


# 5. Demo5：约束非线性规划问题(Scipy.optimize.minimize)
def objF5(args):  # 定义目标函数
    a, b, c, d = args
    fx = lambda x: a * x[0] ** 2 + b * x[1] ** 2 + c * x[2] ** 2 + d
    return fx


def constraint1():  # 定义约束条件函数
    cons = ({'type': 'ineq', 'fun': lambda x: (x[0] ** 2 - x[1] + x[2] ** 2)},  # 不等式约束 f(x)>=0
            {'type': 'ineq', 'fun': lambda x: -(x[0] + x[1] ** 2 + x[2] ** 3 - 20)},  # 不等式约束 转换为标准形式
            {'type': 'eq', 'fun': lambda x: (-x[0] - x[1] ** 2 + 2)},  # 等式约束
            {'type': 'eq', 'fun': lambda x: (x[1] + 2 * x[2] ** 2 - 3)})  # 等式约束
    return cons


# 定义边界约束
b = (0.0, None)
bnds = (b, b, b)
# 定义约束条件
cons = constraint1()
args1 = (1, 2, 3, 8)  # 定义目标函数中的参数
# 求解优化问题
x0 = np.array([1., 2., 3.])  # 定义搜索的初值
res1 = minimize(objF5(args1), x0, method='SLSQP', bounds=bnds, constraints=cons)

print("Optimization problem (res1):\t{}".format(res1.message))  # 优化是否成功
print("xOpt = {}".format(res1.x))  # 自变量的优化值
print("min f(x) = {:.4f}".format(res1.fun))  # 目标函数的优化值
