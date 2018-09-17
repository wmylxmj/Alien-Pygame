# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:46:30 2018

@author: wmy
"""

from settings import Settings
from pygame.sprite import Sprite
import pygame
import math

class Ship(Settings, Sprite):
    
    def __init__(self):
        '''初始化飞船'''
        Settings.__init__(self)
        Sprite.__init__(self)
        # init the screen 
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen_rect = self.screen.get_rect()
        # load the image
        self.image = pygame.image.load('images/ship_1.png')
        self.image_rect = self.image.get_rect()
        # load the decision point
        self.decision_point = pygame.image.load('images/decision_point_1.png')
        self.rect = self.decision_point.get_rect()
        # init the location
        self.rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom
        self.rect.centery = self.image_rect.centery
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        # move flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # fire init
        self.fire_flag = False
        self.fire_count = 0
        self.fire_wait_time = self.ship_fire_wait_time
        self.bullet_speed = self.ship_bullet_speed
        # init speed 
        self.speed = self.ship_normal_speed
        # init image location
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        # the ship is still alive
        self.alive_flag = True
        pass
    
    def update(self):
        '''更新位置'''
        if self.moving_right and self.image_rect.right < self.screen_rect.right:
            self.center_x += self.speed
            pass
        if self.moving_left and self.image_rect.left > 0:
            self.center_x -= self.speed
            pass
        if self.moving_up and self.image_rect.top > 0:
            self.center_y -= self.speed
            pass
        if self.moving_down and self.image_rect.bottom < self.screen_rect.bottom:
            self.center_y += self.speed
            pass
        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        pass
        
    def blitme(self):
        '''画出飞船'''
        if self.alive_flag:            
            self.screen.blit(self.image, self.image_rect)
            if self.speed == self.ship_slow_speed:
                self.screen.blit(self.decision_point, self.rect)
                pass
            pass
        pass 
    
    pass


class ShipBullet(Sprite):
    
    def __init__(self, ship):
        '''初始化子弹'''
        Sprite.__init__(self)
        # load information from ship
        self.ship = ship
        self.screen = ship.screen
        # image init
        self.image = pygame.image.load('images/ship_bullet_1.png')
        self.rect = self.image.get_rect()
        # init the location
        self.rect.centerx = ship.image_rect.centerx
        self.rect.top = ship.rect.top
        # init the shoot angle
        self.angle = 0
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y -= self.ship.bullet_speed * math.cos(self.angle)
        self.rect.y = self.y
        self.x += self.ship.bullet_speed * math.sin(self.angle)
        self.rect.x = self.x
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.rect)
        pass
    
    pass

        