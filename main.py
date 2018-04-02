import epd
from PIL import Image

#import imagedata

EPD_WIDTH = 640
EPD_HEIGHT = 384

def main():
    image = Image.open('640x384.bmp')
    epd.show(image)

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.MONOCOLOR_BITMAP)

if __name__ == '__main__':
    main()
