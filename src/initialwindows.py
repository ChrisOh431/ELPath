from dearpygui.core import *
from dearpygui.simple import *

# For maximum compat (and because I don't see any real reason not to,) the window is designed to fit in smaller screens (laptops, etc)
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 900
FILL_WIDTH = WINDOW_WIDTH-15
VAL_CNT = 20

CHILD_WINDOW_FILL_PARAMS = {
    "width": FILL_WIDTH, 
    "no_resize": True, 
    "no_collapse": True, 
    "no_close": True, 
    "no_move": True
}

def initialize_ELPath():
    # Window settings
    set_global_font_scale(1.5);
    set_theme("Dark Grey")
    set_main_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)
    set_style_window_padding(10, 10)
    add_additional_font("resources/fonts/Roboto_Mono/static/RobotoMono-Regular.ttf", 20)

    with window("ELPath", width=880, height=880):
        set_window_pos("ELPath", 0, 0)

    with window("Main Controls", x_pos=0, y_pos=0, height=WINDOW_HEIGHT//6, **CHILD_WINDOW_FILL_PARAMS):
        add_text("Algorithm: Bubble Sort") # hardcoded for now, since we only have bubble sort haha
        add_spacing(count=5, name="spacing1")

def link_buttons(start_callback, randomize_callback):
    add_button("Start", parent="Main Controls", callback=start_callback)
    add_button("Randomize Data", parent="Main Controls", callback=randomize_callback)
