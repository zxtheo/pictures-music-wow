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

def main():

    img_values = get_image_data(img).to_list()
    music_score1 = make_notes(img_values, pitch, length, rest, bpm, True)
    music_score2 = make_notes(img_values, 'r', 'b', rest, bpm, False)
    create_midi(bpm, [music_score1, music_score2], "test", 120)


        
main()