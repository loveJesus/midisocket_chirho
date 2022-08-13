# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import os
import simpleobsws

logger_chirho = logging.getLogger(__name__)

async def obsws_chirho():
    logger_chirho.info("Aleluya - Starting obsws")
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