# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging

import simpleobsws

logger_chirho = logging.getLogger(__name__)


class ObswsEventInputChirho:
    def __init__(
            self, *args_chirho, base_app_chirho: 'midisocket_chirho.BaseAppChirho',
            obsws_chirho: simpleobsws.WebSocketClient, **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.base_app_chirho = base_app_chirho
        self.obsws_chirho = obsws_chirho
        self.obsws_chirho.register_event_callback(
            self.on_event)  # By not specifying an event to listen to, all events are sent to this callback.
        # self.init_obsws_chirho.register_event_callback(on_switchscenes, 'SwitchScenes')

    async def on_event(self, eventType, eventData):
        logger_chirho.info('Aleluya - New event! Type: {} | Raw Data: {}'.format(
            eventType, eventData))  # Print the event data. Note that `update-type` is also provided in the data

    async def on_switchscenes(self, eventData):
        logger_chirho.info('Hallelujah - Scene switched to "{}".'.format(eventData['sceneName']))
