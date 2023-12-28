import os

class Chat:
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.separated_messages = self.init_next_message()

    def get_chat_name(self):
        return self.name

    def set_chat_name(self, name):
        self.name = name
        return self.name

    def init_next_message(self):
        with open(self.path, 'r') as file:
            for message in file.read().strip().splitlines():
                yield message

    def get_next_message(self):
        return next(self.separated_messages)
    
    def reinit(self):
        self.separated_messages = self.init_next_message()


class ChatManager:
    def __init__(self, current_chat, chats_path):
        self.current_chat = current_chat
        self.chats_path = chats_path
        self.chats = self.create_existing_chats(chats_path)
    
    def get_current_chat_name(self):
        return self.current_chat
    
    def set_current_chat_name(self, name):
        self.current_chat = name
        self.chats[self.current_chat].reinit()

    def get_current_chat_separated(self):
        return self.chats[self.current_chat].get_next_message()
    
    def append_current_chat(self, message):
        # Assuming you want to append a message to the current chat
        self.chats[self.current_chat].messages.append(message)

    @staticmethod
    def create_existing_chats(chats_path):
        chats = {}

        for file_name in os.listdir(chats_path):
            file_path = os.path.join(chats_path, file_name)
            chats[file_name] = Chat(file_name, file_path)

        return chats
