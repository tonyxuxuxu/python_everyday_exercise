"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

"""

from PIL import Image, ImageDraw, ImageFont

text = '555'
img = Image.open('0000.jpg')
img_w, img_h = img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("msyh.ttf", 10)
font_w, font_h = draw.textsize(text,font)
draw.text((img_w-font_w, 0), text, fill="red", font=font)
img.save('0000_out.jpg')


"""
ImageDraw: Creates an object that can be used to draw in the given image.

TrueType：Load a TrueType or OpenType font file, and create a font object. 
This function loads a font object from the given file, and creates a font object for a font of the given size.

"""