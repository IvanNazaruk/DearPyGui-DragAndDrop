from __future__ import annotations

import ctypes.wintypes
from ctypes import wintypes

import pythoncom
import pywintypes
import win32con
from win32comext.shell import shell

from .main import DragAndDropDataObject
from .main import KEYSTATE


def get_data_from_dataObject(dataObject) -> DragAndDropDataObject:
    try:
        # Drag&Drop files
        _format = win32con.CF_HDROP, None, 1, -1, pythoncom.TYMED_HGLOBAL  # noqa
        sm = dataObject.GetData(_format)
    except pywintypes.com_error:  # noqa
        try:
            # Drag&Drop text
            _format = win32con.CF_TEXT, None, 1, -1, pythoncom.TYMED_HGLOBAL  # noqa
            sm = dataObject.GetData(_format)
            # returns a string converted from bytes
            return sm.data.decode("utf-8")
        except pywintypes.com_error:  # noqa
            # Drag&Drop unknown type
            # return nothing
            return None

    # Drag&Drop files
    num_files = shell.DragQueryFile(sm.data_handle, -1)
    files = []
    for i in range(num_files):
        fpath = shell.DragQueryFile(sm.data_handle, i)
        files.append(fpath)
    # returns a list of file paths
    return files


user32 = ctypes.windll.user32
WNDENUMPROC = ctypes.WINFUNCTYPE(wintypes.BOOL,
                                 wintypes.HWND,
                                 wintypes.LPARAM)
user32.EnumWindows.argtypes = [WNDENUMPROC,
                               wintypes.LPARAM]


def get_hwnd_from_pid(pid: int) -> int | None:
    result = None

    def callback(hwnd, _):
        nonlocal result
        lpdw_PID = ctypes.c_ulong()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(lpdw_PID))
        hwnd_PID = lpdw_PID.value

        if hwnd_PID == pid:
            result = hwnd
            return False
        return True

    cb_worker = WNDENUMPROC(callback)
    user32.EnumWindows(cb_worker, 0)
    return result


def key_state_to_keys_list(keyState: int) -> list[KEYSTATE]:
    # https://learn.microsoft.com/en-us/dotnet/api/system.windows.forms.drageventargs.keystate?view=windowsdesktop-7.0#remarks
    key_state_list = []

    # conversion to byte string and reverse it
    keyState = '{0:06b}'.format(keyState)[::-1]
    if bool(int(keyState[0])):
        key_state_list.append(KEYSTATE.LEFT)
    if bool(int(keyState[1])):
        key_state_list.append(KEYSTATE.RIGHT)
    if bool(int(keyState[2])):
        key_state_list.append(KEYSTATE.SHIFT)
    if bool(int(keyState[3])):
        key_state_list.append(KEYSTATE.CTRL)
    if bool(int(keyState[4])):
        key_state_list.append(KEYSTATE.MIDDLE)
    if bool(int(keyState[5])):
        key_state_list.append(KEYSTATE.ALT)
    return key_state_list
