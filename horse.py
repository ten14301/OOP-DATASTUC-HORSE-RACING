
import pygame

class Horse(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.pos_x = pos_x
        self.is_animating = False
        self.round = 0
        self.current_sprite = 0
        self.rect = pygame.Rect(pos_x,pos_y,20,20)

    def animate(self):
        self.is_animating = True
    def stop(self):
        self.kill()

    #ขยับและกำหนดค่าความเร็วของแต่ละเฟรมบนตัวม้า
    def update(self, speed):
        if self.is_animating :
            self.current_sprite += speed
            time_tick = pygame.time.get_ticks()
            self.rect.x +=  ((time_tick // 1000) + id(self)) % 5 + 3
            if self.rect.x >= 800:
                self.rect.x = -self.rect.width
                self.round += 1
            if self.round > 5:
                self.round = 0

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[int(self.current_sprite)]

    @property
    def position(self) -> int:
        return int(self.rect.x)
    
    @property
    def round_(self) -> int:
        return int(self.round)


class Horse_brown(Horse):
    def __init__(self, pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self.sprites = []
        self.sprites.append(pygame.image.load('./assets/brown/move1.png'))
        self.sprites.append(pygame.image.load('./assets/brown/move2.png'))
        self.sprites.append(pygame.image.load('./assets/brown/move3.png'))
        self.sprites.append(pygame.image.load('./assets/brown/move4.png'))
        self.sprites.append(pygame.image.load('./assets/brown/move5.png'))
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(pos_x, pos_y, 20, 20)

class Horse_black(Horse):
    def __init__(self, pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self.sprites = []
        self.sprites.append(pygame.image.load('./assets/black/move-black1.png'))
        self.sprites.append(pygame.image.load('./assets/black/move-black2.png'))
        self.sprites.append(pygame.image.load('./assets/black/move-black3.png'))
        self.sprites.append(pygame.image.load('./assets/black/move-black4.png'))
        self.sprites.append(pygame.image.load('./assets/black/move-black5.png'))
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(pos_x, pos_y, 20, 20)

class Horse_white(Horse):
    def __init__(self, pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self.sprites = []
        self.sprites.append(pygame.image.load('./assets/white/move-white1.png'))
        self.sprites.append(pygame.image.load('./assets/white/move-white2.png'))
        self.sprites.append(pygame.image.load('./assets/white/move-white3.png'))
        self.sprites.append(pygame.image.load('./assets/white/move-white4.png'))
        self.sprites.append(pygame.image.load('./assets/white/move-white5.png'))
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(pos_x, pos_y, 20, 20)

class Horse_grey(Horse):
    def __init__(self, pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self.sprites = []
        self.sprites.append(pygame.image.load('./assets/grey/move-grey1.png'))
        self.sprites.append(pygame.image.load('./assets/grey/move-grey2.png'))
        self.sprites.append(pygame.image.load('./assets/grey/move-grey3.png'))
        self.sprites.append(pygame.image.load('./assets/grey/move-grey4.png'))
        self.sprites.append(pygame.image.load('./assets/grey/move-grey5.png'))
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(pos_x, pos_y, 20, 20)

class Horse_red(Horse):
    def __init__(self, pos_x,pos_y):
        super().__init__(pos_x,pos_y)
        self.sprites = []
        self.sprites.append(pygame.image.load('./assets/red/move-red1.png'))
        self.sprites.append(pygame.image.load('./assets/red/move-red2.png'))
        self.sprites.append(pygame.image.load('./assets/red/move-red3.png'))
        self.sprites.append(pygame.image.load('./assets/red/move-red4.png'))
        self.sprites.append(pygame.image.load('./assets/red/move-red5.png'))
        self.image = self.sprites[self.current_sprite]
        self.rect = pygame.Rect(pos_x, pos_y, 20, 20)
