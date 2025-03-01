import pygame
import random
import time
from pygame import mixer

pygame.init()

# Game window
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Menu")


# Sound
Win_sound = pygame.mixer.Sound("Win.mp3")
Lose_sound = pygame.mixer.Sound("Lose.mp3")
Menu_sound = pygame.mixer.Sound("background.mp3")


# List of Colors to use
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
Aqua = ( 0, 255, 255)
blue = ( 0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = ( 0, 128, 0)
Lime = ( 0, 255, 0)
Maroon = (128, 0, 0)
Navy_Blue = ( 0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = ( 0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
orange = (255,100,10)
yellow = (255,255,0)
blue_green = (0,255,170)
marroon = (115,0,0)
lime = (180,255,100)
pink = (255,100,180)
purple = (240,0,255)
gray = (127,127,127)
magenta = (255,0,230)
brown = (100,40,0)
forest_green = (0,50,0)
navy_blue = (0,0,100)
rust = (210,150,75)
dandilion_yellow = (255,200,0)
highlighter = (255,255,100)
sky_blue = (0,255,255)
light_gray = (200,200,200)
dark_gray = (50,50,50)
tan = (230,220,170)
coffee_brown =(200,190,140)
moon_glow = (235,245,255)

# Font
font = pygame.font.SysFont(None, 35, bold=False, italic=False)
large_font = pygame.font.SysFont(None, 55, bold=False, italic=False)
font_I = pygame.font.SysFont(None, 35, bold=False, italic=True)
large_font_I = pygame.font.SysFont(None, 55, bold=False, italic=True)

# Load pictures
cat_pic = pygame.image.load("cat.png")
mouse_pic = pygame.image.load("mouse.png")
elephant_pic = pygame.image.load("elephant.png")
Rock_pic = pygame.image.load("rock.png")
Paper_pic = pygame.image.load("paper.png")
Scissors_pic = pygame.image.load("scissors.png")
Spock_pic = pygame.image.load("spock.png")
Lizard_pic = pygame.image.load("lizard.png")

# Scale pictures
img_size = (300, 300)
cat_pic = pygame.transform.scale(cat_pic, img_size)
mouse_pic = pygame.transform.scale(mouse_pic, img_size)
elephant_pic = pygame.transform.scale(elephant_pic, img_size)
Rock_pic = pygame.transform.scale(Rock_pic, img_size)
Paper_pic = pygame.transform.scale(Paper_pic, img_size)
Scissors_pic = pygame.transform.scale(Scissors_pic, img_size)
Spock_pic = pygame.transform.scale(Spock_pic, img_size)
Lizard_pic = pygame.transform.scale(Lizard_pic, img_size)

# Draw text helper
def draw_text(text, font, colour, x, y):
    img = font.render(text, True, colour)
    text_rect = img.get_rect(center=(x, y))
    window.blit(img, text_rect)

# Draw button helper
def draw_button(text, x, y, w, h, inactive_colour, active_colour):
    mouse = pygame.mouse.get_pos()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, active_colour, (x, y, w, h))
    else:
        pygame.draw.rect(window, inactive_colour, (x, y, w, h))

    text_surf = font.render(text, True, black)
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(text_surf, text_rect)

    return x + w > mouse[0] > x and y + h > mouse[1] > y

# Main menu function
def main_menu():
    running = True
    Menu_sound.play()
    while running:
        window.fill(Olive)
        draw_text("Game Selection", large_font_I, black, width // 2, 100)

        cme_hover = draw_button("Cat, Mouse, Elephant", 150, 200, 500, 70, red, (255, 100, 100))
        rps_hover = draw_button("Rock, Paper, Scissors", 150, 300, 500, 70, green, (100, 255, 100))
        rpsls_hover = draw_button("Rock, Paper, Scissors, Lizard, Spock", 150, 400, 500, 70, blue, (100, 100, 255))

        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        if mouse_clicked:
            if cme_hover:
                CMEround_selection()
            elif rps_hover:
                RPSround_selection()
            elif rpsls_hover:
                RPSLSround_selection()

        pygame.display.update()

    pygame.quit()

# Number of Round selection for Cat, Mouse, Elephant
def CMEround_selection():
    running = True
    while running:
        window.fill(Gray)
        draw_text("Select Round Option", large_font_I, black, width // 2, 100)

        one_round_hover = draw_button("1 Round", 250, 200, 300, 70, red, (255, 100, 100))
        best_of_3_hover = draw_button("Best of 3", 250, 300, 300, 70, green, (100, 255, 100))
        best_of_5_hover = draw_button("Best of 5", 250, 400, 300, 70, blue, (100, 100, 255))

        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        if mouse_clicked:
            Menu_sound.stop() #Stop the menu tune
            if one_round_hover:
                cat_mouse_elephant_game(1)
                running = False
            elif best_of_3_hover:
                cat_mouse_elephant_game(3)
                running = False
            elif best_of_5_hover:
                cat_mouse_elephant_game(5)
                running = False

        pygame.display.update()


# Cat, Mouse, Elephant game round
def cat_mouse_elephant_game(rounds):
    #To win the game you need to get one of these
    #Cat chases Mouse
    #Mouse spooks Elephant
    #Elephant scares Cat
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

    current_round = 1
    running = True

    sound_start_time = time.time()  # This will start the timer as soon as the game starts
    countdown_time = 5  # 5 seconds countdown

    while running:
        current_time = time.time()
        mouse_clicked = False

        # Calculate remaining time
        time_countdown = int(countdown_time - (current_time - sound_start_time)) if sound_start_time else countdown_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        window.fill(Gray)

        # Display countdown at the top center
        draw_text(f"Time Left: {time_countdown}s", font, black, width // 2, 30)

        # Display current round below timer
        draw_text(f"Round {current_round} of {rounds}", font, black, width // 2, 70)

        # Draw button and choices
        if not round_in_progress:
            # Animate images in center
            if current_time - last_animation_time >= 1:
                animation_index = (animation_index + 1) % 3
                last_animation_time = current_time

            animation_rect = animation_images[animation_index].get_rect(center=(width // 2, height // 2.5))
            window.blit(animation_images[animation_index], animation_rect)

            cat_hover = draw_button("cat", 50, 450, 200, 100, red, (255, 100, 100))
            mouse_hover = draw_button("mouse", 300, 450, 200, 100, green, (100, 255, 100))
            elephant_hover = draw_button("elephant", 550, 450, 200, 100, blue, (100, 100, 255))

            if time_countdown == 0 and not round_in_progress:  # If time runs out and option not selected
                round_in_progress = True
                
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
                computer = random.choice(["Cat", "Mouse", "Elephant"])
                click_handled = True

                if player == computer:
                    result = "It's a tie!"
                elif player == "Cat" and computer == "Mouse":
                    result = "You Win! Cat catches Mouse"
                    player_score += 1
                elif player == "Mouse" and computer == "Elephant":
                    result = "You Win! Mouse frightens Elephant"
                    player_score += 1
                elif player == "Elephant" and computer == "Cat":
                    result = "You Win! Elephant scares the Cat"
                    player_score += 1
                else:
                    result = "Computer wins!"
                    computer_score += 1

        # Display choices and results
        if round_in_progress:
            # Player's choice
            player_pic = cat_pic if player == "Cat" else mouse_pic if player == "Mouse" else elephant_pic
            player_rect = player_pic.get_rect(center=(200, height // 2))
            window.blit(player_pic, player_rect)

            # Computer's choice
            computer_pic = cat_pic if computer == "Cat" else mouse_pic if computer == "Mouse" else elephant_pic
            computer_rect = computer_pic.get_rect(center=(width - 200, height // 2))
            window.blit(computer_pic, computer_rect)

            draw_text(result, large_font, black, width // 2, 100)

            # Next round button
            next_round_hover = draw_button("Next Round", 300, 500, 200, 70, (200, 200, 200), (150, 150, 150))

            if next_round_hover and mouse_clicked and not click_handled:
                player = None
                computer = None
                result = None
                round_in_progress = False
                click_handled = False
                current_round += 1

                # Reset the countdown timer when starting the next round
                sound_start_time = time.time()  # Start countdown on clicking Next Round
                countdown_time = 5

        # Display score
        draw_text(f"Player: {player_score}", font, black, 100, 50)
        draw_text(f"Computer: {computer_score}", font, black, width - 120, 50)

        # Check if all rounds are completed
        if current_round > rounds:
            if player_score > computer_score:
                draw_text("Congratulations, You Win!", large_font, green, width // 2, height // 2)
                Win_sound.play()
            elif computer_score > player_score:
                draw_text("You lose the Computer Wins!", large_font, red, width // 2, height // 2)
                Lose_sound.play()
            else:
                draw_text("It is a Tie, no-one Wins!", large_font, blue, width // 2, height // 2)
                Lose_sound.play()

            pygame.display.update()
            time.sleep(3)
            running = False

        pygame.display.update()

        if not mouse_clicked:
            click_handled = False

    main_menu()

# Number of Round selection for Rock, Paper, Scissors
def RPSround_selection():
    running = True
    while running:
        window.fill(Navy_Blue)
        draw_text("Select Round Option", large_font, black, width // 2, 100)

        one_round_hover = draw_button("1 Round", 250, 200, 300, 70, red, (255, 100, 100))
        best_of_3_hover = draw_button("Best of 3", 250, 300, 300, 70, green, (100, 255, 100))
        best_of_5_hover = draw_button("Best of 5", 250, 400, 300, 70, blue, (100, 100, 255))

        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        if mouse_clicked:
            Menu_sound.stop() #Stop the menu tune
            if one_round_hover:
                Rock_paper_Scissors_game(1)
                running = False
            elif best_of_3_hover:
                Rock_paper_Scissors_game(3)
                running = False
            elif best_of_5_hover:
                Rock_paper_Scissors_game(5)
                running = False

        pygame.display.update()

# Rock-Paper-Scissors game round
def Rock_paper_Scissors_game(rounds):
    #To win the game you need to get one of these
    #Scissors cuts Paper
    #Paper covers Rock
    #Rock crushes Scissors
    player = None
    computer = None
    result = None
    player_score = 0
    computer_score = 0
    round_in_progress = False

    animation_images = [Rock_pic, Paper_pic, Scissors_pic ]
    animation_index = 0
    last_animation_time = time.time()

    click_handled = False

    current_round = 1
    running = True

    sound_start_time = time.time()  # This will start the timer as soon as the game starts
    countdown_time = 5  # 5 seconds countdown

    while running:
        current_time = time.time()
        mouse_clicked = False

        # Calculate remaining time
        time_countdown = int(countdown_time - (current_time - sound_start_time)) if sound_start_time else countdown_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        window.fill(Navy_Blue)

        # Display countdown at the top center
        draw_text(f"Time Left: {time_countdown}s", font, black, width // 2, 30)

        # Display current round below timer
        draw_text(f"Round {current_round} of {rounds}", font, black, width // 2, 70)

        # Draw button and choices
        if not round_in_progress:
            # Animate images in center
            if current_time - last_animation_time >= 1:
                animation_index = (animation_index + 1) % 3
                last_animation_time = current_time

            animation_rect = animation_images[animation_index].get_rect(center=(width // 2, height // 2.5))
            window.blit(animation_images[animation_index], animation_rect)

            Rock_hover = draw_button("Rock", 50, 450, 200, 100, red, (255, 100, 100))
            Scissors_hover = draw_button("Scissors", 300, 450, 200, 100, green, (100, 255, 100))
            Paper_hover = draw_button("Paper", 550, 450, 200, 100, blue, (100, 100, 255))

            if time_countdown == 0 and not round_in_progress:  # If time runs out and option not selected
                computer_score += 1
                round_in_progress = True

            if mouse_clicked and not click_handled:
                if Rock_hover:
                    player = "Rock"
                    round_in_progress = True
                elif Scissors_hover:
                    player = "Scissors"
                    round_in_progress = True
                elif Paper_hover:
                    player = "Paper"
                    round_in_progress = True

                if round_in_progress:
                    computer = random.choice(["Rock", "Scissors", "Paper"])
                    click_handled = True

                    if player == computer:
                        result = "It's a tie!"
                    elif player == "Rock" and computer == "Scissors":
                        result = "You Win! Rock Crushes Scissors"
                        player_score += 1
                    elif player == "Scissors" and computer == "Paper":
                        result = "You Win! Scissors Cuts Paper"
                        player_score += 1
                    elif player == "Paper" and computer == "Rock":
                        result = "You Win! Paper Covers Rock"
                        player_score += 1
                    else:
                        result = "Computer wins!"
                        computer_score += 1

        # Display choices and results
        if round_in_progress:
            # Player's choice
            player_pic = Rock_pic if player == "Rock" else Scissors_pic if player == "Scissors" else Paper_pic
            player_rect = player_pic.get_rect(center=(200, height // 2))
            window.blit(player_pic, player_rect)

            # Computer's choice
            computer_pic = Rock_pic if computer == "Rock" else Scissors_pic if computer == "Scissors" else Paper_pic
            computer_rect = computer_pic.get_rect(center=(width - 200, height // 2))
            window.blit(computer_pic, computer_rect)

            draw_text(result, large_font, black, width // 2, 100)

            # Next round button
            next_round_hover = draw_button("Next Round", 300, 500, 200, 70, (200, 200, 200), (150, 150, 150))

            if next_round_hover and mouse_clicked and not click_handled:
                player = None
                computer = None
                result = None
                round_in_progress = False
                click_handled = False
                current_round += 1
            
                # Reset the countdown timer when starting the next round
                sound_start_time = time.time()  # Start countdown on clicking Next Round
                countdown_time = 5

        # Display score
        draw_text(f"Player: {player_score}", font, black, 100, 50)
        draw_text(f"Computer: {computer_score}", font, black, width - 120, 50)

        # Check if all rounds are completed
        if current_round > rounds:
            if player_score > computer_score:
                draw_text("Congratulations, You Win!", large_font, green, width // 2, height // 2)
                Win_sound.play()
            elif computer_score > player_score:
                draw_text("You lose the Computer Wins!", large_font, red, width // 2, height // 2)
                Lose_sound.play()
            else:
                draw_text("It is a Tie, no-one Wins!", large_font, blue, width // 2, height // 2)
                Lose_sound.play()

            pygame.display.update()
            time.sleep(3)
            running = False

        pygame.display.update()

        if not mouse_clicked:
            click_handled = False

    main_menu()

# Number of Round selection for Rock, Paper, Scissors, Lizard, Spock
def RPSLSround_selection():
    running = True
    while running:
        window.fill(forest_green)
        draw_text("Select Round Option", large_font, black, width // 2, 100)

        one_round_hover = draw_button("1 Round", 250, 200, 300, 70, red, (255, 100, 100))
        best_of_3_hover = draw_button("Best of 3", 250, 300, 300, 70, green, (100, 255, 100))
        best_of_5_hover = draw_button("Best of 5", 250, 400, 300, 70, blue, (100, 100, 255))

        mouse_clicked = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        if mouse_clicked:
            Menu_sound.stop() #Stop the menu tune
            if one_round_hover:
                Rock_paper_Scissors_Lizard_Spock_game(1)
                running = False
            elif best_of_3_hover:
                Rock_paper_Scissors_Lizard_Spock_game(3)
                running = False
            elif best_of_5_hover:
                Rock_paper_Scissors_Lizard_Spock_game(5)
                running = False

        pygame.display.update()


# Rock-Paper-Scissors-lizard-spock round
def Rock_paper_Scissors_Lizard_Spock_game(rounds):
    #To win the game you need to get one of these
    #Scissors cuts Paper
    #Paper covers Rock
    #Rock crushes Lizard
    #Lizard poisons Spock
    #Spock smashes Scissors
    #Scissors decapitates Lizard
    #Lizard eats Paper
    #Paper disproves Spock
    #Spock vaporizes Rock
    #Rock crushes Scissors

    player = None
    computer = None
    result = None
    player_score = 0
    computer_score = 0
    round_in_progress = False

    animation_images = [Rock_pic, Paper_pic, Scissors_pic, Lizard_pic, Spock_pic]
    animation_index = 0
    last_animation_time = time.time()

    click_handled = False

    current_round = 1
    running = True

    sound_start_time = time.time()  # This will start the timer as soon as the game starts
    countdown_time = 5  # 5 seconds countdown

    while running:
        current_time = time.time()
        mouse_clicked = False

        # Calculate remaining time
        time_countdown = int(countdown_time - (current_time - sound_start_time)) if sound_start_time else countdown_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_clicked = True

        window.fill(forest_green)

        # Display countdown at the top center
        draw_text(f"Time Left: {time_countdown}s", font, black, width // 2, 30)

        # Display current round below timer
        draw_text(f"Round {current_round} of {rounds}", font, black, width // 2, 70)

        # Draw button and choices
        if not round_in_progress:
            # Animate images in center
            if current_time - last_animation_time >= 1:
                animation_index = (animation_index + 1) % 3
                last_animation_time = current_time

            animation_rect = animation_images[animation_index].get_rect(center=(width // 2, height // 2.5))
            window.blit(animation_images[animation_index], animation_rect)

            Rock_hover = draw_button("Rock", 20, 450, 136, 100, red, (255, 100, 100))
            Paper_hover = draw_button("Paper", 176, 450, 136, 100, blue, (100, 100, 255))
            Scissors_hover = draw_button("Scissors", 332, 450, 136, 100, green, (100, 255, 100))
            Lizard_hover = draw_button("Lizard", 488, 450, 136, 100, blue, (100, 100, 255))
            Spock_hover = draw_button("Spock", 644, 450, 136, 100, blue, (100, 100, 255))
            
            if time_countdown == 0 and not round_in_progress:  # If time runs out and option not selected
                computer_score += 1
                round_in_progress = True

            if mouse_clicked and not click_handled:
                if Rock_hover:
                    player = "Rock"
                    round_in_progress = True
                elif Scissors_hover:
                    player = "Scissors"
                    round_in_progress = True
                elif Paper_hover:
                    player = "Paper"
                    round_in_progress = True
                elif Lizard_hover:
                    player = "Lizard"
                    round_in_progress = True
                elif Spock_hover:
                    player = "Spock"
                    round_in_progress = True

                if round_in_progress:
                    computer = random.choice(["Rock", "Scissors", "Paper"])
                    click_handled = True

                    if player == computer:
                        result = "It's a tie!"
                    elif player == "Rock" and computer == "Scissors":
                        result = "You Win! Rock Crushes Scissors"
                        player_score += 1
                    elif player == "Scissors" and computer == "Paper":
                        result = "You Win! Scissors Cuts Paper"
                        player_score += 1
                    elif player == "Paper" and computer == "Rock":
                        result = "You Win! Paper Covers Rock"
                        player_score += 1
                    elif player == "Rock" and computer == "Lizard":
                        result = "You Win! Rock crushes Lizard"
                        player_score += 1
                    elif player == "Lizard" and computer == "Spock":
                        result = "You Win! Lizard poisons Spock"
                        player_score += 1
                    elif player == "Spock" and computer == "Scissors":
                        result = "You Win! Spock smashes Scissors"
                        player_score += 1
                    elif player == "Scissors" and computer == "Lizard":
                        result = "You Win! Scissors decapitates Lizard"
                        player_score += 1
                    elif player == "Lizard" and computer == "Paper":
                        result = "You Win! Lizard eats Paper"
                        player_score += 1
                    elif player == "Paper" and computer == "Spock":
                        result = "You Win! Paper disproves Spock"
                        player_score += 1
                    elif player == "Spock" and computer == "Rock":
                        result = "You Win! Spock vaporizes Rock"
                        player_score += 1
                    else:
                        result = "Computer wins!"
                        computer_score += 1

        # Display choices and results
        if round_in_progress:
            # Player's choice
            player_pic = Rock_pic if player == "Rock" else Scissors_pic if player == "Scissors" else Paper_pic
            player_rect = player_pic.get_rect(center=(200, height // 2))
            window.blit(player_pic, player_rect)

            # Computer's choice
            computer_pic = Rock_pic if computer == "Rock" else Scissors_pic if computer == "Scissors" else Paper_pic
            computer_rect = computer_pic.get_rect(center=(width - 200, height // 2))
            window.blit(computer_pic, computer_rect)

            draw_text(result, large_font, black, width // 2, 100)

            # Next round button
            next_round_hover = draw_button("Next Round", 300, 500, 200, 70, (200, 200, 200), (150, 150, 150))

            if next_round_hover and mouse_clicked and not click_handled:
                player = None
                computer = None
                result = None
                round_in_progress = False
                click_handled = False
                current_round += 1

                # Reset the countdown timer when starting the next round
                sound_start_time = time.time()  # Start countdown on clicking Next Round
                countdown_time = 5

        # Display score
        draw_text(f"Player: {player_score}", font, black, 100, 50)
        draw_text(f"Computer: {computer_score}", font, black, width - 120, 50)

        # Check if all rounds are completed
        if current_round > rounds:
            if player_score > computer_score:
                draw_text("Congratulations, You Win!", large_font, green, width // 2, height // 2)
                Win_sound.play()
            elif computer_score > player_score:
                draw_text("You lose the Computer Wins!", large_font, red, width // 2, height // 2)
                Lose_sound.play()
            else:
                draw_text("It is a Tie, no-one Wins!", large_font, blue, width // 2, height // 2)
                Lose_sound.play()

            pygame.display.update()
            time.sleep(3)
            running = False

        pygame.display.update()

        if not mouse_clicked:
            click_handled = False

    main_menu()


# Run the main menu on startup
main_menu()

