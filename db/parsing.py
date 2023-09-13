import os
import json
import cv2
import os.path
from glob import glob


def convert(json_data):
    img_name = json_data['FILE NAME']
    img_resol = json_data['RESOLUTION']
    Bounding = json_data['Bounding']

    # img = cv2.imread('*.json', cv2.IMREAD_GRAYSCALE)

    path = "./image/jpg/" + img_name
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    dy, dx = img.shape

    print(img_name)
    str_pt = img_name.find('.')
    img_name = img_name[:str_pt]
    if not os.path.isdir('./parsing'):
        os.mkdir('./parsing')

    file = open("./parsing/" + img_name + ".txt", 'w')

    for Bounding_info in Bounding:
        x1 = int(Bounding_info['x1'])
        x2 = int(Bounding_info['x2'])
        y1 = int(Bounding_info['y1'])
        y2 = int(Bounding_info['y2'])

        conv_x1 = (x1 + x2) / 2 / dx
        conv_y1 = (y1 + y2) / 2 / dy
        conv_x2 = (x2 - x1) / dx
        conv_y2 = (y2 - y1) / dy

        file.write(f"2 {conv_x1:f} {conv_y1:f} {conv_x2:f} {conv_y2:f}\n")

    file.close()


for filename in glob('./image/json/*.Json', recursive=True):
    with open(filename, 'r', encoding='UTF-8') as json_file:
        json_data = json.load(json_file)
        convert(json_data)
