from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

consumer_object_list = []


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        print('Запросить ссылку')
        self.accept()
        consumer_object_list.append(self)

    def websocket_receive(self, message):
        print(message)
        text = message.get('text')

        for obj in consumer_object_list:
            obj.send(text_data=text)

    def websocket_disconnect(self, message):
        print('Неработающей ссылке')
        consumer_object_list.remove(self)
        raise StopConsumer()
