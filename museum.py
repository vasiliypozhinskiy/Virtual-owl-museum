import pygame
import os
import image_resize
import mainbuttons
import config as c

background = pygame.image.load("covers\\Old_supreme_court_singapore_hall.jpg")
background_rect = background.get_rect()

if background_rect.width > c.screen_width:
    image_resize.scale_image("covers\\Old_supreme_court_singapore_hall.jpg",
                             "covers\\Old_supreme_court_singapore_hall_scaled.jpg", c.screen_width)
    background = pygame.image.load("covers\\Old_supreme_court_singapore_hall_scaled.jpg")
    background_rect = background.get_rect()
    os.remove("covers\\Old_supreme_court_singapore_hall_scaled.jpg")
if background_rect.height > c.screen_height:
    image_resize.scale_image("covers\\Old_supreme_court_singapore_hall.jpg",
                             "covers\\Old_supreme_court_singapore_hall_scaled.jpg", None, c.screen_height)
    background = pygame.image.load("covers\\Old_supreme_court_singapore_hall_scaled.jpg")
    background_rect = background.get_rect()
    os.remove("covers\\Old_supreme_court_singapore_hall_scaled.jpg")

background_rect.centerx = c.screen_width // 2
background_rect.centery = c.screen_height // 2
run = True

buttons = []
exitbutton = mainbuttons.ExitButton((background_rect.right - 175,
                                     background_rect.bottom - 100, 150, 75))
antiquitybutton = mainbuttons.AntiquityButton((background_rect.left + 25,
                                               background_rect.top + 25, 310, 209))
middleagesbutton = mainbuttons.MiddleAgesButton((background_rect.left + 25,
                                                 antiquitybutton.rect.bottom + 50, 210, 209))
RenaissanceButton = mainbuttons.RenaissanceButton((background_rect.left + 25,
                                                   middleagesbutton.rect.bottom + 50, 203, 275))
RealismButton = mainbuttons.RealismButton((antiquitybutton.rect.right + 25,
                                           background_rect.top + 25, 210, 266))
ModernismButton = mainbuttons.ModernismButton((RealismButton.rect.right + 25,
                                               background_rect.top + 25, 205, 212))
ContemporaryArtButton = mainbuttons.ContemporaryArtButton((ModernismButton.rect.right + 25,
                                                           background_rect.top + 25, 310, 179))
OrientalArtButton = mainbuttons.OrientalArtButton((ContemporaryArtButton.rect.right + 25,
                                                   background_rect.top + 25, 310, 215))
buttons.append(exitbutton)
buttons.append(antiquitybutton)
buttons.append(middleagesbutton)
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
