# -*- coding: utf-8 -*-
"""
@Auth :YuanHan Zheng
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from scipy.stats import pearsonr
import jieba
import pandas as pd


def iris_demo():
    """
    sklearn数据集简单使用
    """
    iris = load_iris()
    print("鸢尾花数据集：\n", iris)
    print("查看数据集描述：\n", iris["DESCR"])
    print("查看特征值名字：\n", iris.feature_names)
    print("查看特征值：\n", iris.data, iris.data.shape)

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
    print("训练集的特征值：\n", x_train, x_train.shape)
    print("测试集的特征值：\n", x_test, x_test.shape)
    print("训练集的目标值：\n", y_train, y_train.shape)
    print("测试集的目标值：\n", y_test, y_test.shape)


def dict_name():
    """
    字典特征抽取
    """
    data = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]

    # 实例化转换器类
    transfer = DictVectorizer(sparse=False)
    data_new = transfer.fit_transform(data)
    print("经过特征抽取前：\n", data)
    print("经过特征抽取后：\n", data_new)
    print("特征名字：\n", transfer.get_feature_names_out())


def count_demo():
    """
    文本特征抽取：CountVectorizer
    """
    data = ["life is short,i like python",
            "life is too long,i dislike python"]
    # 实例化转换器类
    transfer = CountVectorizer()
    # 停用词
    # stop_words = ["is", "too"]

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())


def count_chinese_demo():
    """
    中文文本特征抽取：CountVectorizer
    """
    data = ["我 爱 北京 天安门", "天安门 上 太阳 升"]
    # 实例化转换器类
    transfer = CountVectorizer()

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())


def cut_word(text):
    """
    进行中文分词："我爱北京天安门" --> "我 爱 北京 天安门"
    """
    return " ".join(list(jieba.cut(text)))


def count_chinese_demo2():
    """
    中文文本特征抽取，自动分词
    """
    # 将中文文本进行分词
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    # data_new = []
    # for sent in data:
    #     data_new.append(cut_word(sent))
    data_new = [cut_word(sent) for sent in data]
    print(data_new)
    # 实例化转换器类
    transfer = CountVectorizer(stop_words=["一种", "所以"])

    # 调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())

    return None


def tfidf_demo():
    """
    用TF-IDF的方法进行文本特征抽取
    """
    # 将中文文本进行分词
    data = ["一种还是一种今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。",
            "我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。",
            "如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。"]

    # data_new = []
    # for sent in data:
    #     data_new.append(cut_word(sent))
    data_new = [cut_word(sent) for sent in data]

    print(data_new)
    # 实例化转换器类
    transfer = TfidfVectorizer(stop_words=["一种", "所以"])

    # 调用fit_transform
    data_final = transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())

    return None


def minmax_demo():
    """
    归一化
    """
    # 获取数据
    data = pd.read_csv("data/dating.txt")
    data = data.iloc[:, :3]
    print("data:\n", data)

    # 实例化转换器类
    transfer = MinMaxScaler(feature_range=(0, 1))

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)

    return None


def stand_demo():
    """
    标准化
    """
    # 获取数据
    data = pd.read_csv("data/dating.txt")
    data = data.iloc[:, :3]
    print("data:\n", data)

    # 实例化转换器类
    transfer = StandardScaler()

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


def variance_demo():
    """
    过滤低方差特征
    """
    # 获取数据
    data = pd.read_csv("data/factor_returns.csv")
    data = data.iloc[:, 1:-2]
    print("data:\n", data)

    # 实例化转换器类
    transfer = VarianceThreshold(threshold=10)

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new, data_new.shape)

    # 计算某两个变量之间的相关系数
    r1 = pearsonr(data["pe_ratio"], data["pb_ratio"])
    print("相关系数：\n", r1)
    r2 = pearsonr(data['revenue'], data['total_expense'])
    print("revenue与total_expense之间的相关性：\n", r2)

    return None


def pca_demo():
    """
    PCA降维
    """
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]

    # 实例化一个转换器类
    transfer = PCA(n_components=0.95)

    # 调用fit_transform
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)
    return None


if __name__ == "__main__":
    # 代码1：sklearn数据集使用
    iris_demo()

    # 代码2：字典特征抽取
    # dict_demo()

    # 代码3：文本特征抽取：CountVectorizer
    # count_demo()

    # 代码4：中文文本特征抽取：CountVectorizer
    # count_chinese_demo()

    # 代码5：中文分词
    # print(cut_word("我爱北京天安门"))

    # 代码6：中文文本特征抽取，自动分词
    # count_chinese_demo2()

    # 代码7：用TF-IDF的方法进行文本特征抽取
    # tfidf_demo()

    # 代码8：归一化
    # minmax_demo()

    # 代码9：标准化
    # stand_demo()

    # 代码10：低方差特征过滤
    # variance_demo()

    # 代码11：PCA降维
    # pca_demo()
