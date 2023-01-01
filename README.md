# DearPyGui-DragAndDrop

Working Drag-and-drop for DearPyGui, Windows only
![demo](https://user-images.githubusercontent.com/46572469/210178591-3011e753-82ed-4d8f-8652-87375d7366e0.gif)

## How to install/use

1) Install the DearPyGui-DragAndDrop package: </br>
   `pip install DearPyGui-DragAndDrop`

2) Import and then initialize the library after `dpg.create_context()`:

```python
import dearpygui.dearpygui as dpg

import DearPyGui_DragAndDrop as dpg_dnd

dpg.create_context()
dpg_dnd.initialize()
```

3) That's it, just set your function for `drop` and your minimal use case is ready:

```python
import dearpygui.dearpygui as dpg

import DearPyGui_DragAndDrop as dpg_dnd

dpg.create_context()
dpg_dnd.initialize()
dpg.create_viewport(title="Drag and drop example", width=600, height=600)


def drop(data, keys):
    print(f'{data}')
    print(f'{keys}')


dpg_dnd.set_drop(drop)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
```

### More examples of use are in the [Examples folder](https://github.com/IvanNazaruk/DearPyGui-DragAndDrop/tree/main/Examples)

## Supported Formats

- [x] File(s) paths *(will be in the form of a `list of strings`)*
- [x] Text *(will be `string`)*

Everything else will be `None` or will be a `string`

## TODO list:

- [ ] Documentation and code/functions comments
- [ ] Add support for more and other data
  types: [maybe this is the right list](https://learn.microsoft.com/en-us/windows/win32/dataxchg/standard-clipboard-formats#constants)
