from flask import render_template
from flask import jsonify, request
from app import app
import os
import urllib.parse
from lxml import etree
import redis

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/listdoc')
def listdocs():
    folder = "./app/documents/"
    results = [each for each in os.listdir(folder) if each.endswith('.cyw')]
    return jsonify(results)

@app.route('/opendoc/<filename>')
def opendoc(filename):
    redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

    filename = urllib.parse.unquote(filename)
    print(filename)
    docobj = etree.parse("./app/documents/"+filename)

    # Put this into a local cache so that it can be queried / saved (redis)


    return docobj.xpath("chapters/chapter[@position='0']/text")[0].text