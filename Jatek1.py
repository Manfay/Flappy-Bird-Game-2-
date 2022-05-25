import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface,(floor_x_pos,600))
    screen.blit(floor_surface,(floor_x_pos+960,600))

def create_pipe():
    random_pipe_pos =random.choice(pipe_height)
    bottom_pipe=pipe_surface.get_rect(midtop=(960,random_pipe_pos))
    top_pipe=pipe_surface.get_rect(midbottom=(960,random_pipe_pos-a))
    return top_pipe,bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 3
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=720:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe =pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
            
def check(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 600:
        return False
    return True

def rotate_bird(bird):
	new_bird = pygame.transform.rotozoom(bird,-bird_movement * 2,1)
	return new_bird
            
def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird,new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        pont_surface =game_font.render('Pont :',True,(255,255,255))
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect =score_surface.get_rect(center =(200,50))
        pont_rect =pont_surface.get_rect(center =(100,50))
        screen.blit(score_surface,score_rect)
        screen.blit(pont_surface,pont_rect)
    if game_state =='game_over':
        pont_surface =game_font.render('Pont :',True,(255,255,255))
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect =score_surface.get_rect(center =(200,50))
        pont_rect =pont_surface.get_rect(center =(100,50))
        screen.blit(score_surface,score_rect)
        screen.blit(pont_surface,pont_rect)

        gold_surface =game_font.render('Gold :',True,(255,255,255))
        score_surface = game_font.render(str(int(gold)),True,(255,255,255))
        score_rect =score_surface.get_rect(center =(700,50))
        gold_rect =gold_surface.get_rect(center =(600,50))
        screen.blit(score_surface,score_rect)
        screen.blit(gold_surface,gold_rect)

        pont_surface =game_font.render('Rekord :',True,(255,255,255))
        high_score_surface = game_font.render(str(int(high_score)),True,(255,255,255))
        high_score_rect =high_score_surface.get_rect(center =(240,100))
        pont_rect =pont_surface.get_rect(center =(120,100))
        screen.blit(high_score_surface,high_score_rect)
        screen.blit(pont_surface,pont_rect)
        screen.blit(penz_surface,penz_rect)
        
def update_score(score,high_score):
    if score>high_score:
        high_score=score
    return high_score

def update_gold(score,gold):
    if gold != score+1000:
        gold += int(score)
    return int(gold)

pygame.mixer.pre_init(frequency =44100, size=-16, channels=2, buffer =4096)        
pygame.init()
screen = pygame.display.set_mode((960,720))
clock = pygame.time.Clock()
game_font=pygame.font.Font('1/04B_19.ttf',40)

pygame.display.set_caption("Marcibird")
icon = pygame.image.load('1/fel2.png')
pygame.display.set_icon(icon)

#gravitáció és minden más változó
gravity = 0.2
bird_movement = 0
gold = 0
game_active=True
score = 0
high_score = 0
a = 250
b=0
c=True
d=0
ertek=50
ertek2=100
e=0
e2=0
f=0
f2=0
g=0
g2=0
gomb=0
v_e=0
v_e2=0
v_f=0
v_f2=0
valaszt=v_e+v_e2+v_f+v_f2
m=0


bg_surface = pygame.image.load('1/background.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

shop_surface=pygame.image.load('1/shop.png').convert()
shop_rect = shop_surface.get_rect(center=(0,0))

shop2_surface=pygame.image.load('1/shop2.png').convert()
shop2_rect = shop_surface.get_rect(center=(0,0))
#madarak
madar_surface=pygame.image.load('1/madar.png').convert()
madar_rect = madar_surface.get_rect(center=(0,0))
vmadar_surface=pygame.image.load('1/vmadar.png').convert()
vmadar_rect = vmadar_surface.get_rect(center=(0,0))

madar1_surface=pygame.image.load('1/madar1.png').convert()
madar1_rect = madar1_surface.get_rect(center=(0,0))
vmadar1_surface=pygame.image.load('1/vmadar1.png').convert()
vmadar1_rect = vmadar1_surface.get_rect(center=(0,0))

madar2_surface=pygame.image.load('1/madar2.png').convert()
madar2_rect = madar2_surface.get_rect(center=(0,0))
vmadar2_surface=pygame.image.load('1/vmadar2.png').convert()
vmadar2_rect = vmadar2_surface.get_rect(center=(0,0))

madar3_surface=pygame.image.load('1/madar3.png').convert()
madar3_rect = madar3_surface.get_rect(center=(0,0))
vmadar3_surface=pygame.image.load('1/vmadar3.png').convert()
vmadar3_rect = vmadar3_surface.get_rect(center=(0,0))

madar4_surface=pygame.image.load('1/madar4.png').convert()
madar4_rect = madar4_surface.get_rect(center=(0,0))
vmadar4_surface=pygame.image.load('1/vmadar4.png').convert()
vmadar4_rect = vmadar4_surface.get_rect(center=(0,0))

floor_surface = pygame.image.load('1/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

penz_surface=pygame.image.load('1/gold.png').convert_alpha()
penz_rect=penz_surface.get_rect(center=(750,50))

bird_le = pygame.image.load('1/le.png').convert_alpha()
bird_normi = pygame.image.load('1/normi.png').convert_alpha()
bird_fel = pygame.image.load('1/fel.png').convert_alpha()

malac1 = pygame.image.load('1/malac.png').convert_alpha()
malac2 = pygame.image.load('1/malac2.png').convert_alpha()
malac3 = pygame.image.load('1/malac3.png').convert_alpha()

m1le = pygame.image.load('1/m1le.png').convert_alpha()
m1norm = pygame.image.load('1/m1norm.png').convert_alpha()
m1fel = pygame.image.load('1/m1fel.png').convert_alpha()

cicale = pygame.image.load('1/cicale.png').convert_alpha()
cicanorm = pygame.image.load('1/cicanorm.png').convert_alpha()
cicafel = pygame.image.load('1/cicafel.png').convert_alpha()

lmadar4 = pygame.image.load('1/lmadár4.png').convert_alpha()
nmadar4 = pygame.image.load('1/nmadár4.png').convert_alpha()
fmadar4 = pygame.image.load('1/fmadár4.png').convert_alpha()

#frames
m1_frames=[m1le,m1norm,m1fel]
malac_frames=[malac2,malac1,malac3]
bird_frames = [bird_le,bird_normi,bird_fel]
cica_frames=[cicale,cicanorm,cicafel]
bird1_frames = [bird_le,bird_normi,bird_fel]
m4_frames=[lmadar4,nmadar4,fmadar4]

bird_index=0
bird_surface= bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center=(100,360))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP,200)

pipe_surface = pygame.image.load('1/oszlop.png').convert_alpha()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list= []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1500)
pipe_height=[250,300,350,400,450,500]

