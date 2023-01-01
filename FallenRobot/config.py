class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "22438767"
    API_HASH = "97801e073ba92ad0e2f83802403ba4dc"

    CASH_API_KEY = "7ANHDWS7S6KBEZTA"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://dvgqfjfq:E5GacLXkNx-e-uzHqUHMtYruBRfBUUII@snuffleupagus.db.elephantsql.com/dvgqfjfq"  # A sql database url from elephantsql.com

    EVENT_LOGS = "-1001795364397"  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://PlayBeat:xmanagment@cluster0.jkzbqni.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/7afa306cb3df3757bc001.jpg"

    SUPPORT_CHAT = "timepassxdman"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5953213913:AAG6UKNo4fZi28VYx0hTVMn9bRtJkVGxdXM"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "YYPZG1TYRE2R"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5888071928"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [5222353449]  # User id of sudo users
    DEV_USERS = [5222353449]  # User id of dev users
    DEMONS = [5222353449]  # User id of support users
    TIGERS = [5222353449]  # User id of tiger users
    WOLVES = [5222353449]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
