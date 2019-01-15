import pygame                   #导入pygame库
from pygame.locals import *     #导入pygame库中的一些常量
from sys import exit            #导入sys库中的exit函数
from random import randint


#创建子弹类
class Bullet(pygame.sprite.Sprite):

    def __init__(self,bullet_suface,bullet_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_suface
        self.rect = self.image.get_rect()
        self.rect.topleft = bullet_init_pos
        self.speed = 8

    def update(self):
        self.rect.top -= self.speed
        if self.rect.top < -self.rect.height:
            self.kill()

#创建敌人类
class Enemy(pygame.sprite.Sprite):
    def __init__(self,Enemy_suface,Enemy_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = Enemy_suface
        self.rect = self.image.get_rect()
        self.rect.topleft = Enemy_init_pos
        self.speed = 2

        # 爆炸动画画面索引
        self.down_index = 0

    def update(self):
        self.rect.top += self.speed
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
    



#创建Hero类，继承自pygame.sprite.Sprite
class Hero(pygame.sprite.Sprite):

    def __init__(self,hero_surface,hero_init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image =  hero_surface
        self.rect = self.image.get_rect()
        self.rect.topleft = hero_init_pos
        self.speed = 6
        self.is_hit = False

        self.bullets1 = pygame.sprite.Group()
        

    def move(self,offset):
        hero_x=self.rect.left+offset[pygame.K_RIGHT]-offset[pygame.K_LEFT]
        hero_y=self.rect.top+offset[pygame.K_DOWN]-offset[pygame.K_UP]
        
        if hero_x < 0:
            self.rect.left = 0
        elif hero_x > SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left = hero_x
            
        
        if hero_y < 0:
            self.rect.top = 0
        elif hero_y > SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top = hero_y

    def single_shoot(self,bullet1_surface):
        bullet1 = Bullet(bullet1_surface,self.rect.midtop)
        self.bullets1.add(bullet1)


#定义窗口的分辨率
SCREEN_WIDTH =  480
SCREEN_HEIGHT =  640


FRAME_RATE = 60

ANIMATE_CYCLE = 30

#计数ticks
ticks = 0

#去除了不断绘制飞机，容易消耗资源，使用clock，控制最大帧率FRAME_RATE
clock =pygame.time.Clock()

#创建字典，按下上下左右键的的增量
offset ={pygame.K_LEFT:0,pygame.K_RIGHT:0,pygame.K_UP:0,pygame.K_DOWN:0}

#初始化游戏
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('这是一个打飞机游戏！')



#载入背景图
background = pygame.image.load('images/background.png')

gameover = pygame.image.load('images/gameover.png')
#载入资源图
hero_surface=[]
hero_surface.append(pygame.image.load('images/me1.png'))
hero_surface.append(pygame.image.load('images/me2.png'))
hero_surface.append(pygame.image.load('images/me_destroy_1.png'))
hero_surface.append(pygame.image.load('images/me_destroy_2.png'))
hero_surface.append(pygame.image.load('images/me_destroy_3.png'))
hero_surface.append(pygame.image.load('images/me_destroy_4.png'))
hero_pos=[200,500]

#载入子弹1图
bullet1_surface = pygame.image.load('images/bullet1.png')

#载入敌人1图
enemy1_surface = pygame.image.load('images/enemy1.png')

#载入enemy1爆炸的图片
enemy1_down_surface=[]
enemy1_down_surface.append(pygame.image.load('images/enemy1_down1.png'))
enemy1_down_surface.append(pygame.image.load('images/enemy1_down2.png'))
enemy1_down_surface.append(pygame.image.load('images/enemy1_down3.png'))
enemy1_down_surface.append(pygame.image.load('images/enemy1_down4.png'))



#创建玩家
hero = Hero(hero_surface[0],hero_pos)

#创建敌机组
enemy1_group = pygame.sprite.Group()

#创建击毁敌人组
enemy1_down_group = pygame.sprite.Group()


hero_down_index = 1

#事件循环
while True:
    clock.tick(FRAME_RATE)
    #绘制背景
    screen.blit(background,(0,0))

    #绘制飞机,在循环过程中让每过25个周期切换2个飞机图。这样会产生动图的效果
    if ticks >= ANIMATE_CYCLE:
        ticks = 0

        

    if hero.is_hit:
        if ticks%(ANIMATE_CYCLE//2) == 0:
            hero_down_index += 1
        hero.image = hero_surface[hero_down_index]
        if hero_down_index == 5:
            break
    else:
        hero.image =hero_surface[ticks//(ANIMATE_CYCLE//2)]
        
    screen.blit(hero.image,hero.rect)


    #产生子弹start************************
    if ticks%10 == 0:
        hero.single_shoot(bullet1_surface)

    hero.bullets1.update()
    hero.bullets1.draw(screen)
    #产生子弹end**************************


    #产生敌机start************************
    if ticks%30 == 0:
        enemy1 = Enemy(enemy1_surface,[randint(0,SCREEN_WIDTH-enemy1_surface.get_width())
                                      ,-enemy1_surface.get_height()])
        enemy1_group.add(enemy1)

    enemy1_group.update()
    enemy1_group.draw(screen)
    #产生敌机send**************************


    enemy1_down_group.add(pygame.sprite.groupcollide(enemy1_group,hero.bullets1,True,True))

    for enemy1_down in enemy1_down_group:
        screen.blit(enemy1_down_surface[enemy1_down.down_index],enemy1_down.rect)
        if ticks % (ANIMATE_CYCLE//2) == 0:
            if enemy1_down.down_index<3:
                enemy1_down.down_index += 1
            else:
                enemy1_down_group.remove(enemy1_down)
    

    enemy1_down_list = pygame.sprite.spritecollide(hero,enemy1_group,True)
    if len(enemy1_down_list) > 0:
        enemy1_down_group.add(enemy1_down_list)
        hero.is_hit = True



            
    ticks += 1


    #更新屏幕
    pygame.display.update()


    #处理游戏退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


        #按键按下和放开的事件，按下时坐标增3，放开，置零
        if event.type == pygame.KEYDOWN:
            if event.key in offset:
                offset[event.key] = hero.speed   #增量的大小，主飞机移动速度的快慢


        elif event.type == pygame.KEYUP:
            if event.key in offset:
                offset[event.key] = 0

    hero.move(offset)



screen.blit(gameover,(100,500))
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


