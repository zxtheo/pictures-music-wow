#main.py
from service.image_service import get_image_data
from service.note_maker_service import make_notes
from service.music_service import play_music
from service.midi_service import create_midi
from multiprocessing import Process
import sys

rest = 'g'
arguments = sys.argv[1:]
img = arguments[0]
pitch = arguments[1]
length = arguments[2]
bpm = int(arguments[3])
out = arguments[4] if len(arguments)>4 and arguments[4] != "" else "test"

def main():

    img_values = get_image_data(img).to_list()
    music_score1 = make_notes(img_values, pitch, length, rest, bpm)
    music_score2 = make_notes(img_values, 'r', 'b', rest, bpm)
    # play_music(music_score1)
    create_midi(bpm, [music_score1, music_score2], out, 120)

    

    


    # frequency_map = {
    #     "c4":262,
    #     "d4":294,
    #     "e4":330,
    #     "f4":349,
    #     "g4":392,
    #     "a4":440,
    #     "b4":494,
    #     "c5":523,
    #     "d5":587,
    #     "e5":659,
    #     "f5":698,
    #     "g5":784,
    #     "a5":880,
    #     "b5":988,
    #     "c6":1047
    # }

    # frequency_map = {
    #     "c4":60,
    #     "d4":62,
    #     "e4":64,
    #     "f4":65,
    #     "g4":67,
    #     "a4":69,
    #     "b4":71,
    #     "c5":72,
    #     "d5":74,
    #     "e5":76,
    #     "f5":77,
    #     "g5":79,
    #     "a5":81,
    #     "b5":83,
    #     "c6":84
    # }

    # colour_map = {
    #     "0":"c4",
    #     "1":"d4",
    #     "2":"e4",
    #     "3":"f4",
    #     "4":"g4",
    #     "5":"a4",
    #     "6":"b4",
    #     "7":"c5",
    #     "8":"d5",
    #     "9":"e5",
    #     "10":"f5",
    #     "11":"g5",
    #     "12":"a5",
    #     "13":"b5",
    #     "14":"c6"
    # }    
    
    # note_map = {}
    # for i in range(0, 256):
    #     note_map[str(i)] = frequency_map[colour_map[str(round(i/18))]]

    # print (note_map)
        
        
main()
