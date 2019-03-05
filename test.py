#! usr/bin/env python3
# -*- coding:utf-8 -*-
import codecs
input_file = './data/train.txt'
print(input_file)
with codecs.open(input_file, 'r', encoding='utf-8') as f:
    lines = []
    words = []
    labels = []
    for line in f:
        contends = line.strip()
        tokens = contends.split(' ')
        if len(tokens) == 2:
            words.append(tokens[0])
            labels.append(tokens[1])
        else:
            if len(contends) == 0:
                l = ' '.join([label for label in labels if len(label) > 0])
                w = ' '.join([word for word in words if len(word) > 0])
                lines.append([l, w])
                words = []
                labels = []
                continue
        if contends.startswith("-DOCSTART-"):
            words.append('')
            continue
    print("读取到train.txt数据量：" + str(len(lines)))