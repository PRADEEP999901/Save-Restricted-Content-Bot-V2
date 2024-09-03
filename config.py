# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29754529"))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "-Hink")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://")
LOG_GROUP = getenv("LOG_GROUP", "-")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-"))
