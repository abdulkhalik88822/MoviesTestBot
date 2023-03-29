import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# --------- ʙᴏᴛ sᴇᴛᴛɪɴɢs ---------
BUTTON = True
USE_CAPTION_FILTER = True
BROADCAST_AS_COPY = True
BROADCAST_ADMIN_ID = [5709622852]


# --------- ᴍᴏɴɢᴏ ᴅʙ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ---------
DATABASE_URI = "mongodb+srv://TheHanCock:TheHanCock@cluster0.a3kyeiz.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Cluster0"
COLLECTION_NAME = 'HanCock_Files'


# --------- ʙᴏᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ---------
SESSION = 'Media_search'
API_ID = "18719789"
API_HASH = "a03c27be3e14aac40f62cb4e95207fae"
BOT_TOKEN = "5832308062:AAFoMhhBzIntupig2vQpl8oZ7MqGF3uUJwI"   #"6091738037:AAGiTZ854KaXTUg3ZxAAkSmmYj5b9Fdqwgw"


# --------- ᴀᴅᴍɪɴs ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴜsᴇʀs ---------
ADMINS = [5709622852, 5416887843, 5807975896]
CHANNELS = [-1001569112096]
auth_users = []
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
AUTH_CHANNEL = -1001831916389
AUTH_GROUPS = []


# --------- ʟɪɴᴋ sʜᴏʀᴛɴᴇʀ ᴄᴏɴᴠᴇʀᴛᴇʀ ---------
URL_SHORTNER_API = environ.get("URL_SHORTNER_API", "https://urlshortx.com/api?api")
URL_SHORTNER_API_KEY = environ.get("URL_SHORTNER_API_KEY", "9e057515d222131456b51729e54033ab4e1d6936")



# --------- ᴘɪᴄs ʟɪɴᴋs ---------
default_pics_links = """
https://te.legra.ph/file/a30df60e107e11363cb08.jpg
"""
PICS = (environ.get('PICS', default_pics_links)).split()


# --------- sᴛᴀʀᴛ ᴍᴇsᴀᴀɢᴇs ---------
default_start_msg = """
ʜᴇʟʟᴏ
ɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴍᴏᴠɪᴇs 
ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ 
ᴍᴀᴋᴇ ᴀᴅᴍɪɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs
"""
START_MSG = environ.get('START_MSG', default_start_msg)


# --------- ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ---------
default_file_caption = """
📁 {file_name}]
━━━━━━━━━━━━━━━━━━━━━━━━━━━
      ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴠɪᴅᴇᴏ

ɪғ ʏᴏᴜ ʟɪᴋᴇ ᴠɪᴅᴇᴏ ᴛʜᴀɴ ᴘʟᴇᴀsᴇ 
ᴀᴅᴅ sᴏᴍᴇ ᴍᴇᴍʙᴇʀ ᴀɴᴅ sʜᴀʀᴇ ᴛʜᴇ ʟɪɴᴋ
━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

FILE_CAPTION = environ.get('CUSTOM_CAPTION_FILE', default_file_caption)


OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
