#main.py
from service.image_service import get_image_data
import math
from service.note_maker_service import make_notes
pitch = 'r'
length = 'g'
rest = 'b'
bpm = 120

def main():
    img = "doge.jpg"
    img_values = get_image_data(img).to_list()
    # print (img_values)
    music_score = make_notes(img_values, bpm)
    print(music_score)


    # frequency_map = {
    #     "c4":261.63,
    #     "d4":293.66,
    #     "e4":329.63,
    #     "f4":349.23,
    #     "g4":392.00,
    #     "a4":440.00,
    #     "b4":493.88,
    #     "c5":523.25,
    #     "d5":587.33,
    #     "e5":659.25,
    #     "f5":698.46,
    #     "g5":783.99,
    #     "a5":880.00,
    #     "b5":987.77,
    #     "c6":1046.50
    # }

    # colour_map = {
    #     "1":"c4",
    #     "2":"d4",
    #     "3":"e4",
    #     "4":"f4",
    #     "5":"g4",
    #     "6":"a4",
    #     "7":"b4",
    #     "8":"c5",
    #     "9":"d5",
    #     "10":"e5",
    #     "11":"f5",
    #     "12":"g5",
    #     "13":"a5",
    #     "14":"b5",
    #     "15":"c6"
    # }    
    
    # note_map = {}
    # for i in range(1, 256):
    #     note_map[str(i)] = frequency_map[colour_map[str(math.ceil(i/17))]]

    # print (note_map)
        
        
main()