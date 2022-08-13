#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that whosoever believeth in Him should not perish, but have everlasting life.
from typing import Optional

import mido
import asyncio
import logging
import sys

from dotenv import load_dotenv

from midisocket_chirho.midi_input_chirho.inport_monitor_chirho import InportMonitorChirho
from midisocket_chirho.midi_output_chirho.outport_writer_chirho import OutportWriterChirho
from midisocket_chirho.obs_input_chirho.obsws_event_input_chirho import ObswsEventInputChirho
from midisocket_chirho.obs_output_chirho.obsws_output_chirho import ObswsOutputChirho
from midisocket_chirho.obswsinterface_chirho import init_obsws_chirho

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger_chirho = logging.getLogger(__name__)
load_dotenv()

mido.set_backend("mido.backends.rtmidi")
print(mido.get_output_names())
print(mido.get_input_names())


class BaseAppChirho:
    def __init__(self, *args_chirho, **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.is_running_chirho: bool = False
        self.obsws_event_input_chirho: Optional[ObswsEventInputChirho] = None
        self.obsws_output_chirho: Optional[ObswsOutputChirho] = None

    def run_chirho(self):
        self.is_running_chirho = True
        asyncio.run(self._main_chirho())
        logger_chirho.info("Aleluya - Finished BaseApp")

    async def _main_chirho(self):
        # qeue_chirho = asyncio.Queue()
        # screen_chirho = pygame.display.set_mode((320, 200))

        inport_monitor_chirho = InportMonitorChirho(
            base_app_chirho=self, input_name_chirho="Launchpad MK2")
        outport_writer_chirho = OutportWriterChirho(
            base_app_chirho=self, outport_name_chirho="IAC Chirho aleluyas 1")

        try:
            await asyncio.gather(
                asyncio.create_task(inport_monitor_chirho.inport_monitor_chirho()),
                asyncio.create_task(outport_writer_chirho.outport_write_chirho()),
                asyncio.create_task(init_obsws_chirho(self)),
            )
            logger_chirho.info("Aleluya - Finished")

        except Exception as e_chirho:
            logger_chirho.exception(e_chirho)

        inport_monitor_chirho.close_chirho()
        outport_writer_chirho.close_chirho()


if __name__ == "__main__":
    base_app_chirho = BaseAppChirho()
    base_app_chirho.run_chirho()
    logger_chirho.info("Aleluya - Finished Main")
    sys.exit(0)
