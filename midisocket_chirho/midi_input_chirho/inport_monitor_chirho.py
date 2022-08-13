# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import asyncio
import logging
import mido

logger_chirho = logging.getLogger(__name__)

class InportMonitorChirho:
    def __init__(
            self, *args_chirho,
            base_app_chirho: 'obsmidisocket_chirho.BaseAppChirho', input_name_chirho: str = "", **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.base_app_chirho = base_app_chirho
        self.inport_chirho = mido.open_input(input_name_chirho)

    def print_message_chirho(self, msg_chirho: mido.Message):
        """Hallelujah Print a Message"""
        print(str(msg_chirho))

    def close_chirho(self):
        self.inport_chirho.close()
        logger_chirho.info("Aleluya - Closed inport")

    async def inport_monitor_chirho(self):

        while self.base_app_chirho. is_running_chirho:
            for msg_chirho in self.inport_chirho.iter_pending():
                self.print_message_chirho(msg_chirho)
            await asyncio.sleep(0.001)
        logger_chirho.info("Aleluya - Finished inport Monitor")
