# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 22:01:07 2018

@author: wmy
"""

import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
import random
import numpy as np
import math
import time
from ship import Ship, ShipBullet
from stars import Star
from settings import Settings
from aliens import Alien1, AlienBullet1, AlienBullet2, Alien2, \
AlienBullet3, AlienBullet4, AlienBullet5, AlienBullet6, Alien3
from booms import Boom1

class AlineGame(Settings):
    
    def __init__(self):
        '''初始化游戏'''
        Settings.__init__(self)
        # boom init
        self.booms = Group()
        self.ship_boom = Boom1()
        self.boom_count = 0
        # background
        self.background_picture = "images/background_1.jpg"
        self.background_arrow = 0
        # music init
        self.music_count = 0
        # screen init
        self.screen_size = (self.screen_width, self.screen_height)
        # stars init
        self.stars = Group()
        for i in range(self.num_stars):
            new_star = Star()
            self.stars.add(new_star)
            pass
        # ship
        self.ship = Ship()
        self.ship_bullets = Group()
        # aliens
        self.aliens = Group()
        self.aliens_bullets = Group()
        pass
    
    def screen_init(self):
        '''显示屏初始化'''
        self.screen_size = (self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)
        pass
    
    def show_stars(self):
        '''显示星空'''
        for star in self.stars.sprites():
            star.blitme()
            pass
        pass
    
    def show_aliens(self):
        '''显示alien'''
        for alien in self.aliens.sprites():
            alien.blitme()
            pass
        pass
    
    def screen_clear(self):
        '''清屏'''
        self.screen.blit(self.background, (0, self.background_arrow - self.screen_height))
        self.screen.blit(self.background, (0, self.background_arrow))
        self.background_arrow += 1
        if self.background_arrow >= self.screen_height:
            self.background_arrow = 0
            pass
        pass
    
    def play_music(self):
        if self.music_play_flag and pygame.mixer.music.get_busy() == False:
            self.music_count += 1
            if self.music_count > self.num_musics:
                self.music_count = 1
            pygame.mixer.music.load("musics/" + str(self.music_count) + ".mp3")
            pygame.mixer.music.play()
            pass
        pass
    
    def check_events(self):
        '''事件处理'''
        for event in pygame.event.get():                
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                self.music_play_flag = False
                sys.exit()
                pass
            pass
        pressed_keys = pygame.key.get_pressed()
        # right
        if pressed_keys[pygame.K_RIGHT] and self.ship.alive_flag:
            self.ship.moving_right = True
            pass
        else:
            self.ship.moving_right = False
            pass
        # left
        if pressed_keys[pygame.K_LEFT] and self.ship.alive_flag:
            self.ship.moving_left = True
            pass
        else:
            self.ship.moving_left = False
            pass
        # up
        if pressed_keys[pygame.K_UP] and self.ship.alive_flag:
            self.ship.moving_up = True
            pass
        else:
            self.ship.moving_up = False
            pass
        # down
        if pressed_keys[pygame.K_DOWN] and self.ship.alive_flag:
            self.ship.moving_down = True
            pass
        else:
            self.ship.moving_down = False
            pass
        # shoot
        if pressed_keys[pygame.K_z] and self.ship.alive_flag:
            self.ship.fire_flag = True
            pass
        else:
            self.ship.fire_flag = False
            pass
        # restart
        if pressed_keys[pygame.K_SPACE]:
            if len(self.ship_group) == 0:
                self.ship_boom.life_count = 60
                self.ship_boom.start_flag = False
                self.ship.alive_flag = True
                for bullet in self.ship_bullets.copy():    
                    if bullet.rect.centerx < self.ship.rect.centerx + 250 and \
                    bullet.rect.centerx > self.ship.rect.centerx - 250 and \
                    bullet.rect.centery > self.ship.rect.centery - 250 and \
                    bullet.rect.centery < self.ship.rect.centery + 250:               
                        self.ship_bullets.remove(bullet)
                        pass      
                    pass
                for bullet in self.aliens_bullets.copy(): 
                    if bullet.rect.centerx < self.ship.rect.centerx + 250 and \
                    bullet.rect.centerx > self.ship.rect.centerx - 250 and \
                    bullet.rect.centery > self.ship.rect.centery - 250 and \
                    bullet.rect.centery < self.ship.rect.centery + 250:                             
                        self.aliens_bullets.remove(bullet)
                        pass
                    pass
                self.ship_group.add(self.ship)
                pass
            pass
        # slow down
        if pressed_keys[pygame.K_LSHIFT] and self.ship.alive_flag:
            self.ship.speed = self.ship_slow_speed
            pass
        else:
            self.ship.speed = self.ship_normal_speed
            pass
        pass
    
    def ship_fire(self):
        '''ship fire update'''
        # ship fire
        if self.ship.fire_flag == True and self.ship.fire_count >= self.ship.fire_wait_time:
            if self.ship.speed == self.ship_normal_speed:
                # 1
                new_bullet = ShipBullet(self.ship)
                self.ship_bullets.add(new_bullet)
                # 2
                new_bullet = ShipBullet(self.ship)
                new_bullet.angle = float(3.1415926/12)             
                self.ship_bullets.add(new_bullet)
                # 3
                new_bullet = ShipBullet(self.ship)
                new_bullet.angle = float(-3.1415926/12)
                self.ship_bullets.add(new_bullet)
                # 4
                new_bullet = ShipBullet(self.ship)
                new_bullet.angle = float(3.1415926/24)
                self.ship_bullets.add(new_bullet)
                # 5
                new_bullet = ShipBullet(self.ship)
                new_bullet.angle = float(-3.1415926/24)
                self.ship_bullets.add(new_bullet)
                pass
            else:
                # 1
                new_bullet = ShipBullet(self.ship)
                self.ship_bullets.add(new_bullet)
                # 2
                new_bullet = ShipBullet(self.ship)
                new_bullet.x += 24
                self.ship_bullets.add(new_bullet)
                # 3
                new_bullet = ShipBullet(self.ship)
                new_bullet.x -= 24
                self.ship_bullets.add(new_bullet)
                # 4
                new_bullet = ShipBullet(self.ship)
                new_bullet.x += 12
                self.ship_bullets.add(new_bullet)
                # 5
                new_bullet = ShipBullet(self.ship)
                new_bullet.x -= 12
                self.ship_bullets.add(new_bullet)
                pass
            self.ship.fire_count = 0
            pass
        self.ship.fire_count += 1
        # show ship bullets
        for bullet in self.ship_bullets.sprites():
            bullet.blitme()
            pass
        pass
    
    def compute_damage(self):
        '''计算伤害'''
        crashed = pygame.sprite.groupcollide(self.aliens, self.ship_bullets, False, True)   
        for alien in self.aliens:
            try:
                crashed[alien]
                pass
            except:
                pass
            else:
                if self.ship.speed == self.ship_slow_speed:
                    alien.num_life -= 3.5
                else:
                    alien.num_life -= 1        
                if alien.num_life <= 0: 
                    i = 0
                    self.boom_count += 1
                    for boom in self.booms.sprites():
                        i += 1
                        if i == self.boom_count:
                            boom.start_flag = True
                            boom.rect.centerx = alien.rect.centerx
                            boom.rect.centery = alien.rect.centery
                            boom.blitme()
                            break
                        pass
                    self.aliens.remove(alien)
                    pass
                pass
            pass
        pygame.sprite.groupcollide(self.aliens_bullets, self.ship_group, True, True)
        if(len(self.ship_group)==0):
            self.ship.alive_flag = False
            self.ship_boom.start_flag = True
            self.ship_boom.rect.centerx = self.ship.rect.centerx
            self.ship_boom.rect.centery = self.ship.rect.centery
            self.ship_boom.blitme()
            time.sleep(0.1)
            pass    
        pass
    
    def update_booms(self):
        self.ship_boom.update()
        self.ship_boom.blitme()
        for boom in self.booms.sprites():
            boom.update()
            boom.blitme()
            pass
        pass
    
    def delete_bullets(self):
        '''删除出屏幕的子弹'''
        for bullet in self.ship_bullets.copy():
            if bullet.rect.bottom < 0:
                self.ship_bullets.remove(bullet)
                pass
            pass
        for bullet in self.aliens_bullets.copy():
            if bullet.image_rect.top >= self.screen_height or \
            bullet.image_rect.right <= 0 or bullet.image_rect.left >= self.screen_width or \
            bullet.image_rect.bottom <= 0:
                self.aliens_bullets.remove(bullet)
                pass
            pass
        pass  
    
    def aliens_appear(self):
        if len(self.aliens) <= sum(self.aliens_sets) - self.aliens_sets[0] + 1 \
        and len(self.aliens) > sum(self.aliens_sets) - self.aliens_sets[0] - self.aliens_sets[1] + 1:
            self.alien_num_on_screen = self.aliens_num_on_screen_list[0]
            self.aliens_num_on_screen_list.remove(self.aliens_num_on_screen_list[0])
            self.aliens_sets.remove(self.aliens_sets[0])
            pass
        if len(self.aliens) < self.alien_count:              
            for alien in self.aliens:
                self.alien_count -= 1
                self.alien_appear_count += 1
                alien.active_flag = True
                if self.alien_appear_count >= self.alien_num_on_screen:
                    self.alien_appear_count = 0
                    break
                pass
            pass
        pass
    
    def creat_aliens(self):
        self.aliens_sets = []
        self.aliens_num_on_screen_list = []
        for i in range(60):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien1()
            alien.type = '1'
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(60)
        '''the first group of aliens'''
        self.alien_num_on_screen = 15
        for i in range(40):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien2()
            alien.type = '2'
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(40)
        self.aliens_num_on_screen_list.append(10)
        for i in range(60):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien1()
            alien.type = '3'
            alien.shoot_angle = -float(3.1415926/4)
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(60)
        self.aliens_num_on_screen_list.append(15)
        for i in range(40):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien2()
            alien.fire_wait_time = 300
            alien.num_life = 30
            alien.type = '4'
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(40)
        self.aliens_num_on_screen_list.append(10)
        for i in range(8):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien1()
            alien.num_life = 30
            alien.type = '5'
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(8)
        self.aliens_num_on_screen_list.append(2)
        for i in range(12):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien1()
            alien.num_life = 20
            alien.type = '6'
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(12)
        self.aliens_num_on_screen_list.append(3)
        for i in range(4):
            boom = Boom1()
            self.booms.add(boom)
            alien = Alien3()
            alien.num_life = 50
            alien.fire_wait_time = 20
            alien.type = '7'
            self.aliens.add(alien)
            pass
        self.aliens_sets.append(4)
        self.aliens_num_on_screen_list.append(1)
        # init appear aliens
        self.aliens_sets.append(0)
        self.alien_count = len(self.aliens) + 1
        self.alien_appear_count = 0
        pass
    
    def aliens_fire(self):
        '''开火状态更新'''
        # alien fire
        for alien in self.aliens.sprites():
            if alien.fire_count >= alien.fire_wait_time and alien.active_flag:
                if alien.type == '1':
                    new_bullet = AlienBullet2(alien, self.ship)
                    self.aliens_bullets.add(new_bullet)
                    pass
                elif alien.type == '2':
                    new_bullet = AlienBullet4(alien, self.ship)
                    self.aliens_bullets.add(new_bullet)
                    new_bullet = AlienBullet3(alien)
                    self.aliens_bullets.add(new_bullet)
                    pass
                elif alien.type == '3':
                    if alien.shoot_angle <= float(3.1415926/4) and alien.shoot_move_dir == 1:
                        alien.shoot_angle += float(3.1415926/24) 
                        pass 
                    elif alien.shoot_angle >= float(3.1415926/4) and alien.shoot_move_dir == 1:
                        alien.shoot_angle -= float(3.1415926/24) 
                        alien.shoot_move_dir = -1
                        pass
                    elif alien.shoot_angle >= -float(3.1415926/4) and alien.shoot_move_dir == -1:
                        alien.shoot_angle -= float(3.1415926/24) 
                        pass
                    elif alien.shoot_angle <= -float(3.1415926/4) and alien.shoot_move_dir == -1:
                        alien.shoot_angle += float(3.1415926/24) 
                        alien.shoot_move_dir = 1
                        pass
                    new_bullet = AlienBullet1(alien)      
                    self.aliens_bullets.add(new_bullet)
                    pass
                elif alien.type == '4':
                    new_bullet = AlienBullet6(alien, self.ship)
                    new_bullet.speed = 2
                    self.aliens_bullets.add(new_bullet)
                    new_bullet = AlienBullet6(alien, self.ship)
                    new_bullet.speed = 3
                    self.aliens_bullets.add(new_bullet)
                    new_bullet = AlienBullet6(alien, self.ship)
                    new_bullet.speed = 4
                    self.aliens_bullets.add(new_bullet)
                    new_bullet = AlienBullet6(alien, self.ship)
                    new_bullet.speed = 5
                    self.aliens_bullets.add(new_bullet)
                    new_bullet = AlienBullet6(alien, self.ship)
                    new_bullet.speed = 6
                    self.aliens_bullets.add(new_bullet)
                    new_bullet = AlienBullet6(alien, self.ship)
                    new_bullet.speed = 7
                    self.aliens_bullets.add(new_bullet)
                    pass
                elif alien.type == '5':
                    for i in range(0, 24):
                        new_bullet = AlienBullet3(alien)
                        new_bullet.angle = float(3.1415926*i/12)
                        self.aliens_bullets.add(new_bullet)
                        pass
                    pass
                elif alien.type == '6':
                    for i in range(0, 12):
                        new_bullet = AlienBullet3(alien)
                        new_bullet.angle = float(3.1415926*i/6)
                        self.aliens_bullets.add(new_bullet)
                        pass
                    pass
                elif alien.type == '7':
                    for i in range(0, 24):
                        new_bullet = AlienBullet3(alien)
                        new_bullet.angle = float(3.1415926*i/12)
                        self.aliens_bullets.add(new_bullet)
                        pass
                    pass
                alien.fire_count = 0
                pass
            alien.fire_count += 1
            pass
        # show aliens bullets
        for bullet in self.aliens_bullets.sprites():
            bullet.blitme()
            pass
        self.ship.blitme()
        pass
    
    def run_game(self):
        '''运行游戏'''
        pygame.init()
        pygame.mixer.init()
        self.screen_init()
        self.ship_group = Group()
        self.ship_group.add(self.ship)
        pygame.display.set_caption("Alien Invasion")
        self.background = pygame.image.load(self.background_picture).convert()
        self.creat_aliens()
        while True:
            self.screen_clear()
            self.aliens_appear()
            self.aliens.update()
            self.check_events()
            self.ship_fire()
            self.aliens_fire()
            self.compute_damage()
            self.play_music()
            self.show_aliens()
            self.stars.update()
            self.delete_bullets()
            self.show_stars()
            self.update_booms()
            self.ship.update()
            self.ship.blitme()
            self.ship_bullets.update()
            self.aliens_bullets.update()
            pygame.display.flip()
            pass
        pass
    
    pass
    
game = AlineGame()
game.run_game()  