import pygame
import os
import image_resize
import mainbuttons
import config as c


background_path = "covers\\background.jpg"
background = pygame.image.load(background_path)
background_rect = background.get_rect()
normal_background_width = background_rect.width

if background_rect.width > c.screen_width:
    image_resize.scale_image(background_path,
                             background_path[:-4] + "_scaled.jpg", c.screen_width)
    background = pygame.image.load(background_path[:-4] + "_scaled.jpg")
    background_rect = background.get_rect()
    os.remove(background_path[:-4] + "_scaled.jpg")
if background_rect.height > c.screen_height:
    image_resize.scale_image(background_path,
                             background_path[:-4] + "_scaled.jpg", None, c.screen_height)
    background = pygame.image.load(background_path[:-4] + "_scaled.jpg")
    background_rect = background.get_rect()
    os.remove(background_path[:-4] + "_scaled.jpg")

scaled_background_width = background_rect.width
scale_factor = scaled_background_width / normal_background_width

background_rect.centerx = c.screen_width // 2
background_rect.centery = c.screen_height // 2
run = True

buttons = []
exitbutton = mainbuttons.ExitButton(scale_factor, background_rect.right - 175,
                                    background_rect.bottom - 100)
Antiquitybutton = mainbuttons.AntiquityButton(scale_factor, background_rect.left + 25,
                                              background_rect.top + 25)
Middleagesbutton = mainbuttons.MiddleAgesButton(scale_factor, background_rect.left + 25,
                                                Antiquitybutton.rect.bottom + 50)
RenaissanceButton = mainbuttons.RenaissanceButton(scale_factor, background_rect.left + 25,
                                                  Middleagesbutton.rect.bottom + 50)
RealismButton = mainbuttons.RealismButton(scale_factor, Antiquitybutton.rect.right + 25,
                                          background_rect.top + 25)
ModernismButton = mainbuttons.ModernismButton(scale_factor, RealismButton.rect.right + 25,
                                              background_rect.top + 25)
ContemporaryArtButton = mainbuttons.ContemporaryArtButton(scale_factor, ModernismButton.rect.right + 25,
                                                          background_rect.top + 25)
OrientalArtButton = mainbuttons.OrientalArtButton(scale_factor, ContemporaryArtButton.rect.right + 25,
                                                  background_rect.top + 25)
buttons.append(exitbutton)
buttons.append(Antiquitybutton)
buttons.append(Middleagesbutton)
buttons.append(RenaissanceButton)
buttons.append(RealismButton)
buttons.append(ModernismButton)
buttons.append(ContemporaryArtButton)
buttons.append(OrientalArtButton)

while run:
    c.screen.fill((0, 0, 0))
    c.screen.blit(background, background_rect)

    for button in buttons:
        button.draw(c.screen)

    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                run = False

        if i.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (True, False, False):
                mouse_position = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_position):
                        pygame.mouse.set_visible(False)
                        button.clicked()
    c.clock.tick(c.FPS)
    pygame.display.update()
