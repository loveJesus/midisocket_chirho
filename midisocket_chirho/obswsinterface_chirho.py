# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import asyncio
import logging
import os
import simpleobsws

import midisocket_chirho
from midisocket_chirho.obs_input_chirho.obsws_event_input_chirho import ObswsEventInputChirho
from midisocket_chirho.obs_output_chirho.obsws_output_chirho import ObswsOutputChirho

logger_chirho = logging.getLogger(__name__)


async def init_obsws_chirho(base_app_chirho: 'midisocket_chirho.BaseAppChirho'):
    """
    Hallelujah,
    Initialize the OBS Websocket connection.
    """
    logger_chirho.info("Aleluya - Starting obsws")
    obsws_host_chirho = os.getenv("OBS_HOST_CHIRHO", "ws://localhost:4455")
    obsws_password_chirho = os.getenv("OBS_PASSWORD_CHIRHO", "God is good")
    # parameters_chirho = simpleobsws.IdentificationParameters()  # Create an IdentificationParameters object
    # parameters_chirho.eventSubscriptions = (1 << 0) | (1 << 2)  # Subscribe to the General and Scenes categories
    obsws_chirho = simpleobsws.WebSocketClient(
        url=obsws_host_chirho,
        # identification_parameters=parameters_chirho,
        password=obsws_password_chirho)

    await obsws_chirho.connect()
    await obsws_chirho.wait_until_identified()

    obsws_event_input_chirho = ObswsEventInputChirho(base_app_chirho=base_app_chirho, obsws_chirho=obsws_chirho)
    obsws_output_chirho = ObswsOutputChirho(base_app_chirho=base_app_chirho, obsws_chirho=obsws_chirho)
    base_app_chirho.obsws_event_input_chirho = obsws_event_input_chirho
    base_app_chirho.obsws_output_chirho = obsws_output_chirho
    logger_chirho.info("Hallelujah - WS Chirho Logged in")
    await obsws_output_chirho.output_server_chirho()
    await obsws_chirho.disconnect()
    logger_chirho.info("Hallelujah - WS Chirho Disconnect")
