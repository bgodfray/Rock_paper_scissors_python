import pygame
import random
import time

pygame.init()

#create game window
width, height = 800, 600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Cat, Mouse, Elephant")

#  colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0,0,255)

#font
font = pygame.font.SysFont(None, 40, bold=False, italic=False)
large_font = pygame.font.SysFont(None, 60, bold=False, italic=False)

#load pictures
cat_pic = pygame.image.load("cat.png")
mouse_pic = pygame.image.load("mouse.png")
elephant_pic = pygame.image.load("elephant.png")

#scale pictures
img_size = (300,300)
cat_pic = pygame.transform.scale(cat_pic, img_size)
mouse_pic = pygame.transform.scale(mouse_pic, img_size)
elephant_pic = pygame.transform.scale(elephant_pic, img_size)

def draw_text(text, font, colour, x, y):
    img = font.render(text, True, colour)
    text_rect = img.get_rect(center=(x, y))
    window.blit(img, text_rect)

def draw_button(text, x, y, w, h, inactive_colour, active_colour):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, active_colour, (x, y, w, h))
    else:
        pygame.draw.rect(window, inactive_colour, (x, y, w, h))

    text_surf = font.render(text, True, black)
    text_rect = text_surf.get_rect()
    text_rect.center = ((x+(w/2)), (y+(h/2)))
    window.blit(text_surf, text_rect)

    return x+w > mouse[0] > x and y+h > mouse[1] > y

def game_loop():
    player = None
    computer = None
    result = None
    player_score = 0
    computer_score = 0
    round_in_progress = False

    animation_images = [cat_pic, mouse_pic, elephant_pic]
    animation_index = 0
    last_animation_time = time.time()
    
    click_handled = False

    running = True

    while running:
        current_time = time.time()
        mouse_clicked = False

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                mouse_clicked = True
        window.fill(white)

        #draw button and choices
        if not round_in_progress:
            #animate images in center
            if current_time - last_animation_time >=1:
                animation_index = (animation_index+ 1) % 3
                last_animation_time = current_time
            
            animation_rect = animation_images[animation_index].get_rect(center=(width // 2, height //2.5))
            window.blit(animation_images[animation_index], animation_rect)

            cat_hover = draw_button("cat", 50, 450, 200, 100, red, (255,100,100))
            mouse_hover = draw_button("mouse", 300, 450, 200, 100, green, (100,255,100))
            elephant_hover = draw_button("elephant", 550, 450, 200, 100, blue, (100,100,255))

            if mouse_clicked and not click_handled:
                if cat_hover:
                    player = "Cat"
                    round_in_progress = True
                elif mouse_hover:
                    player = "Mouse"
                    round_in_progress = True
                elif elephant_hover:
                    player = "Elephant"
                    round_in_progress = True

                if round_in_progress:
                    computer = random.choice(["Cat","Mouse","Elephant"])
                    click_handled = True

                    if player == computer:
                        result = "Its a tie"
                    elif (player == "Cat" and computer == "Mouse") or \
                        (player == "Mouse" and computer == "Elephant") or \
                        (player == "Elephant" and computer == "Cat"):
                        result = "You Win!"
                        player_score +=1
                    else:
                        result = "Computer wins!"
                        computer_score +=1
        
        #display choices and results
        if round_in_progress:
            # players choice
            player_pic = cat_pic if player == "Cat" else mouse_pic if player == "Mouse" else elephant_pic
            player_rect = player_pic.get_rect(center=(200, height //2))
            window.blit(player_pic, player_rect)

            #computer choice
            computer_pic = cat_pic if computer == "Cat" else mouse_pic if computer == "Mouse" else elephant_pic
            computer_rect = computer_pic.get_rect(center=(width - 200, height //2))
            window.blit(computer_pic, computer_rect)

            draw_text(result, large_font, black, width // 2, 100)
            #next round button
            next_round_hover = draw_button("Next Round", 300,500,200,70, (200,200,200), (150,150,150))

            if next_round_hover and mouse_clicked and not click_handled:
                player = None
                computer = None
                result = None
                round_in_progress = False
                click_handled

        #display score
        draw_text(f"player : {player_score}", font, black,100,50)
        draw_text(f"computer : {computer_score}", font, black,width-120,50)

        pygame.display.update()

        if not mouse_clicked:
            click_handled = False

    pygame.quit()

game_loop()



                
