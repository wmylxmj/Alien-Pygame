# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 21:49:37 2018

@author: wmy
"""

import pygame
from settings import Settings
from pygame.sprite import Sprite
import random
import math

class Alien1(Sprite, Settings):
    
    def __init__(self):
        '''初始化'''
        Sprite.__init__(self)
        Settings.__init__(self)
        # type of alien
        self.type = None
        # active flag
        self.active_flag = False
        # init the screen 
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size) 
        # load image
        self.image = pygame.image.load('images/alien_1.png')
        self.rect = self.image.get_rect()
        # init the location
        self.rect.centerx = random.randint(-50, self.screen_width + 50)
        self.rect.bottom = self.screen.get_rect().top - 50
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.target_x = random.randint(100, self.screen_width - 100)
        self.target_y = random.randint(10, 200)
        # fire init
        self.fire_count = 0
        self.bullet_speed = 2
        self.fire_wait_time = 75
        # move speed
        self.speed = 5
        # number of lives
        self.num_life = 10
        # shoot angle
        self.shoot_move_dir = 1
        self.shoot_angle = 0
        pass
    
    def update(self):
        if self.active_flag and self.rect.top < self.target_y:
            self.y += self.speed
            self.rect.centery = self.y
            pass
        if self.active_flag:
            if self.target_x > self.rect.centerx:
                self.x += random.randint(0, 2)
                self.rect.centerx = self.x
            elif self.target_x < self.rect.centerx:
                self.x -= random.randint(0, 2)
                self.rect.centerx = self.x
            pass
        pass
    
    def blitme(self):
        '''绘制'''
        if self.active_flag:
            self.screen.blit(self.image, self.rect)
            pass
        pass
    
    pass


class Alien2(Sprite, Settings):
    
    def __init__(self):
        '''初始化'''
        Sprite.__init__(self)
        Settings.__init__(self)
        # type of alien
        self.type = None
        # active flag
        self.active_flag = False
        # init the screen 
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size) 
        # load image
        self.image = pygame.image.load('images/alien_2.png')
        self.rect = self.image.get_rect()
        # init the location
        self.rect.centerx = random.randint(-50, self.screen_width + 50)
        self.rect.bottom = self.screen.get_rect().top - 50
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.target_x = random.randint(100, self.screen_width - 100)
        self.target_y = random.randint(10, 200)
        # fire init
        self.fire_count = 0
        self.bullet_speed = 2
        self.fire_wait_time = 75
        # move speed
        self.speed = 5
        # number of lives
        self.num_life = 10
        # shoot angle
        self.shoot_move_dir = 1
        self.shoot_angle = 0
        pass
    
    def update(self):
        if self.active_flag and self.rect.top < self.target_y:
            self.y += self.speed
            self.rect.centery = self.y
            pass
        if self.active_flag:
            if self.target_x > self.rect.centerx:
                self.x += random.randint(0, 2)
                self.rect.centerx = self.x
            elif self.target_x < self.rect.centerx:
                self.x -= random.randint(0, 2)
                self.rect.centerx = self.x
            pass
        pass
    
    def blitme(self):
        '''绘制'''
        if self.active_flag:
            self.screen.blit(self.image, self.rect)
            pass
        pass
    
    pass


class Alien3(Sprite, Settings):
    
    def __init__(self):
        '''初始化'''
        Sprite.__init__(self)
        Settings.__init__(self)
        # type of alien
        self.type = None
        # active flag
        self.active_flag = False
        # init the screen 
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size) 
        # load image
        self.image = pygame.image.load('images/alien_1.png')
        self.rect = self.image.get_rect()
        # init the location
        self.rect.centerx = random.randint(100, self.screen_width - 100)
        self.rect.bottom = self.screen.get_rect().top - 50
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        # fire init
        self.fire_count = 0
        self.target_y = random.randint(10, 200)
        self.bullet_speed = 2
        self.fire_wait_time = 75
        # move speed
        self.speed = 5
        # number of lives
        self.num_life = 10
        self.shoot_move_dir = 1
        self.shoot_angle = 0
        self.move_dir = 1
        pass
    
    def update(self):
        if self.active_flag and self.rect.top < self.target_y:
            self.y += self.speed
            self.rect.centery = self.y
            pass
        if self.active_flag and self.rect.right < self.screen_width \
        and self.rect.left > 0:
            if self.move_dir == 1:
                self.x += 0.5
                pass
            elif self.move_dir == -1:
                self.x -= 0.5
                pass
            pass
        elif self.active_flag and self.rect.right >= self.screen_width and \
        self.move_dir == 1:
            self.move_dir = -1
            self.x -= 0.5
            pass
        elif self.active_flag and self.rect.left <= 0 and \
        self.move_dir == -1:
            self.move_dir = 1
            self.x += 0.5
            pass
        self.rect.centerx = self.x
        pass
    
    def blitme(self):
        '''绘制'''
        if self.active_flag:
            self.screen.blit(self.image, self.rect)
            pass
        pass
    
    pass


'''固定弹'''
class AlienBullet1(Sprite):
    
    def __init__(self, alien):
        '''初始化子弹'''
        Sprite.__init__(self)
        # load informations from alien
        self.alien = alien
        self.screen = alien.screen
        # init image
        self.image = pygame.image.load('images/alien_bullet_1.png')
        self.image_rect = self.image.get_rect()
        # init decision point
        self.decision_point = pygame.image.load('images/decision_point_2.png')
        self.rect = self.decision_point.get_rect()
        # init the location
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        # init the image location
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        # shoot angle
        self.angle = self.alien.shoot_angle
        # speed
        self.speed = self.alien.bullet_speed
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y += self.speed * math.cos(self.angle)
        self.x += self.speed * math.sin(self.angle)
        self.rect.centery = self.y
        self.rect.centerx = self.x
        self.image_rect.centery = self.y
        self.image_rect.centerx = self.x
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.image_rect)
        pass
    
    pass


'''瞄准弹'''
class AlienBullet2(Sprite):
    
    def __init__(self, alien, ship):
        '''初始化子弹'''
        Sprite.__init__(self)
        self.target = ship
        self.alien = alien
        self.screen = alien.screen
        # init image
        self.image = pygame.image.load('images/alien_bullet_1.png')
        self.image_rect = self.image.get_rect()
        # decision point
        self.decision_point = pygame.image.load('images/decision_point_2.png')
        self.rect = self.decision_point.get_rect()
        # location
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        self.move_x = self.target.image_rect.centerx - self.alien.rect.centerx
        self.move_y = self.target.image_rect.centery - self.alien.rect.centery
        self.image_rect.x = self.rect.centerx
        self.image_rect.y = self.rect.centery
        # speed
        self.speed = self.alien.bullet_speed
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y += self.speed * \
        float(self.move_y) / math.sqrt(self.move_x**2 + self.move_y**2)
        self.x += self.speed * \
        float(self.move_x) / math.sqrt(self.move_x**2 + self.move_y**2)
        self.rect.centery = self.y
        self.rect.centerx = self.x
        self.image_rect.centerx = self.x
        self.image_rect.centery = self.y
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.image_rect)
        pass
    
    pass


'''固定弹'''
class AlienBullet3(Sprite):
    
    def __init__(self, alien):
        '''初始化子弹'''
        Sprite.__init__(self)
        # load informations from alien
        self.alien = alien
        self.screen = alien.screen
        # init image
        self.image = pygame.image.load('images/alien_bullet_2.png')
        self.image_rect = self.image.get_rect()
        # init decision point
        self.decision_point = pygame.image.load('images/decision_point_2.png')
        self.rect = self.decision_point.get_rect()
        # init the location
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        # init the image location
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        # shoot angle
        self.angle = self.alien.shoot_angle
        # speed
        self.speed = self.alien.bullet_speed
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y += self.speed * math.cos(self.angle)
        self.x += self.speed * math.sin(self.angle)
        self.rect.centery = self.y
        self.rect.centerx = self.x
        self.image_rect.centery = self.y
        self.image_rect.centerx = self.x
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.image_rect)
        pass
    
    pass


'''瞄准弹'''
class AlienBullet4(Sprite):
    
    def __init__(self, alien, ship):
        '''初始化子弹'''
        Sprite.__init__(self)
        self.target = ship
        self.alien = alien
        self.screen = alien.screen
        # init image
        self.image = pygame.image.load('images/alien_bullet_2.png')
        self.image_rect = self.image.get_rect()
        # decision point
        self.decision_point = pygame.image.load('images/decision_point_2.png')
        self.rect = self.decision_point.get_rect()
        # location
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        self.move_x = self.target.image_rect.centerx - self.alien.rect.centerx
        self.move_y = self.target.image_rect.centery - self.alien.rect.centery
        self.image_rect.x = self.rect.centerx
        self.image_rect.y = self.rect.centery
        # speed
        self.speed = self.alien.bullet_speed
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y += self.speed * \
        float(self.move_y) / math.sqrt(self.move_x**2 + self.move_y**2)
        self.x += self.speed * \
        float(self.move_x) / math.sqrt(self.move_x**2 + self.move_y**2)
        self.rect.centery = self.y
        self.rect.centerx = self.x
        self.image_rect.centerx = self.x
        self.image_rect.centery = self.y
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.image_rect)
        pass
    
    pass


'''固定弹'''
class AlienBullet5(Sprite):
    
    def __init__(self, alien):
        '''初始化子弹'''
        Sprite.__init__(self)
        # load informations from alien
        self.alien = alien
        self.screen = alien.screen
        # init image
        self.image = pygame.image.load('images/alien_bullet_3.png')
        self.image_rect = self.image.get_rect()
        # init decision point
        self.decision_point = pygame.image.load('images/decision_point_1.png')
        self.rect = self.decision_point.get_rect()
        # init the location
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        # init the image location
        self.image_rect.centerx = self.rect.centerx
        self.image_rect.centery = self.rect.centery
        # shoot angle
        self.angle = self.alien.shoot_angle
        # speed
        self.speed = self.alien.bullet_speed
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y += self.speed * math.cos(self.angle)
        self.x += self.speed * math.sin(self.angle)
        self.rect.centery = self.y
        self.rect.centerx = self.x
        self.image_rect.centery = self.y
        self.image_rect.centerx = self.x
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.image_rect)
        pass
    
    pass


'''瞄准弹'''
class AlienBullet6(Sprite):
    
    def __init__(self, alien, ship):
        '''初始化子弹'''
        Sprite.__init__(self)
        self.target = ship
        self.alien = alien
        self.screen = alien.screen
        # init image
        self.image = pygame.image.load('images/alien_bullet_3.png')
        self.image_rect = self.image.get_rect()
        # decision point
        self.decision_point = pygame.image.load('images/decision_point_1.png')
        self.rect = self.decision_point.get_rect()
        # location
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom
        self.y = float(self.rect.centery)
        self.x = float(self.rect.centerx)
        self.move_x = self.target.image_rect.centerx - self.alien.rect.centerx
        self.move_y = self.target.image_rect.centery - self.alien.rect.centery
        self.image_rect.x = self.rect.centerx
        self.image_rect.y = self.rect.centery
        # speed
        self.speed = self.alien.bullet_speed
        pass
    
    def update(self):
        '''更新子弹位置信息'''
        self.y += self.speed * \
        float(self.move_y) / math.sqrt(self.move_x**2 + self.move_y**2)
        self.x += self.speed * \
        float(self.move_x) / math.sqrt(self.move_x**2 + self.move_y**2)
        self.rect.centery = self.y
        self.rect.centerx = self.x
        self.image_rect.centerx = self.x
        self.image_rect.centery = self.y
        pass
    
    def blitme(self):
        '''画出子弹'''
        self.screen.blit(self.image, self.image_rect)
        pass
    
    pass