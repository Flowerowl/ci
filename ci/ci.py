#encoding:utf-8
from __future__ import unicode_literals

import sys
import logging
import json

import yaml
from fabric.api import local, lcd, run
from bottle import run, post


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("ci.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@post('/')
def index():
    with open('data.json') as f:
        git_data = json.loads(f.read())
        if git_data['ref'] == 'refs/heads/master':
            deploy(git_data)

def deploy(git_data):
    config = yaml.load(open('config.yaml'))
    path = config['path']
    command = config['command']
    with lcd(path):
        local(command)
    logger.info(git_data)

run(host='localhost', port=7180)
