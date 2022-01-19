from scipy.optimize import minimize
import numpy as np


# 6. Demo6：约束非线性规划问题(Scipy.optimize.minimize)
def objF6(args):  # 定义目标函数
    a, b, c, d = args
    fx = lambda x: a * x[0] ** 2 + b * x[1] ** 2 + c * x[2] ** 2 + d
    return fx


def constraint2(args):
    xmin0, xmin1, xmin2 = args
    cons = ({'type': 'ineq', 'fun': lambda x: (x[0] ** 2 - x[1] + x[2] ** 2)},  # 不等式约束 f(x)>=0
            {'type': 'ineq', 'fun': lambda x: -(x[0] + x[1] ** 2 + x[2] ** 3 - 20)},  # 不等式约束 转换为标准形式
            {'type': 'eq', 'fun': lambda x: (-x[0] - x[1] ** 2 + 2)},  # 等式约束
            {'type': 'eq', 'fun': lambda x: (x[1] + 2 * x[2] ** 2 - 3)},  # 等式约束
            {'type': 'ineq', 'fun': lambda x: (x[0] - xmin0)},  # x0 >= xmin0
            {'type': 'ineq', 'fun': lambda x: (x[1] - xmin1)},  # x1 >= xmin1
            {'type': 'ineq', 'fun': lambda x: (x[2] - xmin2)})  # x2 >= xmin2
    return cons


# 求解优化问题
args1 = (1, 2, 3, 8)  # 定义目标函数中的参数
args2 = (0.0, 0.0, 0.0)  # xmin0, xmin1, xmin2
cons2 = constraint2(args2)

x0 = np.array([1., 2., 3.])  # 定义搜索的初值
res2 = minimize(objF6(args1), x0, method='SLSQP', constraints=cons2)

print("Optimization problem (res2):\t{}".format(res2.message))  # 优化是否成功
print("xOpt = {}".format(res2.x))  # 自变量的优化值
print("min f(x) = {:.4f}".format(res2.fun))  # 目标函数的优化值
