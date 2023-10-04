import pygame
from button import Button
import game
import json
class Player:
    def __init__(self, name="", coin=0):
        self.name = name
        self.coin = coin

    @property
    def return_name(self):
        return str(self.name)
    
    @property
    def return_coin(self):
        return int(self.coin)
    
    def update_coin(self,coin):
        self.coin += coin

    def update_name(self,name):
        self.name = name

    def create_player_name(self):
        self.name = ""
        self.coin = 100
        display = pygame.display
        background_image = pygame.image.load("./assets/MENU_BG.png")

        background_image = pygame.transform.scale(background_image, (800, 700))
        back_font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 18)
        screen = pygame.display.set_mode((800, 600))
        display.set_caption("Create Player")
        back = Button("<<<", back_font, (30, 50), (52, 78, 91), (100, 120, 140), 50, 50)
        game_instance = game.Game() 
        input_rect = pygame.Rect(300, 300, 200, 40)
        font = pygame.font.Font(None, 36)
        active = False
        pull = False

        text = font.render("NAME", True, (0, 0, 0))
        text_rect = text.get_rect(center=(400, 200))
        create_player_button = Button("Create Player", font, (400, 400), (52, 78, 91), (100, 120, 140), 200, 50)

        while True:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    elif create_player_button.clicked(mouse_pos):  
                        pull = True
                    elif back.clicked(mouse_pos):
                        game_instance.menu_()

                if event.type == pygame.KEYDOWN or pull == True:
                    if active:
                        if len(self.name) <= 8 and self.name.strip() != "" and create_player_button.clicked(mouse_pos):
                            game_instance = game.Game(self.name,self.coin)
                            self.auto_save()
                            game_instance.Choice_bet_play()
                        elif event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]
                        elif len(self.name) < 8:
                            if event.key == pygame.K_SPACE:
                                continue
                            self.name += str(event.unicode)
                        else:
                            pass

            screen.blit(background_image, (0, 0))
            
            txt_surface = font.render(self.name, True, (255, 255, 255))
            width = max(200, txt_surface.get_width()+10)
            input_rect.w = width
            pygame.draw.rect(screen, (0, 0, 0), input_rect)
            screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))

            screen.blit(text, text_rect)
            create_player_button.render(screen, mouse_pos)
            back.render(screen, mouse_pos)

            display.flip()

    def auto_save(self):
    
        file_path = "./data/data.json"
        # อ่านข้อมูล JSON จากไฟล์
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        # อัปเดตข้อมูล
        data["AUTO"]["name"] = self.name
        data["AUTO"]["coin"] = self.coin

        # บันทึกข้อมูล JSON ลงในไฟล์
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)