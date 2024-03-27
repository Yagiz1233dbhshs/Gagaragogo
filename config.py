import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "23471546"))
API_HASH = getenv("API_HASH", "23910ff5097ae15c3fdb6c7cd70e1a29")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7039071910:AAFHC34AltonvmhirMxg3T4LNeneRZy7cdI")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://yunusgmd1:cenap213344@cluster0.srupnsy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 5400))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002020615231"))

# Get this value from @Hot_Girl_Robot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6786458787"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Ferid18/Venoms",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EfsunkarBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Efsunkarr")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", False)
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))
# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))
# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @Venom_string_robot on Telegram
STRING1 = getenv("STRING_SESSION", "AgE7aHwAdQ3D6JtDLnTaNnqx0-nxtlvjZ6t_8MtkX1oJ8hZQ6ttEnHpUSNo0dQJDFHT-OQXDOx09hMOm9X9-_mKbGjbmyGQupz-xuGiTGNLDhsw5kwjVo1F-ivWavlPJq3T4e-VIgyt7y_weDFFPgCOM_mOCvLAQdlTGjeAy-MvDBUhxyjQtaU6ueietrqV34Cd260Vd_YPMqd7o-MKZk5Dbwvf7-tLqqtCsL6vNi8j_wQhNs6fv32tjQ0Ayik93uu9vVJlrXI6PNthPkIT9wsrW6XoWDJWm0kFymGtiHsMl-8OI9ucizP3mJHJ63uHD5LQw0aVvUIfvUv8AU6UKrdz0gvZWpAAAAAFr3-D8AA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", None
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", None
)
PLAYLIST_IMG_URL = None
STATS_IMG_URL = None
TELEGRAM_AUDIO_URL = None
TELEGRAM_VIDEO_URL = None
STREAM_IMG_URL = None
SOUNCLOUD_IMG_URL = None
YOUTUBE_IMG_URL = None
SPOTIFY_ARTIST_IMG_URL = None
SPOTIFY_ALBUM_IMG_URL = None
SPOTIFY_PLAYLIST_IMG_URL = None


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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
