#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
from numpy import *

TRAIN, TEST, K = 10, 10, 1

def read_file(str):
	data, label = [], []
	fr = open(str+'.txt', 'r')
	for i in xrange(TRAIN):
		line = fr.readline().strip().split()
		for x in xrange(1, len(line)):
			line[x] = float(line[x])
		label.append(line[-1])
		data.append(line[1:len(line)])
	return data, label

def read_test(str):
	data = []
	fr = open(str+'.txt', 'r')
	for i in xrange(TEST):
		line = fr.readline().strip().split()
		# print len(line)
		for x in xrange(len(line)):
			line[x] = float(line[x])
		data.append(line[1:len(line)])
	return data

def knn(train, test):
	ret = []
	for i in xrange(5):
		res = 1000000
		for j in xrange(5):
			# 夹角余弦
			# cos_sim = dot(train[j], test[i]) / ( (sum(train[j]**2)**0.5) * (sum(test[i]**2)**0.5))
			# 曼哈顿距离
			# dis = abs(train[j] - test[i])
			# dis = sum(dis)
			# 欧式距离
			dis = train[j] - test[i]
			dis = sum(dis ** 2) ** 0.5
			print dis,
			if res > dis:
				index = j
				res = dis
		print 
		# ret.append(label[index])
		# print label[index]
	return ret
	


def main():
	all_mat, all_label = read_file('dataset_DT')
	train_mat = []
	test_mat = []
	# train_label = []
	print len(all_mat)
	for i in xrange(5):
		train_mat.append(all_mat[i])
		# train_label.append(all_label[i])
	for i in xrange(5, 10):
		test_mat.append(all_mat[i])
	
	# print len(train_mat[0])
	# print len(test_mat[0])
	predict_vec = knn(array(train_mat), array(test_mat)) 
	# f = open('out2.txt', 'w')
	# for i in predict_vec:
		# print >> i

if __name__ == '__main__':
	main()

	