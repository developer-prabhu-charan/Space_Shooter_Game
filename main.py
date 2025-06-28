import random
import math
import pygame
from pygame import mixer
from pyvidplayer import Video 
 
pygame.init()
screen = pygame.display.set_mode((1000, 700))


def intro():
        try:
            vid = Video('assets\\intro.mp4')
            vid.set_size((1000,700))
            screen = pygame.display.set_mode((1000, 700))

            font = pygame.font.SysFont('Algerian', 40)
            surf = font.render('Play', True, 'white')
            button = pygame.Rect(150, 620, 120, 50)

            font1 = pygame.font.SysFont('Algerian', 40)
            surf1 = font1.render('Quit', True, 'white')
            button1 = pygame.Rect(750, 620, 100, 50)

            while True:
                vid.draw(screen, (0, 0))
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        pygame.quit()
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        if button.collidepoint(events.pos):
                            vid.toggle_pause()
                            play()
                            pygame.quit()
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        if button1.collidepoint(events.pos):
                            pygame.quit()
                a, b = pygame.mouse.get_pos()
                if button.x <= a <= button.x + 110 and button.y <= b <= button.y + 60:
                    pygame.draw.rect(screen, 'green', button)
                else:
                    pygame.draw.rect(screen, (110, 110, 100), button)
                screen.blit(surf, (button.x +5, button.y +5))
                a1, b1 = pygame.mouse.get_pos()
                if button1.x <= a1 <= button1.x + 110 and button1.y <= b1 <= button1.y + 60:
                    pygame.draw.rect(screen, 'red', button1)
                else:
                    pygame.draw.rect(screen, (110, 110, 100), button1)
                screen.blit(surf1, (button1.x + 5, button1.y + 5))
                pygame.display.update()
        except:
            pass

# ScoreBoard Function
def scoreBoard(score):
    font1 = pygame.font.SysFont('Times New Roman', 40, 'bold')
    img = font1.render(f'Score:- {score}', True, 'green')
    screen.blit(img, (10, 10))


def gameOver(score, healthPercentage, laserSound):
        laserSound.stop()
        gameover = pygame.font.SysFont('Algerian', 90)
        img = gameover.render('Game Over', True, 'red')
        screen.blit(img, (240, 250))
        gameOverSound1 = mixer.Sound('assets\\gameover1.mp3')
        gameOverSound1.play(-1)

        font1 = pygame.font.SysFont('Times New Roman', 40, 'bold')
        img = font1.render(f'Score:- {score}', True, 'green')
        screen.blit(img, (10, 10))

        health = pygame.font.SysFont('Lucida Calligraphy', 20, 'bold')
        img = health.render(f'Health = {healthPercentage}%', True, 'yellow')
        screen.blit(img, (10, 670))

        font2 = pygame.font.SysFont('Algerian', 40)
        surf2 = font2.render('Main Menu', True, 'white')
        button2 = pygame.Rect(380, 410, 220, 50)

        font3 = pygame.font.SysFont('Algerian', 40)
        surf3 = font3.render('Exit', True, 'white')
        button3 = pygame.Rect(440, 500, 110, 50)

        gameover = pygame.font.SysFont('Algerian', 30)
        img = gameover.render('Spaceship Crashed..!', True, 'orange')
        screen.blit(img, (320, 630))

        while True:
            try:
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        pygame.quit()
                    if events.type == pygame.MOUSEBUTTONDOWN:
                        if button2.collidepoint(events.pos):
                            gameOverSound1.stop()
                            mixer.music.stop()
                            intro()

                    if events.type == pygame.MOUSEBUTTONDOWN:
                        if button3.collidepoint(events.pos):
                            pygame.quit()
                a2, b2 = pygame.mouse.get_pos()
                if button2.x <= a2 <= button2.x + 220 and button2.y <= b2 <= button2.y + 60:
                    pygame.draw.rect(screen, 'green', button2)
                else:
                    pygame.draw.rect(screen, (110, 110, 100), button2)
                screen.blit(surf2, (button2.x + 5, button2.y + 5))

                a3, b3 = pygame.mouse.get_pos()
                if button3.x <= a3 <= button3.x + 110 and button3.y <= b3 <= button3.y + 50:
                    pygame.draw.rect(screen, 'red', button3)
                else:
                    pygame.draw.rect(screen, (110, 110, 100), button3)
                screen.blit(surf3, (button3.x + 5, button3.y + 5))

                pygame.display.update()
            except:
                pass


