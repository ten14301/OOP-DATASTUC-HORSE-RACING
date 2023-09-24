import pygame
class Button:
    def __init__(self, text="", font="", position=(400,300), color_idle=(0,128,255), color_hover=(0,255,128), width=200, height=50):
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

    def render(self, screen, mouse_pos):
        color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_idle
        pygame.draw.rect(screen, color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)