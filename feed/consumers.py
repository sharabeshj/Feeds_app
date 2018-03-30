from channels.generic.websocket import AsyncWebsocketConsumer
import json

class FeedConsumer(AsyncWebsocketConsumer):
	async def connect(self):
		self.user = self.scope["user"]
		if self.user.is_active:
			await self.channel_layer.group_add("users",self.channel_name)
			await self.accept()
		else:
			await self.close()

	async def disconnect(self,close_code):
		await self.channel_layer.group_discard("users",self.channel_name)

	async def receive(self,text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json['message']
		user = text_data_json['user']
		activity_type = text_data_json['activity_type']
		await self.channel_layer.group_send("users",{
			'type' : 'feed_message',
			'text' : json.dumps({
				'user' : user,
				'message' : message,
				'activity_type' : activity_type
			})
		})

	async def feed_message(self,event):
		text = event['text']
		await self.send(text_data = text)