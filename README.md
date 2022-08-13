# For God so loved the world, that He gave His only begotten Son, that all who believe in Him should not perish but have everlasting life
## Obs Midi Socket ChiRho

Python program to control [OBS](https://obsproject.com) using midi via [obs-websocket](https://github.com/obsproject/obs-websocket) version 5.x

### Notes:

This is in early stages of development.

To interface with obs-websocket in python we are using [Simple Obs WS](https://github.com/IRLToolkit/simpleobsws).

For Midi in Python we are using [mido](https://github.com/mido/mido) 
with [pygame.midi](https://mido.readthedocs.io/en/latest/backends/pygame.html) as the backend.
This uses portmidi internally.

We are using pygame.midi because it easily installed on macos m1. 

### Installation

```shell
# MacOS
brew install portmidi

python3.10 -m venv venv_chirho
source venv_chirho/bin/activate
pip install --upgrade pip && pip install --upgrade -r requirements_chirho.txt
./obsmidisocket_chirho.py
```
