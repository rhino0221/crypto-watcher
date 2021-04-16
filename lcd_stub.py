
class LCD(object):
    def __init__(self):
        self.width = 250
        self.height = 122

    def LCD_Init(self):
        pass

    def LCD_Clear(self):
        pass

    def LCD_ShowImage(self, image):
        image.save("image.png")
