# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv
from os import environ

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")

API = environ.get("API", "") # shortlink api
URL = environ.get("URL", "") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "") # bot username without @
VERIFY = environ.get("VERIFY", "True") # set True Or False and make sure spelling is correct and first letter capital.
