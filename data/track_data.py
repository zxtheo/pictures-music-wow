from midiutil.MidiFile import MIDIFile
import os
import sys

class trackData:


    def __init__(self, bpm, name, track_length):
        self.mf = MIDIFile(1)
        self.mf.addTrackName(0, 0, name)
        self.mf.addTempo(0, 0, bpm)
        self.track_length = track_length 
        self.name = name


    def set_channel(self, channel, program):
        self.mf.addProgramChange(1, channel, 0, program)

    def write_to_file(self):
        with (os.fdopen(os.dup(sys.stdout.fileno()), 'wb') if self.name == '-'
            else open("{}.midi".format(self.name), 'wb')) as output_file:
            self.mf.writeFile(output_file)
