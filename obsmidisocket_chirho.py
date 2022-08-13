#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that whosoever believeth in Him should not perish, but have everlasting life.
import mido
import asyncio
import logging
import sys

from dotenv import load_dotenv

from midi_input_chirho.inport_monitor_chirho import InportMonitorChirho
from midi_output_chirho.outport_writer_chirho import OutportWriterChirho
from obswsinterface_chirho import obsws_chirho

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger_chirho = logging.getLogger(__name__)
load_dotenv()

mido.set_backend("mido.backends.pygame")
print(mido.get_output_names())
print(mido.get_input_names())


class BaseAppChirho:
    def __init__(self, *args_chirho, **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.is_running_chirho: bool = True
        asyncio.run(self.main_chirho())
        logger_chirho.info("Aleluya - Finished BaseApp")

    async def main_chirho(self):
        # qeue_chirho = asyncio.Queue()
        # screen_chirho = pygame.display.set_mode((320, 200))

        inport_monitor_chirho = InportMonitorChirho(
            base_app_chirho=self, input_name_chirho="Launchpad MK2")
        outport_writer_chirho = OutportWriterChirho(
            base_app_chirho=self, outport_name_chirho="IAC Driver Bus Aleluya 1")

        try:
            await asyncio.gather(
                asyncio.create_task(inport_monitor_chirho.inport_monitor_chirho()),
                asyncio.create_task(outport_writer_chirho.outport_write_chirho()),
                asyncio.create_task(obsws_chirho()),
            )
            logger_chirho.info("Aleluya - Finished")

        except Exception as e_chirho:
            logger_chirho.exception(e_chirho)

        inport_monitor_chirho.close_chirho()
        outport_writer_chirho.close_chirho()


if __name__ == "__main__":
    BaseAppChirho()
    logger_chirho.info("Aleluya - Finished Main")
    sys.exit(0)
