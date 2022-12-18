import os

class Config:
    API_ID = int( os.getenv("api_id","14672956") )
    API_HASH = os.getenv("api_hash","115e8242ea0423893160bb61a9e05eab")
    CHANNEL = int( os.getenv("channel_files_chat_id","-1001866017806") )
    CHANNEL_USERNAME = os.getenv("channel_username","kblois")
    TOKEN = os.getenv("token","5821948686:AAEsgkTwB6FvyTQfj-fMfA7etHM_AM_7U7w")
    DOMAIN  = os.getenv("domain","https://stream-cloud-production-cbb4.up.railway.app")
