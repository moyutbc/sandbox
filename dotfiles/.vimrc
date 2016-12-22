"----------------------------------------
" tabline
"----------------------------------------
set showtabline=2 

"----------------------------------------
" beep
"----------------------------------------
set visualbell

"----------------------------------------
" tab
"----------------------------------------
set shiftwidth=4
set expandtab
set softtabstop=4

"----------------------------------------
" backspace
"----------------------------------------
set backspace=indent,eol,start

"----------------------------------------
" colorsheme
"----------------------------------------
syntax on
colorscheme molokai
set t_Co=256

"----------------------------------------
" show search result with hightlight
"----------------------------------------
set hlsearch

"----------------------------------------
" key bindings
"----------------------------------------
" window operation 
noremap Wh <C-w>h
noremap Wj <C-w>j
noremap Wk <C-w>k
noremap Wl <C-w>l
noremap W_ <C-w>_
noremap W\| <C-w>\|
noremap W+ <C-w>+
noremap W- <C-w>-
noremap W< <C-w><
noremap W> <C-w>>
" cursor
inoremap <C-j> <Down>
inoremap <C-k> <Up>
inoremap <C-h> <Left>
inoremap <C-l> <Right>
 
" esc
inoremap <silent>jj <ESC>
inoremap <C-[> <ESC>

" noh
noremap <ESC><ESC> :noh<LF>

"----------------------------------------
" open quickfix-window for show grep result 
"----------------------------------------
autocmd QuickfixCmdPost grep,vimgrep,make,bash if len(getqflist()) != 0 | copen | endif

"----------------------------------------
" path 
"----------------------------------------
set path+=/usr/local/include

"----------------------------------------
" NeoBundle
"----------------------------------------
" Note: Skip initialization for vim-tiny or vim-small.
if 0 | endif

if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath^=~/.vim/bundle/neobundle.vim/

" Required:
call neobundle#begin(expand('~/.vim/bundle/'))

" Let NeoBundle manage NeoBundle
" Required:
NeoBundleFetch 'Shougo/neobundle.vim'

" My Bundles here:
" Refer to |:NeoBundle-examples|.
" Note: You don't set neobundle setting in .gvimrc!
NeoBundle 'tyru/skk.vim'
NeoBundle 'Shougo/unite.vim'
NeoBundle 'h1mesuke/unite-outline'
NeoBundle 'itchyny/lightline.vim'

call neobundle#end()

" Required:
filetype plugin indent on

" If there are uninstalled bundles found on startup,
" this will conveniently prompt you to install them.
NeoBundleCheck

"----------------------------------------
" NeoBundle
"----------------------------------------
let skk_jisyo = '/home/chronos/user/.vim/skk-dic/.skk-jisyo'
let skk_large_jisyo = '/home/chronos/user/.vim/skk-dic/SKK-JISYO.L'
let skk_auto_save_jisyo	= 1
let skk_keep_state = 1
let skk_initial_mode = 1
