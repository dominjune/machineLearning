#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from numpy import *

PI = math.pi
TRAIN, TEST = 27751, 11893

ans = []
fr = open('answer.txt', 'r')
for i in xrange(TEST):
    line = fr.readline().strip().split()
    for j in xrange(len(line)):
        ans.append(int(line[j]))

def read_train():
    data, label = [], []
    fr = open('Datac_train.txt', 'r')
    for i in xrange(TRAIN):
        line = fr.readline().strip().split()
        for x in xrange(len(line)-1):
        	line[x] = float(line[x])
        label.append(line[-1])
        data.append(line[:len(line)-1])
    return data, label


def read_test():
	data = []
	fr = open('Datac_test.txt', 'r')
	for i in xrange(TEST):
		line = fr.readline().strip().split()
		# print len(line)
		for x in xrange(len(line)):
			line[x] = float(line[x])
		data.append(line[:len(line)])
	return data

def trainNB(train_mat, train_label):
    length = len(train_mat[0])
    p = train_label.count('1') / float(TRAIN)
    vec0, vec1, p0Vec, p1Vec = [], [], [], []
    for k in xrange(TRAIN):
        if train_label[k] == '0':
            vec0.append(train_mat[k])
        else:
            vec1.append(train_mat[k])
    # 算出每一维度均值和方差
    for i in xrange(length):
        col0 = [l[i] for l in vec0]; col1 = [l[i] for l in vec1]
        m0 = mean(col0); v0 = var(col0)
        m1 = mean(col1); v1 = var(col1)
        # print >> f, v1
        p0Vec.append([m0, v0]); p1Vec.append([m1, v1])
    return p0Vec, p1Vec, p
    
def classifyNB(p0Vec, p1Vec, test, p):
    length = len(p0Vec)
    p1, p0 = p, 1.0-p
    for i in xrange(length):
        p0 *= (1.0 / (2*PI*p0Vec[i][1])**0.5) * exp( -((test[i] - p0Vec[i][0])**2) / (2 * p0Vec[i][1])) # Normal Distribution
        p1 *= (1.0 / (2*PI*p1Vec[i][1])**0.5) * exp( -((test[i] - p1Vec[i][0])**2) / (2 * p1Vec[i][1]))
    if p1 > p0:
        return 1
    else:
        return 0
        
def nb(train, test, label):
    ret = []
    p0Vec, p1Vec, p = trainNB(train, label)
    for i in xrange(TEST):
        res = classifyNB(p0Vec, p1Vec, test[i], p)
        ret.append(res)
    # print ret
    cnt = 0
    for i in xrange(TEST):
    	if ret[i] == ans[i]:
    		cnt += 1
    print cnt * 1.0 / TEST
    return ret

# def normalize(t_mat):
#     col = len(t_mat[0])
#     row = len(t_mat)
    
#     for i in xrange(col):
#         if i != 0:
#             l = [l[i] for l in t_mat]
#             s = sum(l)
#             for x in xrange(row):
#                 t_mat[x][i] /= s
#     return t_mat

def main():
    train_mat, train_label = read_train()
    test_mat = read_test()
    
    # print len(train_mat[0])
    # print len(test_mat[0])
    # train_mat = normalize(train_mat)
    # test_mat = normalize(test_mat)

    predict_vec = nb(array(train_mat), array(test_mat), train_label) 

    # f = open('out1.txt', 'w')
    # for i in predict_vec:
        # print >> f, i
    
if __name__ == '__main__':
    main()