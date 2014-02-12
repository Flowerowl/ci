#encoding:utf-8
from __future__ import unicode_literals

import sys
import locale
import codecs
import logging
import json

import yaml
from fabric.api import local, lcd
from bottle import request, run, post

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

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
    with lcd(path):
        local(command)
    logger.info(git_data)

run(host='10.16.2.202', port=7180)
