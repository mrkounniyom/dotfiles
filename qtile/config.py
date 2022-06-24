"""
QTILE Configuration file. Qtile => docs.qtile.org

Qtile is a window manager for linux written in python.
"""

#
# Import Section
#
import libqtile
import os
import subprocess
import qtheme
#
# Globals
#
mod = "mod4"
terminal = "alacritty"
browser = "brave-browser"
colors = qtheme.doom_one
vanity_gaps=4
single_gap=0

widget_defaults = dict(
    font="JetBrains Mono",
    fontsize=10,
    padding=3,
    background=colors['bg']
)
libqtile.extension_defaults = widget_defaults.copy()
#
# Keys
#
keys = [
    # Movement
    libqtile.config.Key([mod], 'Left', libqtile.lazy.lazy.layout.left(), 'move focus left'),
    libqtile.config.Key([mod], 'Right', libqtile.lazy.lazy.layout.right(), 'move focus right'),
    libqtile.config.Key([mod], 'Up', libqtile.lazy.lazy.layout.up(), 'move focus up'),
    libqtile.config.Key([mod], 'Down', libqtile.lazy.lazy.layout.down(), 'move focus down'),
    libqtile.config.Key([mod, 'shift'], 'Left', libqtile.lazy.lazy.layout.shuffle_left(), 'move window left'),
    libqtile.config.Key([mod, 'shift'], 'Right', libqtile.lazy.lazy.layout.shuffle_right(), 'move window right'),
    libqtile.config.Key([mod, 'shift'], 'Up', libqtile.lazy.lazy.layout.shuffle_up(), 'move window up'),
    libqtile.config.Key([mod, 'shift'], 'Down', libqtile.lazy.lazy.layout.shuffle_down(), 'move window down'),
    libqtile.config.Key(['mod1', 'control'], 'Right', libqtile.lazy.lazy.screen.next_group(skip_empty=True, skip_managed=True), 'Switch to group to the right'),
    libqtile.config.Key([mod], 'Tab', libqtile.lazy.lazy.screen.next_group(skip_empty=True), 'Switch to group to the right'),
    libqtile.config.Key(['mod1', 'control'], 'Left', libqtile.lazy.lazy.screen.prev_group(skip_empty=True, skip_managed=True), 'Switch to group to the left'),
    # Apps/Wm stuff
    libqtile.config.Key([mod], 'q', libqtile.lazy.lazy.window.kill(), 'Quit window'),
    libqtile.config.Key([mod, 'shift'], 'r', libqtile.lazy.lazy.reload_config(), 'Reload Configuration file'),
    libqtile.config.Key([mod, 'shift'], 'q', libqtile.lazy.lazy.shutdown(), 'Quit qtile'),
    libqtile.config.Key([mod], 'Return', libqtile.lazy.lazy.spawn(terminal), 'launch term'),
    libqtile.config.Key([mod], 'w', libqtile.lazy.lazy.next_screen(), 'Change Screens'),
    libqtile.config.Key([mod], 'r', libqtile.lazy.lazy.spawn('rofi -modi window,run,drun,combi -show run -sidebar-mode'), 'Spawn a command prompt widget'),
    #libqtile.config.Key([mod], 'b', libqtile.lazy.lazy.spawn(browser), 'Spawn browser'),
    libqtile.config.Key([mod], 'e', libqtile.lazy.lazy.spawn('emacsclient -nc -a \'emacs\''), 'Spawn emacs``'),
    libqtile.config.Key([mod], 'f', libqtile.lazy.lazy.window.toggle_fullscreen()),
    libqtile.config.Key([mod], 't', libqtile.lazy.lazy.window.toggle_floating()),
    libqtile.config.Key([mod], 'l', libqtile.lazy.lazy.spawn('dm-tool lock'), 'screen lock'),
    libqtile.config.Key([mod], 'F8', libqtile.lazy.lazy.spawn('xrandr --output LVDS-1 --brightness 0.25'), 'Brightness 25'),
    libqtile.config.Key([mod], 'F9', libqtile.lazy.lazy.spawn('xrandr --output LVDS-1 --brightness 0.5'), 'Brightness 50'),
    libqtile.config.Key([mod], 'F10', libqtile.lazy.lazy.spawn('xrandr --output LVDS-1 --brightness 1'), 'Brightness 100'),

    # Layout stuff
    libqtile.config.Key([mod], "i", libqtile.lazy.lazy.layout.grow()),
    libqtile.config.Key([mod], "m", libqtile.lazy.lazy.layout.shrink()),
    libqtile.config.Key([mod], "o", libqtile.lazy.lazy.layout.maximize()),
]
#
# Autostart
#
@libqtile.hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
#
# Layouts
#
layouts = [
    libqtile.layout.MonadTall(
        border_focus=colors['brd'],
        margin=vanity_gaps,
        ratio=0.6
    )
]
#
# Screens
#
def sep():
    return libqtile.widget.Spacer(length=3)
