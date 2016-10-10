bt README
==================

Getting Started
---------------

- Create a python3.5 virtual environment
cd ~/project
pyvenv-3.5 env

source ~/project/env/bin/activate

git clone git@github.com:nishikant/bt.git

- cd <directory containing this file>

python setup.py develop

- $VENV/bin/initialize_bt_db development.ini

uwsgi --ini-paste-logged development.ini

- $VENV/bin/pip install -e .

