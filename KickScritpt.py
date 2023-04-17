import aminofix
import os
import time

client=aminofix.Client()
oldId = []
while True:
    try:
        client.login(email=input("\tEmail >> "), password=input("\tPassword >> "))
        print("\tlogin is successful!\n")
        break
    except:
        print("\tlogin failed, please check your email or password..\n")
while True:
    try:
        link=input("\tenter the link to the chat >>")
        code = client.get_from_code(link)
        print("\tNDCID of the chat was received successfully!\n")
        break
    except:
        print("\tThe attempt to get NDCID from the link failed, check the link for authenticity..\n")
subclient=aminofix.SubClient(comId=code.comIdPost, profile=client.profile)
count=input("\tEnter the number of users in the chat>>")
users=subclient.get_chat_users(chatId=code.objectId, start = 0, size = count)
content="МАМА ПОДОХЛА"
title="МАМА ПОДОХЛА)))"
try:
    subclient.edit_chat(chatId=code.objectId, title=title, content=content, publishToGlobal=1)
    print("\tgood\n")
except:
    pass
while True:
    for userId, name in zip(users.userId, users.nickname):
        if userId in oldId:
            pass
        else:
            try:
                subclient.kick(userId = userId, chatId=code.objectId, allowRejoin = False)
                print(f"\t{name} was successfully kicked\n")
            except:
                print(f"\t{name} has it already been kicked, or is it an assistant\n")
            oldId.append(id)
            
