#midi_service
from midiutil.MidiFile import MIDIFile
from data.track_data import trackData

def create_midi(bpm, score, name, track_length):
    # create your MIDI object
    midif = trackData(bpm, name, track_length)
    
    midif.set_channel(0, 37)
    
    track = 0   # the only track

    time = 0    # start at the beginning
    
    volume = 100
    channel = 0
    time = 0
    for chan in score:
        count = 0
        bar = 0
        for note in chan:
            if count < len(chan) -2:
                if chan[count+1].pitch == note.pitch:
                    count +=1
                    continue
                else:
                    remaining = 4 - bar
                    
                    if remaining > note.length:
                        midif.mf.addNote(track, channel, note.pitch, time, note.length, volume)
                        bar += note.length
                        time += note.length                        
                    else:
                        
                        midif.mf.addNote(track, channel, note.pitch, time, remaining, volume)
                        bar = 0
                        time += remaining
                        
                count +=1
        channel += 1
        time = 0
        bar = 0
    
    midif.write_to_file()
    


    # add some notes
    