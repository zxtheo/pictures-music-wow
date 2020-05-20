#note_maker_service
from data.note_data import NoteData
import math

bass_frequency = {}
synth_frequency = {}

def make_notes(image_data, ipitch, ilength, irest, bpm, bass):
    frequency_map = map_frequencies()
    bass_frequency = frequency_map[1]
    synth_frequency = frequency_map[0]
    music_score = []
    for pixel in image_data:
        rgb = pixel.to_list()

        rgb_dict = {'r': 0, 'g': 1, 'b':2}
        if bass:
            pitch = get_pitch(rgb[rgb_dict[ipitch]], bass_frequency)
        else:
            pitch = get_pitch(rgb[rgb_dict[ipitch]], synth_frequency)

        length = get_note_length(rgb[rgb_dict[ilength]], bpm, bass)
        music_score.append(NoteData(pitch, length, 0))
    return music_score

def get_pitch(n, frequency):
    return frequency[str(n)]

def get_note_length(n, bpm, bass):
    lengths = {}
    if bass:
        lengths = {
            "0":4,  #4
            "1":2, #2
            "2":4,  #4
            "3":2, #2
            "4":4  #4
        }
    else:
        lengths = {
            "0":2, #2
            "1":0.5, #1/2
            "2":1  , #1
            "3":2, #2
            "4":1  #4
        }

    return lengths[str(round(n/63))]



def map_frequencies():

    synth = {
        "c4":60,
        "d4":62,
        "e4":64,
        "f4":65,
        "g4":67,
        "a4":69,
        "b4":71,
        "c5":72,
        "d5":74,
        "e5":76,
        "f5":77,
        "g5":79,
        "a5":81,
        "b5":83,
        "c6":84
    }

    colours = {
        "0":"c4",
        "1":"d4",
        "2":"e4",
        "3":"f4",
        "4":"g4",
        "5":"a4",
        "6":"b4",
        "7":"c5",
        "8":"d5",
        "9":"e5",
        "10":"f5",
        "11":"g5",
        "12":"a5",
        "13":"b5",
        "14":"c6"
    }    

    bass = {
        "c4":24,
        "d4":26,
        "e4":28,
        "f4":29,
        "g4":31,
        "a4":33,
        "b4":35,
        "c5":36,
        "d5":38,
        "e5":40,
        "f5":41,
        "g5":43,
        "a5":45,
        "b5":47,
        "c6":48
    }
    
    synth_frequency = {}
    for i in range(0, 256):
        synth_frequency[str(i)] = synth[colours[str(round(i/18))]]

    bass_frequency_temp = {}
    for i in range(0, 256):
        bass_frequency_temp[str(i)] = bass[colours[str(round(i/18))]]

    return[synth_frequency, bass_frequency_temp]


    

