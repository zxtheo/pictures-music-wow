#main.py
from service.image_service import get_image_data
from service.note_maker_service import make_notes
from service.music_service import play_music
from multiprocessing import Process

pitch = 'b'
length = 'r'
rest = 'g'
bpm = 200

def main():
    img = "better_deep_fried_doge.jpg"
    img_values = get_image_data(img).to_list()
    #print (img_values)
    music_score1 = make_notes(img_values, pitch, length, rest, bpm)
    play_music(music_score1)
    # music_score2 = make_notes(img_values, 'g', 'r', 'b', bpm)
    # play_music(music_score2)
    

    


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