import mido
import random

potential_notes = [57, 56, 53, 52, 51, 48, 47]

def silence(time):
    res = [] 
    message_on = mido.Message('note_on', note=60, velocity=0, time=0)
    res.append(message_on)
    message_off = mido.Message('note_off', note=60, velocity=0, time=time)
    res.append(message_off)
    return res

def add_note(time):
    res = []
    note = potential_notes[random.randint(0,6)]
    velocity = 100 + random.randint(-10, 10)
    message_on = mido.Message('note_on', note = note, velocity = velocity, time = 0)
    res.append(message_on)
    message_off = mido.Message('note_off', note = note, velocity = velocity, time = time)
    res.append(message_off)
    return res