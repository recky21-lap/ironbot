from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP
import asyncio
import sys, time, io


@register(outgoing=True, pattern="^.hc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message.`")
        return
    reply_message = await event.get_reply_message()
    chat = "@AsalAja777_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Reply to actual users message.`")
        return
    await event.edit("`Proses decrypt boss sabar...`")
    await asyncio.sleep(.5)
    await event.edit("`50%...`")
    await asyncio.sleep(.5)
    await event.edit("`70%...`")
    await asyncio.sleep(.5)
    await event.edit("`100%...`")
    await asyncio.sleep(.5)
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=835283956))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Please unblock and try again`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`can you kindly disable your forward privacy settings for good?`")
        else:
            await event.edit(f"```{response.message.message}```")

@register(outgoing=True, pattern="^.sniff(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    chat = "@AsalAja777_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("``````")
        return
    await event.edit("`Proses decrypt boss sabar...`")
    await asyncio.sleep(.5)
    await event.edit("`50%...`")
    await asyncio.sleep(.5)
    await event.edit("`70%...`")
    await asyncio.sleep(.5)
    await event.edit("`100%...`")
    await asyncio.sleep(.5)
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=835283956)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("``````")
            return
        await borg.send_read_acknowledge(conv.chat_id)
        if response.text.startswith("Hi!"):
            await event.edit(
                "```Can you kindly disable your forward privacy settings for good?```"
            )
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, **response.message**)
