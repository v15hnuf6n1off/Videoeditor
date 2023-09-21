#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 vasusen-code ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/vasusen-code/VIDEOconvertor/blob/public/LICENSE> .

import os
from .. import Drone
from telethon import events, Button
from LOCAL.localisation import START_TEXT as st
from LOCAL.localisation import JPG0 as file
from LOCAL.localisation import info_text, spam_notice, help_text, DEV, source_text, SUPPORT_LINK
from ethon.teleutils import mention
from ethon.mystarts import vc_menu

@Drone.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply(f'{st}', 
                      buttons=[
                              [Button.inline("𝙼𝚎𝚗𝚞", data="menu")]
                              ])
    
@Drone.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(event):
    await vc_menu(event)
    
@Drone.on(events.callbackquery.CallbackQuery(data="info"))
async def info(event):
    await event.edit(f'**𝙸𝚗𝚏𝚘:**\n\n{info_text}',
                    buttons=[[
                         Button.inline("𝙼𝚎𝚗𝚞", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="notice"))
async def notice(event):
    await event.answer(f'{spam_notice}', alert=True)
    
@Drone.on(events.callbackquery.CallbackQuery(data="source"))
async def source(event):
    await event.edit(source_text,
                    buttons=[[
                         Button.url(" 𝙲𝚘𝚗𝚝𝚊𝚌𝚝 𝙳𝚎𝚟", url="https://t.me/v15hnuf6n1x")]])
                    
@Drone.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit('**𝚂𝚎𝚝𝚝𝚒𝚗𝚐𝚜 ⚙️**',
                    buttons=[[
                         Button.inline("𝚂𝚎𝚝 𝚃𝚑𝚞𝚖𝚋 🖼️", data="sett"),
                         Button.inline("𝚁𝚎𝚖𝚘𝚟𝚎 𝚃𝚑𝚞𝚖𝚋 🖼️", data='remt')],
                         [
                         Button.inline("𝙵𝚎𝚊𝚝𝚞𝚛𝚎𝚜 💡", data="plugins"),
                         Button.url("𝚂𝚞𝚙𝚙𝚘𝚛𝚝 🗳️", url=f"{SUPPORT_LINK}")],
                         [
                         Button.inline("𝙱𝚊𝚌𝚔", data="menu")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="plugins"))
async def plugins(event):
    await event.edit(f'{help_text}',
                    buttons=[[
                         Button.inline("𝙼𝚎𝚗𝚞 🗂️", data="help")]])
    
@Drone.on(events.callbackquery.CallbackQuery(data="sett"))
async def sett(event):    
    button = await event.get_message()
    msg = await button.get_reply_message() 
    await event.delete()
    async with Drone.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("𝚂𝚎𝚗𝚍 𝙼𝚎 𝙰𝚗𝚢 𝙸𝚖𝚊𝚐𝚎 𝙵𝚘𝚛 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚊𝚜 𝚊 `𝚛𝚎𝚙𝚕𝚢` 𝚝𝚘 𝚝𝚑𝚒𝚜 𝙼𝚎𝚜𝚜𝚊𝚐𝚎.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("𝙽𝚘 𝙼𝚎𝚍𝚒𝚊 𝙵𝚘𝚞𝚗𝚍❗")
        mime = x.file.mime_type
        if not 'png' in mime:
            if not 'jpg' in mime:
                if not 'jpeg' in mime:
                    return await xx.edit("𝙽𝚘 𝙸𝚖𝚊𝚐𝚎 𝙵𝚘𝚞𝚗𝚍 ❗ ")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("𝚃𝚎𝚖𝚙𝚛𝚘𝚊𝚛𝚒𝚕𝚢 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚒𝚜 𝚂𝚊𝚟𝚎𝚍 ✅")
        
@Drone.on(events.callbackquery.CallbackQuery(data="remt"))
async def remt(event):  
    await event.edit('𝚃𝚛𝚢𝚒𝚗𝚐 𝚃𝚘 𝚂𝚊𝚟𝚎')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('𝚂𝚞𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢 𝚁𝚎𝚖𝚘𝚟𝚎𝚍')
    except Exception:
        await event.edit("𝙽𝚘 𝚃𝚑𝚞𝚖𝚋𝚗𝚊𝚒𝚕 𝚒𝚜 𝚏𝚘𝚞𝚗𝚍")
    
