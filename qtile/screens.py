#!/usr/bin/env python

import os, sys, platform
from libqtile import bar, widget
from libqtile.config import Screen, Group
from libqtile.lazy import lazy

colors = [
    "#161320", #Black 0
    "#D9E0EE", #White
    "#DDB6F2", #Mauve
    "#302D41", #Black 3
    "#ABE9B3", #Green
    "#F28FAD", #RED
    "#96CDFB", #Blue
]

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

                )


# Image used in bar
img = "~/.config/qtile/qtile3.png"

screens = [
    #left screen
    Screen(
        top=bar.Bar(
            [
                sep(),
                widget.Clock(foreground=colors[0],format="%Y-%m-%d %a %I:%M %p"),
                widget.TextBox(text=" ⏲", foreground=colors[0], fontsize=18),
                widget.Systray(foreground=colors[0]),
                widget.TextBox(text = "    ", padding = 0, foreground = colors[0],
                               mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                               ),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[6]),
                widget.Mpris2( background=colors[5],
                              foreground=colors[0],
                              name="spotify",
                              stop_pause_text="Music - Paused", scroll_chars=None,
                              display_metadata=["xesam:title", "xesam:artist"],
                              objname="org.mpris.MediaPlayer2.spotify",
                              ),
                widget.TextBox(text="\ue0b2", fontsize=45, padding=0, foreground=colors[6], background=colors[5]),
                widget.WindowTabs(foreground=colors[0], fontsize=18),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[6]),
                grox(),
                widget.TextBox(text="\ue0b2", fontsize=45, padding=0, foreground=colors[6], background=colors[5]),
                widget.CurrentLayout(
                    foreground=colors[0],
                ),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[6]),
                widget.Spacer(length=1, background=colors[5]),
                widget.Image(filename = img, scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=2, background=colors[5]),


            ],
            25,
            background = colors[6],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    #screen 2
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=1, background=colors[5]),
                widget.Image(filename = img,scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=2, background=colors[5]),
                widget.TextBox(text=" ", fontsize=45, padding=-8, foreground=colors[5], background=colors[6]),
                widget.CurrentLayout(
                    foreground=colors[0],
                ),
                widget.TextBox(text=" ", fontsize=45, padding=-8, foreground=colors[6], background=colors[5]),
                grox(),
                widget.TextBox(text=" ", fontsize=45, padding=-8, foreground=colors[5], background=colors[6]),
                widget.WindowTabs(foreground=colors[0]),
                widget.TextBox(text="\ue0b0", fontsize=45, padding=0, foreground=colors[6], background=colors[5]),
                widget.Mpris2( background=colors[5],
                              foreground=colors[0],
                              name="spotify",
                              stop_pause_text="Music - Paused", scroll_chars=None,
                              display_metadata=["xesam:title", "xesam:artist"],
                              objname="org.mpris.MediaPlayer2.spotify",
                              ),
                widget.TextBox(text="\ue0b0", fontsize=45, padding=0, foreground=colors[5], background=colors[6]),
                widget.TextBox(text=" ⏲", foreground=colors[0], fontsize=18),
                widget.Clock(foreground=colors[0], format="%Y-%m-%d %a %I:%M %p"),
                sep(),
            ],
            20,
            background = colors[6],
        )
    ),
]
