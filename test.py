#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 11:15
# @Author  : SongSa
# @Desc    : 
# @File    : test.py
# @Software: PyCharm
with open(r'F:\code\NLP\NLP_job\albert_zh\data\eval_results_albert_zh.txt', 'r', encoding='utf-8') as f:
    step = None
    precision = None
    recall = None
    f1 = None
    for list in f.readlines():
        # print(list)
        if 'global_step ' in list:
            t_step = list.split(' = ')[-1].replace('\n', '')
            step = t_step
        elif 'precision ' in list:
            t_precision = list.split(' = ')[-1].replace('\n', '')
            precision = t_precision
        elif 'recall ' in list:
            t_recall = list.split(' = ')[-1].replace('\n', '')
            recall = t_recall
        else:
            continue
        if recall:
            # print('-------')
            # print(precision)
            # print(recall)
            # print('----')
            f1 = (2*float(precision)*float(recall))/(float(precision) + float(recall))
            print('step: {} --- precision: {} --- recall: {} --- f1: {}'.format(step, precision, recall, f1))
            step = None
            precision = None
            recall = None
            f1 = None