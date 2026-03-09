#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# NVM is commented out for performance - uncomment only when needed
# export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
# [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
export PATH="/usr/bin:$PATH"

alias sd='shutdown -P now'
alias uvim='uv run nvim'
alias nv='nvim'
alias vpn='./vpn'
alias avim='nvim'
alias lvim='NVIM_APPNAME=lazyNvim nvim'
alias cvim='NVIM_APPNAME=customNvim nvim'

export GEMINI_API_KEY="AIzaSyAcEHkmspgzjYDzpEz_ToThiDbz3ygKVCM"
export ENABLE_DEPRECATED_SPECIAL_OUTBOUNDS=false
export TERMINAL=alacritty

export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
alias lnvim='NVIM_APPNAME=~/.config/lazynvim nvim'
