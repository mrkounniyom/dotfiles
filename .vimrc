set nocompatible

" PLugins
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" " alternatively, pass a path where Vundle should install plugins
"
" " let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'whatyouhide/vim-gotham'


"All of your Plugins must be added before the following line
call vundle#end()            " required



filetype plugin indent on 

" syntax highlighting
syntax enable

" General Settings
set number				" show line numbers
set cursorline			" highlight cursor line underneath cursor horizontally
set noswapfile			" No swap
set nobackup			" no auto backups 
set path+=**			" Searches current dir recursively
set t_Co=256			" Set term supports 256
set showmatch			" Show matching brackets
set linebreak
set ignorecase			" case insensitive matching
set smartcase			" smart case matching
set mouse=a				" enable mouse
set shiftwidth=4		" tab == 4
set tabstop=4			" tab == 4
set softtabstop=4
set spelllang=en_us		" def lang for spell check
set showmode			" Show current mode
let NERDTreeQuitOnOpen=1	" Auto CLose NerdTree
let NERDTreeShowHidden=1	" Auto Show Hidden

" Enable auto completion menu after pressing TAB.
set wildmenu
" " Make wildmenu behave like similar to Bash completion.
set wildmode=list:longest
" " There are certain files that we would never want to edit with Vim.
" " Wildmenu will ignore files with these extensions.
set wildignore=*.docx,*.jpg,*.png,*.gif,*.pdf,*.pyc,*.exe,*.flv,*.img,*.xlsx

" Styling 
highlight Comment cterm=italic
highlight CursorLine ctermbg=Black cterm=NONE
highlight CursorLineNr ctermbg=Black cterm=bold ctermfg=Yellow

highlight SpellBad ctermbg=Red ctermfg=Yellow
highlight SpellCap cterm=NONE ctermbg=NONE
highlight SpellRare cterm=NONE ctermbg=NONE
highlight SpellLocal cterm=NONE ctermbg=NONE

" STATUS LINE ------------------------------------------------------------ {{{
"
" " Clear status line when vimrc is reloaded.
set statusline=
"
" " Status line left side.
set statusline+=\ %F\ %M\ %Y\ %R
"
" " Use a divider to separate the left side from the right side.
set statusline+=%=
"
" " Status line right side.
set statusline+=\ ascii:\ %b\ hex:\ 0x%B\ row:\ %l\ col:\ %c\ percent:\ %p%%
"
" " Show the status on the second to last line.
set laststatus=2
"
" " }}}
" start NERDTree and put the cursor back in the other window.
" autocmd VimEnter * NERDTree | wincmd p

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists('s:std_in') | NERDTree | endif
