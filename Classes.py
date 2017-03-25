#Classes

from Loads import *
from Colors import *
from Funcs import *

class Player():
    def __init__(self, x, y):
        self.x = x*32
        self.y = y*32

        self.screen_x = x
        
        self.vect = [0,0]
        
        self.image = pg.Surface((30,30))
        self.image.fill(blue)

        self.on_ground = False



    def apply_motion(self):
        self.x += self.vect[0]
        self.y += self.vect[1]

    def collide_bottom(self, frame):
        x = self.x+self.vect[0]
        y = self.y+self.vect[1]

        try:
            pos = get_grid(x+1,y+30)
            if frame[pos[1]][pos[0]] == 1:
                return True
            pos = get_grid(x+29,y+30)
            if frame[pos[1]][pos[0]] == 1:
                return True
        except:
            return False

    def collide_top(self, frame):
        x = self.x+self.vect[0]
        y = self.y+self.vect[1]

        pos = get_grid(x+1,y)
        if frame[pos[1]][pos[0]] == 1:
            return True
        pos = get_grid(x+29,y)
        if frame[pos[1]][pos[0]] == 1:
            return True

    def collide_left(self, frame):
        x = self.x+self.vect[0]
        y = self.y+self.vect[1]
        pos = get_grid(x,y+3)
        try:
            if pos[0] <= -1:                        #edge of room
                return True
            if frame[pos[1]][pos[0]] == 1:
                return True
            pos = get_grid(x,y+15)
            if frame[pos[1]][pos[0]] == 1:
                return True
            pos = get_grid(x,y+29)
            if frame[pos[1]][pos[0]] == 1:
                return True
        except:
            return False
        
    def collide_right(self,frame):
        x = self.x+self.vect[0]
        y = self.y+self.vect[1]
        pos = get_grid(x+30,y+3)
        try:
            if pos[0] >= len(frame[pos[1]]):     #edge of room
                return True
            if frame[pos[1]][pos[0]] == 1:
                return True
            pos = get_grid(x+30,y+15)
            if frame[pos[1]][pos[0]] == 1:
                return True
            pos = get_grid(x+30,y+29)
            if frame[pos[1]][pos[0]] == 1:
                return True
        except:
            return False



class BgLayer():
    def __init__(self, image, x, ratio):
        self.x = 0
        self.y = 0
        self.image = image
        self.ratio = ratio
        self.width = 800

        self.vel = 0

    def parallax(self):
        self.x += self.vel

    def get_vel(self, vect, ratio):
        self.vel = vect[0] * ratio

        


class Button():
    def __init__(self, x, y, width, height, color, txt_color, font, text, key):
        self.hover = 0
        self.bg = (255,255,255)
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(x,y,width,height)

        self.color = color
        
        self.txt_color = txt_color
        self.font = font
        self.text = text
        
        self.key = key

    def get_image(self):
        img = pg.Surface((self.width, self.height))
        img.fill((self.bg[0]-50*self.hover,self.bg[1]-50*self.hover,self.bg[2]-50*self.hover))
        bwidth = 2
        buff = bwidth - 1
        pg.draw.rect(img, self.color, pg.Rect(buff, buff, self.width-2*buff, self.height-2*buff), bwidth)
        
        text_img = self.font.render(self.text,1,self.txt_color)
        img.blit(text_img,(self.width/2-text_img.get_width()/2,self.height/2-text_img.get_height()/2))  #auto center text
        return img







        

