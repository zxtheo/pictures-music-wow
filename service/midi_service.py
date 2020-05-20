#midi_service
from midiutil.MidiFile import MIDIFile
from data.track_data import trackData

def create_midi(bpm, score, name, track_length):
    # create your MIDI object
    midif = trackData(bpm, name, track_length)
    
    
    track = 0   # the only track

    time = 0    # start at the beginning
    
    volume = 100
    channel = 0
    time = 0
    for chan in score:
        for note in chan:
            midif.mf.addNote(track, channel, note.pitch, time, note.length, volume)
            time += note.length
        channel += 1
        time = 0
        
    midif.write_to_file()
    


    # add some notes
    