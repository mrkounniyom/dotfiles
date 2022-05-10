#!/usr/bin/env bash

# Terminate already running bar instances
# If all your bars have ipc enabled, you can use
# polybar-msg cmd quit
# Otherwise you can use the nuclear option:
killall -q polybar

polybar --config=~/.config/polybar/config2.ini i3-one &
#polybar --config=~/.config/polybar/config2.ini i3-two &

echo "Bars launched..."
