# Added path in ~/.bashrc

# pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/>
echo 'eval "$(pyenv init -)"' >> ~/.profile
