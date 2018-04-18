#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
   @author: xiaolinzi
   @file: manage.py 
   @time: 2018/04/18
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)