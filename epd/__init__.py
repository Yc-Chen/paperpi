from .epd7in5b import EPD

EPD_WIDTH = 640
EPD_HEIGHT = 384

epd = EPD()
epd.init()

def show(image):
    epd.display_frame(epd.get_frame_buffer(image))
