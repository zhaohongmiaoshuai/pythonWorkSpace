#_*_ coding:UTF-8 _*_
import pygame
from pygame.locals import *
import sys
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
bg_color = (70, 0, 70)  # 背景颜色

SCREEN_SIZE = [1200, 800]  # 屏幕大小
BAR_SIZE = [100, 5]  # 挡板大小
BALL_SIZE = [60,70]  # 球的尺寸

class Game(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()  # 定时器
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('接住我的小心心')  # 设置标题

        # ball 初始位置
        self.ball_pos_x = SCREEN_SIZE[0] // 2 - BALL_SIZE[0] / 2
        self.ball_pos_y = 0
        # ball 移动方向
        # self.ball_dir_x = -1 #-1:left 1:right
        self.ball_dir_y = 1  # 1:down

        self.ball_pos = pygame.Rect(self.ball_pos_x, self.ball_pos_y,BALL_SIZE[0],BALL_SIZE[1])

        self.score = 0
        self.bar_pos_x = SCREEN_SIZE[0] // 2 - BAR_SIZE[0] // 2
        self.bar_pos = pygame.Rect(self.bar_pos_x, SCREEN_SIZE[1] - BAR_SIZE[1], BAR_SIZE[0], BALL_SIZE[1])


    def bar_move_left(self):  # 左移
        if self.bar_pos_x > 0:
            self.bar_pos_x = self.bar_pos_x - 5

    def bar_move_right(self):  # 右移
        if self.bar_pos_x + self.bar_pos.width< SCREEN_SIZE[0]:
            self.bar_pos_x = self.bar_pos_x + 5

    def run(self):
        pygame.mouse.set_visible(False)  # 移动鼠标不可见
        bar_move_left = False
        bar_move_right = False

        text = pygame.font.SysFont("宋体",30)

        text_score = text.render("SCORE:",1,WHITE)

        self.screen.blit(text_score,(0,0))

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:  # 当按下关闭按键
                    pygame.quit()
                    sys.exit()  # 接收到退出事件后退出程序

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 鼠标左键按下
                    bar_move_left = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # 左键弹起
                    bar_move_left = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # 右键
                    bar_move_right = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:  # 左键弹起
                    bar_move_right = False

            if bar_move_left == True and bar_move_right == False:
                self.bar_move_left()
            if bar_move_left == False and bar_move_right == True:
                self.bar_move_right()

            self.screen.fill(bg_color)
            self.bar_pos.left = self.bar_pos_x
            pygame.draw.rect(self.screen, WHITE, self.bar_pos)

            ## 球移动
            self.ball_pos.bottom += self.ball_dir_y*3
            # pygame.draw.acircle(self.screen, WHITE, (self.ball_pos.x,self.ball_pos.y),BALL_SIZE[0]//2)
            a = [self.ball_pos.x ,self.ball_pos.y+self.ball_pos.height//4,self.ball_pos.width//2,self.ball_pos.height//2]
            pygame.draw.arc(self.screen, WHITE, a, 0, math.pi)
            b = [self.ball_pos.x + self.ball_pos.width//2,self.ball_pos.y+self.ball_pos.height//4,self.ball_pos.width//2,self.ball_pos.height//2]
            pygame.draw.arc(self.screen, WHITE, b, 0, math.pi)
            pygame.draw.arc(self.screen, WHITE, self.ball_pos, math.pi, math.pi*2)

            ## 判断球是否落到板上
            if self.bar_pos.top <= self.ball_pos.bottom and (
                    self.bar_pos.left <= self.ball_pos.right and self.bar_pos.right >= self.ball_pos.left):
                self.score += 1
                # self.ball_pos.width += 10
                # self.bar_pos.width += 10
                print("Score: ", self.score, end='\r')
            elif self.bar_pos.top <= self.ball_pos.bottom and (
                    self.bar_pos.left > self.ball_pos.right or self.bar_pos.right < self.ball_pos.left):
                print("Game Over: ", self.score)
                return self.score

            ## 更新球下落的初始位置
            if self.bar_pos.top <= self.ball_pos.bottom:
                self.ball_pos_x = random.randint(0, math.fabs(SCREEN_SIZE[0] - self.ball_pos.width))
                self.ball_pos_y = 0
                self.ball_pos = pygame.Rect(self.ball_pos_x, self.ball_pos_y,self.ball_pos.width,self.ball_pos.height)
            text_score = text.render("SCORE: " + str(self.score), 1, WHITE)
            self.screen.blit(text_score, (0, 0))
            pygame.display.update()  # 更新软件界面显示
            self.clock.tick(200)


game = Game()
game.run()  # 启动