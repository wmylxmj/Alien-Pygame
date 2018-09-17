# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:58:50 2018

@author: wmy
"""

import pygame
from settings import Settings
from pygame.sprite import Sprite
import random
import math

class Boom1(Settings, Sprite):
    
    def __init__(self):
        '''init'''
        Settings.__init__(self)
        Sprite.__init__(self)
        # picture
        self.image = pygame.image.load('images/boom_1.png')
        self.rect = self.image.get_rect()
        self.image2 = pygame.image.load('images/boom_2.png')
        self.image2_rect = self.image2.get_rect()
        self.image3 = pygame.image.load('images/boom_3.png')
        self.image3_rect = self.image3.get_rect()
        # init the screen 
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size) 
        self.life_count = 60
        self.start_flag = False
        pass
    
    def update(self):
        '''update'''
        if self.start_flag:
            self.life_count -= 1
            pass
        pass
    
    def blitme(self):
        '''blit'''
        if self.life_count > 40 and self.start_flag == True:
            self.screen.blit(self.image3, self.rect)
            pass
        elif self.life_count > 20 and self.start_flag == True:
            self.screen.blit(self.image, self.rect)
            pass
        elif self.life_count > 0 and self.start_flag == True:
            self.screen.blit(self.image2, self.rect)
        pass
    
    pass