screens=[
    libqtile.config.Screen(
        libqtile.bar.Bar(
            [
                libqtile.widget.Battery(
                    foreground=colors['bg'],
                    background=colors['fg']
                ),
                sep(),
                libqtile.widget.GroupBox(
                    background=colors['bg'],
                    active=colors['fg'],
                    highlight_method='block',
                    hide_unused=True,
                    this_current_screen_border=colors['active'],
                    block_highlight_text_color=colors['bg']
                ),
                sep(),
                libqtile.widget.WindowName(),
                libqtile.widget.DF(
                    foreground=colors['fg'],
                    parition='/',
                    format='{p} ({r:.0f}%/{s}{m})',
                    visible_on_warn=False
                ),
                libqtile.widget.Clock(
                    format='%m/%d/%y %I:%M %P'
                ),
                sep(),
                libqtile.widget.Systray(
                    background=colors['fg'],
                    foreground=colors['bg']
                ),
             ],
            18,
            margin=[4, 4, 0, 4],
            opacity=0.88,
            background=colors['bar']
        )
    )
]
#
# Groups
#
groups = [libqtile.config.Group("❶:DEV"),
          libqtile.config.Group("❷:WWW", matches=[libqtile.config.Match(wm_class=["brave-browser", "Brave-browser-beta"])]),
          libqtile.config.Group("❸:PWD", matches=[libqtile.config.Match(wm_class=["Bitwarden"])]),
          libqtile.config.Group("❹:FUN", matches=[libqtile.config.Match(wm_class=["steam", "Steam", "leagueclientux.exe"])]),
          libqtile.config.Group("❺:DOC"),
          libqtile.config.Group("❻:CHAT", matches=[libqtile.config.Match(wm_class=["discord"])]),
          libqtile.config.Group("❼:MUS", matches=[libqtile.config.Match(wm_class=["Spotify", "spotify", "deadbeef"])]),
          libqtile.config.Group("❽:VID"),
          libqtile.config.Group("❾:EMACS", matches=[libqtile.config.Match(wm_class=["emacs"])])]
tempNum = 1
for group in groups:
    if tempNum < 10:
        keys.extend(
            [
            libqtile.config.Key(
                [mod],
                str(tempNum),
                libqtile.lazy.lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            libqtile.config.Key([mod, "shift"],
                str(tempNum),
                libqtile.lazy.lazy.window.togroup(group.name),
                desc="move window to group {}".format(group.name),
            ),
            ]
            )
    tempNum += 1
#
# Mouse Related
#
mouse = [
    libqtile.config.Drag([mod], "Button1", libqtile.lazy.lazy.window.set_position_floating(), start=libqtile.lazy.lazy.window.get_position()),
    libqtile.config.Drag([mod], "Button3", libqtile.lazy.lazy.window.set_size_floating(), start=libqtile.lazy.lazy.window.get_size()),
    libqtile.config.Click([mod], "Button2", libqtile.lazy.lazy.window.bring_to_front()),
]
#
# Floating
#
libqtile.floating_layout = libqtile.layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *libqtile.layout.Floating.default_float_rules,
    ]
)
libqtile.auto_fullscreen = True
libqtile.focus_on_window_activation = "smart"
libqtile.reconfigure_screens = True
#
# WM_NAME
#
wmname='QTILE'
#
#
#
#
#
#
