import pygame, random

class Actor(pygame.sprite.Sprite):
    boredom_delta = 0.05
    hunger_delta = 0.25
    tiredness_delta = 0.15

    max_char_velue = 1000

    boredom_threshold = 200
    hunger_threshold = 100
    tiredness_threshold = 300

    progress_bar_width = 300
    progress_bar_height = 30

    action_time = 20

    normal_actor = pygame.image.load("hstend.png")
    sad_actor = pygame.image.load("hsa.png")

    play_actor = pygame.image.load("hp.png")
    feed_actor = pygame.image.load("heat.png")
    sleep_actor = pygame.image.load("hs.png")

    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.normal_actor
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.boredom = random.randint(self.boredom_threshold, self.max_char_velue )
        self.hunger = random.randint(self.hunger_threshold, self.max_char_velue )
        self.tiredness = random.randint(self.tiredness_threshold, self.max_char_velue )
        self.is_sleeping= False
 
        self.boredom_progress_bar = ProgressBar(self.progress_bar_width, self.progress_bar_height,
                                                570, 50, self.max_char_velue, self.boredom)
        self.hunger_progress_bar = ProgressBar(self.progress_bar_width, self.progress_bar_height,
                                                570, 95, self.max_char_velue, self.hunger)
        self.tiredness_progress_bar = ProgressBar(self.progress_bar_width, self.progress_bar_height,
                                                570, 140, self.max_char_velue, self.tiredness)
        self.actions = []

    def update(self, surface):
        self.boredom = max(1, self.boredom - self.boredom_delta)
        self.hunger = max(1, self.hunger - self.hunger_delta)
        if self.is_sleeping == True:
           self.tiredness = self.max_char_velue
        else:
            self.tiredness = max(1, self.tiredness - self.tiredness_delta)

        self.boredom_progress_bar.update(self.boredom)
        self.hunger_progress_bar.update(self.hunger)
        self.tiredness_progress_bar.update(self.tiredness)
                                               
        self.boredom_progress_bar.draw(surface, (125, 181, 205))
        self.hunger_progress_bar.draw(surface, (174, 74, 87))
        self.tiredness_progress_bar.draw(surface, (206, 134, 39))

        if not (self.is_sleeping):
            if len(self.actions) == 0:
                if self.boredom <= self.boredom_threshold or \
                   self.hunger <= self.hunger_threshold or \
                   self.tiredness <= self.tiredness_threshold:
                   self = self.sad_actor
                else:
                    self = self.normal_actor
            else:
                action = self.actions[0]
                if (action [0]  == 0):
                    self.image = self.play_actor                         
                elif (action[0] == 1):
                    self.image = self.feed_actor

                self.actions[0][1] -= 1
                if self.actions[0][1] == 0:
                    self.actions.pop(0)

    def play(self):
        if not(self.is_sleeping):
            self.boredom = self.max_char_velue
            self.boredom_progress_bar.update(self.boredom)
            self.actions.append([0, self.action_time])

    def feed(self):
        if not(self.is_sleeping):
            self. hanger = self.max_char_velue
            self.hunger_progress_bar.update(self.hanger)
            self.actions.append([1, self.action_time])
    
    def sleep(self):
        self.tiredness = self.max_char_velue
        self.tiredness_progress_bar.update(self.tiredness)
        if self.is_sleeping == True:
            self.is_sleeping == False
            self.imege = self.normal_actor
        else:
            self.is_sleeping = True
            self.imege = self.sleep_actor

class ProgressBar():
    def __init__(self, width, height, x_pos, y_pos, max_val, current_percent = 0):
        self.width = width
        self.height = height 
        self.current_percent = current_percent 
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.max_val = max_val

    def update(self, curren_val):
        self.current_percent = curren_val / self.max_val

    def draw(self, surface, color):
        filled = self.current_percent * self.width
        pygame.draw.rect(surface, color, pygame.Rect(self.x_pos, self.y_pos,filled,self.height))
        pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(self.x_pos,self.y_pos, self.width, self.height), 5)

class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ks.jpg")
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Button(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
