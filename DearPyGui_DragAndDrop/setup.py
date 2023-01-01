import ctypes
import os
import time

import dearpygui.dearpygui as dpg
import pythoncom
import win32gui
from win32com.server.policy import DesignatedWrapPolicy

from . import tools
from .main import DragAndDrop
from .main import get_drop_effect

hwnd = -1


class DropTarget(DesignatedWrapPolicy):
    _public_methods_ = ['DragEnter', 'DragOver', 'DragLeave', 'Drop']
    _com_interfaces_ = [pythoncom.IID_IDropTarget]  # noqa

    def __init__(self):  # noqa
        self._wrap_(self)

    def DragEnter(self, dataObject, keyState, point, effect):
        ctypes.windll.user32.SetForegroundWindow(hwnd)
        DragAndDrop._DragEnter(tools.get_data_from_dataObject(dataObject),
                               tools.key_state_to_keys_list(keyState))
        return 0, get_drop_effect()
        # return winerror.S_OK, get_drop_effect()

    def DragOver(self, keyState, point, effect):
        DragAndDrop._DragOver(tools.key_state_to_keys_list(keyState))
        return get_drop_effect()

    def DragLeave(self):
        DragAndDrop._DragLeave()

    def Drop(self, dataObject, keyState, point, effect):
        DragAndDrop._Drop(tools.get_data_from_dataObject(dataObject),
                          tools.key_state_to_keys_list(keyState))


def setup():
    global hwnd
    if hwnd != -1:
        return
    hwnd = 0
    # Wait for initialization and appearance of the DPG window
    while dpg.get_frame_count() == 0:
        time.sleep(0.1)

    # Get the window hwnd from its own pid
    hwnd = tools.get_hwnd_from_pid(os.getpid())

    pythoncom.OleInitialize()  # noqa
    pythoncom.RegisterDragDrop(  # noqa
        hwnd,
        pythoncom.WrapObject(  # noqa
            DropTarget(),
            pythoncom.IID_IDropTarget,  # noqa
            pythoncom.IID_IDropTarget  # noqa
        )
    )
    win32gui.PumpMessages()
