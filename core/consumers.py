from channels.generic.websocket import AsyncWebsocketConsumer
import json


class MyConsumer(AsyncWebsocketConsumer) :

    async def connect(self):
        print("connected to websocket successfully")
        return await super().connect()
    
    async def disconnect(self, code):
        print("disconnected")
        return await super().disconnect(code)