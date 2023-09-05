

import json
import os
import pdf2image
import pytesseract
from PIL import Image

def loadCategories(file_name):
    output_folder = 'uploads/categories/' + file_name.strip('.json') + '/'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(output_folder+file_name) as f:
        data=json.load(f)
    return data

def loadJson(file_name):
    output_folder = 'uploads/jsons/' + file_name.strip('.json') + '/'

    with open(output_folder+file_name) as f:
        data = json.load(f)

    return data

def saveJson(file_name,file):
    output_folder = 'uploads/jsons/' + file_name.strip('.json') + '/'
    saveFile = output_folder + file_name
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(saveFile, 'wb') as fp:
        file.save(os.path.join(output_folder, file_name))

def savePdf(file_name,file):
    output_folder = 'uploads/pdfs/' + file_name.strip('.pdf') + '/'
    saveFile=output_folder+file_name
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(saveFile,'wb') as fp:

        file.save(os.path.join(output_folder,file_name))

def saveCategories(file_name,categories):
    output_folder='uploads/categories/'+file_name.strip('.pdf')+'/'
    saveFile=output_folder+file_name.strip('.pdf')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    with open(saveFile+'.json', 'w') as fp:
        json.dump(categories, fp,indent=4)

def convertPDF2IMG(file):
    file_name = os.path.splitext(os.path.basename(file))[0]
    output_folder = 'uploads/images/' + file_name + '/'
    pdflocation='uploads/pdfs/' + file_name.strip('.pdf') +'/'
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Split the pdf into pages
    pages = pdf2image.convert_from_path(pdflocation+file_name+'.pdf',poppler_path=r'C:\Program Files\poppler-23.08.0\Library\bin')
    # Save the pages
    for i in range(len(pages)):
        pages[i].save(output_folder + file_name + "_page_" + str(i) + ".png", "PNG")


def OCR(image_path, boudingbox) -> str:
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    image = Image.open(image_path)
    # Crop the image to the bounding box
    cropped_image = image.crop(boudingbox)
    # Convert the image to grayscale
    cropped_image = cropped_image.convert('L')
    # Convert the image to a string
    text = pytesseract.image_to_string(cropped_image)
    return text
