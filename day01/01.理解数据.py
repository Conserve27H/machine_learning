# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
import matplotlib

matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt

examDict = {
    '学习时间': [0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 1.75, 2.00, 2.25,
             2.50, 2.75, 3.00, 3.25, 3.50, 4.00, 4.25, 4.50, 4.75, 5.00, 5.50],
    '分数': [10, 22, 13, 43, 20, 22, 33, 50, 62,
           48, 55, 75, 62, 73, 81, 76, 64, 82, 90, 93]}
examDf = pd.DataFrame(examDict)
print(examDf.head())
# 学习时间  分数
# 0  0.50  10
# 1  0.75  22
# 2  1.00  13
# 3  1.25  43
# 4  1.50  20


# 提取特征和标签
# 特征features
exam_X = examDf.loc[:, '学习时间'].values
# 标签labels
exam_y = examDf.loc[:, '分数'].values

# 绘制散点图
plt.scatter(exam_X, exam_y, color='b', label='exam data')
# 添加图标标签
plt.xlabel('Hours')  # X轴命名
plt.ylabel('Score')  # Y轴命名

print(plt.show())
