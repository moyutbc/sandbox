# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !


# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi


# Put your fun stuff here.

function dic() {
  grep $1 /home/chronos/user/.dic/gene-utf8.txt -A 1 -wi --color
}

# alias
alias j='jobs -l'
alias f='fg'
alias fg1='fg 1'
alias fg2='fg 2'
alias fg3='fg 3'
alias pdb='python3 -m pdb'
alias vim='/usr/local/work/github-clone/vim/src/vim'


# login directory
cd /usr/local/work

# Linuxbrew
export prefix=/usr/local/linuxbrew
export HOMEBREW_TEMP=$prefix/tmp
PATH="$prefix/bin:$prefix/sbin:$PATH"

# local bash
# /usr/local/bin/bash
PS1='\[\e[1;33m\]\u \[\e[1;32m\]\W \[\e[0;37m\]$ '
SHELL=/usr/local/bin/bash

## Virtualenvwrapper
if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh 
fi

PATH="/home/chronos/user/perl5/bin${PATH:+:${PATH}}"; export PATH;
PERL5LIB="/home/chronos/user/perl5/lib/perl5${PERL5LIB:+:${PERL5LIB}}"; export PERL5LIB;
PERL_LOCAL_LIB_ROOT="/home/chronos/user/perl5${PERL_LOCAL_LIB_ROOT:+:${PERL_LOCAL_LIB_ROOT}}"; export PERL_LOCAL_LIB_ROOT;
PERL_MB_OPT="--install_base \"/home/chronos/user/perl5\""; export PERL_MB_OPT;
PERL_MM_OPT="INSTALL_BASE=/home/chronos/user/perl5"; export PERL_MM_OPT;
