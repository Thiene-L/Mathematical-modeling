from scipy.optimize import brent
import numpy as np


def objf(x):  # 目标函数
    fx = x ** 2 - 8 * np.sin(2 * x + np.pi)
    return fx


xIni = -5.0
xOpt = brent(objf, brack=(xIni, 2))
print("xIni={:.4f}\tfxIni={:.4f}".format(xIni, objf(xIni)))
print("xOpt={:.4f}\tfxOpt={:.4f}".format(xOpt, objf(xOpt)))
