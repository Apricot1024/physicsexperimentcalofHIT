import math
import numpy as np
import matplotlib.pyplot as plt

# 用到的常量和变量
pi = 3.14159
epsilon0 = 8.85 * (10 ** (-12))
d = 0.318
r = 25
A = pi * (r ** 2)
Rn = []
fs = []
fd = []
epsilonr2 = []
epsilonr1 = []
lnf = []
Us1 = []
Us2 = []
Uz1 = []
Uz2 = []
K = []
tan_delta = []

i = 0
j = eval(input("您要计算几组数据？（请输入阿拉伯数字）"))
j = j - 1


# 收集函数
def gettimes1():
    Rn.append(0)
    fd.append(input("请输入倍率（0.01，0.1，1，10）："))
    if fd[i] == "*0.01" or fd[i] == "0.01":
        Rn[i] = 1000000
    elif fd[i] == "*0.1" or fd[i] == "0.1":
        Rn[i] = 100000
    elif fd[i] == "*1" or fd[i] == "1":
        Rn[i] = 10000
    elif fd[i] == "*10" or fd[i] == "10":
        Rn[i] = 1000
    else:
        print("您输入的倍率有误,请重新输入")
        gettimeswrong1()


def gettimeswrong1():
    fd[i] = input("请输入倍率（0.01，0.1，1，10）：")
    if fd[i] == "*0.01" or fd[i] == "0.01":
        Rn[i] = 1000000
    elif fd[i] == "*0.1" or fd[i] == "0.1":
        Rn[i] = 100000
    elif fd[i] == "*1" or fd[i] == "1":
        Rn[i] = 10000
    elif fd[i] == "*10" or fd[i] == "10":
        Rn[i] = 1000
    else:
        print("您输入的倍率有误,请重新输入")
        gettimeswrong1()


def gettimes2():
    Rn.append(0)
    fd.append(input("请输入倍率（0.01，0.1，1，10）："))
    if fd[i] == "*0.01" or fd[i] == "0.01":
        Rn[i]=(300000)
    elif fd[i] == "*0.1" or fd[i] == "0.1":
        Rn[i]=(30000)
    elif fd[i] == "*1" or fd[i] == "1":
        Rn[i]=(3000)
    elif fd[i] == "*10" or fd[i] == "10":
        Rn[i]=(300)
    else:
        print("您输入的倍率有误,请重新输入")
        gettimeswrong2()


def gettimeswrong2():
    fd[i] = input("请输入倍率（0.01，0.1，1，10）：")
    if fd[i] == "*0.01" or fd[i] == "0.01":
        Rn[i] = 300000
    elif fd[i] == "*0.1" or fd[i] == "0.1":
        Rn[i] = 30000
    elif fd[i] == "*1" or fd[i] == "1":
        Rn[i] = 3000
    elif fd[i] == "*10" or fd[i] == "10":
        Rn[i] = 300
    else:
        print("您输入的倍率有误,请重新输入")
        gettimeswrong2()


def getfrenc():
    fs.append(eval(input("请输入频率（未倍乘）(大于等于10，小于等于99)：")))
    if 10 <= fs[i] <= 39:
        gettimes1()

    elif 40 <= fs[i] <= 99:
        gettimes2()
    else:
        print("您输入的频率有误,请重新输入")
        getfrencwrong()


def getfrencwrong():
    fs[i] = (eval(input("请输入频率（未倍乘）(大于等于10，小于等于99)：")))
    if 10 <= fs[i] <= 39:
        gettimes1()

    elif 40 <= fs[i] <= 99:
        gettimes2()
    else:
        print("您输入的频率有误,请重新输入")
        getfrencwrong()


def getnumscollected():
    Us1.append(eval(input("请输入Us1:")))
    Us2.append(eval(input("请输入Us2:")))
    Uz1.append(eval(input("请输入Uz1:")))
    Uz2.append(eval(input("请输入Uz2:")))


# 绘制函数
def pictureplot():
    epsilonr1p = np.array(epsilonr1)
    tan_deltap = np.array(tan_delta)
    lnfp = np.array(lnf)
    plt.figure()
    plt.scatter(lnfp, epsilonr1p)
    plt.figure()
    plt.scatter(lnfp, tan_deltap)
    plt.show()


# 收集数据
while i <= j:  # 收集j组数据
    # 收集频率数据
    getfrenc()

    # 将fd变为浮点数
    fd[i] = eval(fd[i])

    # 收集测量数据
    getnumscollected()

    # 提示
    print("第{}组数据收集已完成！".format(i + 1))
    print("将开始收集下一组数据")
    i = i + 1

# 计算并输出数据数据
i = 0
while i <= j:
    # 隔开
    print("  ")
    print("以下是第{}组结果".format(i + 1))

    # 计算K
    K.append(d / (A * Rn[i] * ((Us1[i] ** 2) + (Us2[i] ** 2))))
    print("K_{} = {}".format(i + 1, K[i]))

    # 计算epsilon
    epsilonr2.append((K[i] * (abs(Us1[i] * Uz1[i] - Us2[i] * Uz2[i]))) / (2 * pi * fs[i] * fd[i] * epsilon0))
    epsilonr1.append((K[i] * (Us2[i] * Uz1[i] + Us1[i] * Uz2[i])) / (2 * pi * fs[i] * fd[i] * epsilon0))
    print("epsilonr1_{}={}".format(i + 1, epsilonr1[i]))
    print("epsilonr2_{}={}".format(i + 1, epsilonr2[i]))

    # 计算tandelta
    tan_delta.append((abs(Us1[i] * Uz1[i] - Us2[i] * Uz2[i])) / (Us2[i] * Uz1[i] + Us1[i] * Uz2[i]))
    print("tan_delta_{} = {}".format(i + 1, tan_delta[i]))

    # 计算ln(f)
    lnf.append(math.log(fs[i] * fd[i]))
    print("ln(f)_{}={}".format(i + 1, lnf[i]))

    # 提示
    i = i + 1

# 画出散点图
pictureplot()
