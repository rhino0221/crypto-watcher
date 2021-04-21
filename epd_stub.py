import logging
from PIL import Image, ImageDraw, ImageFont

logging.basicConfig(level=logging.DEBUG)

class EPD(object):
    
    FULL_UPDATE = 0
    PART_UPDATE = 1
    
    def __init__(self):
        self.width = 250
        self.height = 122

    def init(self, update):
        pass

    def Clear(self, color):
        pass

    def display(self, image):
        pass

    def getbuffer(self, image):
        logging.info("Writing image.png")
        if(image.width == self.width and image.height == self.height):
            logging.debug("Vertical")
            image.save("image.png")
        elif(image.width == self.height and image.height == self.width):
            logging.debug("Horizontal")
            _img = image.transpose(Image.ROTATE_90)
            _img.save("image.png")
            
        
        exit()