
import pygame
from button import Button
import game
import json
class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

    def display_name(self):
        return self.name
    
    def display_coin(self):
        return self.coin

    @staticmethod
    def create_player_name():
        back_font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 18)
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Create Player")
        back = Button("<<<", back_font, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        player_name = ""
        game_instance = game.Game() 
        input_rect = pygame.Rect(300, 300, 200, 40)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        font = pygame.font.Font(None, 36)
        active = False
        
        text = font.render("NAME", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 200))

        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = not active
                    elif back.clicked(mouse_pos):
                        game_instance.menu_()
                    else:
                        active = False
                    color = color_active if active else color_inactive
            

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if len(player_name) <= 8 and player_name.strip() != "":
                                Player.player = player_name
                                Player.coin = 100
                                Player.auto_save(Player.player,Player.coin)
                                game_instance.Choice_bet(Player.player,Player.coin)
                            else:
                                player_name = ""
                        elif event.key == pygame.K_BACKSPACE:
                            player_name = player_name[:-1]
                        elif len(player_name) < 8:
                            player_name += event.unicode
            screen.fill((0, 0, 0))
            pygame.draw.rect(screen, color, input_rect, 2)
            
            txt_surface = font.render(player_name, True, (255, 255, 255))
            width = max(200, txt_surface.get_width()+10)
            input_rect.w = width
            screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
            screen.blit(text, text_rect)
            back.render(screen, mouse_pos)

            pygame.display.flip()

    def auto_save(player_name, player_coin):
        file_path = "./data/data.json"
        
        # อ่านข้อมูล JSON จากไฟล์
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        # อัปเดตข้อมูล
        data["AUTO"]["name"] = player_name
        data["AUTO"]["coin"] = player_coin

        # บันทึกข้อมูล JSON ลงในไฟล์
        with open(file_path, "w") as json_file:
            json.dump(data, json_file, indent=4)
