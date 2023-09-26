import pygame
import time
import json
import easygui
from button import Button
from player import Player
from singlely_Link_list import LinkList
from merg_sort import MergeSort
from My_queue import queue
from pygame import mixer
from horse import Horse_brown, Horse_black, Horse_white, Horse_grey, Horse_red


class Game:
    def __init__(self,coin=0,bet_coin=0,horse_bet="",selected_players=""):
        pygame.init()
        mixer.init()
        self.music = mixer.music
        self.music.load('./assets/music/bg_music.mp3')
        self.display = pygame.display
        self.link_list = LinkList()
        self.merge_sort = MergeSort()
        self.My_queue = queue()
        self.player = Player()
        self.coin = coin
        self.bet_coin = bet_coin
        self.horse_bet = horse_bet
        self.selected_players = selected_players
        self.screen = self.display.set_mode((800, 700))
        self.display.set_caption("Horse Racing")
        self.font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 100)
        self.font_btn = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 32)
        self.font_btn_sound = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 10)
        self.logo_font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 72)
        self.font_save = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 18)
        self.custom_font = pygame.font.Font(None, 20)
        self.link_list.append('./assets/bg.png')
        self.link_list.append('./assets/grey_bg.png')
        self.link_list.append('./assets/final.png')
        self.bg_image = pygame.image.load("".join(self.link_list.get_link_list(1))).convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))


    def run(self):
        mixer.init()
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('./assets/bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))
        self.moving_sprites = pygame.sprite.Group()
        self.start_position_horse()
        go_mus = mixer.music
        go_mus.load('./assets/music/go.wav')

        self.topic_dashboard = "Horse Racing Score-Board"
        go_mus.play()
        for i in range(3, 0, -1):

            # ล้างหน้าจอและเปลี่ยนพื้นหลัง
            self.screen.fill((255, 255, 255))
            self.screen.blit(self.bg_image, (0, 0))

            # แสดงข้อความนับถอยหลัง
            text = self.font.render(str(i), True, (255, 255, 255))
            text_rect = text.get_rect(center=(400, 350))
            self.screen.blit(text, text_rect)
            self.display.flip()
            time.sleep(0.5)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.bg_image, (0, 0))
        self.text = self.font.render("start", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(400, 350))
        self.screen.blit(self.text, self.text_rect)
        self.display.flip()
        time.sleep(1)
        go_mus.stop()
        time.sleep(1)
        go_mus.load('./assets/music/bg_music.mp3')
        go_mus.play()
        run = True
        while run:
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
            if self.My_queue.size() < 5:
                y_positions = [10, 20, 30, 40, 50]
                for i, text in enumerate(self.dashboard_text):
                    text_surface = self.custom_font.render(text, True, (255, 255, 255))
                    self.screen.blit(text_surface, (0, y_positions[i]))
            elif self.My_queue.size() >= 5:
                print(self.My_queue.size())
                print(self.My_queue.items)
                y_positions = [10, 20, 30, 40, 50]
                for i, text in enumerate(self.My_queue.items):
                    text_surface = self.custom_font.render(text, True, (255, 255, 255))
                    self.screen.blit(text_surface, (0, y_positions[i]))
                print(self.horse.round_, self.horseb.round_,self.horsew.round_,self.horseg.round_,self.horser.round_)
                self.round_['horse'] = 0
                self.round_['horseb'] = 0
                self.round_['horseg'] = 0
                self.round_['horsew'] = 0
                self.round_['horser'] = 0
                run = False

            self.display.flip()
            self.clock.tick(60)
        go_mus.stop()
        self.pay_out()




    def render_text(self,text, x, y, color=(0, 0, 0)):
        text_surface = self.font_save.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def select_save(self):
        background_image = pygame.image.load("./assets/MENU_BG.png")
        background_image = pygame.transform.scale(background_image, (800, 700))
        self.music.stop()
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
                                self.selected_players = players[i]
                                self.Choice_bet_play(self.selected_players.name,self.selected_players.coin)

                        for i, button_rect in enumerate(button_rects):
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                current_page = i
                    if self.back.clicked(mouse_pos):
                        self.menu_()
            self.screen.blit(background_image, (0, 0))
            start_idx = current_page * players_per_page
            end_idx = min((current_page + 1) * players_per_page, num_players)

            for i, player in enumerate(players[start_idx:end_idx]):
                box_y = box_y_start + (i % players_per_page) * box_height
                player_box = pygame.Rect(box_x, box_y, box_width, box_height)
                pygame.draw.rect(self.screen, (0, 255, 0), player_box, 2)
                pygame.draw.rect(self.screen, (0, 0, 0), (box_x+5, box_y+5, box_width-10, box_height-10))
                self.render_text(f"SAVE {i + 1 + start_idx}: {player.name}", box_x + 20, box_y + 10, (255, 255, 255))
                self.render_text(f"Coin: {player.coin}", box_x + 20, box_y + 50, (255, 255, 255))


            for i, button_rect in enumerate(button_rects):
                pygame.draw.rect(self.screen, (0, 255, 0), button_rect)
                self.render_text(str(i + 1), button_rect.centerx - 10, button_rect.centery - 10)

            self.back.render(self.screen, mouse_pos)
            self.display.flip()


    def menu_(self):
        self.player.name = ""
        self.music.play()
        self.display.set_caption("Main Menu")

        play_button = Button("NEW GAME", self.font_btn, (400, 300), (52, 78, 91), (0, 0, 0), 280, 80)
        play_continue = Button("Continue", self.font_btn, (400, 400), (52, 78, 91), (0, 0, 0), 280, 80)
        exit = Button("EXIT", self.font_btn, (400, 500), (52, 78, 91), (0, 0, 0), 280, 80)
        stop_music_button = Button("ON", self.font_btn_sound, (50, 650), (52, 78, 91), (0, 0, 0), 50, 50)
        music_button = Button("OFF", self.font_btn_sound, (50, 650), (52, 78, 91), (0, 0, 0), 50, 50)
        background_image = pygame.image.load("./assets/MENU_BG.png")
        background_image = pygame.transform.scale(background_image, (800, 700))

        logo_image = pygame.image.load("./assets/logo.png")
        logo_image = pygame.transform.scale(logo_image, (800, 700))
        logo_image = pygame.transform.scale(logo_image, (500, 150))
        logo_y = (self.screen.get_height() - logo_image.get_height()) // 2 - 100
        music_stop = False 

        while True:
            self.screen.blit(background_image, (0, 0))
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.clicked(mouse_pos):
                        self.player.create_player_name()
                    if play_continue.clicked(mouse_pos):
                        self.select_save()
                    if exit.clicked(mouse_pos):
                        quit()
                    if stop_music_button.clicked(mouse_pos):
                        if (not music_stop):
                            stop_music_button  = music_button 
                            self.music.stop()
                            music_stop = True
                        elif (music_stop):
                            stop_music_button = Button("ON", self.font_btn_sound, (50, 650), (52, 78, 91), (0, 0, 0), 50, 50)
                            self.music.play()
                            music_stop = False

            logo_y -= 0.4
            if logo_y < 50:
                logo_y = 50
            logo_x = (self.screen.get_width() - logo_image.get_width()) // 2
            self.screen.blit(logo_image, (logo_x, logo_y))

            play_button.render(self.screen, mouse_pos)
            play_continue.render(self.screen, mouse_pos)
            exit.render(self.screen, mouse_pos)
            stop_music_button.render(self.screen, mouse_pos)

            self.display.flip()



    def start_position_horse(self):
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

    def Choice_bet_play(self,name,coin):
        self.display.set_caption("Choice To Play")
        self.player.name = name
        self.coin = coin
        self.music.play()
        self.back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        player_info_surface = self.font_save.render(f"Player: {name} Coin: {coin}", True, (255, 255, 255))
        self.Bet_play = Button("BET", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.Play_as_hourse = Button("Play", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Bet_play.clicked(mouse_pos):
                       self.Choice_bet(name,coin)
                    if self.Play_as_hourse.clicked(mouse_pos) :
                       pass
                    if self.back.clicked(mouse_pos) :
                       self.menu_()
            self.screen.blit(player_info_surface, (10, 670))
            self.Bet_play.render(self.screen, mouse_pos)
            self.Play_as_hourse.render(self.screen, mouse_pos)
            self.screen.blit(player_info_surface, (10, 670))
            self.back.render(self.screen, mouse_pos)
            self.display.flip()

    def Choice_bet(self,name,coin):
        self.display.set_caption("BET")
        self.player.name = name
        self.coin = coin
        self.back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        player_info_surface = self.font_save.render(f"Player: {name} Coin: {coin}", True, (255, 255, 255))
        self.win = Button("BET WIN", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.place_ = Button("BET Place", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()  
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.win.clicked(mouse_pos):
                       self.bet_WIN()

                    if self.place_.clicked(mouse_pos) :
                       self.bet_WIN()
                    if self.back.clicked(mouse_pos) :
                       self.Choice_bet_play(name,coin)
            self.screen.blit(player_info_surface, (10, 670))
            self.win.render(self.screen, mouse_pos)
            self.place_.render(self.screen, mouse_pos)
            self.screen.blit(player_info_surface, (10, 670))
            self.back.render(self.screen, mouse_pos)
            self.display.flip()
            
    def order(self):
        self.round_= {
            "horse": self.horse.round_,
            "horseb": self.horseb.round_,
            "horseg": self.horseg.round_,
            "horsew": self.horsew.round_,
            "horser": self.horser.round_
        }
        if max(self.round_.values()) >= 4 :
                self.bg_image = pygame.image.load("".join(self.link_list.get_link_list(3))).convert()
                self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))
                if self.round_['horse'] >= 5 and self.round_['horse'] == max(self.round_.values()):
                    self.horse.stop()
                    if "Horse Brown" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Brown")
                if self.round_['horseb'] >= 5 and self.round_['horseb'] == max(self.round_.values()):
                    self.horseb.stop()
                    if "Horse Black" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Black")
                if self.round_['horseg'] >= 5 and self.round_['horseg'] == max(self.round_.values()):
                    self.horseg.stop()
                    if "Horse Grey" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Grey")
                if self.round_['horsew'] >= 5 and self.round_['horsew'] == max(self.round_.values()):
                    self.horsew.stop()
                    if "Horse White" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse White")
                if self.round_['horser'] >= 5 and self.round_['horser'] == max(self.round_.values()) :
                    self.horser.stop()
                    if "Horse Red" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Red")
        elif(max(self.round_.values()) >= 1):
            self.bg_image = pygame.image.load("".join(self.link_list.get_link_list(2))).convert()
            self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))



    def sort_horses(self):
        horses = [
            (self.horse, self.horse.position, self.horse.round_),
            (self.horseb, self.horseb.position, self.horseb.round_),
            (self.horseg, self.horseg.position, self.horseg.round_),
            (self.horsew, self.horsew.position, self.horsew.round_),
            (self.horser, self.horser.position, self.horser.round_)
        ]
        self.merge_sort.merge_sort(horses)
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
    
                

    def bet_WIN(self,):
        self.display.set_caption("BET WIN")
        player_info_surface = self.font_save.render(f"Player: {self.player.name} Coin: {self.coin}", True, (255, 255, 255))
        self.back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        self.HBr = Button("Horse Brown", self.font_btn, (400, 150), (52, 78, 91), (100, 120, 140), 350, 80)
        self.HB = Button("Horse Black", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.HW = Button("Horse White", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.HR = Button("Horse Red", self.font_btn, (400, 450), (52, 78, 91), (100, 120, 140), 350, 80)
        self.HGR = Button("Horse Grey", self.font_btn, (400, 550), (52, 78, 91), (100, 120, 140), 350, 80)
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.HBr.clicked(mouse_pos):
                        self.horse_bet = "Horse Brown"
                        self.how_much()
                    if self.HB.clicked(mouse_pos):
                        self.horse_bet = "Horse Black"
                        self.how_much()
                    if self.HW.clicked(mouse_pos):
                        self.horse_bet = "Horse White"
                        self.how_much()
                    if self.HR.clicked(mouse_pos):
                        self.horse_bet = "Horse Red"
                        self.how_much()
                    if self.HGR.clicked(mouse_pos):
                        self.horse_bet = "Horse Grey"
                        self.how_much()
                    elif self.back.clicked(mouse_pos):
                        self.Choice_bet(self.player.name,self.coin)
            self.HBr.render(self.screen, mouse_pos)
            self.HB.render(self.screen, mouse_pos)
            self.HW.render(self.screen, mouse_pos)
            self.HR.render(self.screen, mouse_pos)
            self.HGR.render(self.screen, mouse_pos)
            self.back.render(self.screen, mouse_pos)
            self.screen.blit(player_info_surface, (10, 670))
            self.display.flip()

    def how_much(self):
        self.display.set_caption("BET")
        self.H = Button("100", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.TH = Button("1000", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.TTH = Button("10000", self.font_btn, (400, 450), (52, 78, 91), (100, 120, 140), 350, 80)
        self.back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        player_info_surface = self.font_save.render(f"Player: {self.player.name} Coin: {self.coin}", True, (255, 255, 255))
        while True:
            self.screen.fill((52, 78, 91))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.H.clicked(mouse_pos):
                        self.bet_coin = 100
                        if self.coin < self.bet_coin:
                            easygui.msgbox("Not Enough Money", "Alert")
                        else:
                            self.run()
                    if self.TH.clicked(mouse_pos):
                        self.bet_coin = 1000
                        if self.coin < self.bet_coin:
                            easygui.msgbox("Not Enough Money", "Alert")
                        else:
                            self.run()
                    if self.TTH.clicked(mouse_pos):
                        self.bet_coin = 10000
                        if self.coin < self.bet_coin:
                           easygui.msgbox("Not Enough Money", "Alert")
                        else:
                            self.run()
                    if self.back.clicked(mouse_pos):
                        self.Choice_bet(self.player.name,self.coin)
            self.H.render(self.screen, mouse_pos)
            self.TH.render(self.screen, mouse_pos)
            self.TTH.render(self.screen, mouse_pos)
            self.back.render(self.screen, mouse_pos)
            self.screen.blit(player_info_surface, (10, 670))
            self.display.flip()

    def pay_out(self):
        dequeue = self.My_queue.dequeue()
        print(dequeue,self.horse_bet,self.bet_coin,self.coin)
        if dequeue == self.horse_bet:
            self.coin += self.bet_coin * 2
        else:
            self.coin -= self.bet_coin
        if (not self.My_queue.is_empty()):
            for i in range(self.My_queue.size()):
                self.My_queue.dequeue()
        print(self.player.name,self.coin,self.My_queue.size())
        self.player.auto_save(self.player.name,self.coin)
        self.Choice_bet(self.player.name,self.coin)

