TEXT_ERROR="\033[31;1m"
TEXT_RESET="\033[0m"
USER_HOME="$HOME/bin"
DEFAULT_EDITORS=('nano' 'vim' 'emacs' 'vi')
TEXT_EDITOR=""
SHEBANG=""

function Help()
{
	cat <<- EOF | fmt -s
		Usage: shcript [OPTIONS] [SHEBANG] {filename|filepath}
		Creates a new executable shell script and opens it in a text editor.

		FILENAME|FILEPATH:
		      Input either the name or the full path of your new script. The default path is either the current working directory or the ~/bin/ directory if it exists.

		OPTIONS:
		      -h, --help              Display help
		      -e, --editor <editor>   Specify the text editor

		SHEBANG:
		      Adds a shebang to the top of the script.

		      -z, --zsh
		      -b, --bash
		      -s, --bourne
		      -f, --fish
		      -d, --dash
		      -k, --korn
		      -w, --pwsh
		      -p, --python
		      -n, --node
		          --shebang <["env-"]program>      Set a custom shebang (see examples below)

		SHEBANG EXAMPLES:
		      [OPTION]                [RESULT]
		      -z                      #!/usr/bin/zsh
		      --bash                  #!/usr/bin/bash
		      --shebang bash          #!/usr/bin/bash
		      --shebang env-python    #!/usr/bin/env python
		      --shebang env-fish      #!/usr/bin/env fish
	EOF
}

function SetShebang()
{
	SHEBANG="#!/usr/bin/$1"
}

function GetOptions()
{
	got_options=$(getopt --long "help,editor:,zsh,bash,fish,dash,bourne,korn,pwsh,python,node,shebang:" -o "he:zbfdskwpn" -- "$@")
	eval set -- "$got_options"

	while true
	do
		case $1 in
			-h|--help)
				Help
				exit 0
				;;
			-e|--editor)
				shift
				TEXT_EDITOR="/usr/bin/$1"
				;;
			-z|--zsh)
				echo 'zsh'
				SetShebang "zsh"
				;;
			-b|--bash)
				SetShebang "bash"
				;;
			-s|--bourne)
				SetShebang "sh"
				;;
			-f|--fish)
				SetShebang "env fish"
				;;
			-d|--dash)
				SetShebang "dash"
				;;
			-k|--korn)
				SetShebang "korn"
				;;
			-w|--pwsh)
				SetShebang "pwsh"
				;;
			-p|--python)
				SetShebang "env python"
				;;
			-n|--node)
				SetShebang "env node"
				;;
			--shebang)
				shift
				length=${#1}
				[[ "${1:0:4}" == "env-" ]] && SetShebang "env ${1:4:$length}" || SetShebang "$1"
				;;
			--)
				shift
				break;;
			*)
				Help
				printf "\n\n${TEXT_ERROR}[ERROR]${TEXT_RESET} One or more options were incorrectly formatted (probably)\n" | fmt -s
				exit 1
				;;
		esac
		shift
	done

	if [[ -z $1 ]]; then
		Help
		printf "\n\n${TEXT_ERROR}[ERROR]${TEXT_RESET} File name missing!\n" | fmt -s
		exit 1
	fi
}

function GetEditor()
{
	if [[ -n $TEXT_EDITOR ]]; then
		type $TEXT_EDITOR >/dev/null 2>&1 && return 0
	fi

	for editor in "${DEFAULT_EDITORS[@]}"; do
		type $editor >/dev/null && TEXT_EDITOR="/usr/bin/$editor" && return 0
	done

	Help

	printf "\n\n${TEXT_RESET}uh... you either have a really obscure text editor (which, in that case... good for you, Arch user) or you don't have ${TEXT_ERROR}ANY${TEXT_RESET} text editors... which is impressive, to say the least.\n\n${TEXT_ERROR}[ERROR]${TEXT_RESET} Install a text editor\n" | fmt -s
	exit 1
}


GetOptions $@
GetEditor

for last; do true; done
FILEPATH="${USER_HOME:-$(pwd)}/$last"

echo $SHEBANG > $FILEPATH
chmod +x $FILEPATH
$TEXT_EDITOR $FILEPATH