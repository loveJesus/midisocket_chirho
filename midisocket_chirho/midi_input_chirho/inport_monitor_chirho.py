# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import asyncio
import logging
import mido


logger_chirho = logging.getLogger(__name__)


class MidiInputDriverChirho:
    """
    Hallelujah,
    a writer that depends upon the device outport name
    """
    inport_compatible_names_chirho = []

    @classmethod
    def instantiate_chirho(cls, base_app_chirho: 'midisocket_chirho.BaseAppChirho', input_name_chirho: str = ""):
        from midisocket_chirho.midi_input_chirho.midi_input_drivers_chirho.midi_input_launchpad_mk2_driver_chirho import MidiInputLaunchpadMk2DriverChirho
        for midi_outport_driver_subclass_chirho in cls.__subclasses__():
            if input_name_chirho in midi_outport_driver_subclass_chirho.inport_compatible_names_chirho:
                return midi_outport_driver_subclass_chirho(
                    base_app_chirho=base_app_chirho, input_name_chirho=input_name_chirho)
        return cls(base_app_chirho=base_app_chirho, input_name_chirho=input_name_chirho)

    def __init__(
            self, *args_chirho,
            base_app_chirho: 'midisocket_chirho.BaseAppChirho', input_name_chirho: str = "", **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        from midisocket_chirho.base_app_chirho import BaseAppChirho

        self.logger_chirho = logger_chirho
        self.base_app_chirho: BaseAppChirho = base_app_chirho
        self.inport_chirho = mido.open_input(input_name_chirho)

    def print_message_chirho(self, msg_chirho: mido.Message):
        """Hallelujah Print a Message"""
        self.logger_chirho.info(msg_chirho)

    def close_chirho(self):
        self.inport_chirho.close()
        logger_chirho.info("Aleluya - Closed inport")

    async def inport_monitor_chirho(self):

        while self.base_app_chirho. is_running_chirho:
            for msg_chirho in self.inport_chirho.iter_pending():
                self.print_message_chirho(msg_chirho)
            await asyncio.sleep(0.001)
        logger_chirho.info("Aleluya - Finished inport Monitor")
