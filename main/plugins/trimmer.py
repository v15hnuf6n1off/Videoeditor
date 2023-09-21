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

import time, os

from datetime import datetime as dt
from telethon import events
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo
from ethon.telefunc import fast_download, fast_upload
from ethon.pyfunc import video_metadata, bash
from ethon.pyutils import rename

from .. import Drone, BOT_UN

from LOCAL.localisation import SUPPORT_LINK, JPG, JPG2, JPG3

async def trim(event, msg, st, et):
    Drone = event.client
    edit = await Drone.send_message(event.chat_id, "𝚃𝚛𝚢𝚒𝚗𝚐 𝚃𝚘 𝙿𝚛𝚘𝚌𝚎𝚜𝚜", reply_to=msg.id)
    new_name = "out_" + dt.now().isoformat("_", "seconds")
    if hasattr(msg.media, "document"):
        file = msg.media.document
    else:
        file = msg.media
    mime = msg.file.mime_type
    if 'mp4' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + ".mp4"
    elif msg.video:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mp4"
        out = new_name + ".mp4"
    elif 'x-matroska' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".mkv" 
        out = new_name + ".mkv"       
    elif 'webm' in mime:
        name = "media_" + dt.now().isoformat("_", "seconds") + ".webm" 
        out = new_name + ".webm"
    else:
        name = msg.file.name
        ext = (name.split("."))[1]
        out = new_name + ext
    DT = time.time()
    try:
        await fast_download(name, file, Drone, edit, DT, "**𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐**")
    except Exception as e:
        print(e)
        return await edit.edit(f"𝚂𝚘𝚛𝚛𝚢 𝙰𝚗 𝚎𝚛𝚛𝚘𝚛 𝚘𝚌𝚌𝚞𝚛𝚎𝚍 𝚠𝚑𝚒𝚕𝚎 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐.\n\n𝙲𝚘𝚗𝚝𝚊𝚌𝚝 [SUPPORT]({SUPPORT_LINK})", link_preview=False) 
    try:
        await edit.edit("𝚃𝚛𝚒𝚖𝚖𝚒𝚗𝚐")
        bash(f'ffmpeg -i {name} -ss {st} -to {et} -acodec copy -vcodec copy {out}')
        out2 = new_name + '_2_' + '.mp4'
        rename(out, out2)
    except Exception as e:
        print(e)
        return await edit.edit(f"𝚂𝚘𝚛𝚛𝚢 𝙰𝚗 𝚎𝚛𝚛𝚘𝚛 𝚘𝚌𝚌𝚞𝚛𝚎𝚍 𝚠𝚑𝚒𝚕𝚎 𝚃𝚛𝚒𝚖𝚖𝚒𝚗𝚐..\n\n𝙲𝚘𝚗𝚝𝚊𝚌𝚝 [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    UT = time.time()
    text = f"**𝚃𝚛𝚒𝚖𝚖𝚎𝚍 𝙱𝚢** @{BOT_UN}"
    try:
        metadata = video_metadata(out2)
        width = metadata["width"]
        height = metadata["height"]
        duration = metadata["duration"]
        attributes = [DocumentAttributeVideo(duration=duration, w=width, h=height, supports_streaming=True)]
        uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 **')
        await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG3, attributes=attributes, force_document=False)
    except Exception:
        try:
            uploader = await fast_upload(f'{out2}', f'{out2}', UT, Drone, edit, '**𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐**')
            await Drone.send_file(event.chat_id, uploader, caption=text, thumb=JPG, force_document=True)
        except Exception as e:
            print(e)
            return await edit.edit(f"𝚂𝚘𝚛𝚛𝚢 𝙰𝚗 𝚎𝚛𝚛𝚘𝚛 𝚘𝚌𝚌𝚞𝚛𝚎𝚍 𝚠𝚑𝚒𝚕𝚎 𝚄𝚙𝚕𝚙𝚊𝚍𝚒𝚗𝚐..\n\n𝙲𝚘𝚗𝚝𝚊𝚌𝚝 [SUPPORT]({SUPPORT_LINK})", link_preview=False)
    await edit.delete()
    os.remove(name)
    os.remove(out2)
      
      
      
      
