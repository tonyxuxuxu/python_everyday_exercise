"""

第 0010 题： 使用 Python 生成类似于下图中的字母验证码图片

"""

import re
import os
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def image_draw():

    def randomChar():
        return chr(random.randint(65, 90))

    def randomColor():
        return (random.randint(64,255), random.randint(64, 255), random.randint(64, 255))

    width = 240
    height = 60

    image = Image.new('RGB',(width, height), (255, 255, 255))

    font = ImageFont.truetype('./msyh.ttf', 36)

    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill=randomColor())

    for t in range(4):
        draw.text((60*t+10, 10), randomChar(), font=font, fill=randomColor())

    image = image.filter(ImageFilter.BLUR)

    image.save('code.jpg', 'jpeg')
    image.show('code.jpg')

if __name__ == "__main__":
    image_draw()