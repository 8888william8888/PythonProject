#coding=utf-8
import  itchat
from itchat.content import *

@itchat.msg_register(msgType=INCOME_MSG,isFriendChat=True,isGroupChat=False,isMpChat=False)
def recv_msg(msg):
    print(msg['Type'])
    if msg['Type'] == TEXT :
        print(msg['FromUserName'],msg['ToUserName'],":",msg['Text'])
        print(msg['User']['UserName'],":",msg['User']['NickName'])


#登录
itchat.auto_login()
#运行
itchat.run(debug=True)
#退出登录
itchat.logout()
