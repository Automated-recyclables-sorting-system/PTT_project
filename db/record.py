import glob
import os
from pathlib import Path

os.system("cd ./yolov5 && python detect.py --weights yolov5s.pt --source ./data/images")

output = open('record.txt', 'a')
for filename in glob.glob('./image/json/*.txt'):
    with open(os.path.join(os.getcwd(), filename), "r") as f:
        file_name = Path(filename).stem
        content = f.read()
        if content[: 1] == '0':
            output.write(file_name + " 캔\n")
        elif content[: 1] == '1':
            output.write(file_name + " 페트\n")
        elif content[: 1] == '2':
            output.write(file_name + " 유리\n")
f.close()
output.close()