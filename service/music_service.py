#music_service
import winsound, time

def play_music(music_score):
    for note in music_score:
        winsound.Beep(note.pitch, note.length)
        # time.sleep(note.rest/1000)

def test(pitch, length):
    winsound.Beep(pitch, length)
