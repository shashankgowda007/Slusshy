from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        # Process the received data
        # You can send a response back to the client using self.send(text_data)
        pass
