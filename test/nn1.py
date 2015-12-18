#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from numpy import *

PI = math.pi
TRAIN, TEST = 4, 4
INPUT, HIDDEN, OUT = 2, 2, 1
ni = INPUT + 1; nh = HIDDEN + 1
w1 = ones(ni); w2 = ones(ni); w3 = ones(nh); hiddens = ones(nh)

def read_data_all():
    data_all, label = [], []
    fr = open('nn_test.txt', 'r')
    for i in xrange(TRAIN+TEST):
        line = fr.readline().strip().split()
        vec = []
        vec.append(1)   # 补1
        for x in xrange(len(line)):
            vec.append(float(line[x]))
        label.append(int(vec[-1]))
        data_all.append(vec[0:len(vec)-1])
    return data_all, label

def sigmoid(x):  
    return 1.0/(1+exp(-x))  

# 神经网络
def NN(train_mat, train_label, test_mat, test_label, maxIter, alpha):
    train_mat = array(train_mat)
    train_label = array(train_label)
    m, n = shape(train_mat)
    for i in xrange(maxIter):
        for i in xrange(m):
            # update(train_mat[i])
            BP(train_mat[i], train_label[i], alpha)

    # 得到预测向量
    predict_vec = []
    for i in xrange(TEST):
        res = update(test_mat[i])
        print res
        if res > 0.5:
            predict_vec.append(1)
        else:
            predict_vec.append(0)
    print predict_vec

def update(inputs):
    hiddens[1] = sigmoid(sum(inputs * w1))
    hiddens[2] = sigmoid(sum(inputs * w2))
    output = sigmoid(sum(hiddens * w3))
    return output

def BP(inputs, label, alpha):
    output = update(inputs)
    output_error = (output - label) * (output) * (1 - output)
    hidden_error1 = (hiddens[1]) * (1 - hiddens[1]) * (output_error) * (w3[1])
    hidden_error2 = (hiddens[2]) * (1 - hiddens[2]) * (output_error) * (w3[2])
    for i in xrange(nh):
        w3[i] += alpha * output_error * hiddens[i]
    for i in xrange(ni):
        w1[i] += alpha * hidden_error1 * inputs[i]
        w2[i] += alpha * hidden_error2 * inputs[i]
    
# 对训练和测试集进行归一化
def normalize(data_all):
    col = len(data_all[0])
    row = len(data_all)
    # print row
    for i in xrange(col):
        l = [l[i] for l in data_all]
        minn = min(l)
        maxn = max(l)
        s = sum(l)
        for x in xrange(row):
            # min-max归一化
            data_all[x][i] = (data_all[x][i] - minn + 1) / (maxn - minn + 1)
            # sum归一化
            # data_all[x][i] = data_all[x][i] / s
    return data_all

def main():
    data_all, label_all = read_data_all()
    # data_all = normalize(data_all)
    # print data_all
    train_mat = data_all[0:TRAIN]
    test_mat = data_all[TRAIN:TRAIN+TEST]
    train_label = label_all[0:TRAIN]
    test_label = label_all[TRAIN:TRAIN+TEST]
    
    NN(train_mat, train_label, test_mat, test_label, 10, 0.0001)
    
if __name__ == '__main__':
    main()
    