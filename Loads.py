#load files
import pygame as pg


pg.init()
button_font = pg.font.SysFont("Veranda", 20)
piece_font = button_font
credits_font = button_font


block_reg_texture = pg.image.load("Assets/block_reg.png")
block_simple_texture = pg.image.load("Assets/block_simple.png")
block_gradient_texture = pg.image.load("Assets/block_gradient.png")
door_texture = pg.image.load("Assets/door.png")
bg_texture = pg.image.load("Assets/bg_all.png")


#for parallax
bg_back = pg.image.load("Assets/bg_back.png")
bg_bot = pg.image.load("Assets/bg_bot.png")
bg_mid = pg.image.load("Assets/bg_mid.png")
bg_top = pg.image.load("Assets/bg_top.png")