#button
button1_surface=pygame.image.load('1/Button1.png').convert()
button2_surface=pygame.image.load('1/Button2.png').convert()
button3_surface=pygame.image.load('1/Button3.png').convert()
button4_surface=pygame.image.load('1/Button4.png').convert()
button5_surface=pygame.image.load('1/Button5.png').convert()

nyil_surface=pygame.image.load('1/nyil.png').convert()
nyil2_surface=pygame.image.load('1/nyil2.png').convert()
bnyil_surface=pygame.image.load('1/bnyil.png').convert()
bnyil2_surface=pygame.image.load('1/bnyil2.png').convert()

ertek_surface=pygame.image.load('1/ertek.png').convert()
ertek2_surface=pygame.image.load('1/ertek2.png').convert()
click = pygame.mouse.get_pressed()

win_sound= pygame.mixer.Sound('1/win.mp3')
while True:
    #háttérmunka score stb
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #billentyűzet    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 5
                gomb=0
            if event.key == pygame.K_SPACE and game_active==False:
                if gomb ==1:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        pipe_list.clear()
                        bird_rect.center=(100,360)
                        bird_movement=0
                        score =0
                        a = 250
                        bg_surface = pygame.image.load('1/background.png').convert()
                        bg_surface = pygame.transform.scale2x(bg_surface)
                        c=True
                #madárválasztás
                if event.key == pygame.K_SPACE:
                    gomb=1
              
            if score >= 8:
                a=200
            if score >=10:
                bg_surface = pygame.image.load('1/background2.png').convert()
                bg_surface = pygame.transform.scale2x(bg_surface)
            if score >=50:
                bg_surface = pygame.image.load('1/background3.png').convert()
                bg_surface = pygame.transform.scale2x(bg_surface)
            if score >= 48:
                a=150
                
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index <2:
                bird_index +=1
            else:
                bird_index =0
            bird_surface,bird_rect = bird_animation()
    screen.blit(bg_surface,(0,0))

    #él
    if game_active:
        #madár            
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active =check(pipe_list)
        #oszlop
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        score +=0.007
        score_display('main_game')
        
    #meghalt  
    else:
        if gomb!=1:
            high_score = update_score(score,high_score)
            score_display('game_over')
            if c == True:
                gold=update_gold(int(score),int(gold))
                c=False
            #shop első oldal
            if g==0:
                mouse = pygame.mouse.get_pos()
                screen.blit(shop_surface,(240,180))
                screen.blit(madar2_surface,(280,270))
                screen.blit(ertek_surface,(550,290))
                screen.blit(madar1_surface,(280,380))
                screen.blit(ertek2_surface,(550,400))
                screen.blit(nyil_surface,(635,485))
                if 635+60> mouse[0] > 635 and 485+31 > mouse[1] >485:
                    screen.blit(nyil2_surface,(635,485))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        g=1
                        g2=2
                        valaszt=0
                if e2>=1:
                    screen.blit(button5_surface,(450,290))
                    v_e2=1
                else:            
                    if gold >=ertek:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 290+41 > mouse[1] >290:
                            screen.blit(button2_surface,(450,290))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                d=1
                                e2 +=1                  
                        else:
                            screen.blit(button1_surface,(450,290))
                    else:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 290+41 > mouse[1] >290:
                            screen.blit(button4_surface,(450,290))
                        else:
                            screen.blit(button3_surface,(450,290))        
                if f2 >=1:
                    screen.blit(button5_surface,(450,400))
                    v_f2=2
                else:
                    if gold >=ertek2:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 400+41 > mouse[1] >400:
                            screen.blit(button2_surface,(450,400))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                d=2
                                f2+=1
                        else:
                            screen.blit(button1_surface,(450,400))
                    else:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 400+41 > mouse[1] >400:
                            screen.blit(button4_surface,(450,400))
                        else:
                            screen.blit(button3_surface,(450,400))
                if e2 ==1:
                    if d==1:
                        gold -=ertek
                        d=0
                if f2==1:
                    if d==2:
                        gold -=ertek2
                        d=0
            #második oldal            
            else:
                mouse = pygame.mouse.get_pos()
                screen.blit(shop_surface,(240,180))
                screen.blit(madar3_surface,(280,270))
                screen.blit(ertek2_surface,(550,290))
                screen.blit(madar4_surface,(280,380))
                screen.blit(ertek2_surface,(550,400))
                screen.blit(nyil_surface,(635,485))
                screen.blit(bnyil_surface,(265,485))
                if 635+60> mouse[0] > 635 and 485+31 > mouse[1] >485:
                    screen.blit(nyil2_surface,(635,485))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if valaszt==15:
                            g=2
                            g2=3
                    if event.type == pygame.MOUSEBUTTONUP:
                        valaszt=v_e+v_e2+v_f+v_f2
                if 265+60> mouse[0] > 265 and 485+31 > mouse[1] >485:
                    screen.blit(bnyil2_surface,(265,485))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if g2==2:
                            g=0
                if e>=1:
                    screen.blit(button5_surface,(450,290))
                    v_e=4
                else:            
                    if gold >=ertek2:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 290+41 > mouse[1] >290:
                            screen.blit(button2_surface,(450,290))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                d=1
                                e+=1                   
                        else:
                            screen.blit(button1_surface,(450,290))
                    else:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 290+41 > mouse[1] >290:
                            screen.blit(button4_surface,(450,290))
                        else:
                            screen.blit(button3_surface,(450,290))
                if f>=1:
                    screen.blit(button5_surface,(450,400))
                    v_f=8
                else:
                    if gold >=ertek2:
                        mouse = pygame.mouse.get_pos()
                        click = pygame.mouse.get_pressed()
                        if 450+77> mouse[0] > 450 and 400+41 > mouse[1] >400:
                            screen.blit(button2_surface,(450,400))
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                d=2
                                f+=1
                        else:
                            screen.blit(button1_surface,(450,400))
                    else:
                        mouse = pygame.mouse.get_pos()
                        if 450+77> mouse[0] > 450 and 400+41 > mouse[1] >400:
                            screen.blit(button4_surface,(450,400))
                        else:
                            screen.blit(button3_surface,(450,400))
                if e ==1:
                    if d==1:
                        gold -=ertek2
                        d=0
                if f==1:
                    if d==2:
                        gold -=ertek2
                        d=0
            if g==2:
                mouse = pygame.mouse.get_pos()
                screen.blit(shop2_surface,(210,180))
                screen.blit(bnyil_surface,(245,485))
                win_surface =game_font.render('Gratulalok nyertel !',True,(255,255,255))
                win_rect =win_surface.get_rect(center =(480,280))
                screen.blit(win_surface,win_rect)
                win_sound.play()
                if 245+60> mouse[0] > 245 and 485+31 > mouse[1] >485:
                    screen.blit(bnyil2_surface,(245,485))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if g2==3:
                            g=1
                            g2=2
                        win_sound.stop()
        #kiválasztás
        else:
            screen.blit(shop2_surface,(210,180))
            high_score = update_score(score,high_score)
            score_display('game_over')
            valaszt=v_e+v_e2+v_f+v_f2
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if c == True:
                gold=update_gold(int(score),int(gold))
                c=False
            if valaszt ==0:
                screen.blit(vmadar_surface,(255,210))
            else:
                if valaszt==1:
                    if m==0:
                        screen.blit(madar_surface,(255,210))
                        screen.blit(madar2_surface,(410,210))
                        if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                m=1
                        if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                m=2
                                bird_frames=malac_frames
                    if m==1:    
                        if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                bird_frames=bird1_frames
                                m=1
                        if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                bird_frames=malac_frames
                                m=2
                        screen.blit(vmadar_surface,(255,210))
                        screen.blit(madar2_surface,(410,210))
                    if m==2:
                        if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                bird_frames=bird1_frames
                                m=1
                        screen.blit(madar_surface,(255,210))
                        screen.blit(vmadar2_surface,(410,210))                  
                else:
                    if valaszt==2:
                        if m==0:
                            screen.blit(madar_surface,(255,210))
                            screen.blit(madar1_surface,(410,210))
                            if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    m=1
                            if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    m=2
                                    bird_frames=m1_frames
                        if m==1:    
                            if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    bird_frames=bird1_frames
                                    m=1
                            if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    bird_frames=m1_frames
                                    m=2
                            screen.blit(vmadar_surface,(255,210))
                            screen.blit(madar1_surface,(410,210))
                        if m==2:
                            if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    bird_frames=bird1_frames
                                    m=1
                            screen.blit(madar_surface,(255,210))
                            screen.blit(vmadar1_surface,(410,210))
                    else:
                        if valaszt==4:
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar3_surface,(410,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=cica_frames
                            if m==1:    
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=2
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar3_surface,(410,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar3_surface,(410,210))
                        if valaszt==8:                            
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar4_surface,(410,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=m4_frames
                            if m==1:    
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=2
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar4_surface,(410,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar4_surface,(410,210))
                        if valaszt==3:
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m1_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2        
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar1_surface,(565,210))
                        if valaszt==5:                            
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=cica_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2        
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar3_surface,(565,210))
                        if valaszt==6:
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=m1_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=cica_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2        
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(vmadar3_surface,(565,210))
                        if valaszt==9:                           
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=3
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2        
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar4_surface,(565,210))
                        if valaszt ==10:                           
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=m1_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=3
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar1_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2        
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(vmadar4_surface,(565,210))
                        if valaszt ==12:                            
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar3_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=cica_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=3
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar3_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar3_surface,(410,210))
                                screen.blit(madar4_surface,(565,210))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=2        
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar3_surface,(410,210))
                                screen.blit(vmadar4_surface,(565,210))
                        if valaszt ==7: 
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m1_frames
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=4
                                        bird_frames=cica_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=4
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                            if m==4:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(vmadar3_surface,(255,315))
                        if valaszt ==11:                           
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m1_frames
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=4
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar1_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==4:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(vmadar4_surface,(255,315))
                        if valaszt ==13:                  
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=cica_frames
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=4
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==4:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(vmadar4_surface,(255,315))
                        if valaszt ==14:                  
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=cica_frames
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=4
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m4_frames
                                        m=4
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(vmadar3_surface,(565,210))
                                screen.blit(madar4_surface,(255,315))
                            if m==4:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=3
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar1_surface,(410,210))
                                screen.blit(madar3_surface,(565,210))
                                screen.blit(vmadar4_surface,(255,315))    
                        if valaszt ==15:                  
                            if m==0:
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                                screen.blit(madar4_surface,(410,315))
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=2
                                        bird_frames=malac_frames
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=3
                                        bird_frames=m1_frames
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=4
                                        bird_frames=cica_frames
                                if 410+130> mouse[0] > 410 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=5
                                        bird_frames=m4_frames
                            if m==1:    
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=4
                                if 410+130> mouse[0] > 410 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=5
                                        bird_frames=m4_frames
                                screen.blit(vmadar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                                screen.blit(madar4_surface,(410,315))
                            if m==2:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=4
                                if 410+130> mouse[0] > 410 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=5
                                        bird_frames=m4_frames
                                screen.blit(madar_surface,(255,210))
                                screen.blit(vmadar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                                screen.blit(madar4_surface,(410,315))
                            if m==3:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=cica_frames
                                        m=4
                                if 410+130> mouse[0] > 410 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=5
                                        bird_frames=m4_frames
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(vmadar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                                screen.blit(madar4_surface,(410,315))
                            if m==4:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 410+130> mouse[0] > 410 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=5
                                        bird_frames=m4_frames
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(vmadar3_surface,(255,315))
                                screen.blit(madar4_surface,(410,315))
                            if m==5:
                                if 255+130> mouse[0] > 255 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=bird1_frames
                                        m=1
                                if 410+130> mouse[0] > 410 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=malac_frames
                                        m=2
                                if 565+130> mouse[0] > 565 and 210+90 > mouse[1] >210:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        bird_frames=m1_frames
                                        m=3
                                if 255+130> mouse[0] > 255 and 315+90 > mouse[1] >315:
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        m=4
                                        bird_frames=cica_frames
                                screen.blit(madar_surface,(255,210))
                                screen.blit(madar2_surface,(410,210))
                                screen.blit(madar1_surface,(565,210))
                                screen.blit(madar3_surface,(255,315))
                                screen.blit(vmadar4_surface,(410,315))       
    floor_x_pos +=-1
    draw_floor()
    if floor_x_pos <= -480:
        floor_x_pos = 0
    
              
    pygame.display.update()
    clock.tick(100)
    
