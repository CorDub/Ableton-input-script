import mido

print("Available MIDI output ports:")
for port in mido.get_output_names():
    print(repr(port))