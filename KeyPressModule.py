import pygame

# initialize a window for pygame. Whenever we have to make a keypress it has to be in a game window

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()  #to check if it's true or false it has to go in a certain format. Creating a suitable format
    myKey = getattr(pygame, 'K_{}'.format(keyName))  # this is the format that's needed
    if keyInput[myKey]:
        ans = True
    pygame.display.update()

    return ans


def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")


if __name__ == '__main__':
    init()
    while True:
        main()
