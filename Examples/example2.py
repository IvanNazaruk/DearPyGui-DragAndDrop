import dearpygui.dearpygui as dpg

import DearPyGui_DragAndDrop as dpg_dnd

dpg.create_context()
dpg_dnd.initialize()
dpg.create_viewport(title="Drag and drop example2", width=600, height=600)

with dpg.window() as window:
    drop_text = dpg.add_text()
    drop_keys = dpg.add_text()
dpg.set_primary_window(window, True)

with dpg.window(modal=True, autosize=True, show=False) as drop_window:
    dpg.add_text("Drop!", color=(0, 255, 0))


def drop(data, keys):
    dpg.configure_item(drop_window, show=False)
    dpg.set_value(drop_text, f'{data}')
    dpg.set_value(drop_keys, f'{keys}')


def drag_enter(data, keys):
    dpg.configure_item(drop_window, show=True)


def drag_leave():
    dpg.configure_item(drop_window, show=False)


dpg_dnd.set_drop(drop)
dpg_dnd.set_drag_enter(drag_enter)
dpg_dnd.set_drag_leave(drag_leave)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
