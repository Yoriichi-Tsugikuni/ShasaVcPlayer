#
# Copyright (C) 2021-2022 by MdNoor786@Github, < https://github.com/MdNoor786 >.
#
# This file is part of < https://github.com/MdNoor786/ShasaVcPlayer > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/MdNoor786/ShasaVcPlayer/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client

import config

from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING1),
            no_updates=True,
        )
        self.two = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING2),
            no_updates=True,
        )
        self.three = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING3),
            no_updates=True,
        )
        self.four = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING4),
            no_updates=True,
        )
        self.five = Client(
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_name=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER(__name__).minfo(f"Starting Assistant Clients")
        if config.STRING1:
            await self.one.start()
            try:
                await self.one.join_chat("TeamLionX")
                await self.one.join_chat("Chattingzonexd")
                await self.one.join_chat("LionXsupport")
            except:
                pass
            assistants.append(1)
            try:
                await self.one.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).minfo(f"Assistant Started as {self.one.name}")
        if config.STRING2:
            await self.two.start()
            try:
                await self.two.join_chat("TeamLionX")
                await self.two.join_chat("Chattingzonexd")
                await self.two.join_chat("LionXsupport")
            except:
                pass
            assistants.append(2)
            try:
                await self.two.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).minfo(f"Assistant Two Started as {self.two.name}")
        if config.STRING3:
            await self.three.start()
            try:
                await self.three.join_chat("TeamLionX")
                await self.three.join_chat("Chattingzonexd")
                await self.three.join_chat("LionXsupport")
            except:
                pass
            assistants.append(3)
            try:
                await self.three.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = get_me.first_name + " " + get_me.last_name
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).minfo(f"Assistant Three Started as {self.three.name}")
        if config.STRING4:
            await self.four.start()
            try:
                await self.four.join_chat("TeamLionX")
                await self.four.join_chat("Chattingzonexd")
                await self.four.join_chat("LionXsupport")
            except:
                pass
            assistants.append(4)
            try:
                await self.four.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.four.name = get_me.first_name + " " + get_me.last_name
            else:
                self.four.name = get_me.first_name
            LOGGER(__name__).minfo(f"Assistant Four Started as {self.four.name}")
        if config.STRING5:
            await self.five.start()
            try:
                await self.five.join_chat("TeamLionX")
                await self.five.join_chat("Chattingzonexd")
                await self.five.join_chat("LionXsupport")
            except:
                pass
            assistants.append(5)
            try:
                await self.five.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! "
                )
                sys.exit()
            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.five.name = get_me.first_name + " " + get_me.last_name
            else:
                self.five.name = get_me.first_name
            LOGGER(__name__).minfo(f"Assistant Five Started as {self.five.name}")
