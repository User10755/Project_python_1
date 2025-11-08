from pygame import *
window_0 = display.set_mode((700, 500))
display.set_caption('Догонялки')
image_1 = transform.scale(image.load('background.jpg'),(700, 500))
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
mixer.music.set_volume(0.2)

class GameObject(sprite.Sprite) :
    def __init__(self, picture, x , y , speed_object) :
        super().__init__()
        self.picture = picture
        self.x = x
        self.y = y
        self.speed_object = speed_object
        self.image = transform.scale(image.load(picture),(30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def draw(self) :
        window_0.blit(self.image, (self.rect.x, self.rect.y))
class Player_Game(GameObject) :
    def update(self)  :
        keypressed = key.get_pressed()
        if keypressed [K_w] and self.rect.y > 0 :
            self.rect.y -= self.speed_object
        if keypressed [K_a] and self.rect.x > 0 :
            self.rect.x -= self.speed_object
        if keypressed [K_d] and self.rect.x < 600 :
            self.rect.x += self.speed_object
        if keypressed [K_s] and self.rect.y < 400 :
            self.rect.y += self.speed_object
class Player_Game_1(GameObject) :
    direction = 'right'
    def update(self) :
        if self.rect.x <= 400 :
            self.direction = 'right'
        if self.rect.x >= 600  :
            self.direction = 'left'
        if self.direction == 'left' :
            self.rect.x -= self.speed_object
        else :
            self.rect.x += self.speed_object
class Wall(sprite.Sprite)   :
    def __init__(self, color_0 , x , y , a, b)  :
        super().__init__() 
        self.image = Surface((a ,b))
        self.image.fill(color_0)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self) :
        window_0.blit(self.image, (self.rect.x, self.rect.y)) 
w = [] 
w
w.append(Wall((138, 18, 224), 200, 130, 100, 20))
w.append(Wall((138, 18, 224), 200, 40 , 20, 100))
w.append(Wall((138, 18, 224),120 , 30 , 100 , 20))
w.append(Wall((138, 18, 224),200, 130, 20, 100))
w.append(Wall((138, 18, 224), 300 , 130, 20, 100))
w.append(Wall((138, 18, 224), 110, 35, 20, 100))
w.append(Wall((138, 18, 224), 30, 130 , 100, 20))
w.append(Wall((138, 18, 224), 30 , 130, 20, 100))
w.append(Wall((138, 18, 224), 30 , 220 , 100 , 20))
w.append(Wall((138, 18, 224),120, 220, 20, 100))
w.append(Wall((138, 18, 224),200 , 220 , 20, 100))
w.append(Wall((138, 18, 224), 30 , 300 , 100, 20))
w.append(Wall((138, 18, 224), 30, 300, 20, 100))
w.append(Wall((138, 18, 224), 30, 300, 20, 100))
w.append(Wall((138, 18, 224), 30 , 400 , 100 , 20))
w.append(Wall((138, 18, 224), 70 , 400 , 320, 20))
w.append(Wall((138, 18, 224),300 ,230 , 100 , 20)) 
w.append(Wall((138, 18, 224), 400, 20, 20 , 230))
w.append(Wall((138, 18, 224), 400 , 20 , 100 , 20))
w.append(Wall((138, 18, 224), 490 , 20 , 20 , 150))
w.append(Wall((138, 18, 224), 490 , 150 , 100 , 20))
w.append(Wall((138, 18, 224), 570 , 70 , 20 , 100))
w.append(Wall((138, 18, 224), 570 , 70 , 100 , 20))
w.append(Wall((138, 18, 224), 650 , 70 , 20 , 170))
w.append(Wall((138, 18, 224), 520 , 240 , 150 , 20)) 
w.append(Wall((138, 18, 224) , 520 ,240 , 20 , 100))
w.append(Wall((138, 18, 224), 520, 340 , 150 , 20))
w.append(Wall((138, 18, 224), 650 , 340 , 20 , 100))
w.append(Wall((138, 18, 224), 470, 430 , 200 , 20))
w.append(Wall((138, 18, 224) , 470 ,430 , 20 , 100))
w.append(Wall((138, 18, 224) , 380 , 480 , 90 , 20))
w.append(Wall((138, 18, 224) ,380 , 350 , 20, 200))
w.append(Wall((138, 18, 224) , 300 , 250 , 20 , 90))
w.append(Wall((138, 18, 224), 300 , 50 , 20 , 90))



gameobjet = Player_Game('hero.png', 130, 50, 3)
gameobjet_1 = Player_Game_1('cyborg.png', 400 , 180 , 3)
game_object_2 = GameObject('treasure.png', 420, 50, 50)
sound_money = mixer.Sound('money.ogg')
sound_kick = mixer.Sound('kick.ogg')
finish = False
run = True
clock = time.Clock()
font.init()
font = font.Font(None, 70)
text_win =  font.render('YOU WIN!', True , (255, 179, 0))
text_lose = font.render('YOU LOSE! :(', True , (255, 0 , 0))

while run :
    if not finish :

        window_0.blit(image_1, (0, 0))
        gameobjet.draw()
        gameobjet_1.draw()
        game_object_2.draw()
        gameobjet.update()  
        gameobjet_1.update()
        
        for a in w  :
            a.draw()
        if sprite.collide_rect(gameobjet, game_object_2) :
            window_0.blit(text_win, (200 , 200))
            finish = True
            sound_money.play()
            
        
        
        for a in w :

            if sprite.collide_rect(gameobjet, a) or sprite.collide_rect(gameobjet, gameobjet_1) :
                
                finish = True
                window_0.blit(text_lose, (200, 200))
                sound_kick.play()


            
    for a in event.get() :
        if a.type == QUIT :
            run = False
    display.update()
    clock.tick(60)
