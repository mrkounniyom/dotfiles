#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

HISTCONTROL=ignoreboth:erasedups
HISTSIZE=1000
shopt -s histappend
export RANGER_LOAD_DEFAULT_RC=FALSE

if [ -f ~/.bashali ]; then
	source ~/.bashali
fi

_set_liveuser_PS1() {
    PS1='[\u@\h \W]\$ '
    if [ "$(whoami)" = "liveuser" ] ; then
        local iso_version="$(grep ^VERSION= /usr/lib/endeavouros-release 2>/dev/null | cut -d '=' -f 2)"
        if [ -n "$iso_version" ] ; then
            local prefix="eos-"
            local iso_info="$prefix$iso_version"
            PS1="[\u@$iso_info \W]\$ "
        fi
    fi
}
_set_liveuser_PS1
unset -f _set_liveuser_PS1

ShowInstallerIsoInfo() {
    local file=/usr/lib/endeavouros-release
    if [ -r $file ] ; then
        cat $file
    else
        echo "Sorry, installer ISO info is not available." >&2
    fi
}



[[ "$(whoami)" = "root" ]] && return

[[ -z "$FUNCNEST" ]] && export FUNCNEST=100          # limits recursive functions, see 'man bash'

## Use the up and down arrow keys for finding a command in history
## (you can write some initial letters of the command first).
bind '"\e[A":history-search-backward'
bind '"\e[B":history-search-forward'

################################################################################
## Some generally useful functions.
## Consider uncommenting aliases below to start using these functions.
##
## October 2021: removed many obsolete functions. If you still need them, please look at
## https://github.com/EndeavourOS-archive/EndeavourOS-archiso/raw/master/airootfs/etc/skel/.bashrc

_open_files_for_editing() {
    # Open any given document file(s) for editing (or just viewing).
    # Note1:
    #    - Do not use for executable files!
    # Note2:
    #    - Uses 'mime' bindings, so you may need to use
    #      e.g. a file manager to make proper file bindings.

    if [ -x /usr/bin/exo-open ] ; then
        echo "exo-open $@" >&2
        setsid exo-open "$@" >& /dev/null
        return
    fi
    if [ -x /usr/bin/xdg-open ] ; then
        for file in "$@" ; do
            echo "xdg-open $file" >&2
            setsid xdg-open "$file" >& /dev/null
        done
        return
    fi

    echo "$FUNCNAME: package 'xdg-utils' or 'exo' is required." >&2
}

#------------------------------------------------------------

## Aliases for the functions above.
## Uncomment an alias if you want to use it.
##

# alias ef='_open_files_for_editing'     # 'ef' opens given file(s) for editing
# alias pacdiff=eos-pacdiff
################################################################################

# Starship prompt
# ~/.bashrc
export PATH="$HOME/scripts:$HOME/.cargo/bin:$HOME/.emacs.d/bin:$HOME/Applications:/usr/sbin:$PATH"
export var=($RANDOM % 10)


# Colorful Man Pages
#export LESS_TERMCAP_mb=$'\e[1;32m' # enter blinking mode - red
#export LESS_TERMCAP_md=$'\e[1;35m' # enter double-bright mode - bold, magenta
#export LESS_TERMCAP_se=$'\e[0m'     # leave standout mode
#export LESS_TERMCAP_so=$'\e[01;33m' # enter standout mode - yellow
#export LESS_TERMCAP_ue=$'\e[0m'     # leave underline mode
#export LESS_TERMCAP_us=$'\e[1;4;36m' # enter underline mode - cyan

export PAGER="most"

if [ $var -gt 20000  ] ; then
	colorscript -r
else
	pokemon-colorscripts -r
fi
eval "$(starship init bash)"
