#coding=utf-8
import  itchat
from itchat.content import *

@itchat.msg_register(msgType=INCOME_MSG,isFriendChat=True,isGroupChat=True,isMpChat=True)
def recv_msg(msg):
    print(msg);

#登录
itchat.auto_login()
#运行
itchat.run(debug=True)
#退出登录
itchat.logout()
