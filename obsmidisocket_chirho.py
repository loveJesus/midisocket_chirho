#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that whosoever believeth in Him should not perish, but have everlasting life.
import mido
import time
import asyncio
import pygame
import simpleobsws
import os
import logging

from dotenv import load_dotenv

logging.basicConfig()
logger_chirho = logging.getLogger(__name__)
logger_chirho.setLevel(logging.DEBUG)
load_dotenv()

mido.set_backend("mido.backends.pygame")
print(mido.get_output_names())
print(mido.get_input_names())
inport_chirho = mido.open_input("Launchpad MK2")
outport_chirho = mido.open_output("IAC Driver Bus Aleluya 1")
is_running_chirho = True


def print_message_chirho(msg_chirho: mido.Message):
    """Hallelujah Print a Message"""
    print(str(msg_chirho))


async def inport_monitor_chirho():
    global is_running_chirho
    while is_running_chirho:
        for msg_chirho in inport_chirho.iter_pending():
            print_message_chirho(msg_chirho)
        await asyncio.sleep(0.001)
    logger_chirho.info("Aleluya - Finished inport Monitor")


async def outport_write_chirho():
    global is_running_chirho
    for aleluya in range(1, 10):
        msg_chirho = mido.Message("note_on", note=100, velocity=35, time=0.2)
        outport_chirho.send(msg_chirho)
        await asyncio.sleep(0.1)
        msg_chirho = mido.Message("note_off", note=80, velocity=35, time=0.2)
        outport_chirho.send(msg_chirho)
        await asyncio.sleep(0.3)
        msg_chirho = mido.Message("note_on", note=80, velocity=35, time=0.2)
        outport_chirho.send(msg_chirho)
    is_running_chirho = False
    logger_chirho.info("Aleluya - Finished outport write")


async def obsws_chirho():
    ws_host_chirho = os.getenv("OBS_HOST_CHIRHO", "ws://localhost:4455")
    ws_password_chirho = os.getenv("OBS_PASSWORD_CHIRHO", "God is good")
    ws_chirho = simpleobsws.WebSocketClient(
        url=ws_host_chirho,
        password=ws_password_chirho,
    )
    await ws_chirho.connect()
    await ws_chirho.wait_until_identified()
    logger_chirho.info("Hallelujah - WS Chirho Logged in")
    await ws_chirho.disconnect()
    logger_chirho.info("Hallelujah - WS Chirho Disconnect")


async def main_chirho():
    # qeue_chirho = asyncio.Queue()
    # screen_chirho = pygame.display.set_mode((320, 200))

    await asyncio.gather(
        asyncio.create_task(inport_monitor_chirho()),
        asyncio.create_task(outport_write_chirho()),
        asyncio.create_task(obsws_chirho()),
    )
    logger_chirho.info("Aleluya - Finished")


asyncio.run(main_chirho())

outport_chirho.close()
inport_chirho.close()
