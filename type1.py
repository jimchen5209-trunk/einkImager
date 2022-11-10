#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import paho.mqtt.client as mqtt
import struct
import os
picdir = '/media/jimchen5209/LinuxData/Git/e-Paper/RaspberryPi_JetsonNano/python/pic/'

import logging
import time
import json
from PIL import Image,ImageDraw,ImageFont
from img2bytearray import convert_to_bytearray

logging.basicConfig(level=logging.DEBUG)

with open('./config.json', 'r') as fs:
    config = json.loads(fs.read())

client = mqtt.Client()
client.username_pw_set(config['mqtt']['username'], config['mqtt']['password'])
client.connect(config['mqtt']['host'], config['mqtt']['port'], 60)

client.loop_start()

try:
    logging.info("epd1in54_V2 Demo")
    
    logging.info("init and Clear")
    time.sleep(1)
    
    # Drawing on the image
    logging.info("1.Drawing on the image...")
    image = Image.new('1', (200, 200), 255)  # 255: clear the frame
    
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
    font12 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 10)
    draw.rectangle((40, 0, 200, 24), fill = 0)
    draw.text((0, 2), '11月', font = font18, fill = 0)
    draw.text((50, 0), ' 7  8  9 10 11 12', font = font, fill = 255)
    draw.text((12, 24), '10:00', font = font12, fill = 0)
    draw.text((12, 38), '11:00', font = font12, fill = 0)
    draw.text((12, 52), '12:00', font = font12, fill = 0)
    draw.text((12, 66), '13:00', font = font12, fill = 0)
    draw.text((12, 80), '14:00', font = font12, fill = 0)
    draw.text((12, 94), '15:00', font = font12, fill = 0)
    draw.text((12, 108), '16:00', font = font12, fill = 0)
    draw.text((12, 122), '17:00', font = font12, fill = 0)
    draw.text((12, 136), '18:00', font = font12, fill = 0)
    draw.text((12, 150), '19:00', font = font12, fill = 0)
    draw.text((12, 164), '20:00', font = font12, fill = 0)
    draw.text((12, 178), '21:00', font = font12, fill = 0)
    draw.text((12, 192), '22:00', font = font12, fill = 0)
    client.publish('eink/image', bytearray(convert_to_bytearray(image, 200, 200)), qos=2)
    time.sleep(2)
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")