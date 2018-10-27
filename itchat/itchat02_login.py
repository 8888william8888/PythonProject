#coding=utf-8
import  itchat
def qr_cb(uuid, status, qrcode):
    print("uuid",uuid)
    print("status",status)
    print("qrcode",qrcode)


def login_cb():
    me=itchat.search_friends()
    print(me)


#def login(self, enableCmdQR=False, picDir=None, qrCallback=None,loginCallback=None, exitCallback=None):
#itchat.login(enableCmdQR=False,picDir='./qq.png',loginCallback=login_cb)
#命令行模式
itchat.login(enableCmdQR=2,loginCallback=login_cb)
