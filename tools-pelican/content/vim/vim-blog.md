title: VIM Basics
authors: Ben Guthrie; Sebastien Lemaire
date: 2018-03-05
tags: vim, basics, training, editor
slug: vim-basics

# What is VIM?

**VIM** is a text editor with a relatively high learning curve, but many advantages. For example, **VIM** is ubiquitous - it is installed by default on almost all operating systems - as well as being highly configurable and efficient. It can be used for anything from quick text editing, to code writing as a fully functional, configurable IDE.


# Setting up the vim environment

**VIM** is installed by default on almost all machines. The training material used in this workshop can be found [https://gitlab.com/Nanoseb/feeg6003-vim](here).

If using the virtual machine:

Navitage to home directory
```vim
cd ~
```

Setup the environment
```py
goto_level 1
```

### NOTE:
This workshop contains very many commands. It is not expected that you will learn all of these commands by the end of the workshop - instead, it will serve as a "cheatsheet" to refer back to while using VIM. However, after a short time you will most likely find you remember all the commands you need.

# VIM Basics: Opening files, navigation, insert mode

## Opening and closing files

Create/open a file called **filename**
```vim
vim filename
```

Insert some text
```
i
[INSERT TEXT]
<ESC>
```
Close the file
```py
:wq # Save and exit (alternatively ZZ)
:q! # Discard changes
```

## Normal and Insert modes
**VIM** starts in normal mode. In this mode, you can navigate around the text, use commands, and edit text. Most of your time will be spent in this mode.

Insert mode allows inserting text, but nothing else. This mode can be entered in a number of ways:

```py
i # Insert before the cursor
a # Append after cursor
o # Insert on a new line below the cursor
```
```py
I # Insert at the end beginning of the line
A # Append to the end of the line
O # Insert on a new line above the cursor
```
Press `<ESC>` to return to normal mode.

## Navigation
All navigation is done using the keyboard, in normal mode.

| Command | Movement |
| :-- | :-- |
| `h`, `j`, `k`, `l` | Left, down, up, right |
| `w` | To the start of the next word |
| `W` | To the start of the next WORD |
| `e`, `E` | To the end of the next word / WORD |
| `b`, `B` | To the start of the previous word / WORD |
| `0`, `$` | To the start / end of the line |
| `(`, `)` | Forward / backward one sentence |
| `{`, `}` | Forward / backward one paragraph |
| `gg`, `G` | To the start / end of the file |

The difference between a word and a WORD is that the former only contains alphanumeric characters and underscores, while the latter includes everything up to the next whitespace.

# Commands and config files. 

Setup the environment
```vim
goto_level 2
```

## VIM Commands

**VIM** has many commands to enable efficient text editing. Some are rarely used, others will be used all the time. Commands can be formed by combining operators, in the form `verb` `modifier` `noun`. All commands must be entered in normal mode.
 
Some useful commands are the following:

|Verbs|Modifiers|Nouns|
|:--|:--|:--|
|`d`: *delete (and copy)* | `1`,`2`,`3`... | `s`: *sentence* |
|`c`: *change* | `i`: *inside* | `p`: *paragraph* |
|`y`: *yank (copy)* | `a`: *around* | `w`: *word* |
| | `t`: *to character* | `'`, `"`, `(`, `<`, ... |

To perform commands on a whole line:

   `dd`: *delete line*  
   `yy`: *copy line*  
   `C`: *change the line from the cursor position*  
   `S`: *change the entire line*  
   `5dd`: *delete 5 lines*  

Other useful commands:

   `x`: *delete the character under the cursor*  
   `r`: *replace the character under the cursor*  
   `u`, `Ctrl-r`: *undo / redo*  
   `p`: *paste after/below the cursor*  
   `P`: *paste before/above the cursor*  
   `.`: *repeat the last command*  

Some examples of combined commands:
```py
d2w # Delete 2 words
yis # Yank (copy) inside sentence
ct{character} # Change up to the next {character}
dW # delete (1) WORD
```

Many commands can also be preceded by a number - this will tell **VIM** to repeat the command N times. E.g.:
```py
30i* <ESC> # Insert 30 asterisks (*)
3p # Paste 3 times
```

#### You can now try the exercises in level 2


## Config file

The .vimrc file contains optional runtime configuration settings, such as key maps, customisation and plugin management.

For example, the following line allows you to use `jk` instead of `<ESC>` to return to normal mode. This tends to be more efficient since your hands don't need to leave the home keys.
```vim
inoremap jk <esc>
```

Feel free to look at the .vimrc files used in the different levels for an example of what they are used for.

For your own use, a recommended vim configuration can be found [https://gitlab.com/Nanoseb/feeg6003-vim/blob/master/level_5/.vimrc](here).

# More advanced navigation

```vim
goto_level 3
```
Trying to navigate a large file using the hjkl keys can feel slow and clunky, even using the navigation commands described earlier. Here we will introduce two ways to speed up navigation.

Firstly, modifiers can be placed before navigation commands, e.g.:
   
   `2w`: *Move forward two words*  
   `5l`: *Move right 5 characters*  

You can go to a specific line number by typing, e.g., `:10` or `10G` to go to line 10.

Finally, in **VIM** you can search for both characters and strings. When combined with **VIM** commands, this can enable rapid editing of an large file...

### Searching for characters

Search for closing bracket )
```python
t) # Jump up to )
f) # Jump onto )
; # (After searching) jump to the next occurance
```
The above commands can also be used as a noun in combined commands:
```python
ct) # Change all text up to the next )
```

These commands will work for any character, including alphanumeric characters.

### Searching for strings

This is more useful than character searching, and you will use it very regularly.

Search for all occurances of a certain string:
```python
/string # Find all occurances of string
* # Find all occurances of the word under the cursor
:%s/old/new/g # Replace all occurances of old with new
```
Jump between occurances of the string:
```python
n # Jump to next
N # Jump to previous
```

Searching can become particularly powerful when combined with the dot command.

#### Now try the exercises in level 3, and the **VIM** golf challenge - how many ways can you find to complete it?



# VISUAL mode

We have seen ==Normal== and ==Insert mode== previously, the Visual mode can be quite useful too, it deals with text selection. If you don't have a mouse, selecting text in a terminal is not easy, the ==VISUAL mode== is meant to make this accessible.

On a selected text you will be able to run commands and functions (copy, delete/cut, and more advanced functions)

## How does it works?

Enter in visual mode:

| Command | Definition |
|:--|:--|
| `v` | Character based selection |
| `V` | Whole line selection |
| `ctrl+v` | Block based selection |

The you can use displacement keystroke to expand the selection:
`h` `j` `k` `l`, `$` `0`, `(` `)`, `G` `gg` ...

Once you have your text selected use any of the command you already know to modify the text: `y`, `d`, `x`, `I` ...


#### You can now try the exercises in level 4

# Command line `:`

Functions can be run from a command prompt with `:`

### File opening
To open a new file without moving from your current vim instance:
- In the current window `:e path/to/file`
- In a new tab `:tabe path/to/file`

### Text `s`ubstitution

Text substitution is also quite useful, the syntax is simular to the command line tool `sed`.
```py
:s/old/new/    # act on the current line/selection
```
If one want to substitute every iteration on the line, `g` is needed like so:
```py
:s/old/new/g    # modify every 'old' of the line
```
To apply the substitution on the entire file, just add a `%` at the begining:
```py
:%s/old/new/g    # act on the entire file
```

VISUAL mode can also be used here, to apply a substitution only on the selected text.

### Run bash commands
**Vim** can run bash commands directly without leaving its interface, and act on the current file.

| Command | Definition |
|:--|:--|
|`:r ! bash_command` | add output of a bash command |
|`:! command `      | filter selection with command |

Here are a couple of examples:
```
:r ! ls 
:! sort          # alphabetical sort of lines (-R for random)
:! bc            # computes simple calculus using bc
```


#### Now try the exercises in level 5

# Plugins

**VIM** is a versatile text editor, you can expand its capabilities with plugins, 

Example of plugin:

- python pep8 check
- file broswer inside vim
- ctag view
- autocompletion
- anything else you can imagine ...

### Plugin manager

Plugin manager is preferable to easily install and remove them, [https://github.com/tpope/vim-pathogen](pathogen) is maybe the simplest one, it just needs 1 line in the `.vimrc`, and 1 file in `~/.vimautoload`

To install a plugin just copy its folder to `~/.vim/bundle`

### Plugin installation

You can give a try at installing the plugin presented today:

- First you can have a look at its structure/code: 
```
 cd headerplugin
 ls -R 
 vim -p plugin/*
```
- One liner installation:
```
cp -r headerplugin ~/.vim/bundle/headerplugin
```

Now open a file in vim and run the command `:WriteHeader` for example.

### Plugin selection
Some websites have quite extensive list of plugins like [https://vimawesome.com/](this one), here is just a small list of the one we use

- [github.com/scrooloose/nerdtree](NerdTree)
- [github.com/majutsushi/tagbar](Tagbar)
- [github.com/xtal8/traces.vim](Traces)
- [github.com/ervandew/supertab](Supertab)
- [github.com/vim-syntastic/syntastic](Syntastic)

#### To try these plugin you can run the level 6

- nerdtree: `[ctrl]+n`
- tagbar: `[ctrl]+t`
- supertab: `[tab]`
- headerplugin: `:WriteHeader`, `:ToggleComment`

# Further learning
The best way to learn **VIM** it is to actually use it, don't try to learn all the commands in one go by heart etc. just learn progressively, and expand your command vocabulary as you get use to the commands you already know.

same for you configuration file, don't start with a very huge configuration file copy/pasted from the internet, start with a couple of lines and add more as you want to expand the possibilities of **VIM**.

#### Games/interactive tutorials
To learn and play at the same time you can try the following sites

- [www.vim-adventures.com](Vim Adventures)
- [www.vimgolf.com](Vim Golf)
- [www.vimgenius.com](Vim Genius)

#### Documentation
More text based documentation:

- [www.vim.wikia.com](Vim Tips wiki)
- [www.vim.rtorr.com](Vim cheat sheet)
- [www.danielmiessler.com/study/vim](A more complete tutorial)

#### Things we didn't talk about
There is way more things to discover with vim, here is a keyword list of things you can google to know more: vimdiff, buffer, vimscript, split window, modeline, spellcheck, macro, folding, markers...


# Bonus: 
## Vim keybinding everywhere else
It is not because you can't use vim directly that you can't benefit from its keybinding, most text editor have a **VIM** plugin that mimic **VIM** behaviour. Same web browser with vim plugin can be quite useful for a mouse less surfing. 

Here is a small list of plugin:

- Firefox/chrome: ==vimium==
- Eclipse: ==vimwarp==
- Sublime: ==actualvim==
- atom: ==vim-mode-plus==
- Visual studio: ==vsvim==
- Evince: `hjkl` works by default

