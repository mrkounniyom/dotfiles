#!/usr/bin/env bash

/usr/bin/emacs --daemon &
xrandr --auto --output HDMI-A-0 --mode 2560x1440
xrandr --auto --output DisplayPort-1 --mode 3840x2160 --right-of HDMI-A-0
nitrogen --head=0 --set-scaled --random ~/wallpapers/
nitrogen --head=1 --set-scaled --random ~/wallpapers/
#xfce4-power-manager &
steam &
discord &
picom -bf --experimental-backend &
xrandr --dpi 140
xrdb /home/mk/.Xresources
