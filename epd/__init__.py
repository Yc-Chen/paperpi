import epd7in5b

epd = epd7in5b.EPD()
epd.init()

def show(image):
    epd.display_frame(epd.get_frame_buffer(image))
