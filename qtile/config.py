# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# http://docs.qtile.org/en/latest/index.html
#

from typing import List  # noqa: F401
import subprocess, os, re, sys, importlib
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#config imports
def reload(module):
    if module in sys.modules:
        importlib.reload(sys.modules[module])

reload("keys")
from keys import keys
reload("screens")
from screens import screens

mod = "mod4"
alt = "mod1"
terminal = "alacritty"

colors = [
    "#161320", #Black 0
    "#D9E0EE", #White
    "#DDB6F2", #Mauve
    "#302D41", #Black 3
    "#ABE9B3", #Green
    "#F28FAD", #RED
    "#96CDFB", #Blue
]


#groups = [Group(i) for i in "123456789"]
groups = [Group("1:DEV"),
          Group("2:WWW", matches=[Match(wm_class=["brave-browser", "Brave-Browser"])]),
          Group("3:OBS", matches=[Match(wm_class=["obs"])]),
          Group("4:FUN", matches=[Match(wm_class=["steam", "Steam"])]),
          Group("5:DOC"),
          Group("6:CHAT", matches=[Match(wm_class=["discord"])]),
          Group("7:MUS", matches=[Match(wm_class=["Spotify", "spotify"])]),
          Group("8:VID"),
          Group("9:EDIT", matches=[Match(wm_class=["emacs", "geany"])])]
from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

margin_size=5
single_size=3

layouts = [
    #layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    layout.MonadTall(
        border_focus=colors[4],
        margin=margin_size,
        single_margin=single_size,
                    ),
    #layout.MonadWide(),
    layout.RatioTile(
        border_focus=colors[5],
        margin=margin_size,
        single_margin=single_size,
                     ),
    layout.Tile(border_focus=colors[5],
        margin=margin_size,
        single_margin=single_size,
                ),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

widget_defaults = dict(
    font="mononoki Nerd Font",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "QTILE"
