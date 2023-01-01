import dearpygui.dearpygui as dpg

import DearPyGui_DragAndDrop as dpg_dnd

dpg.create_context()
dpg_dnd.initialize()
dpg.create_viewport(title="Drag and drop example4", width=600, height=600)

with dpg.theme() as hover_drag_theme_1:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 180, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (25, 50, 75), category=dpg.mvThemeCat_Core)
with dpg.theme() as hover_drag_theme_2:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Border, (250, 5, 60), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (45, 15, 5), category=dpg.mvThemeCat_Core)
with dpg.theme() as hover_drag_theme_3:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Border, (205, 0, 255), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (65, 30, 100), category=dpg.mvThemeCat_Core)
with dpg.theme() as hover_drag_theme_4:
    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_Border, (0, 255, 60), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_PopupBg, (30, 65, 30), category=dpg.mvThemeCat_Core)

with dpg.window() as window:
    drop_text = dpg.add_text()
    drop_keys = dpg.add_text()
dpg.set_primary_window(window, True)

with dpg.window(modal=True, autosize=True, show=False) as drop_window:
    dpg.add_text("Drop here!", color=(0, 255, 0))


def drop(data, keys):
    dpg.configure_item(drop_window, show=False)
    dpg.bind_item_theme(drop_window, None)
    dpg_dnd.set_drop_effect()

    dpg.set_value(drop_text, f'{data}')
    dpg.set_value(drop_keys, f'{keys}')


def drag_over(keys):
    if not dpg.is_item_hovered(drop_window):
        dpg.bind_item_theme(drop_window, None)
        dpg_dnd.set_drop_effect()
        return

    hover_drag_theme = hover_drag_theme_1
    if dpg_dnd.KEYSTATE.ALT in keys and dpg_dnd.KEYSTATE.CTRL in keys:
        hover_drag_theme = hover_drag_theme_2
    elif dpg_dnd.KEYSTATE.ALT in keys:
        hover_drag_theme = hover_drag_theme_3
    elif dpg_dnd.KEYSTATE.CTRL in keys:
        hover_drag_theme = hover_drag_theme_4

    dpg.bind_item_theme(drop_window, hover_drag_theme)
    dpg_dnd.set_drop_effect(dpg_dnd.DROPEFFECT.MOVE)


def drag_enter(data, keys):
    dpg.configure_item(drop_window, show=True)


def drag_leave():
    dpg.configure_item(drop_window, show=False)
    dpg.bind_item_theme(drop_window, None)
    dpg_dnd.set_drop_effect()


dpg_dnd.set_drop(drop)
dpg_dnd.set_drag_over(drag_over)
dpg_dnd.set_drag_enter(drag_enter)
dpg_dnd.set_drag_leave(drag_leave)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
