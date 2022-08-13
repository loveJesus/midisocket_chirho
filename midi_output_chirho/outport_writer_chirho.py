# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import asyncio
import logging
import mido


logger_chirho = logging.getLogger(__name__)


class OutportWriterChirho:
    def __init__(
            self, *args_chirho,
            base_app_chirho: 'obsmidisocket_chirho.BaseAppChirho',  outport_name_chirho: str = "", **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.base_app_chirho = base_app_chirho
        self.outport_chirho = mido.open_output(outport_name_chirho)

    def close_chirho(self):
        self.outport_chirho.close()
        logger_chirho.info("Aleluya - Closed outport")

    async def outport_write_chirho(self):
        for aleluya in range(1, 10):
            msg_chirho = mido.Message("note_on", note=100, velocity=35, time=0.2)
            self.outport_chirho.send(msg_chirho)
            await asyncio.sleep(0.1)
            msg_chirho = mido.Message("note_off", note=80, velocity=35, time=0.2)
            self.outport_chirho.send(msg_chirho)
            await asyncio.sleep(0.3)
            msg_chirho = mido.Message("note_on", note=80, velocity=35, time=0.2)
            self.outport_chirho.send(msg_chirho)
        self.base_app_chirho.is_running_chirho = False
        logger_chirho.info("Aleluya - Finished outport write")
