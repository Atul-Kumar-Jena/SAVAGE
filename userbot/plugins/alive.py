 
import asyncio
from telethon import events
from userbot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot import ALIVE_NAME, "SAVAGE user"
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SAVAGE user"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

PM_IMG = Config.ALIVE_PIC
pm_caption = "__             **🔥 らΛƔΛƓƐ 🔥**  __\n\n"

pm_caption += f"               __↼🄼🄰🅂🅃🄴🅁⇀__\n**『[{DEFAULTUSER}](tg://user?id={kraken})』**\n\n"
pm_caption += "✘ ΔβØỮŦ Μ¥ Ş¥ŞŦ€Μ ✘\n\n"
pm_caption += "➾ **𝐓𝐄𝐋𝐄𝐓𝐇𝐎𝐍**  ➣ 𝟏.𝟏𝟕.𝟓\n"
pm_caption += "➾ **𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ** ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqURitfHVMgXMeENMPJA)\n"
pm_caption += "➾ **𝐒𝐎𝐂𝐈𝐀𝐋  **  ➣ [𝐉𝐎𝐈𝐍](https://t.me/joinchat/VhpqUT83rKwiDnghqupK8w)\n"
pm_caption += "➾ **𝐂𝐑𝐄𝐀𝐓𝐎𝐑** ➣ [⚡𝐒𝐀𝐌𝐄𝐄𝐑⚡](@SAMEER_795)\n" 

pm_caption += " \n\n"
pm_caption += "[✨ Đ€ƤŁØ¥ ¥ØỮŘ ŞΔVΔǤ€ 2.0 ✨](https://github.com/sameerpanthi/SAVAGE)"


@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
