import pygame

class Button:
    def __init__(self, text="", font="", position=(400, 300), color_idle=(0, 128, 255), color_hover=(0, 0, 0), width=200, height=50):
        self.text = text
        self.font = font
        self.position = position
        self.color_idle = color_idle
        self.color_hover = color_hover

        self.rect = pygame.Rect(
            self.position[0] - width // 2,
            self.position[1] - height // 2,
            width,
            height,
        )
        self.arrow_icon = ">"
        self.shadow_color = (128, 128, 128)
        self.shadow_offset = (10, 10) 

    def render(self, screen, mouse_pos):
        shadow_rect = self.rect.copy()
        shadow_rect.topleft = (self.rect.left + self.shadow_offset[0], self.rect.top + self.shadow_offset[1])
        pygame.draw.rect(screen, self.shadow_color, shadow_rect)

        color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_idle
        pygame.draw.rect(screen, color, self.rect)

        arrow_x = self.rect.left - 30
        arrow_y = (self.rect.centery - self.font.get_height() // 2) + 15

        if color == self.color_hover:
            arrow_text_surface = self.font.render(self.arrow_icon, True, (51,51, 255))
            arrow_text_rect = arrow_text_surface.get_rect(left=arrow_x, centery=arrow_y)
            screen.blit(arrow_text_surface, arrow_text_rect)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
