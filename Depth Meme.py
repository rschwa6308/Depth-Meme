
from Levels import *
from Classes import *


speed = 7
cam_buffer = 200        #pixel buffer maintained around player by camera










#init window
pg.init()
dim = (800,640)
screen = pg.display.set_mode(dim)



###           width x height x depth
###constructs   25  x  20    x   3    3d array
##level = [[[0 for x in range(30)] for y in range(20)] for z in range(3)]
##
##level[0][15][10] = 1
##
##level[1][15][10] = 1
##level[1][15][11] = 1
##
##level[2][15][10] = 1
##level[2][15][11] = 1
##level[2][15][12] = 1





#draws given frame and player to screen
def display(frame, player, layers, x_disp):
    #detirmine if camera is applied
    if abs(player.screen_x-dim[0]) <= cam_buffer:
        cam = True
    else:
        cam = False
        
    #background layers
    screen.blit(bg_back, (0,0))
    for layer in layers:
        screen.blit(layer.image, (layer.x, 0))
        if cam:
            layer.get_vel(player.vect, layer.ratio)
            layer.parallax()
    if cam:
        x_disp = dim[0]-player.x-cam_buffer
            
    #blocks
    for y in range(len(frame)):
        for x in range(len(frame[y])):
            if frame[y][x] is 1:
                screen.blit(block_gradient_texture, (x*32+x_disp,y*32))
            elif frame[y][x] is 2:
                screen.blit(door_texture, (x*32+x_disp,y*32))
                
                
    #player
    player.screen_x = player.x + x_disp
    screen.blit(player.image, (player.screen_x, player.y))
    #flip display
    pg.display.update()




def overlay(screen, buttons):
    #box
    box = pg.Surface((300,400))
    box.fill(white)

    #border
    pg.draw.rect(box, grid_color, pg.Rect(0,0,299,399),2)

    #heading
    head_img = piece_font.render("Success!",True,grid_color)
    box.blit(head_img, (box.get_width()/2-head_img.get_width()/2,box.get_height()/2-head_img.get_height()/2-150))

    #message
    mess_img_0 = credits_font.render("You beat the level.", True, grid_color)
    mess_img_1 = credits_font.render("Great work!",True,grid_color)
    box.blit(mess_img_0, (box.get_width()/2-mess_img_0.get_width()/2,box.get_height()/2-mess_img_0.get_height()/2-75))
    box.blit(mess_img_1, (box.get_width()/2-mess_img_1.get_width()/2,box.get_height()/2-mess_img_1.get_height()/2-50))

    #buttons
    for button in buttons:
        box.blit(button.get_image(), (button.x,button.y))
        
    #blit box to screen
    screen.blit(box,(250,100))
    
    #flip display
    pg.display.update()






#build level
#level = build_level(test_level)

###prints level in readable format
##for frame in level:
##    for row in frame:
##        print row
##    print "\n"





#init bg layers
layer_1 = BgLayer(bg_bot, 0, -0.1)  #-0.1
layer_2 = BgLayer(bg_mid, 0, -0.3)  #-0.3
layer_3 = BgLayer(bg_top, 0, -0.5)  #-0.5
layers = [layer_1, layer_2, layer_3]

#init camera vars
x_disp = 0




#init room
player = Player(5,15)

z = 0
display(level[z], player, layers, x_disp)



clock = pg.time.Clock()

