import threading

from . import main as __main
from . import setup as __setup
from .main import DROPEFFECT, KEYSTATE
from .main import DragAndDrop, DragAndDropDataObject
from .main import set_drag_enter, set_drag_over, set_drag_leave, set_drop
from .main import set_drop_effect, get_drop_effect

__version__ = "1.0.0"

def initialize():
    if isinstance(__main._DragAndDropForFunctions, type):
        __main._DragAndDropForFunctions = __main._DragAndDropForFunctions()

    threading.Thread(target=__setup.setup, daemon=True).start()
