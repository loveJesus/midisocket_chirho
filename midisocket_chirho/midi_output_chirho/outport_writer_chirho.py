# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import asyncio
import logging
import mido

logger_chirho = logging.getLogger(__name__)


class MidiOutportDriverChirho:
    """
    Hallelujah,
    a writer that depends upon the device outport name
    """
    outport_compatible_names_chirho = []

    @classmethod
    def instantiate_chirho(cls, base_app_chirho: 'midisocket_chirho.BaseAppChirho',  outport_name_chirho: str = ""):
        from midisocket_chirho.midi_output_chirho.midi_output_drivers_chirho.midi_output_launchpad_mk2_driver_chirho import MidiOutportDriverLaunchpadMk2Chirho

        logger_chirho.info("Aleluya. FOR PORT- {}".format(outport_name_chirho))
        for midi_outport_driver_subclass_chirho in cls.__subclasses__():
            logger_chirho.info("Aleluya - {}".format(midi_outport_driver_subclass_chirho.outport_compatible_names_chirho))
            if outport_name_chirho in midi_outport_driver_subclass_chirho.outport_compatible_names_chirho:
                return midi_outport_driver_subclass_chirho(
                    base_app_chirho=base_app_chirho, outport_name_chirho=outport_name_chirho)
        return cls(base_app_chirho=base_app_chirho, outport_name_chirho=outport_name_chirho)

    def __init__(
            self, *args_chirho,
            base_app_chirho: 'midisocket_chirho.BaseAppChirho',  outport_name_chirho: str = "", **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        from midisocket_chirho.base_app_chirho import BaseAppChirho
        self.base_app_chirho: BaseAppChirho = base_app_chirho
        self.outport_chirho = mido.open_output(outport_name_chirho)

    def close_chirho(self):
        self.outport_chirho.close()
        logger_chirho.info("Aleluya - Closed outport")

    async def outport_write_chirho(self):
        aleluya = 0
        while self.base_app_chirho.is_running_chirho:
            aleluya += 1
            self.outport_chirho.send(mido.Message("note_on", note=20, velocity=35, time=0.2, channel=14))
            await asyncio.sleep(0.2)
            logger_chirho.info("Aleluya - {}".format(aleluya))
            self.outport_chirho.send(mido.Message("note_on", note=8, velocity=35, time=0.2))
            await asyncio.sleep(0.2)
            self.outport_chirho.send(mido.Message("note_off", note=20, velocity=35, time=0.2, channel=14))
            await asyncio.sleep(0.3)
            self.outport_chirho.send(mido.Message("note_off", note=8, velocity=35, time=0.2))

        self.outport_chirho.send(mido.Message("note_off", note=20, velocity=35, time=0.2, channel=14))
        self.outport_chirho.send(mido.Message("note_off", note=8, velocity=35, time=0.2))
        self.base_app_chirho.is_running_chirho = False
        logger_chirho.info("Aleluya - Finished outport write")
