import numpy as np

# 输入比较矩阵
array = np.array([[1, 2, 7, 5, 5],
                  [1 / 2, 1, 4, 3, 3],
                  [1 / 7, 1 / 4, 1, 1 / 2, 1 / 3],
                  [1 / 5, 1 / 3, 2, 1, 1],
                  [1 / 5, 1 / 3, 3, 1, 1]])

# 定义一个max_cr用来判断一致性是否可以接受
max_cr = 0.1

# 一致性指标RI表(层次分析法很少有大于10个指标，如果超过10则建立二级指标体系)
n_ri = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                 [0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]])

# 给出对象数目
n = array.shape[0]
# 给出矩阵的特征值(eigenvalue)和特征向量(eigenvector)
eigenvalue, eigenvector = np.linalg.eig(array)
# 给出矩阵最大特征值
max_eigenvalue = max(list(map(abs, eigenvalue)))
# 计算CI
ci = (max_eigenvalue - n) / (n - 1)
# 计算CR
cr = ci / n_ri[1][n - 1]

# 判断一致性是否通过
if cr > max_cr:
    # 一致性未通过
    print("一致性未通过！请修改判断矩阵！")
else:
    # 一致性通过，给出权重
    # 给出绝对值最大的特征值对应的特征向量
    max_eigenvector = eigenvector[:, list(map(abs, eigenvalue)).index(max_eigenvalue)]
    # 标准化特征向量即为权重
    standard_max_eigenvector = list(map(abs, max_eigenvector)) / sum(list(map(abs, max_eigenvector)))
    print(standard_max_eigenvector)
