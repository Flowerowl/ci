#encoding:utf-8
from __future__ import unicode_literals

import logging
import json

import yaml
from fabric.api import cd, run, env
from bottle import run, post


@post('/')
def index():


def deploy():
    config = yaml.load(open('config.yaml'))
    path = config['path']
    command = config['command']

run(host='localhost', port=8080)
