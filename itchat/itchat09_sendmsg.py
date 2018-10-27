#coding=utf-8
import  itchat
import  time

#登录
itchat.auto_login()

#根据昵称找用户
user=itchat.search_friends(nickName='赵德柱')[0]

#每隔5秒给用户发一个短信
for i in range(10):
    itchat.send_msg(msg="辣鸡短信，不必理会！",toUserName=user['UserName'])
    time.sleep(5)

#退出登录
itchat.logout()

