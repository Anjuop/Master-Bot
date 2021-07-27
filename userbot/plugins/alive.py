# COPYRIGHT (C) 2021 BY MASTERBOT22 AND PROBOYX, ALAIN

"""
(((((((((((((((((((((((@MASTERBOT22)))))))))))))))))))))))))))
(((((((((((((((((((((((@MASTERBOT22)))))))))))))))))))))))))))
(((((((((((((((((((((((@MASTERBOT22)))))))))))))))))))))))))))
(((((((((((((((((((((((@MASTERBOT22)))))))))))))))))))))))))))
                 MADE BY MASTERBOT AND PROBOY X
                   DISIGNED BY ALAIN_CHAMPION
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE THIS LINES
"""

from telethon import events, Button, custom
import re, os
from MASTERBOT import PHOTO, xbot, BOT, VERSION
from userbot import bot
@xbot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  MASTERBOT = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  MASTERBOT += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  MASTERBOT += f"{BOT} VERSION : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  MASTERBOT += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  MASTERBOT += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  MASTERBOT += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  MASTERBOT += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/MASTERBOTOP/LEGEND-BOT")]]
  BUTTON += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="MASTERBOT")]]
  await xbot.send_file(event.chat_id, PHOTO, caption=MASTERBOT,  buttons=BUTTON)




@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"MASTERBOT")))
async def callback_query_handler(event):
# inline by MASTERBOT22 and PROBOY22 🔥
  PROBOYX = [[Button.url("REPO-LEGEND", "https://github.com/MASTERBOTOP/LEGEND-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGEND", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMASTERBOTOP%2Flegendpack&template=https%3A%2F%2Fgithub.com%2FMASTERBOTOP%2Flegendpack")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=PROBOYX)


@xbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
# inline by MASTERBOT22 and PROBOY22 🔥
  MASTERBOT = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {BOT}\n\n"
  MASTERBOT += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  MASTERBOT += f"{BOT} OS : {VERSION} ʟᴀsᴛᴇsᴛ\n\n"
  MASTERBOT += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  MASTERBOT += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  MASTERBOT += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  MASTERBOT += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTONS = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{BOT} 𝚁𝙴𝙿𝙾", "https://github.com/MASTERBOTOP/LEGEND-BOT")]]
  BUTTONS += [[custom.Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="MASTERBOT")]]
  await event.edit(text=MASTERBOT, buttons=BUTTONS)


@xbot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await xbot.send_message(event.chat, "ʀᴇᴘᴏ ᴏғ ʟᴇɢᴇɴᴅ-ʙᴏᴛ", buttons=[[Button.url("⚜️ ʀᴇᴘᴏ ⚜️", "https://github.com/MASTERBOTOP/LEGEND-BOT")]])
