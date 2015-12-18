#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from numpy import *

PI = math.pi
TRAIN, TEST = 6, 4
maxAcc = 0

def read_data_all():
	data_all, label = [], []
	fr = open('pla_test.txt', 'r')
	for i in xrange(TRAIN+TEST):
		line = fr.readline().strip().split()
		vec = []
		vec.append(1)	# 补1
		for x in xrange(len(line)):
			vec.append(float(line[x]))
		if int(vec[-1]) == 1:
			label.append(1)
		else:
			label.append(-1)
		data_all.append(vec[0:len(vec)-1])
	return data_all, label

def sign(x):  
    if x > 0:
    	return 1
    else:
    	return -1  

# 感知器
def PLA(dataMatrix, classLabels, test_mat, test_label, maxIter, alpha):
    
    length = len(dataMatrix)
    for i in xrange(length):
        classLabels[i] = float(classLabels[i])
    dataMatrix = array(dataMatrix)
    classLabels = array(classLabels)
    m, n = shape(dataMatrix)
    # 训练权重
    weights = ones(n)
    for i in xrange(maxIter):
        for i in range(m):
            h = sign(sum(dataMatrix[i] * weights))
            if h != classLabels[i]:
            	weights = weights + classLabels[i] * dataMatrix[i]

    # 得到预测向量
    predict_vec = []
    for i in xrange(TEST):
        res = sign(sum(test_mat[i] * weights))
        # print res
        if res > 0:
        	predict_vec.append(1)
        else:
        	predict_vec.append(-1)
    print predict_vec
    # 计算预测的准确率
    # global maxAcc
    # cnt = 0
    # for i in xrange(TEST):
    #     if test_label[i] == predict_vec[i]:
    #         cnt += 1
    # if maxAcc < cnt*1.0/TEST:
    #     maxAcc = cnt*1.0/TEST
    #     print (maxAcc, maxIter)
        # return w     
    # print ("Accuracy: ", cnt*1.0/TEST)

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
    # print len(data_all[0])
    data_all = normalize(data_all)

    train_mat = data_all[0:TRAIN]
    test_mat = data_all[TRAIN:TRAIN+TEST]
    train_label = label_all[0:TRAIN]
    test_label = label_all[TRAIN:TRAIN+TEST]
    # print len(test_mat[0])
    alpha = 1
    maxIter = 100
    PLA(train_mat, train_label, test_mat, test_label, maxIter, alpha)
    # f = open('out.txt', 'w')
    # for i in w:
    #     print >> f, i
    
if __name__ == '__main__':
    main()
	