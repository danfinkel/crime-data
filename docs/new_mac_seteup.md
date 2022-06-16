# Steps for Setting Up New Mac

## Download iterm2
See www.iterm2.com

## Change default shell from zsh to bash
Start up iterm2, go to Preferences and Profiles. Under the command header enter `/bin/bash` for Send Text as Start

## Download and install Homebrew
go to www.homebrew.com

## Install python
```
brew install python
```

Add `alias python=/usr/local/bin/python3.9` to .bashrc

## Install Java8
```
brew tap homebrew/cask-versions
brew install --cask homebrew/cask-versions/adoptopenjdk8
```

Confirm Java 8 is active as follows:
```
java -version

openjdk version "1.8.0_292"
OpenJDK Runtime Environment (AdoptOpenJDK)(build 1.8.0_292-b10)
OpenJDK 64-Bit Server VM (AdoptOpenJDK)(build 25.292-b10, mixed mode)
```

## Install git
`brew install git`

## Install postgres
`brew install postgres`

## Install venv
```
brew install pyenv pyenv-virtualenv

cat << 'EOM' > ~/.pyenv_init
# --pyenv initialization
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
# So sub-shells in bash can see the pyenv function
export -f pyenv
EOM

echo "source ~/.pyenv_init" >> ~/.bash_profile

source ~/.bash_profile

pyenv install 3.9.7

pyenv virtualenv 3.9.7 my-venv-3.9.7 
```