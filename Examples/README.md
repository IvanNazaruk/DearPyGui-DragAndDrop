# Examples

You can find several scenarios here, from simple to advanced, for using the library.<br>
Below you can see what they look like and their brief description.

## [Example №1: the simplest use case](example1.py)

Probably the simplest and most used example of using.
Drop the file into the program and our `drop` (change text) function will be called.
![example_1](https://user-images.githubusercontent.com/46572469/210179706-f187b70b-6649-44d4-880b-a6b35a961d08.gif)

## [Example №2: little interactivity](example2.py)

An example with a little interactivity, in the form of a pop-up window that says `Drop!`
(This is "similar" to the popup in Discord when you try to send a file by drag and drop).
This one has more functions, but also seems to be nothing complicated.
In `drag_enter` and `drag_leave` we hide and show the window respectively, and in `drop` we add hiding the window.
![example_2](https://user-images.githubusercontent.com/46572469/210180323-1ab73614-0f35-49e8-b5e1-7c65c332e44b.gif)

## [Example №3: more interactivity!](example3.py)

In this example, you can only drop a file in the popup window.
Added a function `drag_over` which checks the pointing to the window and, depending on the result,
changes the theme of the window and the style of the cursor.
![example_3](https://user-images.githubusercontent.com/46572469/210180650-b91c77d8-19da-4452-ad69-f8caa0201c32.gif)

## [Example №4: keys usage](example4.py)

Let's expand our example again, now the window theme depends on the key presses (CTRL, ALT, SHIFT).
![example_4](https://user-images.githubusercontent.com/46572469/210181492-3a9bca4a-005a-4e5c-b8cf-4a39b041ef27.gif)

## [Example №5: inheriting *DragAndDrop* or how to add an extra function to Drag And Drop](example5.py)

Probably you need a lot of *DragAndDrop* functions when developing some applications, 
and only one function can be attached to `set_drop`. 
And there is a solution for this, namely to use the class *DragAndDrop*, or rather inherit it.
When `__init__` is called in *DragAndDrop* (`super().__init__()`), 
this object (`self`) gets to the Drag-and-Drop functions queue, 
where certain functions will be called in the future, for example `{DragAndDrop_oject}.DragOver`.
This example uses only `DragOver` and `Drop`, but also has `DragEnter` and `DragLeave` 
which correspond to the functions `.set_drag_enter` and `.set_drag_leave` respectively. 
I would also like to add that all functions `.set_*` are called first in the queue 
(if you `.initialize()` before the DragAndDrop classes). 
And the "function" of setting the cursor style will be called after the queue is finished 
(that is, the last called `.set_drop_effect` will be taken).<br>

A little about the example: there are several "areas" in 
which you can drop a file and the text in them will change when it `drop`

![example_5](https://user-images.githubusercontent.com/46572469/210182508-d2232d43-0df3-4531-a34b-e773f9000ef9.gif)
