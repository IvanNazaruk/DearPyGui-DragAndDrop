import dearpygui.dearpygui as dpg

import DearPyGui_DragAndDrop as dpg_dnd

dpg.create_context()
dpg_dnd.initialize()
dpg.create_viewport(title="Drag and drop example5", width=600, height=600)

with dpg.theme() as hover_drag_theme:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 180, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ChildBg, (25, 50, 75), category=dpg.mvThemeCat_Core)


class ChildWindow(dpg_dnd.DragAndDrop):
    window: int = None
    dpg_text: int

    def __init__(self):
        super().__init__()

    def create(self):
        with dpg.child_window(width=-1, height=50) as self.window:
            self.dpg_text = dpg.add_text(parent=self.window)

    def DragOver(self, keyState: list[dpg_dnd.KEYSTATE]):
        if self.window is None:
            return
        if dpg.is_item_hovered(self.window):
            dpg.bind_item_theme(self.window, hover_drag_theme)
            dpg_dnd.set_drop_effect(dpg_dnd.DROPEFFECT.MOVE)
        else:
            dpg.bind_item_theme(self.window, None)

    def Drop(self, dataObject: dpg_dnd.DragAndDropDataObject, keyState: list[dpg_dnd.KEYSTATE]):
        if self.window is None:
            return
        dpg.bind_item_theme(self.window, None)
        if dpg.is_item_hovered(self.window):
            dpg.set_value(self.dpg_text, f'{dataObject}')

def drag_over(keys):
    dpg_dnd.set_drop_effect()


dpg_dnd.set_drag_over(drag_over)

with dpg.window() as window:
    for i in range(5):
        child_window = ChildWindow()
        child_window.create()
        dpg.add_spacer(height=25)

dpg.set_primary_window(window, True)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
