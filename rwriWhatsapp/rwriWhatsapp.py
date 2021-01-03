
import pandas as pd
from whatsapp_chat_parser import get_messages


class WhatsAppParser:

    @staticmethod
    def run():
        messages = get_messages("../data/_chat.txt")
        for message in messages["chats"]:
            print(message["author"])
            print(message["message"])
            print(message["timestamp"])

        for descriptive_message in messages["descriptive_messages"]:
            print(descriptive_message)

        df = pd.DataFrame(messages['chats'])
        print(df.head())

