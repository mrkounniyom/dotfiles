#  ___________________.___.____     ___________
#  \_____  \__    ___/|   |    |    \_   _____/
#   /  / \  \|    |   |   |    |     |    __)_
#  /   \_/.  \    |   |   |    |___  |        \
#  \_____\ \_/____|   |___|_______ \/_______  /
#         \__>                    \/        \/
#
# http://docs.qtile.org/en/latest/index.html
#

from typing import List  # noqa: F401
import subprocess, os, re, sys, importlib
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtheme import theme
from keys import keys

#config imports
def reload(module):
    if module in sys.modules:
        importlib.reload(sys.modules[module])

reload("keys")
from keys import keys
#reload("screens")
#from screens import screens
reload("qtheme")
from qtheme import theme


mod = "mod4"
alt = "mod1"
terminal = "alacritty"
# Sets theming from qtheme
colors = theme.Dracula
# Image used in bar
img = "~/.config/qtile/arch.png"


#groups = [Group(i) for i in "123456789"]
groups = [Group("➊:DEV"),
          Group("➋:WWW", matches=[Match(wm_class=["brave-browser", "Brave-Browser"])]),
          Group("➌:OBS", matches=[Match(wm_class=["obs"])]),
          Group("➍:FUN", matches=[Match(wm_class=["steam", "Steam", "leagueclientux.exe"])]),
          Group("➎:DOC"),
          Group("➏:CHAT", matches=[Match(wm_class=["discord"])]),
          Group("➐:MUS", matches=[Match(wm_class=["Spotify", "spotify", "deadbeef"])]),
          Group("➑:VID"),
          Group("➒:EMACS", matches=[Match(wm_class=["emacs"])]),
          Group("⓵:GEANY", matches=[Match(wm_class=["geany"])]),
          Group("⓶:FILES", matches=[Match(wm_class=["Thunar", "ranger"])]),
          Group("⓷:VM", matches=[Match(wm_class=["virt-manager"])]),
          Group("⓸:PWD", matches=[Match(wm_class=["bitwarden"])]),
          Group("⓹:?"),
          Group("⓺:?"),
          Group("⓻:?"),
          Group("⓼:?"),
          Group("⓽:?"),

          ]
#from libqtile.dgroups import simple_key_binder
#dgroups_key_binder = simple_key_binder("mod4")

tempNum = 1
#f = open("test.txt", "x")
for group in groups:
    #f.write(group.name)
    #f.write(" " + str(tempNum) + " - ")
    if tempNum < 10:
        keys.extend(
            [
            Key(
                [mod],
                str(tempNum),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key([mod, "shift"],
                str(tempNum),
                lazy.window.togroup(group.name),
                desc="move window to group {}".format(group.name),
            ),
            ]
            )
    else:
 #       break;
        keys.extend(
            [
            Key(
                [mod, alt],
                str(tempNum-9),
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            Key([mod, alt, "shift"],
                str(tempNum-9),
                lazy.window.togroup(group.name),
                desc="move window to group {}".format(group.name),
            ),

            ]
        )

    tempNum += 1
#f.close()

margin_size=5
single_size=3

layouts = [
    layout.MonadTall(
        border_focus=colors[4],
        margin=margin_size,
        single_margin=single_size,
                    ),
    layout.RatioTile(
        border_focus=colors[4],
        margin=margin_size,
        single_margin=single_size,
                     ),
    layout.Tile(border_focus=colors[4],
        margin=margin_size,
        single_margin=single_size,
                ),
]

widget_defaults = dict(
    font="mononoki Nerd Font",
    fontsize=12,
    padding=3,
    background=colors[7]
)
extension_defaults = widget_defaults.copy()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", start=lazy.window.get_position()),
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

#  __________
#  \______   \_____ _______
#   |    |  _/\__  \\_  __ \
#   |    |   \ / __ \|  | \/
#   |______  /(____  /__|
#          \/      \/

# Widget documentation -> see http://docs.qtile.org/en/latest/manual/ref/widgets.


def sep():
    return widget.Spacer(
        length=1,
    )

def grox(fontsize):
    return widget.GroupBox(
					foreground=colors[2],
                    background=colors[5],
                    active=colors[0],
                    inactive=colors[7],
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
                    fontsize=fontsize

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
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[7], background=colors[6]),
                widget.WindowTabs(foreground=colors[5], fontsize=18),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[7]),
                grox(14),
                widget.TextBox(text="\ue0b2", fontsize=45, padding=0, foreground=colors[6], background=colors[5]),
                widget.CurrentLayout(
                    foreground=colors[0], background=colors[6],
                ),
                widget.TextBox(text="\ue0b2", fontsize=60, padding=0, foreground=colors[5], background=colors[6]),
                widget.Spacer(length=1, background=colors[5]),
                widget.Image(margin = 2, filename = img, scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
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
    fontsize = 24
    return bar.Bar(
            [
                widget.Spacer(length=2, background=colors[5]),
                widget.Image(margin=2, filename = img,scale = True, background=colors[5], mouse_callbacks = {'Button1': lazy.spawn("rofi -show drun")}),
                widget.Spacer(length=2, background=colors[5]),
                widget.TextBox(text=" ", fontsize=45+fontsize, padding=-8, foreground=colors[5], background=colors[6]),
                widget.CurrentLayout(fontsize=fontsize,
                    foreground=colors[0], background=colors[6],
                ),
                widget.TextBox(text=" ", fontsize=45+fontsize, padding=-8, foreground=colors[6], background=colors[5]),
                grox(fontsize),
                widget.TextBox(text=" ", fontsize=45+fontsize, padding=-8, foreground=colors[5], background=colors[7]),
                widget.WindowTabs(fontsize=fontsize, foreground=colors[5]),
                widget.TextBox(text="\ue0b0", fontsize=45+fontsize, padding=0, foreground=colors[7], background=colors[6]),
                widget.OpenWeather(fontsize=fontsize, foreground=colors[0], background=colors[6],
                                   zip=55901, padding=5, metric = False),
                widget.TextBox(text="\ue0b0", fontsize=45+fontsize, padding=0, foreground=colors[6], background=colors[5]),
                widget.Mpris2( fontsize=fontsize, background=colors[5],
                              foreground=colors[0],
                              name="spotify",
                              stop_pause_text="Music - Paused", scroll_chars=None,
                              display_metadata=["xesam:title", "xesam:artist"],
                              objname="org.mpris.MediaPlayer2.spotify",
                              ),
                widget.TextBox(text="\ue0b0", fontsize=45+fontsize, padding=0, foreground=colors[5], background=colors[6]),
                widget.TextBox(text=" ⏲", foreground=colors[0], background=colors[6], fontsize=18+fontsize),
                widget.Clock(foreground=colors[0], background=colors[6], format="%Y-%m-%d %a %I:%M %p", fontsize=fontsize),
                widget.Spacer(length=5, background=colors[6]),
            ],
            25+fontsize,
            background = colors[6],
            margin=[5, 5, 5, 5], # Space around bar as int or list of ints [N E S W].
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

###

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="Tk"),  # gitk
        Match(wm_class="tk"),  # gitk
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


wmname = "QTILE"
