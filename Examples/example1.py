import dearpygui.dearpygui as dpg

import DearPyGui_DragAndDrop as dpg_dnd

dpg.create_context()
dpg_dnd.initialize()
dpg.create_viewport(title="Drag and drop example1", width=600, height=600)

with dpg.window() as window:
    drop_text = dpg.add_text()
    drop_keys = dpg.add_text()
dpg.set_primary_window(window, True)


def drop(data, keys):
    dpg.set_value(drop_text, f'{data}')
    dpg.set_value(drop_keys, f'{keys}')


dpg_dnd.set_drop(drop)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
