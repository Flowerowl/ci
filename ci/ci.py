#encoding:utf-8
from __future__ import unicode_literals

import sys
import logging
import json

import yaml
from fabric.api import local, cd, run, env
from bottle import request, run, post


env.hosts = ['10.16.2.202']

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("ci.log")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@post('/')
def index():
    git_data = request.json
    if git_data['ref'] == 'refs/heads/master':
        deploy(git_data)

def deploy(git_data):
    config = yaml.load(open('config.yaml'))
    path = config['path']
    command = config['command']
    with cd(path):
        run(command)
    logger.info(git_data)

run(host='10.16.2.34', port=7180)
