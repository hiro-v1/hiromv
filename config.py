import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "25802693"))
API_HASH = getenv("API_HASH", "803393e9f1b6ea523853ce2126208c17")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "8188904216:AAEz1PZGamqtR06gmQlC_Sg7Bx6dTVzLgs4")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME", "hiro_v1")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME", "hiroMV1_bot")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME", "hiro musik vidio okef")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME", "molesinika")
EVALOP = list(map(int, getenv("EVALOP", "1282758415").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://kensay:Kentos123$@cluster0.gm457.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10000"))

# Duration Limit for downloading Songs in MP3 or MP4 format from bot
SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "18000")
)  # Remember to give value in Minutes

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002450685314"))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5634309575"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/hiro-v1/hiromv",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MLBBShopHiro")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+scN8hOJlLn0yOWY9")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Time after which you're assistant account will leave chats automatically.
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400000")
)  # Remember to give value in Seconds


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "250"))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Ge@STRINGSEASO_NBOT2 session from @STRINGSEASO_NBOT
STRING1 = getenv("STRING_SESSION", "BQDNvmIAlqpQ3dLIHa2qWB1d75X8LaNeTZlkoKAGodFU01FoGT6CyToPtO6BxQknWT59Y20owyTUIwbLz71890w6MV_BKoQI997GW_cKItPukCzy7AcR6yvTf9DcSVg6oXCtPfEo7MpBskvWcJuoCfuczXXXxN1GuLIlvTzDyYJHGy3H5YZcBuIaVTWGlQm1MGY7u4GOPrV0ek6Ah0L6SQkBk3ol06gz-KXB9jh5P3Hh_xozkfYhImzYIMpbb3IDIGIGB1BBcZmDwxcJgDpuOn48aQFT9ztOtvpEPNVjcZzyvz5SZpNAuFxiF5eX39jnqy6Z_JiajJzR_2HW75N3tSUwaORmJAAAAAFP1L3HAA")
STRING2 = getenv("STRING_SESSION2", "BQGJt8UASnSl0-EA4GnwGJjH_5CDEvqngpMi6LpLUDrcKeeqMSSXlCy0XeUy9Uy7Rz5eV8rPoLU0l4TArOApOawnasMxo39d7MSShoM6R-RRKXA93Dsz9TwIJGgIfpkqWJuYhrbUbr7gATrr7B4M-c9Co8knQiaxVbPoyUhO5X8P5qIonkgDtwhAjajRBivgXtlWqLedyDKT4i2VljiyP3wfZV6zlgkb5Iozg3ZlWT7RcvGTHC7vwqphg_GtqZV8KRAjZISEvINjTOmHjytETFxSm-JyPv3nt69ij8CJiib5KjRmsKUsZeo30YuUa7_13fQ2CQAlNJIU4BwywrvPLfaCPZOrMgAAAAFP1L3HAA")
STRING3 = getenv("STRING_SESSION3", "1BVtsOJYBu3QPdqKzWyzZzvFo7GlxBSW0PrtTeEoRkQ3oOvWVh1AGTAuZfwOfYDHJbSpoe_CsKFS0jzonTD_950vJbkQQOmlQlQXXv7J5G8rXY9GLwlt5S9BhkbVcIZtphDNi-v3WnUneWYzr9MvEqVJNwIMsUvah-1XxRDWx5ZQMwDcC6UIF9HCYAL_ocAUfcp71sZHKtvJx7KXt4a5GMfIQ7DMvfYpQpQWKt75qMnWih-dQrewyXb7Mg127FVLmX6wQu-WGQzeqN7Fq4nYGrOh0_RsYrt6BlhKiBt0v8l6LzZnAhl8IrrwOQuZrcqKKeAZ5Muatdn8gmCJ1LQNmmA_VreTAeKc=")
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/dec61e858d57c14343455.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/7795e58425337d0455e95.jpg"
STATS_IMG_URL = "https://graph.org/file/136c57e473c33a0c62152.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/982b01ba53c3d69b0d0ce.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/d2081243af7c1d7578b7b.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/61024698bfc926e95d57a.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
