# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
import logging

import simpleobsws

logger_chirho = logging.getLogger(__name__)


class ObswsEventInputChirho:
    def __init__(
            self, *args_chirho, base_app_chirho: 'midisocket_chirho.base_app_chirho.BaseAppChirho',
            obsws_chirho: simpleobsws.WebSocketClient, **kwargs_chirho):
        super().__init__(*args_chirho, **kwargs_chirho)
        self.base_app_chirho = base_app_chirho
        self.obsws_chirho = obsws_chirho
        self.obsws_chirho.register_event_callback(
            self.on_event_chirho)  # By not specifying an event to listen to, all events are sent to this callback.
        # self.obsws_chirho.register_event_callback(self.on_switchscenes_chirho, 'SwitchScenes')

    async def on_event_chirho(self, eventType_chirho, eventData_chirho):
        logger_chirho.info('Aleluya - New event! Type: {} | Raw Data: {}'.format(
            eventType_chirho, eventData_chirho))  # Print the event data. Note that `update-type` is also provided in the data
        if eventType_chirho == "CurrentProgramSceneChanged":
            await self.on_switchscenes_chirho(eventData_chirho)

    async def on_switchscenes_chirho(self, eventData):
        scene_name_chirho = eventData['sceneName']
        self.base_app_chirho.current_scene_name_chirho = scene_name_chirho
        logger_chirho.info('Hallelujah - Scene switched to "{}".'.format(scene_name_chirho))

