import pygame

pygame.init()
screen=pygame.display.set_mode([600,675])
pygame.display.set_caption('Iks Oks')
screen.fill([255,255,255])
table = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
i = 0
running = True
while running == True:
    pygame.draw.line(screen, [0,0,0], [200,20], [200,580], 6)
    pygame.draw.line(screen, [0,0,0], [400,20], [400,580], 6)
    pygame.draw.line(screen, [0,0,0], [20,200], [580,200], 6)
    pygame.draw.line(screen, [0,0,0], [20,400], [580,400], 6)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             pygame.quit()
        x,y = pygame.mouse.get_pos()
        if 0 < x < 200 and 0 < y < 200 and pygame.mouse.get_pressed()[0] == True and table[0] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [20,20], [180,180], 5)
            pygame.draw.line(screen, [0,0,255], [180,20], [20,180], 5)
            table[0] = "x"
            i += 1
        elif 200 < x < 400 and 0 < y < 200  and pygame.mouse.get_pressed()[0] == True and table[1] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [220,20], [380,180], 5)
            pygame.draw.line(screen, [0,0,255], [220,180], [380,20], 5)
            table[1] = "x"
            i += 1
        elif 400 < x < 600 and 0 < y < 200  and pygame.mouse.get_pressed()[0] == True and table[2] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [420,20], [580,180], 5)
            pygame.draw.line(screen, [0,0,255], [580,20], [420,180], 5)
            table[2] = "x"
            i += 1
        elif 0 < x < 200 and 200 < y < 400  and pygame.mouse.get_pressed()[0] == True and table[3] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [20,220], [180,380], 5)
            pygame.draw.line(screen, [0,0,255], [180,220], [20,380], 5)
            table[3] = "x"
            i += 1
        elif 200 < x < 400 and 200 < y < 400  and pygame.mouse.get_pressed()[0] == True and table[4] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [220,220], [380,380], 5)
            pygame.draw.line(screen, [0,0,255], [380,220], [220,380], 5)
            table[4] = "x"
            i += 1
        elif 400 < x < 600 and 200 < y < 400  and pygame.mouse.get_pressed()[0] == True and table[5] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [420,220], [580,380], 5)
            pygame.draw.line(screen, [0,0,255], [580,220], [420,380], 5)
            table[5] = "x"
            i += 1
        elif 0 < x < 200 and 400 < y < 600  and pygame.mouse.get_pressed()[0] == True and table[6] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [20,420], [180,580], 5)
            pygame.draw.line(screen, [0,0,255], [180,420], [20,580], 5)
            table[6] = "x"
            i += 1
        elif 200 < x < 400 and 400 < y < 600  and pygame.mouse.get_pressed()[0] == True and table[7] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [220,420], [380,580], 5)
            pygame.draw.line(screen, [0,0,255], [380,420], [220,580], 5)
            table[7] = "x"
            i += 1
        elif 400 < x < 600 and 400 < y < 600  and pygame.mouse.get_pressed()[0] == True and table[8] == "-" and i % 2 == 0:
            pygame.draw.line(screen, [0,0,255], [420,420], [580,580], 5)
            pygame.draw.line(screen, [0,0,255], [580,420], [420,580], 5)
            table[8] = "x"
            i += 1
        elif 0 < x < 200 and 0 < y < 200 and pygame.mouse.get_pressed()[0] == True and table[0] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [100,100], 90, 5)
            i += 1
            table[0] = "o"
        elif 200 < x < 400 and 0 < y < 200  and pygame.mouse.get_pressed()[0] == True and table[1] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [300,100], 90, 5)
            i += 1
            table[1] = "o"
        elif 400 < x < 600 and 0 < y < 200  and pygame.mouse.get_pressed()[0] == True and table[2] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [500,100], 90, 5)
            i += 1
            table[2] = "o"
        elif 0 < x < 200 and 200 < y < 400  and pygame.mouse.get_pressed()[0] == True and table[3] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [100,300], 90, 5)
            i += 1
            table[3] = "o"
        elif 200 < x < 400 and 200 < y < 400  and pygame.mouse.get_pressed()[0] == True and table[4] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [300,300], 90, 5)
            i += 1
            table[4] = "o"
        elif 400 < x < 600 and 200 < y < 400  and pygame.mouse.get_pressed()[0] == True and table[5] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [500,300], 90, 5)
            i += 1
            table[5] = "o"
        elif 0 < x < 200 and 400 < y < 600  and pygame.mouse.get_pressed()[0] == True and table[6] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [100,500], 90, 5)
            i += 1
            table[6] = "o"
        elif 200 < x < 400 and 400 < y < 600  and pygame.mouse.get_pressed()[0] == True and table[7] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [300,500], 90, 5)
            i += 1
            table[7] = "o"
        elif 400 < x < 600 and 400 < y < 600  and pygame.mouse.get_pressed()[0] == True and table[8] == "-" and i % 2 == 1:
            pygame.draw.circle(screen, [255,0,0], [500,500], 90, 5)
            i += 1
            table[8] = "o"
        if table[0] == table[1] == table[2] == "x":
            pygame.draw.line(screen, [0,0,0], [20,100], [580,100], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[3] == table[4] == table[5] == "x":
            pygame.draw.line(screen, [0,0,0], [20,300], [580,300], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[6] == table[7] == table[8] == "x":
            pygame.draw.line(screen, [0,0,0], [20,500], [580,500], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[0] == table[3] == table[6] == "x":
            pygame.draw.line(screen, [0,0,0], [100,20], [100,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[1] == table[4] == table[7] == "x":
            pygame.draw.line(screen, [0,0,0], [300,20], [300,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[2] == table[5] == table[8] == "x":
            pygame.draw.line(screen, [0,0,0], [500,20], [500,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[0] == table[4] == table[8] == "x":
            pygame.draw.line(screen, [0,0,0], [20,20], [580,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[2] == table[4] == table[6] == "x":
            pygame.draw.line(screen, [0,0,0], [580,20], [20,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[0] == table[1] == table[2] == "o":
            pygame.draw.line(screen, [0,0,0], [20,100], [580,100], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[3] == table[4] == table[5] == "o":
            pygame.draw.line(screen, [0,0,0], [20,300], [580,300], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[6] == table[7] == table[8] == "o":
            pygame.draw.line(screen, [0,0,0], [20,500], [580,500], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[0] == table[3] == table[6] == "o":
            pygame.draw.line(screen, [0,0,0], [100,20], [100,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[1] == table[4] == table[7] == "o":
            pygame.draw.line(screen, [0,0,0], [300,20], [300,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[2] == table[5] == table[8] == "o":
            pygame.draw.line(screen, [0,0,0], [500,20], [500,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[0] == table[4] == table[8] == "o":
            pygame.draw.line(screen, [0,0,0], [20,20], [580,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif table[2] == table[4] == table[6] == "o":
            pygame.draw.line(screen, [0,0,0], [580,20], [20,580], 6)
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O je pobednik!', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif i == 0 or i == 2 or i == 4 or i == 6 or i == 8:
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('X na potezu', True, (0,0,0))
            screen.blit(img, (20, 600))
        elif i == 1 or i == 3 or i == 5 or i == 7:
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('O na potezu', True, (0,0,0))
            screen.blit(img, (20, 600))
        else:
            screen.fill([255,255,255], (0, 600, 600, 100))
            font = pygame.font.SysFont(None, 100)
            img = font.render('Nerešeno', True, (0,0,0))
            screen.blit(img, (20, 600))

    pygame.display.flip()

