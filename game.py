
import pygame
import time
import json
from button import Button
from player import Player
from horse import Horse_brown, Horse_black, Horse_white, Horse_grey, Horse_red

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 700))
        pygame.display.set_caption("Horse Racing")
        self.font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 100)
        self.font_btn = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 32)
        self.logo_font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 72)
        self.font_save = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 18)
        self.backgrounds = ['./assets/bg.png', './assets/final.png']
        self.current_background = 0
        self.custom_font = pygame.font.Font(None, 20)
        self.lst_ = []
        self.dashboard_text = []
        self.type_bet = ""
        self.slected_players = ""
        self.bg_image = pygame.image.load(self.backgrounds[self.current_background]).convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))
        self.position = [375, 430, 485, 540, 595]
        n = len(self.position)
        random_numbers = [hash(obj + time.time()) for obj in self.position]
        for i in range(n):
            j = random_numbers[i] % (n - 1)
            self.position[i], self.position[j] = self.position[j], self.position[i]
        self.horse = Horse_brown(0, self.position[0])
        self.horseb = Horse_black(0, self.position[1])
        self.horsew = Horse_white(0, self.position[2])
        self.horseg = Horse_grey(0, self.position[3])
        self.horser = Horse_red(0, self.position[4])


    def run(self):
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('./assets/bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))
        self.moving_sprites = pygame.sprite.Group()
        self.start_position_horse()
        self.topic_dashboard = "Horse Racing Score-Board"
        for i in range(3, 0, -1):
            # ล้างหน้าจอและเปลี่ยนพื้นหลัง
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.bg_image, (0, 0))

            # แสดงข้อความนับถอยหลัง
            text = self.font.render(str(i), True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 350))
            self.screen.blit(text, text_rect)
            pygame.display.flip()
            time.sleep(1)
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg_image, (0, 0))
        self.text = self.font.render("start", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(400, 350))
        self.screen.blit(self.text, self.text_rect)
        pygame.display.flip()
        time.sleep(1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            self.order()
            self.score_board()
            self.illutionist()

            self.screen.blit(self.bg_image, (0, 0))
            self.moving_sprites.draw(self.screen)
            self.moving_sprites.update(0.2)
            text_dashboard_topic = self.custom_font.render(self.topic_dashboard, True, (255, 255, 255))
            self.screen.blit(text_dashboard_topic, (0, 0))
            if len(self.lst_) < 5:
                y_positions = [10, 20, 30, 40, 50]
                for i, text in enumerate(self.dashboard_text):
                    text_surface = self.custom_font.render(text, True, (255, 255, 255))
                    self.screen.blit(text_surface, (0, y_positions[i]))
            elif len(self.lst_) >= 5:
                y_positions = [10, 20, 30, 40, 50]
                for i, text in enumerate(self.lst_):
                    text_surface = self.custom_font.render(text, True, (255, 255, 255))
                    self.screen.blit(text_surface, (0, y_positions[i]))
            pygame.display.flip()
            self.clock.tick(60)

    def render_text(self,text, x, y):
        text_surface = self.font_save.render(text, True, (255, 255, 255))  # Text color: white
        self.screen.blit(text_surface, (x, y))

    def select_save(self):
        with open('./data/data.json', 'r') as json_file:
            data = json.load(json_file)
        self.back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)

        players = []
        for player_key, player_data in data.items():
            player_name = player_data["name"]
            player_coin = player_data["coin"]
            player = Player(player_name, player_coin)
            players.append(player)

        current_page = 0 
        players_per_page = 4 


        num_players = len(players)
        num_pages = (num_players + players_per_page - 1) // players_per_page
        current_page = 0


        box_width = int(0.75 * self.screen.get_width()) 
        box_height = (self.screen.get_height() - 100) // players_per_page
        box_x = (self.screen.get_width() - box_width) // 2
        box_y_start = 30

        button_rects = []
        for i in range(num_pages):
            button_x = 50 + i * 70
            button_rect = pygame.Rect(button_x, self.screen.get_height() - 50, 50, 30)
            button_rects.append(button_rect)
        while True:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == 1: 
                        mouse_x, mouse_y = event.pos

                        for i in range(current_page * players_per_page, min((current_page + 1) * players_per_page, num_players)):
                            if box_x <= mouse_x <= box_x + box_width and box_y_start + (i % players_per_page) * box_height <= mouse_y <= box_y_start + (i % players_per_page + 1) * box_height:
                                self.slected_players = players[i]
                                self.Choice_bet()

                        for i, button_rect in enumerate(button_rects):
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                current_page = i
                    if self.back.clicked(mouse_pos):
                        self.menu_()

            self.screen.fill((0, 0, 0))
            start_idx = current_page * players_per_page
            end_idx = min((current_page + 1) * players_per_page, num_players)

            for i, player in enumerate(players[start_idx:end_idx]):
                box_y = box_y_start + (i % players_per_page) * box_height
                player_box = pygame.Rect(box_x, box_y, box_width, box_height)
                pygame.draw.rect(self.screen, (0, 128, 255), player_box, 2)

                self.render_text(f"SAVE {i + 1 + start_idx}: {player.name}", box_x + 20, box_y + 10)
                self.render_text(f"Coin: {player.coin}", box_x + 20, box_y + 50)


            for i, button_rect in enumerate(button_rects):
                pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
                self.render_text(str(i + 1), button_rect.centerx - 10, button_rect.centery - 10)

            
            self.back.render(self.screen, mouse_pos)
            pygame.display.flip()


    def menu_(self):
        pygame.display.set_caption("Main Menu")
        run = True
        self.player = Player("",0)
        self.logo_text = "Horse Racing"
        self.logo_surface = self.logo_font.render(self.logo_text, True, (0, 0, 0))
        self.play_button = Button("NEW GAME", self.font_btn, (400, 280), (52, 78, 91), (100, 120, 140), 280, 80)
        self.play_continue = Button("Continue", self.font_btn, (400, 380), (52, 78, 91), (100, 120, 140), 280, 80)
        self.exit = Button("EXIT", self.font_btn, (400, 480), (52, 78, 91), (100, 120, 140), 280, 80)
        background_image = pygame.image.load("./assets/MENU_BG.png") 
        background_image = pygame.transform.scale(background_image, (800, 700))

        logo_y = (self.screen.get_height() - self.logo_surface.get_height()) // 2 - 100

        while True:
            self.screen.blit(background_image, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.play_button.clicked(mouse_pos):
                        Player.create_player_name()
                    if self.play_continue.clicked(mouse_pos):
                        self.select_save()
                    if self.exit.clicked(mouse_pos):
                        quit()

            logo_y -= 0.4
            if logo_y < 100:
                logo_y = 100 
            logo_x = (self.screen.get_width() - self.logo_surface.get_width()) // 2
            self.screen.blit(self.logo_surface, (logo_x, logo_y))

            self.play_button.render(self.screen, mouse_pos)
            self.play_continue.render(self.screen, mouse_pos)
            self.exit.render(self.screen, mouse_pos)

            pygame.display.flip()



    def start_position_horse(self):
        self.moving_sprites.add(self.horse)
        self.moving_sprites.add(self.horseb)
        self.moving_sprites.add(self.horsew)
        self.moving_sprites.add(self.horseg)
        self.moving_sprites.add(self.horser)
        self.horse.animate()
        self.horseb.animate()
        self.horsew.animate()
        self.horseg.animate()
        self.horser.animate()

    def illutionist(self):
        if self.round_['horse'] < max(self.round_.values()) and self.round_['horse'] != 4:
            self.horse.image.set_alpha(0)
        else:
            self.horse.image.set_alpha(255)
        if self.round_['horseb'] < max(self.round_.values()) and self.round_['horseb'] != 4:
            self.horseb.image.set_alpha(0)
        else:
            self.horseb.image.set_alpha(255)
        if self.round_['horseg'] < max(self.round_.values()) and self.round_['horseg'] != 4:
            self.horseg.image.set_alpha(0)
        else:
            self.horseg.image.set_alpha(255)
        if self.round_['horsew'] < max(self.round_.values()) and self.round_['horsew'] != 4:
            self.horsew.image.set_alpha(0)
        else:
            self.horsew.image.set_alpha(255)
        if self.round_['horser'] < max(self.round_.values()) and self.round_['horser'] != 4:
            self.horser.image.set_alpha(0)
        else:
            self.horser.image.set_alpha(255)

    def Choice_bet(self):
        pygame.display.set_caption("BET")
        self.win = Button("BET WIN", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.place_ = Button("BET Place", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.place_win = Button("BET Place WIN", self.font_btn, (400, 450), (52, 78, 91), (100, 120, 140),350, 80)
        print(self.slected_players)
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.win.clicked(mouse_pos) and self.slected_players != "":
                       machine_bet = Machine_bet(self.slected_players.name,self.slected_players.coin,"WIN")
                       machine_bet.bet_WIN()
                    elif self.win.clicked(mouse_pos):
                       machine_bet = Machine_bet(Player.player,Player.coin,"WIN")
                       machine_bet.bet_WIN()

                    if self.place_.clicked(mouse_pos) and self.slected_players != "":
                       machine_bet = Machine_bet(self.slected_players.name,self.slected_players.coin,"WIN")
                       machine_bet.bet_WIN()
                    elif self.place_.clicked(mouse_pos):
                       machine_bet = Machine_bet(Player.player,Player.coin,"Place")
                       machine_bet.bet_WIN()
                    if self.place_win.clicked(mouse_pos) and self.slected_players != "":
                       machine_bet = Machine_bet(self.slected_players.name,self.slected_players.coin,"WIN")
                       machine_bet.bet_WIN()
                    elif self.place_win.clicked(mouse_pos):
                       machine_bet = Machine_bet(Player.player,Player.coin,"Place_WIN")
                       machine_bet.bet_WIN()
            self.win.render(self.screen, mouse_pos)
            self.place_.render(self.screen, mouse_pos)
            self.place_win.render(self.screen, mouse_pos)
            pygame.display.flip()
            
    def order(self):
        self.round_= {
            "horse": self.horse.round_,
            "horseb": self.horseb.round_,
            "horseg": self.horseg.round_,
            "horsew": self.horsew.round_,
            "horser": self.horser.round_
        }
        if max(self.round_.values()) >= 4 :
                current_background = 1
                self.bg_image = pygame.image.load(self.backgrounds[current_background]).convert()
                self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))
                if self.round_['horse'] >= 5 and self.round_['horse'] == max(self.round_.values()):
                    self.horse.stop()
                    if "Horse Brown" not in self.lst_:
                        self.lst_.append("Horse Brown")
                if self.round_['horseb'] >= 5 and self.round_['horseb'] == max(self.round_.values()):
                    self.horseb.stop()
                    if "Horse Black" not in self.lst_:
                        self.lst_.append("Horse Black")
                if self.round_['horseg'] >= 5 and self.round_['horseg'] == max(self.round_.values()):
                    self.horseg.stop()
                    if "Horse Grey" not in self.lst_:
                        self.lst_.append("Horse Grey")
                if self.round_['horsew'] >= 5 and self.round_['horsew'] == max(self.round_.values()):
                    self.horsew.stop()
                    if "Horse White" not in self.lst_:
                        self.lst_.append("Horse White")
                if self.round_['horser'] >= 5 and self.round_['horser'] == max(self.round_.values()) :
                    self.horser.stop()
                    if "Horse Red" not in self.lst_:
                        self.lst_.append("Horse Red")

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][1] > right_half[j][1] or (left_half[i][1] == right_half[j][1] and left_half[i][2] > right_half[j][2]):
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    def sort_horses(self):
        horses = [
            (self.horse, self.horse.position, self.horse.round_),
            (self.horseb, self.horseb.position, self.horseb.round_),
            (self.horseg, self.horseg.position, self.horseg.round_),
            (self.horsew, self.horsew.position, self.horsew.round_),
            (self.horser, self.horser.position, self.horser.round_)
        ]
        self.merge_sort(horses)
        sorted_horses = [(horse[0].__class__.__name__, horse[2]) for horse in horses]

        return sorted_horses

    def score_board(self):
        self.dashboard_text = []
        sorted_horses = self.sort_horses()
        for horse,round_ in sorted_horses:
            if round_ == 5:
                self.dashboard_text.append(f"{horse} Round: finish")
            else:
                self.dashboard_text.append(f"{horse} Round: {round_}")


