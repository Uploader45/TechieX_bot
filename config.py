import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5389849727:AAHUcsA7UtQddWj_vQat_jnsdZfv5dJ-tso")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", "15668875"))
    API_HASH = os.environ.get("API_HASH", "9126d3e935a1553bedf9bd822f3b4ad9")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 500000000
    TG_MAX_FILE_SIZE = 1800000000
    FREE_USER_MAX_FILE_SIZE = 500000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "579974245"))
    SESSION_NAME = "KNIGHT-RANGER-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "")
    MAX_RESULTS = "50"
