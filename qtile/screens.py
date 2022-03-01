#!/usr/bin/env python

import os
from libqtile import bar, widget
from libqtile.config import Screen
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


screens = [
    #left screen
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=2, background=colors[5]),
                widget.Image(filename = "~/.config/qtile/arch.png",scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=10),
                widget.CurrentLayout(
                    foreground=colors[0],
                ),
                widget.GroupBox(
                    background=colors[5],
                    active=colors[0],
                    inactive=colors[3],
                    this_current_screen_border=colors[4],
                    this_screen_border=colors[4],
                    #Other Screen
                    other_current_screen_border=colors[1],
                    other_screen_border=colors[1],
                    highlight_method='block',
                    use_mouse_wheel=False,
                    hide_unused=True,
                ),
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground=colors[0]),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox(text = "    ", padding = 0, foreground = colors[0],
                               mouse_callbacks = {'Button1': lazy.spawn('pavucontrol')},
                               ),
                widget.Systray(
                    foreground=colors[0],
                ),
                widget.Clock(foreground=colors[0],format="%Y-%m-%d %a %I:%M %p"),
                widget.Spacer(length=10),

            ],
            20,
            background = colors[6],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
    #screen 2
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(length=2, background=colors[5]),
                widget.Image(filename = "~/.config/qtile/arch.png",scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=10),
                widget.CurrentLayout(
                    foreground=colors[0],
                ),
                widget.GroupBox(
                    background=colors[5],
                    active=colors[0],
                    inactive=colors[3],
                    this_current_screen_border=colors[4],
                    this_screen_border=colors[4],
                    #Other Screen
                    other_current_screen_border=colors[1],
                    other_screen_border=colors[1],
                    highlight_method='block',
                    use_mouse_wheel=False,
                    hide_unused=True,
                ),
                #widget.WindowName(),
                widget.Spacer(length=5),
                widget.WindowTabs(foreground=colors[0]),
                widget.Clock(foreground=colors[0], format="%Y-%m-%d %a %I:%M %p"),
                widget.Spacer(length=10),

            ],
            20,
            background = colors[6],
        )
    ),
]