class Machine_bet:
    def __init__(self, name, coin, bettype):
        self.player = Player(name, coin)
        self.coin = 0
        self.horse = ""
        self.place = 0
        self.bettype = bettype
        self.game = Game()
        self.bet_coin = 0
        self.font_btn = pygame.font.Font(None, 32)
        self.screen = pygame.display.set_mode((800, 700))

    def bet_WIN(self):
        pygame.display.set_caption("BET")
        self.HBr = Button("Horse Brown", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.HB = Button("Horse Black", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.HW = Button("Horse White", self.font_btn, (400, 450), (52, 78, 91), (100, 120, 140), 350, 80)
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.HBr.clicked(mouse_pos):
                        self.how_much()
                    if self.HB.clicked(mouse_pos):
                        self.how_much()
                    if self.HW.clicked(mouse_pos):
                        self.how_much()
            self.HBr.render(self.screen, mouse_pos)
            self.HB.render(self.screen, mouse_pos)
            self.HW.render(self.screen, mouse_pos)
            pygame.display.flip()

    def how_much(self):
        pygame.display.set_caption("BET")
        self.H = Button("100", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.TH = Button("1000", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.TTH = Button("10000", self.font_btn, (400, 450), (52, 78, 91), (100, 120, 140), 350, 80)
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.H.clicked(mouse_pos):
                        self.bet_coin = 100
                        self.game.run()
                    if self.TH.clicked(mouse_pos):
                        self.bet_coin = 1000
                        self.game.run()
                    if self.TTH.clicked(mouse_pos):
                        self.bet_coin = 10000
                        self.game.run()
            self.H.render(self.screen, mouse_pos)
            self.TH.render(self.screen, mouse_pos)
            self.TTH.render(self.screen, mouse_pos)
            pygame.display.flip()

