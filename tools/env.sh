MYPWD="command -p pwd"
tools_dir=$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && $MYPWD)
project_dir=$(cd -P $tools_dir/.. && $MYPWD)

export CRIME=$project_dir

alias crime="cd $CRIME"
