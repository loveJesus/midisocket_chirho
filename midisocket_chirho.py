#!/usr/bin/env python3
# For God so loved the world, that He gave His only begotten Son, that whosoever believeth in Him should not perish, but have everlasting life.
from typing import Optional

import mido
import asyncio
import logging
import sys

from dotenv import load_dotenv

from midisocket_chirho.base_app_chirho import BaseAppChirho

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
logger_chirho = logging.getLogger(__name__)
load_dotenv()

mido.set_backend("mido.backends.rtmidi")
print(mido.get_output_names())
print(mido.get_input_names())

if __name__ == "__main__":
    base_app_chirho = BaseAppChirho()
    base_app_chirho.run_chirho()
    logger_chirho.info("Aleluya - Finished Main")
    sys.exit(0)
