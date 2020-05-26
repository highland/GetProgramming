#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Somewhat refactored solution to Lesson 38 Capstone Project
(removing deep if elif structures)

Created on Tue May 26 18:04:41 2020

@author: mark
"""

import tkinter
import random


class Player(object):
    def __init__(self, canvas, color):
        size = random.randint(1, 100)
        x1 = random.randint(100, 700)
        y1 = random.randint(100, 700)
        x2 = x1 + size
        y2 = y1 + size
        self.color = color
        self.coords = (x1, y1, x2, y2)
        self.piece = canvas.create_rectangle(self.coords, tags=color)
        canvas.itemconfig(self.piece, fill=color)

    moves_map = {'u': (0, -10, 0, -10),
                 'd': (0, 10, 0, 10),
                 'l': (-10, 0, -10, 0),
                 'r': (10, 0, 10, 0)}

    def move(self, direction):
        move = Player.moves_map[direction]
        self.coords = tuple(now + change
                            for now, change
                            in zip(self.coords, move))
        canvas.coords(self.piece, self.coords)


key_map_player1 = {'w': 'u', 's': 'd', 'a': 'l', 'd': 'r'}
key_map_player2 = {'i': 'u', 'k': 'd', 'j': 'l', 'l': 'r'}


def handle_key(event):
    if event.char in key_map_player1:
        direction = key_map_player1[event.char]
        player1.move(direction)
    elif event.char in key_map_player2:
        direction = key_map_player2[event.char]
        player2.move(direction)
    check_for_tag()


def check_for_tag():
    yellow_xy = canvas.bbox(1)
    overlapping = canvas.find_overlapping(*yellow_xy)
    if 2 in overlapping:
        canvas.create_text(100, 100, font=("Arial", 20), text="Tag!")


window = tkinter.Tk()
window.geometry("800x800")
window.title("Tag!")
canvas = tkinter.Canvas(window)
canvas.pack(expand=1, fill='both')

player1 = Player(canvas, "yellow")
player2 = Player(canvas, "blue")
canvas.bind_all('<Key>', handle_key)

window.mainloop()
