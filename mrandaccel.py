import random
import mido
import time
from helpers import silence, add_note

output_port_name = "ToAbleton 1"
mid = mido.MidiFile()
track = mido.MidiTrack()
mid.tracks.append(track)
bpm = 87
tempo = mido.bpm2tempo(bpm)
timings = []

def time_per_note(note, bpm):
    res = (60/bpm) / (note/4)
    print(res)
    return res

def add_to_track(valid, time):
    percent = random.randint(0,100)
    if percent < valid:
        silent_note = silence(time)
        track.append(silent_note[0])
        timings.append(time_per_note(time, bpm))
        track.append(silent_note[1])
        timings.append(time_per_note(time, bpm))
    else:
        note = add_note(time)
        track.append(note[0])
        timings.append(time_per_note(time, bpm))
        track.append(note[1])
        timings.append(time_per_note(time, bpm))


def output(track, timings):
    try:
        with mido.open_output(output_port_name) as output:
            print(f"Sending MIDI messages to {output_port_name}...")
            for index, message in enumerate(track):
                if message.type == 'note_on':
                    print(message)
                    output.send(message)
                    time.sleep(timings[index])
                else:
                    print(message)
                    output.send(message)
            # for message in track:
            #     output.send(message)
            #     print(message.bytes())
                
            print(f"All MIDI messages sent!")
    except IOError as e:
        print(f"Could not open MIDI output port: {output_port_name}")
        print(f"{e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        # for message in track:
        #     print(message.bytes())

# -- Actual script --

# Two first measures

for x in range(16):
    if x<8:
        add_to_track(80, 4)
    if 7<x<16:
        add_to_track(60, 4)

# Third measure

for x in range(16):
    add_to_track(40, 8)

# Last measure - First half

for x in range(16):
    add_to_track(20, 16)

# Last measure - Second half

for x in range(32):
    add_to_track(20, 32)

output(track, timings);