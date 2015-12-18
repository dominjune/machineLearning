#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from numpy import *
from gensim import corpora, models, similarities
from pprint import pprint   # pretty-printer
from collections import defaultdict
from time import clock

# 训练样本数量，特征数量
TRAIN, TEST, FEATURE = 7, 7, 4
# 预测向量
predict_vec = []
keys = []
errors = []

# 读取文件
def read_data_all():
	data_all, label_all = [], []
	with open('tree_test.txt', 'r') as fr:
		for line in fr.readlines():
		    word = line.strip().split()
		    for x in xrange(len(word)-1):
		    	word[x] = int(word[x])
		    label_all.append(word[-1])
		    data_all.append(word[0:len(word)])
   		return data_all, label_all

# 计算熵
def calcEntropy(data):
	num = len(data)
	labelCount = {}
	for featureVec in data:
		# print featureVec
		label = featureVec[-1]
		if label not in labelCount.keys():
			labelCount[label] = 0
		labelCount[label] += 1

	entropy = 0.0

	for key in labelCount:  
		prob = float(labelCount[key])/num
		if prob != 0:  
			entropy -= prob*log(prob)/log(2)
	return entropy		

# 建决策树
def buildTree(data):
	# bestFeature = findBestFeature(data)
	label = [l[-1] for l in data]
	# bestFeature = findBestFeature(data)
	# print label
	if label.count(label[0]) == len(label):		# count数第一个标签的个数
		return label[0]
	# if len(data[0])==1:  # no more features, vote for the most
		# return most_occur_label(label)  

	bestFeature = findBestFeature(data)
	# print bestFeature
	bestFeatureLabel = bestFeature + 1

	decisionTree = {bestFeatureLabel: {}}
	featureValue = [l[bestFeature] for l in data]
	kindsOfFeature = set(featureValue)


	for feature in kindsOfFeature:
		subData = choose(data, bestFeature, feature)
		decisionTree[bestFeatureLabel][feature] = buildTree(subData)
	return decisionTree


# 找到信息增益最大的特征
def findBestFeature(data):
	num = len(data[0])-1
	# print num
	HD = calcEntropy(data)
	Gain = 0.0
	bestFeature = -1
	for i in xrange(num):
		featureValue = [l[i] for l in data]
		kindsOfFeature = set(featureValue)
		HDA = 0.0
		for feature in kindsOfFeature:
			subData = choose(data, i, feature)
			prob = len(subData) / float(len(data))
			HDA += prob * calcEntropy(subData)
		# print HD-HDA
		if HD - HDA > Gain:
			Gain = HD - HDA
			bestFeature = i
	return bestFeature

# 选出对应特征的值的向量
def choose(data, i, feature):
	ret = []
	for f in data:
		if f[i] == feature:
			newFeatureVec = f[:i]  
			newFeatureVec.extend(f[i+1:])
			ret.append(newFeatureVec)  
	return ret

def most_occur_label(classList):
    classCount = {}  
    for vote in classList:  
        if vote not in classCount.keys():  
            classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.iteritems(),key = operator.itemgetter(1),reverse = True)  
    # print sortedClassCount
    return sortedClassCount[0][0]  


def predict(tree, newObject):
	while isinstance(tree,dict):  
		key = tree.keys()[0]
		tree = tree[key][newObject[key]]
	return tree  

def main():
	data_all, label_all = read_data_all()
	train_mat = data_all[0:TRAIN]
	test_mat = []
	for i in xrange(TRAIN, TRAIN+TEST):
		vec = data_all[i]
		test_mat.append(vec[0:4])
	print train_mat

	train_label = label_all[0:TRAIN]
	decision_tree = buildTree(train_mat)
	print decision_tree
	# for i in xrange(TEST):
	# 	print predict(decision_tree, test_mat[i])

if __name__ == '__main__':
	main()
	
	