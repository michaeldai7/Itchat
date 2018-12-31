#coding=utf8
import itchat, time

itchat.auto_login(True)

SINCERE_WISH = u'来自https://github.com/michaeldai7?tab=repositories'

friendList = itchat.get_friends(update=True)[1:]
for friend in friendList:
    # 如果是演示目的，把下面的方法改为print即可
    itchat.send(SINCERE_WISH)
    time.sleep(.5)