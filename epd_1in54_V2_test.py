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
# client.on_publish = on_publish
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
    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    draw.rectangle((0, 10, 200, 34), fill = 0)
    draw.text((8, 12), 'hello world', font = font, fill = 255)
    draw.text((8, 36), u'微雪电子', font = font, fill = 0)
    draw.line((16, 60, 56, 60), fill = 0)
    draw.line((56, 60, 56, 110), fill = 0)
    draw.line((16, 110, 56, 110), fill = 0)
    draw.line((16, 110, 16, 60), fill = 0)
    draw.line((16, 60, 56, 110), fill = 0)
    draw.line((56, 60, 16, 110), fill = 0)
    draw.arc((90, 60, 150, 120), 0, 360, fill = 0)
    draw.rectangle((16, 130, 56, 180), fill = 0)
    draw.chord((90, 130, 150, 190), 0, 360, fill = 0)
    client.publish('eink/image', bytearray(convert_to_bytearray(image, 200, 200)), qos=2)
    time.sleep(2)
    
    # read bmp file 
    # logging.info("2.read bmp file...")
    # image = Image.open(os.path.join(picdir, '1in54.bmp'))
    # client.publish('eink/image', convert_to_bytearray(image, 200, 200), qos=2)
    # time.sleep(2)
    
    # read bmp file on window
    # logging.info("3.read bmp file on window...")
    # image1 = Image.new('1', (200, 200), 255)  # 255: clear the frame
    # bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    # image1.paste(bmp, (50,50))    
    # client.publish('eink/image', convert_to_bytearray(image1, 200, 200), qos=2)
    # time.sleep(2)
    
    # partial update
    # logging.info("4.show time...")
    # time_image = image1
    # # Image.new('1', (epd.width, epd.height), 255)
    # epd.displayPartBaseImage(epd.getbuffer(time_image))
    
    # epd.init(1) # into partial refresh mode
    # time_draw = ImageDraw.Draw(time_image)
    # num = 0
    # while (True):
    #     time_draw.rectangle((10, 10, 120, 50), fill = 255)
    #     time_draw.text((10, 10), time.strftime('%H:%M:%S'), font = font, fill = 0)
    #     newimage = time_image.crop([10, 10, 120, 50])
    #     time_image.paste(newimage, (10,10))  
    #     epd.displayPart(epd.getbuffer(time_image))
    #     num = num + 1
    #     if(num == 20):
    #         break
    
    # logging.info("Clear...")
    # epd.init(0)
    # epd.Clear(0xFF)
    
    # logging.info("Goto Sleep...")
    # epd.sleep()
        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    # epd1in54_V2.epdconfig.module_exit()
    # exit()