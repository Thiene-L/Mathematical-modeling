# 导入包
import numpy as np
import cvxpy as cp

# 设置目标函数中变量个数
n = 3

# 输入目标函数的系数
c = np.array([3, 1, 3])

# 输入约束条件的系数矩阵（3×3）
a = np.array([[-1, 2, 1], [0, 4, -3], [1, -3, 2]])

# 输入b值（3×1）
b = np.array([4, 2, 3])

# 创建x，个数是3
x = cp.Variable(n, integer=True)

# 明确目标函数（此时c是3×1，x是3×1,但python里面可以相乘）
objective = cp.Maximize(cp.sum(c * x))

# 明确约束条件，其中a是3×3，x是3×1,a*x=b(b为3×1的矩阵)
constriants = [0 <= x, a * x <= b]
# 求解问题
prob = cp.Problem(objective, constriants)
# 这里solver必须使用cp.CPLEX,否则计算不出来
resluts = prob.solve(solver=cp.CPLEX)

# 输入结果
print(prob.value)  # 目标函数的值
print(x.value)  # 各x的值