def health(healthPercentage):
        health = pygame.font.SysFont('Lucida Calligraphy', 20, 'bold')
        img = health.render(f'Health = {healthPercentage}%', True, 'yellow')
        screen.blit(img, (10, 670))
        return healthPercentage

#lib@4321

# Collision Function
def collision(spaceshipX, powerX, spaceshipY, powerY, speedX, speedY, enemyX1, enemyY1, enemyX2, enemyY2, herobulletX, herobulletY, enemybulletX1, enemybulletY1, enemybulletX2, enemybulletY2):
    distanceP = (math.sqrt(math.pow(spaceshipX + 20 - powerX, 2) + math.pow(spaceshipY + 20 - powerY + 20, 2)))
    distanceS = (math.sqrt(math.pow(spaceshipX + 25 - speedX, 2) + math.pow(spaceshipY + 10 - speedY + 40, 2)) / 2)
    distance1_1 = (math.sqrt(math.pow(herobulletX - enemyX1 - 25, 2) + math.pow(herobulletY - enemyY1, 2)))
    distance1_2 = (math.sqrt(math.pow(enemybulletX1 - spaceshipX - 20, 2) + math.pow(enemybulletY1 - spaceshipY - 50, 2)))
    distance1_3 = (math.sqrt(math.pow(spaceshipX - enemyX1, 2) + math.pow(spaceshipY + 10 - enemyY1 + 10, 2)) / 2)
    distance1_4 = (math.sqrt(math.pow(enemybulletX1 + 10 - herobulletX - 10, 2) + math.pow(enemybulletY1 - herobulletY, 2)) / 2)
    distance2_1 = (math.sqrt(math.pow(herobulletX - enemyX2 - 25, 2) + math.pow(herobulletY - enemyY2, 2)))
    distance2_2 = (math.sqrt(math.pow(enemybulletX2 - spaceshipX - 20, 2) + math.pow(enemybulletY2 - spaceshipY - 50, 2)))
    distance2_3 = (math.sqrt(math.pow(spaceshipX - enemyX2, 2) + math.pow(spaceshipY + 10 - enemyY2 + 10, 2)) / 2)
    distance2_4 = (math.sqrt(math.pow(enemybulletX2 + 10 - herobulletX - 10, 2) + math.pow(enemybulletY2 - herobulletY, 2)) / 2)
     
    if distance1_1 < 30:
        explsionSound = mixer.Sound('assets\\explosion1.mp3')
        explsionSound.play()
        return 1
    elif distance1_2 < 35:
        bulletHit = mixer.Sound('assets\\bulletHit.mp3')
        bulletHit.play()
        return 2
    elif distance1_3 < 30:
        blast = mixer.Sound('assets\\blast.mp3')
        blast.play()
        return 3
    elif distance1_4 < 3:
        return 4

    elif distance2_1 < 30:
        explsionSound = mixer.Sound('assets\\explosion1.mp3')
        explsionSound.play()
        return 5
    elif distance2_2 < 35:
        bulletHit = mixer.Sound('assets\\bulletHit.mp3')
        bulletHit.play()
        return 6
    elif distance2_3 < 30:
        blast = mixer.Sound('assets\\blast.mp3')
        blast.play()
        return 7
    elif distance2_4 < 3:
        return 8

    elif distanceP < 30:
        healthSound = mixer.Sound('assets\\health1.mp3')
        healthSound.play()
        return 100
    elif distanceS < 20:
        speedSound = mixer.Sound('assets\\speed1.mp3')
        speedSound.play()
        return 200

    

