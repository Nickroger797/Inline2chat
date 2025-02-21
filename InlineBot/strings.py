# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

from pyrogram import __version__
from InlineBot import (
    OWNER_ID,
    FILTER_COMMAND,
    DELETE_COMMAND,
    CUSTOM_START_MESSAGE
)

if CUSTOM_START_MESSAGE:
    START_MESSAGE = CUSTOM_START_MESSAGE
else:
    START_MESSAGE = """<b>🍾 Hey {mention},

🫧 I am an Inline Saver Bot.\n\n🧧 you can save inline filters and It can be use in any of your chats easily.\n\n🧊 Click help for more details</b> 
"""

HELP_MESSAGE = f"""<b><u>🍃 Available Commands 🍃</u></b>

🌊 <b>/{FILTER_COMMAND.lower()}</b> <i>[keyword] [message or reply to message]</i>
    <i>Add an Inline filter, you can use MarkDown for formatting</i>
    
🪄 <b>/{DELETE_COMMAND.lower()}</b> <i>[keyword]</i>
    <i>Delete existing Filter</i>
    
👻 <b>/filters</b>
    <i>To see the filters</i>
    
💀 <b>/export</b>
    <i>Export a Backup file of filters, this can be import by others</i>
    
👀 <b>/stats</b>
    <i>See the Bot's Statistics</i>
    
❄️ <b>/broadcast</b> <i>[reply to any message]</i>
    <i>Broadcast any Messages to Bot users</i>
    
<b><u>🍁 This Commands not for you 🍁</u></b>

💦 <b>/delall</b>
    <i>Delete all of the filters</i>
    
🥢 <b>/import</b> <i>[reply to an exported file]</i>
    <i>Import filters from Backup file</i>
"""

ABOUT_MESSAGE = f"""<b><u>🤭 ABOUT ME 🤭</u></b>

<b>○ Maintained by : <a href='tg://user?id={OWNER_ID}'>This Person</a>
🧨Updates Channel : <a href='https://t.me/codexbotmaker'>Codexownerr</a>
👻Support Group : <a href='https://t.me/codexdisscus'>Codex Bot Support</a>
🤡 Source Code : <a href='https://t.me/codexdisscus'>Nhii hai bhai</a>
👀 Language : <a href='https://www.python.org/'>Python 3</a>
🩸 Library : <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio {__version__}</a></b>
"""

MARKDOWN_HELP = """<b><u>💫 Markdown Formatting 💫</u></b>

💀 <b>Bold Words</b> :
    format: <code>*Bold Text*</code>
    show as: <b>Bold Text</b>
    
🍃 <b>Italic Text</b>
    format: <code>_Italic Text_</code>
    show as: <i>Italic Text</i>
    
💦 <b>Code Words</b>
    format: <code>`Code Text`</code>
    show as: <code>Code Text</code>
    
🤫 <b>Under Line</b>
    format: <code>__UnderLine Text__</code>
    show as: <u>UnderLine Text</u>
    
🏮 <b>StrikeThrough</b>
    format: <code>~StrikeThrough Text~</code>
    show as: <s>StrikeThrough Text</s>
    
🌊 <b>Hyper Link</b>
    format: <code>[Text](https://t.me/codexbotmaker)</code>
    show as: <a href='https://t.me/codexbotmaker'>Text</a>
    
🍁 <b>Buttons</b>
    <u>Url Button</u>:
    <code>[Button Text](buttonurl:https://t.me/codexbotmaker)</code>
    <u>Alert Button</u>:
    <code>[Button Text](buttonalert:Alert Text)</code>
    <u>In Sameline</u>:
    <code>[Button Text](buttonurl:https://t.me/codexbotmaker:same)</code></i>

🪄 <b>Notes:</b>
    <i>Keep every Buttons in Seperate line when formating</i>
    <i>Your alert message text must be less than 200 characters, otherwise bot will ignore that button</i>

🧧 <b>Tip:</b> <i>You can add buttons for sticker and video note in /add command</i>"""
