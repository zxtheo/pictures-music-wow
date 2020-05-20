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
    music_score1 = make_notes(img_values, pitch, length, rest, bpm, True)
    music_score2 = make_notes(img_values, 'r', 'b', rest, bpm, False)
    # play_music(music_score1)
    create_midi(bpm, [music_score1, music_score2], out, 120)


        
main()
