import os
import eel

from backend.features import *
from backend.command import *

eel.init("template")

playOptimusSound()

os.system('Start msedge.exe --app="http://localhost:8000/index.html')
eel.start('index.html', mode=None, host='localhost', block=True)
