from pygame import *
init()
#setting dimension variable
s_wid=500
s_hei=500
r_size=50
#setting color variable
black=(0,0,0)
white=(250,250,250)
yellow=(255,255,0)
#creating windows of pygame
screen=display.set_mode((s_wid,s_hei))
screen.fill(black)
#creating object
draw.rect(screen,yellow,(0,0,r_size,r_size))
#runing variable
run=True
#gaming loop
while run:
    for e in event.get():
        if e.type==QUIT:
            run=False
        elif e.type==MOUSEMOTION:
            rect_x,rect_y=mouse.get_pos()
            if(rect_x<s_wid-r_size and rect_y<s_hei-r_size):
                screen.fill(black)
                draw.rect(screen,yellow,(rect_x,rect_y,r_size,r_size))
    display.update()
quit()
