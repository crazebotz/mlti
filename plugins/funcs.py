#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import Config
from pyrogram import filters
from pyrogram import Client
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from urllib.parse import quote_plus, unquote
import math, os, time, datetime, aiohttp, asyncio, mimetypes, logging
from helpers.download_from_url import download_file, get_size
from helpers.file_handler import send_to_transfersh_async, progress
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from helpers.display_progress import progress_for_pyrogram, humanbytes
from helpers.tools import execute
from helpers.ffprobe import stream_creator
from helpers.thumbnail_video import thumb_creator
from helpers.url_uploader import leecher2
from helpers.video_renamer import rnv2
from helpers.audio_renamer import rna2
from helpers.file_renamer import rnf2
from helpers.vconverter import to_video2
from helpers.media_info import cinfo2
from helpers.link_info import linfo2

logger = logging.getLogger(__name__)

HELP_TXT = """
🎭Welcome Dear.... I am Multi Usage BOT [Powered By @Dasuwaprofa✨] 

♻️My BOT Supporting...🔰

🔶4Gb files Direct Upload (Premium Users Only❤️)
🔶Multi Tasking Features (At One Time🔂)
🔶ANy Video Download,Upload,Stream,Encode,Compress...ETC🚀
🔶ANy Audio Download,Upload,Convert,Merged...ETC🚀
🔶No Time Gaps,No Flood Waiting,No Restrictions🔥

🔔IMPORTANT NOTICE🔔
🟥Your must Pay 5$ Monthly to Use This Bot Because I stopped my free Service🐕‍🦺
"""

@Client.on_message(filters.command(["start"]))
async def start(client , m):
    """Send a message when the command /start is issued."""
    await m.reply_text(text=f"Hi Dear✨ I am Multi Usage BOT🗃️\n\n♻️See /help for ℹ️More Information...Powered By @Dasuking🔥")

    
@Client.on_message(filters.command(["help"]))
async def help(client , m):
    """Send a message when the command /help is issued."""
    await m.reply_text(text=f"{HELP_TXT}")   

@Client.on_message(filters.private & filters.command(["rnv"]))
async def rnv1(client , u):

    if u.from_user.id in Config.AUTH_USERS:
        await rnv2(client , u)
    elif not Config.AUTH_USERS:
        await rnv2(client , u)
    else:
        await u.reply_text(text=f"Hey Ponsi🤬 You cant use Me...ℹ️Because You Are Not Paid User⛔\n\n🤖To Use Me:\n[♻️PAY_HERE♻️](https://t.me/Dasuwaprofa)", quote=True, disable_web_page_preview=True)
        return
    
@Client.on_message(filters.private & filters.command(["rna"]))
async def rna1(client , u):

    if u.from_user.id in Config.AUTH_USERS:
        await rna2(client , u)
    elif not Config.AUTH_USERS:
        await rna2(client , u)
    else:
        await u.reply_text(text=f"Hey Ponsi🤬 You cant use Me...ℹ️Because You Are Not Paid User⛔\n\n🤖To Use Me:\n[♻️PAY_HERE♻️](https://t.me/Dasuwaprofa)", quote=True, disable_web_page_preview=True)
        return

@Client.on_message(filters.private & filters.command(["rnf"]))
async def rnf1(client , u):

    if u.from_user.id in Config.AUTH_USERS:
        await rnf2(client , u) 
    elif not Config.AUTH_USERS:
        await rnf2(client , u)
    else:
        await u.reply_text(text=f"Hey Ponsi🤬 You cant use Me...ℹ️Because You Are Not Paid User⛔\n\n🤖To Use Me:\n[♻️PAY_HERE♻️](https://t.me/Dasuwaprofa)", quote=True, disable_web_page_preview=True)
        return
   
@Client.on_message(filters.private & filters.command(["c2v"]))
async def to_video1(client , u):

    if u.from_user.id in Config.AUTH_USERS:
        await to_video2(client , u) 
    elif not Config.AUTH_USERS:
        await to_video2(client , u) 
    else:
        await u.reply_text(text=f"Hey Ponsi🤬 You cant use Me...ℹ️Because You Are Not Paid User⛔\n\n🤖To Use Me:\n[♻️PAY_HERE♻️](https://t.me/Dasuwaprofa)", quote=True, disable_web_page_preview=True)
        return
    
@Client.on_message(filters.private & (filters.audio | filters.document | filters.video))
async def cinfo1(client , m):
    await cinfo2(client , m)


@Client.on_message(filters.private & filters.incoming & filters.text & (filters.regex('^(ht|f)tp*')))
async def linfo1(client , m):
    await linfo2(client , m)

@Client.on_message(filters.private & filters.command(["upload"]))
async def leecher1(client , u):

    if u.from_user.id in Config.AUTH_USERS:
        await leecher2(client , u)
    elif not Config.AUTH_USERS:
        await leecher2(client , u)
    else:
        await u.reply_text(text=f"Hey Ponsi🤬 You cant use Me...ℹ️Because You Are Not Paid User⛔\n\n🤖To Use Me:\n[♻️PAY_HERE♻️](https://t.me/Dasuwaprofa)", quote=True, disable_web_page_preview=True)
        return
