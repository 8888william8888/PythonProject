#coding=utf-8
import  itchat
from  itchat.storage.templates import ContactList
itchat.auto_login()
print(itchat.get_contact())
print(itchat.get_chatrooms())
print(itchat.get_friends())
print(itchat.get_mps())

print(type(itchat.get_contact()))
print(type(itchat.get_chatrooms()))
print(type(itchat.get_friends()))
print(type(itchat.get_mps()))
