from text_display import *
import sunny

def Hello():
    #clear() #clear the screen

    display_text("Hey you, yes you! Hello there!")
    press_enter()

    #sunny.sunny_display()

def Info():

    display_text("This is Sunny, a post-secondary student who studies full time on campus. \nHer parents are responsible her tuition, but her groceries and rent come out of her pocket.")
    display_text("Sadly, being a student is no small cost and Sunny's financial state is not the best right now.")
    display_text("Your task is to help Sunny make some crucial financial decisions through the next month.")
    display_text("To do this, you will need to know a few things...")

    press_enter()

def Tutorial():

    display_text("---HEALTH---")
    print("This is Sunny's Health. If it drops below 30%, she will get sick and you will have to pay for medicine to increase it.")
    display_text("If it reaches 0%, it will be game over")

    display_text("---FINANCES---")
    print("This is Sunny's Finances a.k.a How much money she has. This is the main focus of the game.")
    display_text("Your goal is to grow it as much as you can by the end of the month")

    display_text("---HAPPINESS---")
    print("This is Sunny's Happiness. While saving money is important, it is also important to take care of our \nmental health and stress levels.")
    print("Certain activities such as going out with friends or choosing to rest instead of going to work will increase happiness.")
    print("However, it may cost some money...")
    display_text("If Sunny's Happiness drops beolow a certain threshold, her Health will begin to decrease.")


Hello()
Info()
Tutorial()
