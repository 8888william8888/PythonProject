#!/usr/bin/python
#coding=utf-8
import cv2
import matplotlib.pyplot as plt
import matplotlib.font_manager
import itchat
import os
import sys

class DataFromWebchat:
    def __init__(self,facedir):
        #初始化存放目录
        self.facedir=facedir
        pass
    def downloadFriendsFaces(self):
        #登录
        print("开始登录.....")
        itchat.auto_login(hotReload=True)
        #获取好友列表
        print("开始获取好友列表.....")
        friends=itchat.get_friends()
        #下载好友头像
        counter=0
        print("开始下载好友头像.....")
        for friend in  friends:
            print(".",end="")
            if (counter+1)%60==0:
                print()
            sys.stdout.flush()
            username=friend['UserName']
            #获取图像并保存
            filename=self.facedir+"face%05d.png"%(counter)
            with open(filename,"wb") as fd:
                faceData = itchat.get_head_img(userName=username)
                fd.write(faceData)
            counter+=1
            #下面是为了提高测试速度，正是运行可以注释掉
            #if counter>=50:
            #    break
        print("")
        print("好友头像下载完毕！")
class AiR:
    def __init__(self,facedir):
        #分类器初始化
        self.classfier=cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
        #图像目录
        self.facedir=facedir
    def recognize(self):
        sum=0
        isface=0
        #遍历图像目录逐个识别
        print("开始识别好友头像是否是人脸.....")
        files=os.listdir(self.facedir)
        for file in files:

            if (sum+1)%60==0:
                print()
            file=self.facedir + file
            if os.path.splitext(file)[1] == ".png":
                img=cv2.imread(file)
                faces=self.classfier.detectMultiScale(image=img,scaleFactor=1.2,minNeighbors=5)
                if len(faces)>0:
                    isface+=1
                    print("\033[32m.\033[0m", end="")
                else:
                    print("\033[31mx\033[0m", end="")
                sys.stdout.flush()
                sum+=1
        print()
        print("头像识别完毕！")
        return (sum,isface)

class VisualData:
    def __init__(self):
        #初始化绘制环境
        self.font = matplotlib.font_manager.FontProperties(fname="msyh.ttf")
        plt.figure(figsize=(8, 5), dpi=80)
        plt.axes(aspect=1)

    def visualPie(self,data):
        sum=data[0]
        isfaces=data[1]
        print("数据分析可视化!")
        pie=plt.pie((100.0*isfaces/sum,100.0*(sum-isfaces)/sum),   #绘制数据
                labels=("使用人脸做头像","不使用人脸做头像"),  # 性别展示标签
                colors=("red","gray"),  # 饼图区域配色
                labeldistance=1.1,  # 标签距离圆点距离
                autopct='%5.2f%%',  # 饼图区域文本格式
                shadow=False,  # 饼图是否显示阴影
                startangle=0,  # 饼图起始角度
                pctdistance=0.6,  # 饼图区域文本距离圆点距离
            )
        for item in pie[1]:
            item.set_fontproperties(self.font)
        plt.title('微信好友使用人脸头像情况(总数=%d)'%data[0],fontproperties=self.font)
        plt.show()

FACEDIR="./faces/"
class AnalysisApp:
    data=DataFromWebchat(FACEDIR)
    ai = AiR(FACEDIR)
    visual=VisualData()

    def analysis(self):
        print("开始分析.....")
        self.data.downloadFriendsFaces()
        sum,isfaces=self.ai.recognize()
        self.visual.visualPie((sum,isfaces))
app=AnalysisApp()
app.analysis()

