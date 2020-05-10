import pygame


def scale_image(input_image_path, output_image_path, width=None, height=None):
    input_image = pygame.image.load(input_image_path)
    input_image_rect = input_image.get_rect()
    original_width = input_image_rect.width
    original_height = input_image_rect.height

    if width:
        scale_factor = width / original_width
        output_image = pygame.transform.scale(input_image, (round(width), round(original_height * scale_factor)))
        pygame.image.save(output_image, output_image_path)
    if height:
        scale_factor = height / original_height
        output_image = pygame.transform.scale(input_image, (round(original_width * scale_factor), round(height)))
        pygame.image.save(output_image, output_image_path)
