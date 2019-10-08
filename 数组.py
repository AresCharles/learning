import numpy as np
import pandas as pd

print("交换数组np.arange(9).reshape(3,3)中的第1列和第2列")
data = np.arange(9).reshape(3, 3)
data[:,[0, 1]] = data[:, [1, 0]]
print(data)

print("交换数组np.arange(9).reshape(3,3)中的第1行和第3行")
data1 = np.arange(9).reshape(3, 3)
data1[:,[0, 2]] = data1[:, [2, 0]]
print(data1)

print("找到数组np.arange(9).reshape(3,3)中每一行的最大值")
data2 = np.arange(9).reshape(3, 3)
print(data2.max(1))

print("找到数组np.arange(9).reshape(3,3)中每一列的最大值")
data2 = np.arange(9).reshape(3, 3)
print(data2.max(0))