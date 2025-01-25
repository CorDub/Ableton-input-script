import mido
import random

potential_notes = [57, 56, 53, 52, 51, 48, 47]

def velocity():
    return 90 + random.randint(-30, +30)

def note(range):
    octave = [-12, 0, 12]
    res = 0
    if range == 0:
        res = potential_notes[random.randint(2,4)]
    elif range == 1:
        res = potential_notes[random.randint(1,5)] + octave[random.randint(0,2)]
    else:
        res = potential_notes[random.randint(0,6)] + octave[random.randint(0,2)]
    return res
    

def silence(time):
    res = [] 
    message_on = mido.Message('note_on', note=60, velocity=0, time=0)
    res.append(message_on)
    message_off = mido.Message('note_off', note=60, velocity=0, time=time)
    res.append(message_off)
    return res

def add_note(time, range):
    vel = velocity()
    value = note(range)
    res = []
    message_on = mido.Message('note_on', note = value, velocity = vel, time = 0)
    res.append(message_on)
    message_off = mido.Message('note_off', note = value, velocity = vel, time = time)
    res.append(message_off)
    return res