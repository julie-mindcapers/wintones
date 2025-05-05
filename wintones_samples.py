# wintones: python notes player
# Copyright (c) 2025 Mindcapers LLC
# MIT License

# https://www.geeksforgeeks.org/python-winsound-module/

import winsound
import wintones
import time

def playAll(noteList, len):
    for note in noteList:
        winsound.Beep(int(note), len)
        time.sleep((len/1000.0) + 0.1)

def scaleF3(len):
    winsound.Beep(int(wintones.NOTE_F3), len)
    winsound.Beep(int(wintones.NOTE_G3), len)
    winsound.Beep(int(wintones.NOTE_A3), len)
    winsound.Beep(int(wintones.NOTE_BF3), len)
    winsound.Beep(int(wintones.NOTE_C4), len)
    winsound.Beep(int(wintones.NOTE_D4), len)
    winsound.Beep(int(wintones.NOTE_E4), len)
    winsound.Beep(int(wintones.NOTE_F4), len)

def rainbow():
    wintones.PlayNote(wintones.NOTE_F4, 800)
    wintones.PlayNote(wintones.NOTE_F5, 800)
    wintones.PlayNote(wintones.NOTE_E5, 400)
    wintones.PlayNote(wintones.NOTE_C5, 200)
    wintones.PlayNote(wintones.NOTE_D5, 200)
    wintones.PlayNote(wintones.NOTE_E5, 400)
    wintones.PlayNote(wintones.NOTE_F5, 400)

winsound.Beep(int(wintones.NOTE_C4), 500)
time.sleep(1)

#notes = wintones.GetNoteList()
#playAll(notes, 200)
#time.sleep(1)

scaleF3(200)
time.sleep(1)

rainbow()
time.sleep(1)


