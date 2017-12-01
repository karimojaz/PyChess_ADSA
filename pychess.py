#!/usr/bin/env python3

import pygame
from gui import *
from pygame.locals import *

initializeUI()

keepon = 1
while keepon :
    for event in pygame.event.get():
        if event.type == QUIT:
            keepon = 0
