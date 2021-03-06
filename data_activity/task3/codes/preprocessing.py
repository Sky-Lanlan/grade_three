from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import OneHotEncoder
from numpy import vstack, array, nan
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import PolynomialFeatures
from numpy import log1p
from sklearn.preprocessing import FunctionTransformer


# 导入IRIS数据集
iris = load_iris()
# 特征矩阵
iris.data
# 目标向量
iris.target


# 标准化，返回值为标准化后的数据
StandardScaler().fit_transform(iris.data)

# 区间缩放，返回值为缩放到[0, 1]区间的数据
MinMaxScaler().fit_transform(iris.data)

# 归一化，返回值为归一化后的数据
Normalizer().fit_transform(iris.data)

# 二值化，阈值设置为3，返回值为二值化后的数据,简化数据
Binarizer(threshold=3).fit_transform(iris.data)

# 哑编码，对IRIS数据集的目标值，返回值为哑编码后的数据
OneHotEncoder().fit_transform(iris.target.reshape((-1, 1)))

# 由于iris数据集没有缺失值，所以对数据集新增一个样本
# 缺失值计算，返回值为计算缺失值后的数据
# 参数missing_value为缺失值的表示形式，默认为NaN
# 参数strategy为缺失值填充方式，默认为mean（均值）
Imputer().fit_transform(vstack((array([nan, nan, nan, nan]), iris.data)))

# 多项式转换
# 参数degree为度，默认值为2
PolynomialFeatures().fit_transform(iris.data)

# 自定义转换函数为对数函数的数据变换
# 第一个参数是单变元函数
FunctionTransformer(log1p).fit_transform(iris.data)
