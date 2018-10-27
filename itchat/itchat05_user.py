#coding=utf-8
import  itchat

from itchat.storage.templates import  Chatroom
from itchat.storage.templates import User
from itchat.storage.templates import MassivePlatform


itchat.auto_login()
list_contact=itchat.get_contact()
list_chatrooms=itchat.get_chatrooms()
list_friends=itchat.get_friends()
list_mps=itchat.get_mps()

print(list_contact[0].keys())
print(list_chatrooms[0].keys())
print(list_friends[0].keys())
print(list_mps[0].keys())