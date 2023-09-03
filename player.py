
import pygame

class Player:
    def __init__(self, name, coin):
        self.name = name
        self.coin = coin

    def display_info(self):
        print(f"Selected Player: {self.name}")

    @staticmethod
    def create_player_name():
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Create Player Example")

        player_name = ""
        input_rect = pygame.Rect(300, 300, 200, 40)
        input_color = pygame.Color('lightskyblue3')
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        font = pygame.font.Font(None, 36)
        active = False

        text = font.render("Enter Player Name (max 8 characters):", True, (255, 255, 255))
        text_rect = text.get_rect(center=(400, 200))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if len(player_name) <= 8 and player_name.strip() != "":
                                return player_name
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

            pygame.display.flip()