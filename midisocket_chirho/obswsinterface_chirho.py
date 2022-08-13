# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging
import os
import simpleobsws

from midisocket_chirho.obs_input_chirho.obsws_event_input_chirho import ObswsEventInputChirho

logger_chirho = logging.getLogger(__name__)


async def obsws_chirho():
    logger_chirho.info("Aleluya - Starting obsws")
    obsws_host_chirho = os.getenv("OBS_HOST_CHIRHO", "ws://localhost:4455")
    obsws_password_chirho = os.getenv("OBS_PASSWORD_CHIRHO", "God is good")
    obsws_chirho = simpleobsws.WebSocketClient(
        url=obsws_host_chirho,
        password=obsws_password_chirho,
    )
    await obsws_chirho.connect()
    await obsws_chirho.wait_until_identified()
    obsws_event_input_chirho = ObswsEventInputChirho(obsws_chirho=obsws_chirho)
    logger_chirho.info("Hallelujah - WS Chirho Logged in")
    await obsws_chirho.disconnect()
    logger_chirho.info("Hallelujah - WS Chirho Disconnect")
