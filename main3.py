from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import epd7in5
from logger import logger

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    epd = epd7in5.EPD()
    epd.init()

    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 24)
    # draw.text((200, 10), 'e-Paper demo', font = font, fill = 255)
    # draw the horizontal lines
    draw.line((0, 0, 640, 0), fill=0, width=2)
    draw.line((0, 128, 640, 128), fill=0, width=2)
    draw.line((0, 256, 640, 256), fill=0, width=2)
    draw.line((0, 381, 640, 381), fill=0, width=2)
    # draw the vertical lines
    draw.line((0, 0, 0, 384), fill=0, width=2)
    draw.line((160, 0, 160, 384), fill=0, width=2)
    draw.line((320, 0, 320, 384), fill=0, width=2)
    draw.line((480, 0, 480, 384), fill=0, width=2)
    draw.line((638, 0, 638, 384), fill=0, width=2)
    # draw.arc((240, 120, 580, 220), 0, 360, fill = 255)
    # draw.rectangle((0, 80, 160, 280), fill = 255)
    # draw.arc((40, 80, 180, 220), 0, 360, fill = 0)
    logger.debug('Going to send to screen')
    image2 = Image.open('monocolor.bmp')
    epd.display_frame(epd.get_frame_buffer(image2), epd.get_frame_buffer(image))
    logger.debug('Frame displayed')
    #
    # image = Image.open('monocolor.bmp')
    # epd.display_frame(epd.get_frame_buffer(image))

if __name__ == '__main__':
    main()
