# python-api-practice
Rest API Practice with Python

# Reference page
[Django REST Frameworkを使って爆速でAPIを実装する](https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8)  
[Django REST framework with Vue.js](https://qiita.com/yuuki_1204_/items/d892aa0ba935a1ac7594)  

## Setting
- VS Code with Python  
[Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites)  

[Visual Studio CodeでPython開発環境を整える](https://qiita.com/84zume/items/27d143f529396c9fa1cc)  

- Pyenv, Pypenv  
[2018年のPythonプロジェクトのはじめかた](https://qiita.com/sl2/items/1e503952b9506a0539ea)  
[Pyenv, Pipenvを利用したプロジェクト構築](https://www.wakuwakubank.com/posts/255-python-pipenv-pyenv/)  
[pyenv-virtualenvでディレクトリ単位のpython環境構築](https://qiita.com/niwak2/items/5490607be32202ce1314)  

  - Pyenv => change python version = nodebrew same.
  - Pipenv => package manager = npm same.

## Make Environment
``` bash
# install pyenv
brew install pyenv

# edit .bash_profile
vi ~/.bash_profile
# add lines
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
# load .bash_profile
source ~/.bash_profile

# install python
pyenv install 3.6.5
pyenv global 3.6.5

# check pyenv-virtualenv
pyenv versions

# install pipenv
brew install pipenv

# install library with pipenv => make Pipfile
pipenv install django django-filter djangorestframework
# install pylint
pipenv install pylint

# Add setting.json with VS Code.
// Whether to lint Python files.
"python.linting.enabled": true,
// Whether to lint Python files using pylint.
"python.linting.pylintEnabled": true,
```

## Create Django Project
``` bash
# shell login
pipenv shell
# create django Project
django-admin startproject XXXXX
```

## Build Setup

``` bash
# in pipenv shell

# migration
python manage.py makemigrations
python manage.py migrate
# import init data
python manage.py loaddata fixture.json
# start web server. access to http://localhost:8000/vuejs/api/
python manage.py runserver
```
