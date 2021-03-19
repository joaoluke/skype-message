import data
import mensage
from skpy import Skype

sk = Skype(data.USERNAME, data.PASSWORD)


def post_message_group(msg, channel_id):
    """Post a message for group"""
    group_message = sk.chats.chat(channel_id)
    group_message.sendMsg(msg)


post_message_group(mensage.msg, data.CHANNEL_ID)
