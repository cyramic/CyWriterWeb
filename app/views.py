from flask import render_template
from flask import jsonify, request
from app import app
import os
import urllib.parse
from lxml import etree
from . import document
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
    filename = urllib.parse.unquote(filename)
    print(filename)
    xmlobj = etree.parse("./app/documents/"+filename)
    print("Opened XML object")
    docobj = document.Document(xmlobj)
    print(docobj)
    # Put this into a local cache so that it can be queried / saved (redis)
    # Put this into a local cache so that it can be queried / saved (redis)


    return xmlobj.xpath("chapters/chapter[@position='0']/text")[0].text