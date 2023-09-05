from ultralytics import YOLO
from PIL import Image
import os
import pdf2image
from utils import OCR






def detect(directory):

    model = YOLO('best.pt')



    source = []

    for filename in os.listdir(directory):
        source.append(directory + '/' + filename)

    categories = []
    # Run inference on the source
    results = model(source)
    for index, r in enumerate(results):
        boundingBoxes = r.boxes.xyxy.tolist()
        for box in boundingBoxes:
            categoy = {
                'categoryName': OCR(source[index], box).strip(),
                'x': box[0],
                'y': box[1],
                'page': index
            }
            categories.append(categoy)

    return categories



