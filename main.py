from config import config
from telethon.sync import TelegramClient

api_id: int = config.API_ID
api_hash: str = config.API_HASH
channel_username = '@bbcrussian'

with TelegramClient('session_name', api_id, api_hash) as client:
    for message in client.iter_messages(channel_username, limit=10):
        print(f"{message.date} - {message.sender_id}: {message.text}")
