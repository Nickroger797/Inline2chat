# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

import re
import os
import uuid
from typing import List
from telegraph import upload_file
from pyrogram.types import InlineKeyboardButton
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)
logger.info("Generating button...")
try:
    pass
except Exception as t_e:
    logger.error(f"Error in upload_photo: {t_e}")

BTN_URL_REGEX = r"\[(.+?)\](?:\((buttonurl|buttonalert):(.+?)\))?"

SMART_OPEN = '“'
SMART_CLOSE = '”'
START_CHAR = ('\'', '"', SMART_OPEN)

def split_quotes(text: str) -> List:
    text = text.strip()  # Ensure no leading/trailing spaces
    if any(text.startswith(char) for char in START_CHAR):
        counter = 1
        while counter < len(text):
            if text[counter] == "\\":
                counter += 1
            elif text[counter] == text[0] or (text[0] == SMART_OPEN and text[counter] == SMART_CLOSE):
                break
            counter += 1
        else:
            return text.split(None, 1)

        key = remove_escapes(text[1:counter].strip())
        rest = text[counter + 1:].strip()
        return list(filter(None, [key, rest]))
    return text.split(None, 1)
        
def replace_href(text):
    regex = r"(.*)\[(.*)\]\((.*)\)(.*)"
    matches = re.search(regex, text, re.DOTALL)
    if matches:
        text = re.sub(regex,r"\1<a href='\3'>\2</a>\4",text)
        text = replace_href(text)
    return text
        
import html

def remove_md(text: str) -> str:
    markdown_map = {
        r'\b__([^_]+)__\b': ('<u>', '</u>'),
        r'\b\*\*([^*]+)\*\*\b': ('<b>', '</b>'),
        r'\b`([^`]+)`\b': ('<code>', '</code>'),
        r'\b_([^_]+)_\b': ('<i>', '</i>'),
        r'\b~([^~]+)~\b': ('<s>', '</s>'),
    }

    for md, html_tags in markdown_map.items():
        text = re.sub(md, rf"{html_tags[0]}\1{html_tags[1]}", text)

    return replace_href(html.escape(text.strip()))

def generate_button(text: str, id: str):
    logging.info(f"generate_button received: text='{text}', id='{id}'")

    if not text:
        logging.error("generate_button failed: text is empty!")
        return None

    text = text.strip()  # Remove unnecessary spaces
    btns = []
    datalist = []
    matches = list(re.finditer(BTN_URL_REGEX, text, re.MULTILINE))

    logging.info(f"Regex matches found: {matches}")

    if not matches:
        logging.error("generate_button failed: No button matches found!")
        print("⚠️ No buttons found! Use the format: [Text](buttonurl:URL) or [Text](buttonalert:Alert Message)")
        return None

    clean_text = re.sub(BTN_URL_REGEX, "", text, re.MULTILINE).strip()

    if not clean_text:
        logging.warning(f"clean_text is empty! Using original text: '{text}'")
        clean_text = text

    logging.info(f"generate_button returning: clean_text='{clean_text}', btns={btns}, datalist={datalist}")

    return remove_md(clean_text), btns, datalist
   
    j = 0
    for match in matches:
        button_text = match.group(1).strip()
        button_text = re.sub(r"<b>|</b>|<code>|</code>|<u>|</u>|<i>|</i>", "", button_text)

        btn_type, btn_data = match.group(2), match.group(3).strip()

        if btn_type == "buttonurl":
            btns.append([InlineKeyboardButton(text=button_text, url=btn_data)])
        elif btn_type == "buttonalert" and len(btn_data) < 200:
            datalist.append(btn_data)
            btns.append([InlineKeyboardButton(text=button_text, callback_data=f"alertmessage:{j}:{id}")])
            j += 1

    clean_text = re.sub(BTN_URL_REGEX, "", text, re.MULTILINE).strip()
    
    logging.info(f"generate_button returning: clean_text='{clean_text}', btns={btns}, datalist={datalist}")
    
    return remove_md(clean_text), btns, datalist

def remove_escapes(text: str) -> str:
    counter = 0
    res = ""
    is_escaped = False
    while counter < len(text):
        if is_escaped:
            res += text[counter]
            is_escaped = False
        elif text[counter] == "\\":
            is_escaped = True
        else:
            res += text[counter]
        counter += 1
    return res

async def upload_photo(message):
    msg = await message.reply_text("<code>Please wait..</code>")
    _T_LIMIT = 5242880  # 5MB limit
    if not (message.photo and message.photo.file_size <= _T_LIMIT):
        await msg.edit("<i>Sorry, this photo is too large or unsupported.</i>")
        return False

    dl_loc = await message.download()
    try:
        response = upload_file(dl_loc)
        link = f'https://telegra.ph{response[0]}'
        await msg.delete()
        logger.info(f"Photo uploaded successfully: {link}")
    except Exception as t_e:
        logger.error(f"Upload failed: {t_e}")
        await msg.edit_text(f"<i>Upload failed: {t_e}</i>")
        link = False
    finally:
        if os.path.exists(dl_loc):
            os.remove(dl_loc)
    
    return link

def make_dict(data_list: List[dict], keywords: List[str]):
    dict_list = []
    for item in data_list:
        if item.get('text') in keywords:
            continue

        new_id = str(uuid.uuid4())
        old_id = item.get('_id')

        new_data = {
            '_id': new_id,
            'text': item.get('text', ''),
            'reply': item.get('reply', ''),
            'file': item.get('file', ''),
            'alert': item.get('alert', ''),
            'type': item.get('type', ''),
            'btn': item.get('btn', '').replace(old_id, new_id)  # Fix possible KeyError
        }
        
        dict_list.append(new_data)

    return dict_list
    
