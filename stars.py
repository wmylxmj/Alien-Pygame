# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 14:08:11 2018

@author: wmy
"""

import pygame
from settings import Settings
from pygame.sprite import Sprite
import random

class Star(Sprite, Settings):
    
    def __init__(self):
        '''初始化星星'''
        Sprite.__init__(self)
        Settings.__init__(self)
        # init the screen 
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        # image load
        self.image = pygame.image.load('images/star_1.png')
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(0, self.screen_width)
        self.rect.centery = random.randint(0, self.screen_height)
        self.y = float(self.rect.y)
        self.move_speed = self.star_move_speed
        pass
    
    def update(self):
        '''更新星星位置信息'''
        if(self.y < self.screen_height):
            self.y += self.move_speed
            self.rect.y = self.y
            pass
        else:
            self.rect.centerx = random.randint(0, self.screen_width)
            self.y = 0
            self.rect.y = self.y
            pass
        pass
    
    def blitme(self):
        '''画出星星'''
        self.screen.blit(self.image, self.rect)
        pass
    
    pass