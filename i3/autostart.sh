#!/bin/sh



# compositor
killall picom
while pgrep -u $UID -x picom >/dev/null; do sleep 1; done
picom --experimental-backends --vsync &

#~/.config/i3/polybar/launch.sh &

killall pasystray
pasystray &
killall spotifyd
~/.cargo/bin/spotifyd &

#bg
nitrogen --random ~/wallpapers --set-scaled
#~/.fehbg &
#clipmenud &
dunst &
~/scripts/autotiling &
nm-applet &
discord &
emacs --daemon & 

