import pygame

class Button:
    def __init__(self, text="", font="", position=(400, 300), color_idle=(0, 128, 255), color_hover=(0, 0, 0), width=200, height=50, corner_radius=80):
        self.text = text
        self.font = font
        self.position = position
        self.color_idle = color_idle
        self.color_hover = color_hover
        self.width = width
        self.height = height
        self.corner_radius = corner_radius
        self.rect = pygame.Rect(self.position[0] - self.width // 2, self.position[1] - self.height // 2, self.width, self.height)

        self.shadow_color = (128, 128, 128)
        self.shadow_offset = (10, 10)

    def render(self, screen, mouse_pos):
        shadow_rect = self.rect.copy()
        shadow_rect.topleft = (self.rect.left + self.shadow_offset[0], self.rect.top + self.shadow_offset[1])
        pygame.draw.rect(screen, self.shadow_color, shadow_rect, border_radius=self.corner_radius)

        color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_idle
        pygame.draw.rect(screen, color, self.rect, border_radius=self.corner_radius)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


class Select_button(Button):
    def __init__(self, text="", font="", position=(400, 300), color_idle=(0, 128, 255),color_hover=(0, 0, 0), width=200, height=50):
        super().__init__(text, font, position, color_idle, color_hover, width, height)
        self.selected = False
        self.rect = pygame.Rect(
            self.position[0] - width // 2,
            self.position[1] - height // 2,
            width,
            height,
        )

        self.shadow_color = None
        self.shadow_offset = (10, 10)

    def render_change(self, screen, mouse_pos):
        if self.shadow_color is not None:
            shadow_rect = self.rect.copy()
            shadow_rect.topleft = (self.rect.left + self.shadow_offset[0], self.rect.top + self.shadow_offset[1])
            pygame.draw.rect(screen, self.shadow_color, shadow_rect)

        RED = (255, 0, 0)
        if self.selected:
            color = RED
        else:
            color = self.color_hover if self.rect.collidepoint(mouse_pos) else self.color_idle

        pygame.draw.rect(screen, color, self.rect)

        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

class AdditionalSelect_button(Select_button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected = False

class TypeSelect_button(Select_button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.selected = False