done = False
while not done:
    clock.tick(60)
    #user input
    for event in pg.event.get():
        #quit window
        if event.type == pg.QUIT:
            done = True
        #mouse input
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                pos = get_grid(player.x+15,player.y+15)
                if z < len(level)-1 and level[z+1][pos[1]][pos[0]] is 0:    #check not last frame and dest is empty
                    z += 1
                    display(level[z], player, layers, x_disp)
            elif event.button == 5:
                pos = get_grid(player.x+15,player.y+15)
                if z > 0  and level[z-1][pos[1]][pos[0]] is 0:              #check not last frame and dest is empty
                    z -= 1
                    display(level[z], player, layers, x_disp)

        #keyboard input
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                pass
            elif event.key == pg.K_DOWN:
                pass
            elif event.key == pg.K_w:
                if player.on_ground:
                    player.vect[1] = -speed
            elif event.key == pg.K_s:
                player.vect[1] = speed
            elif event.key == pg.K_a:
                player.vect[0] = -speed
            elif event.key == pg.K_d:
                player.vect[0] = speed
                
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                player.vect[1] = 0
            elif event.key == pg.K_s:
                player.vect[1] = 0
            elif event.key == pg.K_a:
                player.vect[0] = 0
            elif event.key == pg.K_d:
                player.vect[0] = 0

    #gravity
    player.vect[1] += 0.2

    #floor detection
    if player.y >= dim[1]-30 and player.vect[1] > 0:
        player.vect[1] = 0
        player.y = dim[1]-30
        player.on_ground = True
    else:
        player.on_ground = False

    #left wall detection
    if player.x <= 0 and player.vect[1] < 0:
        player.vect[0] = 0
        player.x = 0
        
    #right wall detection
    if player.x >= dim[0] and player.vect[1] > 0:
        player.vect[0] = dim[0]
        player.x = dim[0]


    #apply player collision
    if player.vect[1] > 0:      #bottom
        if player.collide_bottom(level[z]):
            player.vect[1] = 0
            player.on_ground = True
        else:
            on_ground = False

    elif player.vect[1] < 0:    #top
        if player.collide_top(level[z]):
            player.vect[1] *= -0.2 + 0.01

    if player.vect[0] < 0:      #left
        if player.collide_left(level[z]):
            pos = get_grid(player.x+15+x_disp, player.y+15)
            player.x = pos[0]*32
            player.vect[0] = 0
            
    elif player.vect[0] > 0:    #right
        if player.collide_right(level[z]):
            pos = get_grid(player.x+15+x_disp, player.y+15)
            player.x = pos[0]*32+2
            player.vect[0] = 0


    #door collision
    pos = get_grid(player.x+15+x_disp, player.y+15)
    if level[z][pos[1]][pos[0]] == 2:
        print "door"
        ###pop up window###
        buttons = [
            Button(20,190,260,50, grid_color, piece_color, button_font, "Next Level","N"),
            Button(20,260,260,50, grid_color, piece_color, button_font, "Replay","R"),
            Button(20,330,260,50, grid_color, piece_color, button_font, "Home","H")
            
        ]
        overlay(screen, buttons)
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                
                #down button
                elif event.type == pg.MOUSEBUTTONDOWN:
                    for button in buttons:
                       if button.rect.collidepoint((event.pos[0]-250,event.pos[1]-100)):   #compensate for offset origin
                           button.hover = 3
                           overlay(screen, buttons)

                #up button
                elif event.type == pg.MOUSEBUTTONUP:
                    for button in buttons:
                        if button.hover == 3:   #include 'button.rect.collidepoint(event.pos)' if cursor must be over button to activate
                            button.hover = 0
                            overlay(screen, buttons)
                            #programmatic control
                            if button.key == "N":
                                main(screen, level+1)
                                done = True
                            elif button.key == "R":
                                print "restart"
                                main(screen, level)    #does not work!?!?!
                                done = True
                            elif button.key == "H":
                                done = True
                                
            #hover shading
            pos = (pg.mouse.get_pos()[0]-250,pg.mouse.get_pos()[1]-100)  #compensate for offset origin
            for button in buttons:
                if button.rect.collidepoint(pos) and button.hover == 0:
                    button.hover = 1
                    overlay(screen, buttons)
                elif not button.rect.collidepoint(pos) and button.hover == 1:   #will only update screen when necessary
                    button.hover = 0
                    overlay(screen, buttons)
        
    
        
    player.apply_motion()
    display(level[z], player, layers, x_disp)





pg.quit()
