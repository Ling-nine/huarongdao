import pygame,sys
from pygame.locals import *

pygame.init()
size = 700,600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('华容道')
text = pygame.font.SysFont('SimHei',32)

color1 = (0,0,255)
board = [['3,','1,','1?','6,'],
         ['3.','1.','1;','6.'],
         ['5,','2,','2.','4,'],
         ['5.','7,','7,','4.'],
         ['7,','0,','0,','7,']]

bk = pygame.transform.scale(pygame.image.load('.\边框.png').convert(),(424,560))
cc = pygame.transform.scale(pygame.image.load('.\曹操.png').convert_alpha(),(186,186))#1
gy = pygame.transform.scale(pygame.image.load('.\关羽.png').convert_alpha(),(186,92))#2
hz = pygame.transform.scale(pygame.image.load('.\黄忠.png').convert_alpha(),(92,186))#3
mc = pygame.transform.scale(pygame.image.load('.\马超.png').convert_alpha(),(92,186))#4
zf = pygame.transform.scale(pygame.image.load('.\张飞.png').convert_alpha(),(92,186))#5
zy = pygame.transform.scale(pygame.image.load('.\赵云.png').convert_alpha(),(92,186))#6
zu = pygame.transform.scale(pygame.image.load('.\卒.png').convert_alpha(),(92,92))#7
bes = 0
num = 0
hro = {'1,':cc,'2,':gy,'3,':hz,'4,':mc,'5,':zf,'6,':zy,'7,':zu}

def bes_get(bes):
     if len(board) != py+1 and board[py+1][px] == '0,':
          bes+=1
     if py != 0 and board[py-1][px] == '0,':
          bes+=1
     if len(board[0]) != px+1 and board[py][px+1] == '0,':
          bes+=1
     if px != 0 and board[py][px-1] == '0,':
          bes+=1
     return bes

