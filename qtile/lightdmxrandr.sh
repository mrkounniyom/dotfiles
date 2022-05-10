#!/usr/bin/env bash

xrandr --auto --output HDMI-A-0 --mode 2560x1440
xrandr --auto --output DisplayPort-1 --mode 3840x2160 --right-of HDMI-A-0
