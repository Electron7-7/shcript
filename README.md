# shcript
### A shell command that makes shell commands!
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
