#midi_service
from midiutil.MidiFile import MIDIFile

def create_midi(bpm, score):
    # create your MIDI object
    mf = MIDIFile(1)     # only 1 track
    track = 0   # the only track

    time = 0    # start at the beginning
    mf.addTrackName(track, time, "Sample Track")
    mf.addTempo(track, time, bpm)
    
    volume = 100
    channel = 0
    time = 0
    for note in score:
        mf.addNote(track, channel, note.pitch, time, note.length, volume)
        time += note.length
    
    with open("mymidifile.midi", 'wb') as output_file:
        mf.writeFile(output_file)
    


    # add some notes
    
    

