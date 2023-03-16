from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .db_query import userdata
import json

# Web socket url : ws://127.0.0.1:8000/user/
# ws://127.0.0.1:8000/user/?id=ce8b61f4-5259-46ec-a697-20452b17a3bc   
# ===> user-id: ce8b61f4-5259-46ec-a697-20452b17a3bc  ==> ID needed for getting user detail in consumer.py

class ChatConsumer(AsyncWebsocketConsumer):
    
    
    async def connect(self):
        print("======",self.scope['query_string'])
        print("======",type(self.scope['query_string']))

        output = str(self.scope['query_string'], 'UTF-8').split("=")
        print("======",output[1])

        userobj = await userdata(output[1])
        print("-----",userobj.username)

        # self.planid = self.scope["url_route"]["kwargs"]
        # self.room_name = self.scope['user']
        # self.room_group_name = "chat_%s" % self.room_name

        # await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    
    

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))
 