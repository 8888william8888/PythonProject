#coding=utf-8
import  itchat

itchat.auto_login()
list_friends=itchat.get_friends()

one_user=list_friends[0]
for key in one_user:
    print(key,":",one_user[key])
