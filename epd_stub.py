
class EPD(object):
    def __init__(self):
        self.width = 250
        self.height = 122

    def init(self):
        pass

    def Clear(self):
        pass

    def LCD_ShowImage(self, image):
        image.save("image.png")
