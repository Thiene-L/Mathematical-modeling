# 导入包
from scipy import optimize
import numpy as np

# 确定c, A, b, Aeq, beq
c = np.array([2, 3, -5])
A = np.array([[-2, 5, -1], [1, 3, 1]])
b = np.array([-10, 12])
Aeq = np.array([[1, 1, 1]])
beq = np.array([7])

# 求解
res = optimize.linprog(-c, A, b, Aeq, beq)
print(res)

