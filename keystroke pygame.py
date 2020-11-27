#Importing and initialising pygame
from pygame import *
init()
#declaring variables
red=(250,0,0)
green=(0,250,0)
blue=(0,0,250)
black=(0,0,0)
rect_x=0
rect_y=0
move=20
s_width=700
s_height=700
rectx_side=80
recty_side=30
#setting up screen
screen=display.set_mode((s_width,s_height))
screen.fill(black)
#drawing an object
draw.rect(screen,blue,(rect_x,rect_y,rectx_side,recty_side),1)
#event loop
run=True
while run:
    for e in event.get():
        if e.type==QUIT or (e.type==KEYDOWN and e.key==K_ESCAPE):
            run=False
        elif e.type==KEYDOWN:
            if e.key==K_LEFT and rect_x>0:
                rect_x-=move
            elif e.key==K_RIGHT and rect_x<s_width-rectx_side:
                rect_x+=move
            elif e.key==K_DOWN and rect_y<s_height-recty_side:
                rect_y+=move
            elif e.key==K_UP and rect_y>0:
                rect_y-=move
    screen.fill(black)
    draw.rect(screen,blue,(rect_x,rect_y,rectx_side,recty_side),1)
    display.flip()
quit()
