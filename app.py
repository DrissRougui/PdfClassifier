from flask import Flask,request
from flask_cors import CORS, cross_origin
from utils import convertPDF2IMG,saveCategories,savePdf,saveJson,loadJson,loadCategories
from detect import detect
import pickle
import classifier



app=Flask(__name__)
CORS(app)

BASE_FOLDER = 'uploads/images/'

@app.route('/pdf', methods=['POST'])
@cross_origin()
def categories():
    file = request.files['file']

    filename=file.filename
    savePdf(filename,file)
    convertPDF2IMG(filename)
    categories=detect(BASE_FOLDER+filename.strip('.pdf'))
    saveCategories(filename,categories)
    return categories



@app.route('/fields', methods = ['POST'])
@cross_origin()
def fields():

    #data=request.get_json()
    #categories=data.get('categories')
    #fields=data.get('fields')
    file = request.files['json']
    filename=file.filename
    saveJson(filename,file)
    fields=loadJson(filename)
    categories=loadCategories(filename)
    return classifier.classify(categories,fields)
