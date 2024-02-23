#!/usr/bin/env python
import argparse
import subprocess
from pathlib import Path
from sys import exit

TEXT_EDITORS = ['nano', 'vim', 'emacs', 'vi']
text_editor: str

def Main():
	filepath = SetFilePath()
	if args.shebang != None:
		filepath.write_text("#!/usr/bin/%s" % (args.shebang))
	else:
		filepath.touch()

	subprocess.check_call(['chmod', '+x', filepath])

	if args.no_editor:
		print("Script %s created at: %s" % (args.filename, filepath))
		exit(0)

	OpenEditor(filepath)

def OpenEditor(file_path):
	for editor in TEXT_EDITORS:
		if CheckCommand(editor):
			subprocess.call([editor, file_path])
			exit(0)
		else:
			print('uh... you either have a really obscure text editor (which, in that case... good for you, Arch user) or you don\'t have ANY text editors... which is impressive, to say the least.\n\n[ERROR] Install a text editor\n')
			exit(1)

def CheckCommand(command) -> bool:
	try:
		subprocess.check_call(['which', command], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
		return True
	except subprocess.CalledProcessError:
		return False

def SetFilePath() -> Path:
	if args.output != None:
		if Path(args.output).is_dir():
			return Path("%s/%s" % (args.output, args.filename))
		print('[WARNING]: Output path invalid; using default output path ($HOME/bin or the current working directory if $HOME/bin does not exist)')
	user_bin = Path("%s/bin" % (Path.home()))
	if user_bin.is_dir():
		return Path("%s/bin/%s" % (Path.home(), args.filename))
	return Path.cwd()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='shcript')
	parser.add_argument('-z', '--zsh', action='store_const', const='zsh', dest='shebang', help='shortcut flag for adding a zsh shebang')
	parser.add_argument('-b', '--bash', action='store_const', const='bash', dest='shebang', help='shortcut flag for adding a bash shebang')
	parser.add_argument('-s', '--bourne', action='store_const', const='sh', dest='shebang', help='shortcut flag for adding a bourne shell shebang (godspeed, soldier)')
	parser.add_argument('--no-editor', action='store_true', dest='no_editor', help='create the script without opening it in a text editor')
	parser.add_argument('--editor', type=str, help='specify the text editor to open the newly created script in. The default editors are, in order of importance: Nano->Vim->Emacs->Vi')
	parser.add_argument('--shebang', type=str, dest='shebang', help='Adds a custom shebang at the top of the script. Only the interpreter name is needed, not the full path (i.e: "zsh" instead of "/usr/bin/zsh"). If the shebang ends with "env <interpreter>", make sure to use quotation marks (i.e: --shebang "env python")')
	parser.add_argument('--output', help='the output path of the new script (default: "$HOME/bin" if it exists, otherwise "./")')
	parser.add_argument('filename', type=str, help='the name of the new script')
	args = parser.parse_args()

	exit(Main())
