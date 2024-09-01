# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29754529"))
API_HASH = getenv("API_HASH", "dd54732e78650479ac4fb0e173fe4759")
BOT_TOKEN = getenv("BOT_TOKEN", "7309382995:AAEVjtHpLEae6m3YzcwYargErXkOgu-Hink")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://telegram-bot:ydk4Nf7BxRREklv9@test.1r1ni.mongodb.net/?retryWrites=true&w=majority&appName=test")
LOG_GROUP = getenv("LOG_GROUP", "-1002208385419")
CHANNEL_ID = int(getenv("CHANNEL_ID", "neetumamvoca"))
