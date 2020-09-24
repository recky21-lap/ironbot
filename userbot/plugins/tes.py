from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.hc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message.`")
        return
    reply_message = await event.get_reply_message()
    chat = "@hcdecryptor_bot"
    await event.edit("`Processing`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=461843263)
                )
                await bot.forward_messages(chat, reply_message)
                response = await response
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Please unblock @sangmatainfo_bot and try again`")
                return
            if response.text.startswith("Forward"):
                await event.edit(
                    "`Can you kindly disable your forward privacy settings for good?`"
                )
            else:
                await event.delete()
                await bot.forward_messages(event.chat_id, response.message)

    except TimeoutError:
        return await event.edit("`Error: `@SangMataInfo_bot` is not responding!.`")


CMD_HELP.update(
    {
        "sangmata": ">`.hc` \
          \nUsage: View user history.\n"
    }
)
