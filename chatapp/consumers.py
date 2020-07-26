import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Activeuser,Chat_message,Chat_room
from .datetime import get_datetime
from django.contrib.auth.models import User
from login.models import Student

class ChatConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connected ',event)
        room_number=str(self.scope['path']).split('/')[3]
        self.room_number=room_number
        await  self.send({
            "type":"websocket.accept"
        })
        user=str(self.scope['user'])
        self.user=user
        chat_room = "room"+room_number
        self.chat_room = chat_room

        await self.channel_layer.group_add(
            chat_room,
            self.channel_name
        )
        await self.active_user(user,room=self.room_number)
        photo_url= await self.get_photo_url(user)
        self.photo_url="/Media/"+photo_url
        data={
            "connected":True,
                "user":user,
            "url":self.photo_url
        }
        await self.channel_layer.group_send(
            self.chat_room,
            {
                "type": "chat_message",
                "text": json.dumps(data),

            }

        )


    async def websocket_receive(self,event):
        print('receive ',event)
        front_text=event.get('text',None)
        await self.save_message(front_text,self.user,self.room_number)
        if front_text is not None:
            data={
                "message":front_text,
                "username":str(self.scope['user']),
                "datetime":get_datetime(),
                "url":self.photo_url
            }


            await self.channel_layer.group_send(
                self.chat_room,
                {
                    "type":"chat_message",
                    "text":json.dumps(data),


                }

             )

    async def chat_message(self,event):
        print('message:',event)
        await self.send({
            'type':"websocket.send",
            'text':event['text'],
        })

    async def websocket_disconnect(self,event):
        await self.dective_user(self.user)
        print('disconnected ',event)

        # send group message that user disconnected
        data = {
            "disconnected" :True,
                "user":str(self.scope['user'])
        }
        await self.channel_layer.group_send(
            self.chat_room,
            {
                "type": "chat_message",
                "text": json.dumps(data),

            }

        )


    @database_sync_to_async
    def active_user(self, user,room):
        user_data = Activeuser.objects.get(name=user)
        student=Student.objects.get(id=user_data.id)
        room_obj = Chat_room.objects.get(id=room)
        if not user_data:
            user = Activeuser(name=user, connected=True,room=room,student=student)
            user.save()
        else:
            user_data.connected=True
            user_data.room=room_obj
            user_data.save()

    @database_sync_to_async
    def dective_user(self, user,):
        user = Activeuser.objects.get(name=user)
        user.connected=False
        user.save()



    @database_sync_to_async
    def save_message(self, message,user,room):
        user_data = User.objects.get(username=user)
        room_obj=Chat_room.objects.get(id=room)
        student = Student.objects.get(id=user_data.id)
        chat = Chat_message(message=message,user=user_data,room=room_obj,student=student)
        chat.save()
        print("message saved")

    @database_sync_to_async
    def get_photo_url(self,user):
        user_data = User.objects.get(username=user)
        student = Student.objects.get(id=user_data.id)
        return str(student.photo)



