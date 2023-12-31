import pygame
import time
import json
import random
import easygui
from button import Button,Select_button,TypeSelect_button,AdditionalSelect_button
from player import Player
from singlely_Link_list import LinkList
from My_tree import BinarySearchTree
from merg_sort import MergeSort
from My_queue import queue
from My_stack import Stack
from pygame import mixer
from horse import Horse_brown, Horse_black, Horse_white, Horse_grey, Horse_red, Player_Horse_red


class Game:
    def __init__(self,name="",coin=0,bet_coin=0,selected_players="", type_bet = "",result="",b_result=""):
        pygame.init()
        mixer.init()
        self.music = mixer.music
        self.music.load('./assets/music/bg_music.mp3')
        self.display = pygame.display
        self.link_list = LinkList()
        self.merge_sort = MergeSort()
        self.My_queue = queue()
        self.bet_queue = queue()
        self.binary_tree = BinarySearchTree()
        self.player = Player(name,coin)
        self.horser = Player_Horse_red(0, 375)
        self.type_bet = type_bet
        self.bet_coin = bet_coin
        self.bet_result = b_result
        self.result_ = result
        self.position = [375, 430, 485, 540, 595]
        self.horse_stack = Stack()
        self.horse_stack2 = Stack()
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

                run = False

            self.display.flip()
            self.clock.tick(60)
        go_mus.stop()
        self.round_['horse'] = 0
        self.round_['horseb'] = 0
        self.round_['horseg'] = 0
        self.round_['horsew'] = 0
        self.round_['horser'] = 0
        self.pay_out()

    def run_manual(self):
        mixer.init()
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load('./assets/bg.png').convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (800, 700))
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.horser)
        go_mus = mixer.music
        go_mus.load('./assets/music/go.wav')
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
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                is_up_pressed = False
            if keys[pygame.K_UP] and not is_up_pressed and self.horser.round_ < 5:
                self.horser.animate()
                is_up_pressed = True
            else:

                self.horser.wait()
                
            self.screen.blit(self.bg_image, (0, 0))
            self.moving_sprites.update(0.2)
            self.horser.update_manual(0.2)
    
            self.moving_sprites.draw(self.screen)

            if self.horser.round_ >= 1:
                run = False
            print(self.horser.round_)
            self.display.flip()
            self.clock.tick(60)
        go_mus.stop()
        self.horser.round_ = 0
        self.result_manual()

    def render_text(self,text, x, y, color=(0, 0, 0)):
        text_surface = self.font_save.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def select_save(self):
        self.player.name = ""
        self.player.coin = 0
        background_image = pygame.image.load("./assets/MENU_BG.png")
        background_image = pygame.transform.scale(background_image, (800, 700))
        self.music.stop()
        with open('./data/data.json', 'r') as json_file:
            data = json.load(json_file)
        self.back = Button("<<<", self.font_save, (30, 50), (52, 78, 91), (100, 120, 140), 50, 50)

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
                                self.player.update_name(self.selected_players.name)
                                self.player.update_coin(self.selected_players.coin)
                                print(self.selected_players.coin)
                                self.Choice_bet_play()

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
        self.music.play(-1)
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
                        self.create_player_name()
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
                            self.music.play(-1)
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
        count = 0
        n = len(self.position)
        random_numbers = [hash(obj + time.time()) for obj in self.position]
        
        for i in range(n):
            j = random_numbers[i] % (n - 1)
            self.position[i], self.position[j] = self.position[j], self.position[i]



        while count < 5:
            if count % 2 == 0:
                self.horse_stack2.push(int(self.position[count]))
                print("Count")
            else:
                self.horse_stack.push(int(self.position[count]))
                print("Count2")
            print(count,self.position[count])
            count += 1
            
        self.horse = Horse_brown(0, self.horse_stack.pop())
        self.horseb = Horse_black(0, self.horse_stack.pop())
        self.horsew = Horse_white(0, self.horse_stack2.pop())
        self.horseg = Horse_grey(0, self.horse_stack2.pop())
        self.horser = Horse_red(0, self.horse_stack2.pop())
        
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
        horse_images = [self.horse.image, self.horseb.image, self.horseg.image, self.horsew.image, self.horser.image]
        
        max_round_value = max(self.round_.values())
        
        for horse_name, horse_image in zip(['horse', 'horseb', 'horseg', 'horsew', 'horser'], horse_images):
            if self.round_[horse_name] < max_round_value and self.round_[horse_name] != 4:
                horse_image.set_alpha(0)
            else:
                horse_image.set_alpha(255)

    def create_player_name(self):
            self.player.name = ""
            self.player.coin = 0
            self.name = ""
            self.coin = 100
            display = pygame.display
            background_image = pygame.image.load("./assets/MENU_BG.png")

            background_image = pygame.transform.scale(background_image, (800, 700))
            back_font = pygame.font.Font('./font/NineteenNinetySeven-11XB.ttf', 18)
            display.set_caption("Create Player")
            back = Button("<<<", back_font, (30, 50), (52, 78, 91), (100, 120, 140), 50, 50)
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
                            self.menu_()

                    if event.type == pygame.KEYDOWN or pull == True:
                        if active:
                            if len(self.name) <= 8 and self.name.strip() != "" and create_player_button.clicked(mouse_pos):
                                self.player.update_name(self.name)
                                self.player.update_coin(self.coin)
                                self.player.auto_save()
                                self.Choice_bet_play()
                            elif event.key == pygame.K_BACKSPACE:
                                self.name = self.name[:-1]
                            elif len(self.name) < 8:
                                if event.key == pygame.K_SPACE:
                                    continue
                                self.name += str(event.unicode)
                            else:
                                pass

                self.screen.blit(background_image, (0, 0))
                
                txt_surface = font.render(self.name, True, (255, 255, 255))
                width = max(200, txt_surface.get_width()+10)
                input_rect.w = width
                pygame.draw.rect(self.screen, (0, 0, 0), input_rect)
                self.screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))

                self.screen.blit(text, text_rect)
                create_player_button.render(self.screen, mouse_pos)
                back.render(self.screen, mouse_pos)

                display.flip()

    def Choice_bet_play(self):
        self.display.set_caption("Choice To Play")
        self.music.stop()
        self.back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        player_info_surface = self.font_save.render(f"Player: {self.player.name} Coin: {self.player.coin}", True, (0, 0, 0))
        self.Bet_play = Button("BET", self.font_btn, (400, 250), (52, 78, 91), (100, 120, 140), 350, 80)
        self.Play_as_hourse = Button("Play", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        while True:
            self.screen.fill((220,220,220))
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.Bet_play.clicked(mouse_pos):
                       self.bet_()
                    if self.Play_as_hourse.clicked(mouse_pos) :
                       self.run_manual()
                    if self.back.clicked(mouse_pos) :
                       self.menu_()
            self.screen.blit(player_info_surface, (10, 670))
            self.Bet_play.render(self.screen, mouse_pos)
            self.Play_as_hourse.render(self.screen, mouse_pos)
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
                if self.round_['horse'] == 5 and self.round_['horse'] == max(self.round_.values()):
                    self.horse.stop()
                    if "Horse Brown" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Brown")
                if self.round_['horseb'] == 5 and self.round_['horseb'] == max(self.round_.values()):
                    self.horseb.stop()
                    if "Horse Black" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Black")
                if self.round_['horseg'] == 5 and self.round_['horseg'] == max(self.round_.values()):
                    self.horseg.stop()
                    if "Horse Grey" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse Grey")
                if self.round_['horsew'] == 5 and self.round_['horsew'] == max(self.round_.values()):
                    self.horsew.stop()
                    if "Horse White" not in self.My_queue.items:
                        self.My_queue.enqueue("Horse White")
                if self.round_['horser'] == 5 and self.round_['horser'] == max(self.round_.values()) :
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
            if round_ >= 5:
                self.dashboard_text.append(f"{horse} Round: finish")
            else:
                self.dashboard_text.append(f"{horse} Round: {round_}")

    def monte_carlo_horse_racing(self,num_iterations):
        wins = [0, 0, 0, 0, 0]

        for _ in range(num_iterations):
            winning_horse_idx = random.randint(0, 4)
            player_choice_idx = random.randint(0, 4)

            if player_choice_idx == winning_horse_idx:
                wins[player_choice_idx] += 1

        win_rates = [wins[i] / num_iterations for i in range(5)]

        return win_rates
    
    def bet_(self):
        self.screen.fill((0,0,0))
        button_width = 100
        button_height = 50
        button_spacing = 20
        button_x_start = 200  
        button_y_start = 110
        back = Button("<<<", self.font_save, (30, 30), (52, 78, 91), (100, 120, 140), 50, 50)
        num_iterations = 10000
        win_rates = self.monte_carlo_horse_racing(num_iterations)
        message = ""
        for i, horse in enumerate(["Horse Brown", "Horse Black", "Horse White", "Horse Grey", "Horse Red"]):
            win_rate_percentage = win_rates[i] * 100
            horse_info = f"{horse} - Win Rate: {win_rate_percentage:.2f}%"
            message += horse_info + "\n"

        easygui.msgbox(message, "อัตราการชนะของม้า")
        money = True
        notenough = True
        BLACK = (0, 0, 0)
        BROWN = (102,51,0)
        GREY = (220,220,220)
        RED = (255, 0, 0)
        player_info_surface = self.font_save.render(f"Player: {self.player.return_name} Coin: {self.player.return_coin}", True, BLACK)
        buttons = []
        name_horse = ["Horse Brown", "Horse Black", "Horse White", "Horse Grey", "Horse Red"]
        for i, name in enumerate(name_horse):
            button = Select_button(
                text=f"{name}",
                font=self.font_save,
                position=(
                    button_x_start,
                    button_y_start + (100 + button_spacing) * i,
                ),
                color_idle=BROWN,
                color_hover=RED,
                width=300,
                height=80,
            )
            buttons.append(button)

        image_paths = {
            "Horse Brown": "./assets/brown/move1.png",
            "Horse Black": "./assets/black/move-black1.png",
            "Horse White": "./assets/white/move-white1.png",
            "Horse Grey": "./assets/grey/move-grey1.png",
            "Horse Red": "./assets/red/move-red1.png"
        }

        button_images = {}
        image_positions = {}

        for i, button in enumerate(buttons):
            image_path = image_paths.get(button.text)
            if image_path:
                button_images[button.text] = pygame.image.load(image_path)
                image_positions[button.text] = (button_x_start - 170, (button_y_start - 50) + (100 + button_spacing) * i)
        additional_buttons = []
        numbers = [100, 1000, 10000]
        for i, number in enumerate(numbers):
            button = AdditionalSelect_button(
                text=f"{number}",
                font=self.font_save,
                position=(
                    button_x_start + 400,
                    button_y_start+ 200 + (button_height + button_spacing) * i,
                ),
                color_idle=BLACK,
                color_hover=RED,
                width=button_width,
                height=button_height,
            )
            additional_buttons.append(button)

        Type_buttons = []
        Types = ["Bet Win", "Bet Place"]
        for i, type in enumerate(Types):
            button = TypeSelect_button(
                text=f"{type}",
                font=self.font_save,
                position=(
                    button_x_start + 400,
                    button_y_start + (button_height + button_spacing) * i,
                ),
                color_idle=BLACK,
                color_hover=RED,
                width=button_width+50,
                height=button_height,
            )
            Type_buttons.append(button)

        submit_button = Select_button(
            text="START RACE!",
            font=self.font_save,
            position=(button_x_start+400, 550),
            color_idle=BLACK,
            color_hover=RED,
            width=button_width + 100,
            height=button_height,
        )

        running = True
        selected_buttons = [] 
        selected_additional_buttons = [] 
        selected_type_buttons = []

        while running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in Type_buttons:
                            if button.clicked(event.pos):
                                if len(selected_type_buttons) < 1 and money or button.selected and money:
                                    button.selected = not button.selected
                                    if button.selected:
                                        selected_type_buttons.append(button)
                                    else:
                                        selected_type_buttons.remove(button)
                        selected_texts = [button.text for button in selected_type_buttons]

                        for button in buttons:
                            if button.clicked(event.pos):
                                if ("".join(selected_texts) == "Bet Place"):
                                    if len(selected_buttons) < 3 and money or button.selected and money:
                                        button.selected = not button.selected
                                        if button.selected:
                                            selected_buttons.append(button)
                                        else:
                                            selected_buttons.remove(button)
                                elif ("".join(selected_texts) == "Bet Win"):
                                    if len(selected_buttons) < 1 and money or button.selected and money:
                                        button.selected = not button.selected
                                        if button.selected:
                                            selected_buttons.append(button)
                                        else:
                                            selected_buttons.remove(button)
                                elif (("".join(selected_texts) != "Bet Win") and money or ("".join(selected_texts) == "Bet Place") and money):
                                    easygui.msgbox("กรุณาเลือกประเภทก่อน", "Alert")

                        for button in additional_buttons:
                            if button.clicked(event.pos):
                                if len(selected_additional_buttons) < 1 or button.selected and self.player.return_coin >= 100:
                                    button.selected = not button.selected
                                    if button.selected:
                                        selected_additional_buttons.append(button)
                                        selected_money = [button.text for button in selected_additional_buttons]
                                        selected_money_value = int("".join(selected_money))
                                        if self.player.return_coin >= selected_money_value:
                                            money = True
                                            notenough = True
                                        elif self.player.return_coin < selected_money_value:
                                            money = False                                                        
                                        else:
                                            selected_additional_buttons.remove(button)
                                        print(money)

                        if submit_button.clicked(event.pos):
                            idx = 1
                            if (notenough):
                                if (("".join(selected_texts)) == "Bet Place" and len(selected_additional_buttons) == 1 and len(selected_buttons) == 3  ):
                                    for selected_button in selected_buttons[:3]:
                                        print(f"{idx}. {selected_button.text}")
                                        self.bet_queue.enqueue(selected_button.text)
                                        idx += 1
                                    for money_button in selected_additional_buttons[:1]:
                                        print(f"{idx}. {money_button.text}")
                                        self.bet_coin = int(money_button.text)
                                        idx += 1
                                    for type_button in selected_type_buttons[:1]:
                                        print(f"{idx}. {type_button.text}")
                                        self.bet_type = type_button.text
                                        idx += 1
                                    self.run()  
                                elif (("".join(selected_texts))== "Bet Win" and len(selected_additional_buttons) == 1 and len(selected_buttons) == 1):
                                    for selected_button in selected_buttons[:1]:
                                        print(f"{idx}. {selected_button.text}")
                                        self.bet_queue.enqueue(selected_button.text)
                                        idx += 1
                                    for money_button in selected_additional_buttons[:1]:
                                        print(f"{idx}. {money_button.text}")
                                        self.bet_coin = int(money_button.text)
                                        idx += 1
                                    for type_button in selected_type_buttons[:1]:
                                        print(f"{idx}. {type_button.text}")
                                        self.bet_type = type_button.text
                                        idx += 1
                                    self.run()  
                                else:
                                    easygui.msgbox("กรุณาเลือกให้ครบก่อน", "Alert")                                                          
                            elif (not notenough):
                                easygui.msgbox("ฮั่นแนนนนนนนนน่.....", "Alert")
    
                        elif (submit_button.clicked(event.pos) and len(selected_additional_buttons) != 1 and len(selected_buttons) != 3 and notenough or submit_button.clicked(event.pos) and len(selected_additional_buttons) != 1 and len(selected_buttons) != 1 and notenough):
                            easygui.msgbox("กรุณาเลือกให้ครบก่อน", "Alert")
                        elif (not money):
                            easygui.msgbox("ไปหาเงินมาก่อนนะจ๊ะ.....", "Alert")
                            money = True
                            notenough = False
                    if back.clicked(mouse_pos):
                        self.Choice_bet_play()

            self.screen.fill(GREY)
            self.screen.blit(player_info_surface, (10, 670))

            for button in buttons:
                button.render_change(self.screen, pygame.mouse.get_pos())

            for button in buttons:
                image = button_images.get(button.text)
                position = image_positions.get(button.text)
                if image and position:
                    self.screen.blit(image, position)

            for button in additional_buttons + [submit_button] + Type_buttons:
                button.render_change(self.screen, pygame.mouse.get_pos())
            back.render(self.screen, mouse_pos)
            pygame.display.flip()

    def result(self):
        self.display.set_caption("PayOUT")
        self.OK = Button("OK", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.music.stop()
        result_text = self.font.render(f"{self.result_[0]}", True, (0, 0, 0))
        money = self.font_btn.render(f"{self.result_[1]} {self.bet_result}", True, (0, 0, 0))

        text_width, text_height = result_text.get_size()
        money_width, money_height = money.get_size()
        screen_width, screen_height = self.screen.get_size()
        text_x = (screen_width - text_width) // 2
        money_x = (screen_width - money_width) // 2

        while True:
            self.screen.fill((220, 220, 220))
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.OK.clicked(mouse_pos):
                        self.Choice_bet_play()

            self.screen.blit(result_text, (text_x + 10, 100))
            self.screen.blit(money, (money_x + 20, 500))
            self.OK.render(self.screen, mouse_pos)
            self.My_queue.clear()
            self.bet_queue.clear()
            self.player.auto_save()
            self.display.flip()

    def result_manual(self):
        self.display.set_caption("Manual PayOUT")
        OK = Button("OK", self.font_btn, (400, 350), (52, 78, 91), (100, 120, 140), 350, 80)
        self.music.stop()
        result_text = self.font_btn.render("YOU GOT MONEY!!!", True, (0, 0, 0))
        money = self.font_btn.render("+ 100", True, (0, 0, 0))
        self.player.update_coin(100)
        self.player.auto_save()
        text_width, text_height = result_text.get_size()
        money_width, money_height = money.get_size()
        screen_width, screen_height = self.screen.get_size()
        text_x = (screen_width - text_width) // 2
        money_x = (screen_width - money_width) // 2

        while True:
            self.screen.fill((220, 220, 220))
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if OK.clicked(mouse_pos):
                        self.Choice_bet_play()

            self.screen.blit(result_text, (text_x + 10, 100))
            self.screen.blit(money, (money_x + 10, 500))
            OK.render(self.screen, mouse_pos)
            self.display.flip()


    def pay_out(self):
        check = True
        if self.bet_type == "Bet Win":
            if (not self.bet_queue.is_empty()):
                dequeue = self.My_queue.dequeue()
                dequeue_bet = self.bet_queue.dequeue()
                if dequeue == dequeue_bet:
                    self.bet_result = self.bet_coin * 0.5
                    self.player.update_coin(self.bet_coin * 0.5)
                    self.result_ = ["WIN", "+"]
                    self.result()
                elif (dequeue != dequeue_bet):
                    self.bet_result = -self.bet_coin
                    self.player.update_coin(-self.bet_coin)
                    self.result_ = ["LOSE", ""]
                    self.result()
        elif self.bet_type == "Bet Place":
            count = 0
            check = False
            for i in range(3):
                dequeue = self.My_queue.dequeue()
                dequeue_bet = self.bet_queue.dequeue()
                self.binary_tree.insert(i, dequeue_bet, "Win")
                print(self.binary_tree.find_bet(i, dequeue))
                if (self.binary_tree.find_bet(i, dequeue) == "Win"):
                    check = True
                    count += 1
            print(check,count)
            if (check == True and count == 3):
                self.bet_result = self.bet_coin * 3
                self.result_ = ["WIN", "+"]
                self.player.update_coin(self.bet_coin * 3)
            else:
                self.result_ = ["LOSE", ""]
                self.bet_result = -self.bet_coin
                self.player.update_coin(-self.bet_coin)
            self.My_queue.clear()
            self.bet_queue.clear()
            self.binary_tree.clear()
            self.player.auto_save()
            self.result()     

if __name__ == "__main__":
    game = Game()
    game.menu_()

