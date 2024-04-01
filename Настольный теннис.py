
import pygame
size = width, height = (640, 480)
screen = pygame.display.set_mode(size)
fps = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont(None, 30)

def button(x_button, y_button, width_button, height_button, stroka):
    color = pygame.Color(50, 150, 150)
    pygame.draw.rect(screen, color, (x_button+3, y_button+3, width_button, height_button), 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2]+30, hsv[3])
    pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 0)
    color.hsva = (hsv[0], hsv[1], hsv[2], hsv[3])
    pygame.draw.rect(screen, color, (x_button, y_button, width_button, height_button), 3)
    
    font = pygame.font.SysFont('timesnewroman', 30, bold = True, italic = False)
    text = font.render(stroka, 0, (255, 0, 0))
    dx = width_button//2 - text.get_width()//2
    dy = height_button//2 - text.get_height()//2
    screen.blit(text, (x_button + dx, y_button + dy)) 


x=320
y=240
r=10
vx=3
vy=3

br_x=500
br_y=200
br_w=10
br_h=100
score_r = 0
b_speed=5
bl_x=100
bl_y=200
bl_w=10
bl_h=100
score_l = 0

width_button = 200
height_button = 50
x_button = width//2 - width_button//2
y_button = 200

PAGE = 'menu'
color_bg = 'white'

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        keyboard = pygame.key.get_pressed()
        buttons_mouse = pygame.mouse.get_pressed()
        pos_mouse = pygame.mouse.get_pos()
        
        if keyboard[pygame.K_o]:
            br_y -= b_speed             
        if keyboard[pygame.K_l]:
            br_y += b_speed
        if keyboard[pygame.K_w]:
            bl_y -= b_speed
        if keyboard[pygame.K_s]:
            bl_y += b_speed
        
    screen.fill(color_bg)
    
    if PAGE == 'menu':
        button(x_button, y_button, width_button, height_button, 'Начать')
        button(x_button, y_button + 60, width_button, height_button, 'Помощь')
        button(x_button, y_button + 120, width_button,height_button, 'Выход')    
        
        if pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button and pos_mouse[1]<y_button+height_button and buttons_mouse[0]:       
            PAGE = 'game'
            
        if pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button+60 and pos_mouse[1]<y_button+60+height_button and buttons_mouse[0]:       
            PAGE = 'help'
            
        if pos_mouse[0]>x_button and pos_mouse[0]<x_button+width_button and pos_mouse[1]>y_button+120 and pos_mouse[1]<y_button+120+height_button and buttons_mouse[0]:       
            PAGE = 'exit'               
            
    if PAGE == 'help':
        color_bg = 'white'
        
        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu' 
            color_bg = 'white'
            
        font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
        text = font.render("                    ", 0, (255, 0, 0))
        dx = width_button//2 - text.get_width()//2
        screen.blit(text, (dx, 50)) 
            
        font = pygame.font.SysFont('timesnewroman',20, bold = True, italic = False)
        text = font.render("Управление платформой:", 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 70))
        
        font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
        text = font.render("Чтобы запустить шарик, нужно нажать на ПРОБЕЛ", 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 90)) 
        
        font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
        text = font.render("Платформа управляется СТРЕЛКАМИ", 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 110))  
        
        font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
        text = font.render("Для победы нужно сбить все блоки", 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 130))  
        
        font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
        text = font.render("Если шарик платформой не отбить - то ты проиграл", 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 150)) 
        
        font = pygame.font.SysFont('timesnewroman', 20, bold = True, italic = False)
        text = font.render("Удачи в игре!", 0, (255, 0, 0))
        dx = width//2 - text.get_width()//2
        screen.blit(text, (dx, 230))          
            
    if PAGE == 'exit':
        run = False
            
    if PAGE == 'game':
        
        if keyboard[pygame.K_ESCAPE]:
            PAGE = 'menu' 
        
        pygame.draw.circle(screen, 'red', (x, y), r, 3)
        x+=vx
        y+=vy
        
        if x+r>740:
            score_r += 1
            x=150
            y=240        
         
        if x-r<-100:
            score_l += 1 
            x=450
            y=240        
        
        if y+r>480 or y-r<0:
            vy=-vy
        
        pygame.draw.rect(screen, 'black', (br_x, br_y, br_w, br_h), 0)
        if x+r>br_x and x-r<br_x+br_w and y+r>br_y and y-r<br_y+br_h:
            vx=-vx
        
        pygame.draw.rect(screen, 'black', (bl_x, bl_y, bl_w, bl_h), 0)
        if x+r>bl_x and x-r<bl_x+bl_w and y+r>bl_y and y-r<bl_y+bl_h:
            vx=-vx    
    
        text_l = font.render("Игрок 1", False, (0, 0, 0))
        text_r = font.render("Игрок 2", False, (0, 0, 0))
        screen.blit(text_l, (70, 0))
        screen.blit(text_r, (470, 0))
    
        text_l = font.render(str(score_l), True, (255, 0, 0))
        text_r = font.render(str(score_r), True, (255, 0, 0))
        screen.blit(text_l, (100, 30))
        screen.blit(text_r, (500, 30))
        
        if score_l>=11:
            text = font.render("Победил Игрок 2", True, (255, 0, 0))
            screen.blit(text, (width//2 - text.get_width()//2, 240))
            vx=0
            vy=0
            
        
        if score_r>=11:
            text = font.render("Победил Игрок 1", True, (255, 0, 0))
            screen.blit(text, (width//2 - text.get_width()//2, 240))
            vx=0
            vy=0
                
                
            
            
    pygame.display.flip()
    fps.tick(60)
pygame.quit()