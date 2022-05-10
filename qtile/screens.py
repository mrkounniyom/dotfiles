#!/usr/bin/env python

import os, sys, platform, importlib
from libqtile import bar, widget, qtile
from libqtile.config import Screen, Group
from libqtile.lazy import lazy

#config imports
def reload(module):
    if module in sys.modules:
        importlib.reload(sys.modules[module])
reload("qtheme")
from qtheme import theme

colors = theme.Nord

# Image used in bar
img = "~/.config/qtile/arch.png"

# Widget documentation -> see http://docs.qtile.org/en/latest/manual/ref/widgets.


def sep():
    return widget.Spacer(
        length=1,
    )

def grox():
    return widget.GroupBox(
                    background=colors[5],
                    active=colors[0],
                    inactive=colors[3],
                    this_current_screen_border=colors[4],
                    this_screen_border=colors[4],
                    #Other Screen
                    other_current_screen_border=colors[1],
                    other_screen_border=colors[1],
                    highlight_method='line',
                    highlight_color=[colors[5]],
                    use_mouse_wheel=False,
                    hide_unused=True,
                    disable_drag=True,

                )

def _theme():
    bleh = qtile.cmd_screens()
    #screens[0].bar["top"].opacity = 0.25
    f = open("text", "w")
    f.write(str(bleh))
    f.close()

def barLeft():
    return bar.Bar(
            [

                #widget.TextBox(text="X", foreground=colors[0], background=colors[6], fontsize=33,
                #               mouse_callbacks={
                #                   "Button1": _theme
                #               }),
                widget.Clock(foreground=colors[0], background=colors[6], format="%Y-%m-%d %a %I:%M %p"),
                widget.TextBox(text=" ⏲", foreground=colors[0], background=colors[6], fontsize=18),
                widget.Systray(foreground=colors[0], background=colors[6]),
                widget.TextBox(text = "    ", padding = 0, foreground = colors[0], background=colors[6],
                               mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                               ),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[6]),
                widget.TextBox(text="\ue0b2", fontsize=45, padding=0, foreground=colors[7], background=colors[5]),
                widget.WindowTabs(foreground=colors[5], fontsize=18),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[7]),
                grox(),
                widget.TextBox(text="\ue0b2", fontsize=45, padding=0, foreground=colors[6], background=colors[5]),
                widget.CurrentLayout(
                    foreground=colors[0], background=colors[6],
                ),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[6]),
                widget.Spacer(length=1, background=colors[5]),
                widget.Image(filename = img, scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=2, background=colors[5]),

            ],
            25,
            background = colors[6],
            margin=[1, 1, 1, 1], # Space around bar as int or list of ints [N E S W].
            opacity = 1, # Bar Opacity
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        )

def barRight():
    return bar.Bar(
            [
                widget.Spacer(length=1, background=colors[5]),
                widget.Image(filename = img,scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=2, background=colors[5]),
                widget.TextBox(text=" ", fontsize=45, padding=-8, foreground=colors[5], background=colors[6]),
                widget.CurrentLayout(
                    foreground=colors[0], background=colors[6],
                ),
                widget.TextBox(text=" ", fontsize=45, padding=-8, foreground=colors[6], background=colors[5]),
                grox(),
                widget.TextBox(text=" ", fontsize=45, padding=-8, foreground=colors[5], background=colors[7]),
                widget.WindowTabs(foreground=colors[5]),
                widget.TextBox(text="\ue0b0", fontsize=45, padding=0, foreground=colors[7], background=colors[6]),
                widget.OpenWeather(foreground=colors[0], background=colors[6],
                                   zip=55901),
                widget.TextBox(text="\ue0b0", fontsize=45, padding=0, foreground=colors[6], background=colors[5]),
                widget.Mpris2( background=colors[5],
                              foreground=colors[0],
                              name="spotify",
                              stop_pause_text="Music - Paused", scroll_chars=None,
                              display_metadata=["xesam:title", "xesam:artist"],
                              objname="org.mpris.MediaPlayer2.spotify",
                              ),
                widget.TextBox(text="\ue0b0", fontsize=45, padding=0, foreground=colors[5], background=colors[6]),
                widget.TextBox(text=" ⏲", foreground=colors[0], background=colors[6], fontsize=18),
                widget.Clock(foreground=colors[0], background=colors[6], format="%Y-%m-%d %a %I:%M %p"),
            ],
            20,
            background = colors[6],
            margin=[1, 1, 1, 1], # Space around bar as int or list of ints [N E S W].
            opacity = 1, # Bar Opacity
       )



screens = [
    #left screen
    Screen(
        top=barLeft()
    ),
    #screen 2
    Screen(
        top=barRight()
    ),
]

