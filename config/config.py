# Just copy this file to config.py and change it to your info.
from pyrogram import filters

# Get these two from https://my.telegram.org
API_ID = 1383845
API_HASH = "0e3d2c299cc3c5cc26c283cecd2eb97c"

# Get this from @Botfather
TOKEN = "1673411552:AAFLmadz0_ESKkoYM_O_kEiRydpK7Ov_d48"

# Your MongoDB URI (using a database named "vcpb"), if you don't provide, you can't use the playlist feature and wont see now playing message
MONGO_DB_URI = "mongodb://root:dkkaj0123@mongodb/admin?replicaSet=rs0"

# The IDs of the users which can stream, skip, pause and change volume
SUDO_USERS = [
    1131653685
]

# The ID of the group where your bot streams
GROUP = -1001269473865

# Users must join the group before using the bot (note: the bot should be admin in the group if you enable this)
USERS_MUST_JOIN = False

# Choose the preferred language for your bot. If English leave as it is, or change to the code of any supported language.
LANG = "en"

# Max video duration allowed for user downloads in minutes
DUR_LIMIT = 5

# No need to touch the following.
LOG_GROUP = GROUP if MONGO_DB_URI != "" else None
SUDO_FILTER = filters.user(SUDO_USERS)
