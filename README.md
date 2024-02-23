# shcript
### A shell command that makes shell commands!

###### (finally, no more "touch file; chmod +x file; $EDITOR file"!)

## Now a binary!
shcript is now a binary, programmed in python! I'll still include the original shell script but I highly reccomend using the binary instead as it's much more optimized.

### shcript
```
usage: shcript [-h] [-z] [-b] [-s] [--no-editor] [--editor EDITOR] [--shebang SHEBANG] [-o OUTPUT] filename

positional arguments:
  filename           the name of the new script

options:
  -h, --help         show this help message and exit
  -z, --zsh          shortcut flag for adding a zsh shebang
  -b, --bash         shortcut flag for adding a bash shebang
  -s, --bourne       shortcut flag for adding a bourne shell shebang (godspeed, soldier)
  --no-editor        create the script without opening it in a text editor
  --editor EDITOR    specify the text editor to open the newly created script in. The default editors are, in order of importance: Nano->Vim->Emacs->Vi
  --shebang SHEBANG  Adds a custom shebang at the top of the script. Only the interpreter name is needed, not the full path (i.e: "zsh" instead of "/usr/bin/zsh"). If the shebang ends with "env
                     <interpreter>", make sure to use quotation marks (i.e: --shebang "env python")
  --output OUTPUT          the output path of the new script (default: "$HOME/bin" if it exists, otherwise "./")
```
---
### shcript.sh
###### (P.S: I recommend removing the ".sh" extension from the script if you want to add it to your executables folder since it'll be a lot easier to type. I only added the extension so that GitHub would correctly categorize the project language as being "shell", lol).

```
Usage: shcript [OPTIONS] [SHEBANG] {filename|filepath}
Creates a new executable shell script and opens it in a text editor.

FILENAME|FILEPATH:
	Input either the name or the full path of your new script.
	The default path is either the current working directory
	or the ~/bin/ directory if it exists.

OPTIONS:
	-h, --help		Display help
	-e, --editor <editor>	Specify the text editor

SHEBANG:
	Add a shebang to the top of the script.
	-z, --zsh
	-b, --bash
	-s, --bourne
	-f, --fish
	-d, --dash
	-k, --korn
	-w, --pwsh
	-p, --python
	-n, --node
	    --shebang <["env-"]program>   Set a custom shebang (see examples below)

SHEBANG EXAMPLES:
	[OPTION]		[RESULT]
	-z			#!/usr/bin/zsh
	--bash			#!/usr/bin/bash
	--shebang bash		#!/usr/bin/bash
	--shebang env-python	#!/usr/bin/env python
	--shebang env-fish	#!/usr/bin/env fish
```