def play():
    mixer.init()
    

    gamespeed = 0.2

    # Loading & Initializing The Icon To Pygame Window
    icon = pygame.image.load('assets\\icon.png')
    pygame.display.set_icon(icon)

    # Declaring Speed Boost Image
    speed = pygame.image.load('assets\\speed.png')
    speedImg = pygame.transform.scale(speed, (30,30))
    speedX = random.randint(0, 650)
    speedY = 0

    # Declaring Power-Up Image
    power = pygame.image.load('assets\\power-up.png')
    powerImg = pygame.transform.scale(power,(30,30))
    powerX = random.randint(0, 650)
    powerY = 0

    # Declaring The Background Image
    background = pygame.image.load('assets\\bg.jpg')

    # Spaceship
    spaceship = pygame.image.load('assets\\space.png')
    spaceshipImg = pygame.transform.scale(spaceship, (70,70))
    spaceshipX = 470
    spaceshipY = 630
    changeSpaceshipX = 0
    changeSpaceshipY = 0

    # Enemies
    enemy1 = (pygame.image.load('assets\\enemy_1.png'))
    enemyImg1 = pygame.transform.scale(enemy1, (70,70))
    enemyY1 = (-10)
    enemyX1 = (random.randint(0, 635))
    enemy1Speed = 0

    enemy2 = (pygame.image.load('assets\\enemy_2.png'))
    enemyImg2 = pygame.transform.scale(enemy2, (70,70))
    enemyY2 = (random.randint(-600, 0))
    enemyX2 = (random.randint(0, 635))
    enemy2Speed = 0

    # Hero Bullets
    herobullet1 = pygame.image.load('assets\\herobullet1.png')
    herobulletImg1 = pygame.transform.scale(herobullet1, (20,30))
    herobulletX = 495
    herobulletY = 645

    # Enemy Bullets
    enemybullet1 = pygame.image.load('assets\\enemy1bullet1.png')
    enemybulletImg1 = pygame.transform.scale(enemybullet1, (30,20))
    enemybulletX1 = enemyX1 + 10
    enemybulletY1 = enemyY1 + 20

    enemybullet2 = pygame.image.load('assets\\enemy2bullet1.png')
    enemybulletImg2 = pygame.transform.scale(enemybullet2, (30,20))
    enemybulletX2 = enemyX2 + 10
    enemybulletY2 = enemyY2 + 20

    # initializing SpaceBar Pressed As False
    checkSpacePressed = False

    # Initial Score Is Set To Zero
    score = 0

    healthPercentage = 100

    laserSound = mixer.Sound('assets\\laser2.mp3')


    # Setting Name To Pygame Window
    pygame.display.set_caption('assets\\Space Shooter Game')

    
    
    changeSpaceshipXl = -0.8
    changeSpaceshipXr = 0.8

    speedLt = [3,4,5, 10,11,12, 17,18,19, 26, 35,36,37, 41, 43, 45,46,47, 53, 59,60,61, 67, 71,72,73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 163, 167, 173, 179, 181, 191, 193, 197, 199]
    healthLt = [2,3,4,5, 7, 9,10,11, 13, 15,16,17, 23,24,25, 26,27, 33,34, 37, 40,41,42, 45, 48, 50,51,52, 55,56,59, 62,63,64, 69, 70, 71, 75, 79, 85, 89, 90, 92, 94, 99, 100, 109]

    numLt = [5, 10, 15]

    screen.blit(background, (0, 0))
    pygame.display.update()
    count = 1

    # Main Code(Backbone) To Our Game
    running = True
    while running:
        # Collision Function Call
        collisionOccured = collision(spaceshipX, powerX, spaceshipY, powerY, speedX, speedY, enemyX1, enemyY1, enemyX2, enemyY2, herobulletX, herobulletY, enemybulletX1, enemybulletY1, enemybulletX2, enemybulletY2)
        if collisionOccured == 200:
            speedY = 0
            speedX = random.randint(0, 635)
            changeSpaceshipXl = -2
            changeSpaceshipXr = 2
            gamespeed += 0.3
        # Initializing The Background Image
        screen.blit(background, (0, 0))
        # Checking The Which Keys Pressed
        for event in pygame.event.get():
            try:
                # Actions According To Keys Pressed
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        changeSpaceshipX = changeSpaceshipXl - gamespeed
                    elif event.key == pygame.K_RIGHT:
                        changeSpaceshipX = changeSpaceshipXr + gamespeed
                    elif event.key == pygame.K_SPACE:
                        checkSpacePressed = True
                        if count == 1:
                            laserSound.play(-1)
                            herobulletX = spaceshipX + 25
                            herobulletY = 645
                            count = 2

                elif event.type == pygame.KEYUP:
                    changeSpaceshipX = 0
            except:
                pass
        # Moving The Spaceship According To Keys Pressed
        spaceshipX += changeSpaceshipX
        spaceshipY += changeSpaceshipY

        # Conditions For Not Allow The Spaceship To Out Of The Screen
        if spaceshipX <= 0:
            spaceshipX = 0
        elif spaceshipX >= 930:
            spaceshipX = 930
            
        if score < 3:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.1
        elif score > 3 and score < 10:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.2
        elif score > 10 and score < 15:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.3
        elif score > 15 and score < 20:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.35
        elif score > 20 and score < 25:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.4
        elif score > 25 and score < 30:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.45
        elif score > 30 and score < 35:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.5
        elif score > 35 and score < 40:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.55
        elif score > 40 and score < 45:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.6
        elif score > 45 and score < 50:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.65
        elif score > 50 and score < 55:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.7
        elif score > 55 and score < 60:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.75
        elif score > 60 and score < 65:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.8
        elif score > 65 and score < 70:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.85
        elif score > 70 and score < 75:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.9
        elif score > 75 and score < 80:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 0.95
        elif score > 80 and score < 85:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1
        elif score > 85 and score < 90:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.1
        elif score > 90 and score < 95:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.15
        elif score > 95 and score < 100:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.2
        elif score > 103 and score < 110:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.25
        elif score > 110 and score < 115:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.3
        elif score > 115 and score < 120:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.35
        elif score > 120 and score < 125:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.4
        elif score > 125 and score < 130:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.45
        elif score > 130 and score < 135:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.5
        elif score > 135 and score < 140:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.55
        elif score > 140 and score < 145:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.6
        elif score > 145 and score < 150:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.65
        elif score > 150 and score < 155:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.7
        elif score > 155 and score < 160:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.75
        elif score > 160 and score < 165:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.8
        elif score > 165 and score < 170:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.85
        elif score > 170 and score < 175:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.9
        elif score > 175 and score < 180:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 1.95
        elif score > 180 and score < 185:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2
        elif score > 185 and score < 190:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.1
        elif score > 190 and score < 195:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.15
        elif score > 195 and score < 200:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.2
        elif score > 203 and score < 210:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.25
        elif score > 210 and score < 215:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.3
        elif score > 215 and score < 220:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.35
        elif score > 220 and score < 225:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.4
        elif score > 225 and score < 230:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.45
        elif score > 230 and score < 235:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.5
        elif score > 235 and score < 240:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.55
        elif score > 240 and score < 245:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.6
        elif score > 245 and score < 250:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.65
        elif score > 250 and score < 255:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.7
        elif score > 255 and score < 260:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.75
        elif score > 260 and score < 265:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.8
        elif score > 265 and score < 270:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.85
        elif score > 270 and score < 275:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.9
        elif score > 275 and score < 280:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.95
        elif score > 280 and score < 285:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2
        elif score > 285 and score < 290:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.1
        elif score > 290 and score < 295:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.15
        elif score > 295 and score < 300:
            enemy1Speed = enemy2Speed = enemyBulletSpeed = 2.2

        # Enemy Movement Speed
        enemyY1 += enemy1Speed
        enemyY2 += enemy2Speed

        # Hero Bullet Movement
        if checkSpacePressed is True:
            screen.blit(herobulletImg1, (herobulletX, herobulletY))
            herobulletY -= (gamespeed + 0.5) + 3

        # Code To Respawn The Hero's Bullet Which Is Gone Out Of The Screen
        if herobulletY <= 0:
            herobulletX = spaceshipX + 25
            herobulletY = 645

        # Checking The Type Of Collision
        if collisionOccured == 1:
            herobulletX = 820
            enemyY1 = -10
            enemyX1 = random.randint(0, 735)
            score += 1
        elif collisionOccured == 2:
            enemybulletX1 = 800
            enemybulletY1 = 100
            if healthPercentage >= 5:
                healthPercentage -= 5

        elif collisionOccured == 3:
            enemyY1 = -10
            enemyX1 = random.randint(0, 735)
            if healthPercentage in numLt:
                healthPercentage = 0
            if healthPercentage >= 21:
                healthPercentage -= 20

        elif collisionOccured == 4:
            enemybulletX1 = 800
            herobulletX = 800

        elif collisionOccured == 5:
            herobulletX = 820
            enemyY2 = -10
            enemyX2 = random.randint(0, 735)
            score += 1
        elif collisionOccured == 6:
            enemybulletX2 = 800
            enemybulletY2 = 100
            if healthPercentage >= 5:
                healthPercentage -= 5

        elif collisionOccured == 7:
            enemyY2 = -10
            enemyX2 = random.randint(0, 735)
            if healthPercentage in numLt:
                healthPercentage = 0
            if healthPercentage >= 21:
                healthPercentage -= 20

        elif collisionOccured == 8:
            enemybulletX2 = 800
            herobulletX = 800

        elif collisionOccured == 100:
            powerY = 0
            powerX = random.randint(0, 735)
            if healthPercentage <= 0:
                gameOver(score, healthPercentage, laserSound)
            if healthPercentage < 100:
                healthPercentage += 15
        if healthPercentage <= 0:
                gameOver(score, healthPercentage, laserSound)

        # Code To Respawn The Enemy
        if enemyY1 > 800:
            enemyY1 = -10
            enemyX1 = random.randint(0, 735)
            score -= 1

        if enemyY2 > 800:
            enemyY2 = -10
            enemyX2 = random.randint(0, 735)
            score -= 1

        # Calling The Score board Function
        scoreBoard(score)
    
        # Calling The Health Function
        health(healthPercentage)

        # Adding The SpaceShip To The window
        screen.blit(spaceshipImg, (spaceshipX, spaceshipY))

        # Adding Enemy Bullet To The Window
        screen.blit(enemybulletImg1, (enemybulletX1, enemybulletY1))
        enemybulletY1 += enemyBulletSpeed + 0.2

        if enemyY2 >= 0:
            screen.blit(enemybulletImg2, (enemybulletX2, enemybulletY2))
            enemybulletY2 += enemyBulletSpeed + 0.2

        # Adding The Enemy To The Window
        screen.blit(enemyImg1, (enemyX1, enemyY1))
        if score >= 5:
            screen.blit(enemyImg2, (enemyX2, enemyY2))
        # Code To Respawn The enemy's Bullet Which Is Gone Out Of The Screen
        if enemybulletY1 >= 700:
            enemybulletX1 = enemyX1 + 10
            enemybulletY1 = enemyY1 + 20

        if enemybulletY2 >= 700:
            enemybulletX2 = enemyX2 + 10
            enemybulletY2 = enemyY2 + 20

        

        # Adding Power-up To The Window
        if score in healthLt:
            screen.blit(powerImg, (powerX, powerY))
            powerY += 0.8
        else:
            powerX = random.randint(0, 650)
            powerY = 0

        if powerY >= 800:
            powerY = 0
            powerX = random.randint(0, 735)

        # Adding Speed Boost To The Window
        if score in speedLt:
            screen.blit(speedImg, (speedX, speedY))
            speedY += 0.8
        else:
            speedX = random.randint(0, 650)
            speedY = 0
            changeSpaceshipXl = -0.8
            changeSpaceshipXr = 0.8

        if speedY >= 700:
            speedY = 0
            speedX = random.randint(0, 735)

        if healthPercentage >= 101:
            healthPercentage = 100

        # Updating Our Display Everytime
        pygame.display.update()
intro()