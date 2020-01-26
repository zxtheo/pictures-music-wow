#image_data

class ImageData:
    def __init__(self, pixels):
        self.image_data = []
        for pixel in pixels:
            self.image_data.append(_Pixel(pixel))
        
    def to_list(self):
        data_list = []
        for pixel in self.image_data:
            data_list.append(pixel)
        return data_list

class _Pixel:
    def __init__(self, pixel):
        self.r, self.g, self.b = pixel

    def to_list(self):
        return [self.r, self.g, self.b]