while True:
     #操作检测
     x = pygame.mouse.get_pos()[0]
     y = pygame.mouse.get_pos()[1]
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
          if event.type == MOUSEMOTION:
               color1 = (0,0,255)

          if 500 < x < 614 and 80 < y < 120:
               color1 = (255,255,0)

          if event.type ==  MOUSEBUTTONDOWN:
               if 27 < x < 397 and 51 < y < 515:
                    px,py = int((x-27)//92.5),int((y-51)//92.5)
                    #print(board[py][px],py,px)
                    #控制曹操
                    if board[py][px][0] == '1':
                         if board[py][px][1] == '?':
                              px-=1
                         if board[py][px][1] == '.':
                              py-=1
                         if board[py][px][1] == ';':
                              py-=1
                              px-=1
                         #上下
                         if py != 0 and board[py-1][px] == '0,' and board[py-1][px+1] == '0,':
                              board[py-1][px],board[py][px],board[py+1][px] = board[py][px],board[py+1][px],board[py-1][px]
                              board[py-1][px+1],board[py][px+1],board[py+1][px+1] = board[py][px+1],board[py+1][px+1],board[py-1][px+1]
                              num+=1
                         elif len(board) != py+2 and board[py+2][px] == '0,' and board[py+2][px+1] == '0,':
                              board[py+2][px],board[py+1][px],board[py][px] = board[py+1][px],board[py][px],board[py+2][px]
                              board[py+2][px+1],board[py+1][px+1],board[py][px+1] = board[py+1][px+1],board[py][px+1],board[py+2][px+1]
                              num+=1
                         #左右
                         elif px != 0 and board[py][px-1] == '0,' and board[py+1][px-1] == '0,':
                              board[py][px-1],board[py][px],board[py][px+1] = board[py][px],board[py][px+1],board[py][px-1]
                              board[py+1][px-1],board[py+1][px],board[py+1][px+1] = board[py+1][px],board[py+1][px+1],board[py+1][px-1]
                              num+=1
                         elif len(board[0]) != px+2 and board[py][px+2] == '0,' and board[py+1][px+2] == '0,':
                              board[py][px+2],board[py][px+1],board[py][px] = board[py][px+1],board[py][px],board[py][px+2]
                              board[py+1][px+2],board[py+1][px+1],board[py+1][px] = board[py+1][px+1],board[py+1][px],board[py+1][px+2]
                              num+=1
                         
                         if board[py][px][1] == '?':
                              px-=1
                         if board[py][px][1] == '.':
                              py-=1
                         if board[py][px][1] == ';':
                              py-=1
                              px-=1
                    #控制关羽
                    elif board[py][px][0] == '2':
                         if board[py][px][1] == ',':
                              #左右
                              if px > 0 and board[py][px-1] == '0,':
                                   board[py][px-1],board[py][px],board[py][px+1] = board[py][px],board[py][px+1],board[py][px-1]
                                   num+=1
                              elif len(board[0]) > px+2 and board[py][px+2] == '0,':
                                   board[py][px+2],board[py][px+1],board[py][px] = board[py][px+1],board[py][px],board[py][px+2]
                                   num+=1
                              #上下
                              elif py > 0 and board[py-1][px] == '0,' and board[py-1][px+1] == '0,':
                                   board[py-1][px],board[py][px] = board[py][px],board[py-1][px]
                                   board[py-1][px+1],board[py][px+1] = board[py][px+1],board[py-1][px+1]
                                   num+=1
                              elif len(board) > py+1 and board[py+1][px] == '0,' and board[py+1][px+1] == '0,':
                                   board[py+1][px],board[py][px] = board[py][px],board[py+1][px]
                                   board[py+1][px+1],board[py][px+1] = board[py][px+1],board[py+1][px+1]
                                   num+=1

                         elif board[py][px][1] == '.':
                              #右左
                              if len(board[0]) > px+1 and board[py][px+1] == '0,':
                                   board[py][px-1],board[py][px],board[py][px+1] = board[py][px+1],board[py][px-1],board[py][px]
                                   num+=1
                              elif px-2 >= 0 and board[py][px-2] == '0,':
                                   board[py][px-2],board[py][px-1],board[py][px] = board[py][px-1],board[py][px],board[py][px-2]
                                   num+=1
                              #上下
                              elif py > 0 and board[py-1][px-1] == '0,' and board[py-1][px] == '0,':
                                   board[py-1][px],board[py][px] = board[py][px],board[py-1][px]
                                   board[py-1][px-1],board[py][px-1] = board[py][px-1],board[py-1][px-1]
                                   num+=1
                              elif len(board) > py+1 and board[py+1][px-1] == '0,' and board[py+1][px] == '0,':
                                   board[py+1][px],board[py][px] = board[py][px],board[py+1][px]
                                   board[py+1][px-1],board[py][px-1] = board[py][px-1],board[py+1][px-1]
                                   num+=1
                    #控制黄忠,马超,张飞,赵云
                    elif board[py][px][0] in ['3','4','5','6']:
                         if board[py][px][1] == ',':
                              #上下
                              if py > 0 and board[py-1][px] == '0,':
                                   board[py-1][px],board[py][px],board[py+1][px] = board[py][px],board[py+1][px],board[py-1][px]
                                   num+=1
                              elif len(board) > py+2 and board[py+2][px] == '0,':
                                   board[py+2][px],board[py+1][px],board[py][px] = board[py+1][px],board[py][px],board[py+2][px]
                                   num+=1
                              #左右
                              elif px > 0 and board[py][px-1] == '0,' and board[py+1][px-1] == '0,':
                                   board[py][px-1],board[py][px] = board[py][px],board[py][px-1]
                                   board[py+1][px-1],board[py+1][px] = board[py+1][px],board[py+1][px-1]
                                   num+=1
                              elif len(board[0]) > px+1 and board[py][px+1] == '0,' and board[py+1][px+1] == '0,':
                                   board[py][px+1],board[py][px] = board[py][px],board[py][px+1]
                                   board[py+1][px+1],board[py+1][px] = board[py+1][px],board[py+1][px+1]
                                   num+=1

                         elif board[py][px][1] == '.':
                              #下上
                              if len(board) > py+1 and board[py+1][px] == '0,':
                                   board[py+1][px],board[py][px],board[py-1][px] = board[py][px],board[py-1][px],board[py+1][px]
                                   num+=1
                              elif py-2 >= 0 and board[py-2][px] == '0,':
                                   board[py-2][px],board[py-1][px],board[py][px] = board[py-1][px],board[py][px],board[py-2][px]
                                   num+=1
                              #左右
                              elif px > 0 and board[py][px-1] == '0,' and board[py-1][px-1] == '0,':
                                   board[py][px-1],board[py][px] = board[py][px],board[py][px-1]
                                   board[py-1][px-1],board[py-1][px] = board[py-1][px],board[py-1][px-1]
                                   num+=1
                              elif len(board[0]) > px+1 and board[py][px+1] == '0,' and board[py-1][px+1] == '0,':
                                   board[py][px+1],board[py][px] = board[py][px],board[py][px+1]
                                   board[py-1][px+1],board[py-1][px] = board[py-1][px],board[py-1][px+1]
                                   num+=1

                    #控制卒               
                    elif board[py][px][0] == '7':
                         bes = bes_get(0)
                         if bes == 1:
                              if len(board) > py+1 and board[py+1][px] == '0,':
                                   board[py+1][px],board[py][px] = board[py][px],board[py+1][px]
                                   num+=1
                              if py > 0 and board[py-1][px] == '0,':
                                   board[py-1][px],board[py][px] = board[py][px],board[py-1][px]
                                   num+=1
                              if len(board[0]) > px+1 and board[py][px+1] == '0,':
                                   board[py][px+1],board[py][px] = board[py][px],board[py][px+1]
                                   num+=1
                              if px > 0 and board[py][px-1] == '0,':
                                   board[py][px-1],board[py][px] = board[py][px],board[py][px-1]
                                   num+=1
                         elif bes > 1:
                              z = 30
                              if x-27 < px*92.5+z:
                                   #print('左')
                                   if px != 0 and board[py][px-1] == '0,':
                                        board[py][px-1],board[py][px] = board[py][px],board[py][px-1]
                                        num+=1
                              elif x-27 > px*92.5+93.25-z:
                                   #print('右')
                                   if len(board[0]) != px+1 and board[py][px+1] == '0,':
                                        board[py][px+1],board[py][px] = board[py][px],board[py][px+1]
                                        num+=1
                              elif y-51 < py*92.5+z:
                                   #print('上')
                                   if py != 0 and board[py-1][px] == '0,':
                                        board[py-1][px],board[py][px] = board[py][px],board[py-1][px]
                                        num+=1
                              elif y-51 > py*92.5+93.25-z:
                                   #print('下')
                                   if len(board) != py+1 and board[py+1][px] == '0,':
                                        board[py+1][px],board[py][px] = board[py][px],board[py+1][px]
                                        num+=1
                              bes = 0
                   
               #重新开始
               if color1[0]:
                    board = [['3,','1,','1?','6,'],
                             ['3.','1.','1;','6.'],
                             ['5,','2,','2.','4,'],
                             ['5.','7,','7,','4.'],
                             ['7,','0,','0,','7,']]
                    num = 0
                    pass
          if event.type ==  MOUSEBUTTONUP:
               stard = True

     screen.fill((255,255,255))
     screen.blit(bk,(0,0))
     #文本
     screen.blit(text.render('重新开始',1,color1),(500,80))
     screen.blit(text.render('次数:' + str(num),1,(0,0,255)),(500,160))
     #screen.blit(text.render(str(x)+' '+str(y),1,(0,0,255)),(500,240))
     #图像
     for i in range(len(board)):
          for j in range(len(board[i])):
               if board[i][j] in hro:
                    screen.blit(hro[board[i][j]],(int(j*93.25+27),int(i*93.25+50)))
     pygame.draw.rect(screen,(0,255,0),(27,51,1,1),0)#x370y464
     pygame.draw.rect(screen,(0,255,0),(397,515,1,1),0)
     if board[3][1] == '1,':
          screen.blit(text.render('胜利',1,(255,128,0)),(500,320))
     #更新图像
     pygame.display.flip()
     #延迟2毫秒
     pygame.time.delay(2)
