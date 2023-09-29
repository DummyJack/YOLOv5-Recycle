import os
import random
import argparse
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('--training_set_path', default='train', type=str, help='input training set path')
parser.add_argument('--val_path', default='valid', type=str, help='output validation set path')
opt = parser.parse_args()

total_percent = 1.0
train_percent = 0.8

inputFilePath = opt.training_set_path
valFilePath = opt.val_path

allImg = os.listdir(inputFilePath+"/images")
if not os.path.exists(valFilePath):
    os.makedirs(valFilePath + "/images")
    os.makedirs(valFilePath + "/labels")
    print("create val images and labels dir")

num = len(allImg) # 總張數
totalDataNum = int(num * total_percent)
totalTrainingNum = int(totalDataNum * train_percent)

print("總張數:" + str(totalDataNum))
print("總訓練集張數:" + str(totalTrainingNum))

trainingSetNames = random.sample(allImg, totalTrainingNum)

for imgName in allImg:
    if not imgName in trainingSetNames:
        imgpath = os.path.join(inputFilePath, "images", imgName)
        shutil.move(imgpath, os.path.join(valFilePath, "images"))
        labelpath = os.path.join(inputFilePath, "labels", imgName[:-4]+".txt")
        shutil.move(labelpath, os.path.join(valFilePath, "labels"))
