import sys
import json
import time
import paho.mqtt.client as mqtt
from img2bytearray import convert_to_bytearray
from PIL import Image

with open('./config.json', 'r') as fs:
    config = json.loads(fs.read())

client = mqtt.Client()
client.username_pw_set(config['mqtt']['username'], config['mqtt']['password'])
client.connect(config['mqtt']['host'], config['mqtt']['port'], 60)

client.loop_start()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path_to_black_image = str(sys.argv[1])
        path_to_red_image = str(sys.argv[2]) if len(sys.argv) > 2 else None

        im_black = Image.open(path_to_black_image).convert('1')
        im_red = Image.open(path_to_red_image).convert('1') if path_to_red_image != None else None
        
        client.publish('eink/image2/black', bytearray(convert_to_bytearray(im_black, 640, 384)), qos=2)
        client.publish('eink/image2/red', bytearray(convert_to_bytearray(im_red, 640, 384)) if im_red != None else "BLANK", qos=2)
        time.sleep(2)
    else:
        print("please specify the location of image i.e img2bytearray.py /path/to/black /path/to/red_image")
