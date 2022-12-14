# Credit: https://github.com/leon-anavi/rpi-examples
 
# List of tone-names with frequency
TONES = {"c6":1047,
    "b5":988,
    "a5":880,
    "g5":784,
    "f5":698,
    "e5":659,
    "eb5":622,
    "d5":587,
    "c5":523,
    "b4":494,
    "a4":440,
    "ab4":415,
    "g4":392,
    "gb4":370,
    "f4":349,
    "e4":330,
    "d4":294,
    "c4":262}
 
# SONGS is a collection of songs
# Song is a list of tones with name and 1/duration. 16 means 1/16 beat
SONGS = {}
SONGS['Fur_Elise'] = [
    ["e5",16],["eb5",16],
    ["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
    ["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
    ["b4",8],["p",16],["e4",16],["ab4",16],["b4",16],
    ["c5",8],["p",16],["e4",16],["e5",16],["eb5",16],
    ["e5",16],["eb5",16],["e5",16],["b4",16],["d5",16],["c5",16],
    ["a4",8],["p",16],["c4",16],["e4",16],["a4",16],
    ["b4",8],["p",16],["e4",16],["c5",16],["b4",16],["a4",4]
    ]
 
SONGS['Baby_Shark'] = [
        ["d4",4],["e4",4],["g4",8],["g4",8],["g4",8],["g4",16],["g4",8],["g4",16],["g4",8],
        ["d4",8],["e4",8],["g4",8],["g4",8],["g4",8],["g4",16],["g4",8],["g4",16],["g4",8],
        ["d4",8],["e4",8],["g4",8],["g4",8],["g4",8],["g4",16],["g4",8],["g4",16],["g4",8],
        ["g4",8],["g4",8],["gb4",4]
        ]
 