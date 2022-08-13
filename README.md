# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
## Midi Socket ChiRho

Python program to control things like [OBS](https://obsproject.com) using midi via [obs-websocket](https://github.com/obsproject/obs-websocket) version 5.x

### Notes:

This is in early stages of development.

To interface with obs-websocket in python we are using [Simple Obs WS](https://github.com/IRLToolkit/simpleobsws).

For Midi in Python we are using [mido](https://github.com/mido/mido) 
by default uses [python-rtmidi](https://github.com/SpotlightKid/python-rtmidi). 
Can also use [pygame.midi](https://mido.readthedocs.io/en/latest/backends/pygame.html) as the backend 
for example which uses [portmidi](https://github.com/PortMidi/PortMidi) internally.


### Installation

```shell
# MacOS
brew install rtmidi jack2 portmidi

python3.10 -m venv venv_chirho
source venv_chirho/bin/activate
pip install --upgrade pip && pip install --upgrade -r requirements_chirho.txt --global-option=build_ext --global-option="-L/opt/homebrew/lib/" --global-option=build_ext --global-option="-I/opt/homebrew/include/"
./midisocket_chirho.py
```
