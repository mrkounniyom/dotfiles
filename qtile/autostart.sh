#!/bin/sh
killall picom
killall pasystray
killall spotifyd

while pgrep -u $UID -x picom >/dev/null; do sleep 1; done

picom --experimental-backends &

pulseaudio &

pasystray &
spotifyd &

nitrogen --random ~/wallpapers --set-scaled

dunst &
nm-applet &
#nmcli c up Home

emacs --daemon &

