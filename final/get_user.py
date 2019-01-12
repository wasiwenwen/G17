import pygame
pygame.init()
validChars = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font('Starjhol.ttf', 40)
    self.image = self.font.render("enter your name", False, [99,148,248])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    self.image = self.font.render(self.text, False, [255, 255, 255])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos

screen = pygame.display.set_mode([600, 600])

shiftDown = False
def get_user():
    global running,shiftDown,screen
    textBox = TextBox()
    textBox.rect.center = [300, 240]
    running = True
    while running:

        black   = (0, 0, 0)
        screen.fill(black)
        screen.blit(textBox.image, textBox.rect)
        pygame.display.flip()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYUP:
                if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = False
            if e.type == pygame.KEYDOWN:
                textBox.add_chr(pygame.key.name(e.key))
                if e.key == pygame.K_SPACE:
                    textBox.text += " "
                    textBox.update()
                if e.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = True
                if e.key == pygame.K_BACKSPACE:
                    textBox.text = textBox.text[:-1]
                    textBox.update()
                if e.key == pygame.K_RETURN:
                    if len(textBox.text) > 0:
                        print (textBox.text)
                    running = False
    return (textBox.text)
