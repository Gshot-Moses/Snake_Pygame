import pygame
#import pyttsx
from random import randint

#constants
width = 10
height = 10
margin = 3
x_speed = width + margin
y_speed = 0

class Segment(pygame.sprite.Sprite):
	#Snake segment
		def __init__(self, x, y):
				pygame.sprite.Sprite.__init__(self)
				self.image = pygame.surface.Surface([width, height])
				self.image.fill([randint(0, 255), randint(0, 255), randint(0, 255)])
				self.rect = self.image.get_rect()
				#self.rect.center = [320, 240]
				self.rect.x = x
				self.rect.y = y
        
		def kill(self):
				self.rect.x = 0
				self.rect.y = 0
		
		def paste(self):
				window.blit(self.image, self.rect)

        
class Apple(pygame.sprite.Sprite):
    #width = 10
    
		def __init__(self):
				pygame.sprite.Sprite.__init__(self)
				self.image = pygame.surface.Surface([width, height])
				self.rect = self.image.get_rect()
				self.rect.center = [randint(125, 397), randint(43, 397)]

		def locate(self):
				x = randint(125, 397)
				y = randint(43, 397)
				self.image.fill([randint(0, 255),randint(0, 255),randint(0, 255)])
				self.rect.x = x
				self.rect.y = y
		
		def kill(self):
				self.rect.x = 0
				self.rect.y = 0
		
		def paste(self):
				window.blit(self.image, self.rect)
        
def arena():
		rect_obj = pygame.Rect(120, 40, 400, 400)
		pygame.draw.rect(window, [0, 0, 0], rect_obj, 3)
    
#engine = pyttsx.init()
#engine.setProperty('rate', 120)
#engine.say('Welcome to pygame. This is a small introduction and I hope you will enjoy. Have fun.')
#engine.runAndWait()
pygame.init()
pygame.mixer.init()
screen = [640, 480]
window = pygame.display.set_mode(screen, pygame.FULLSCREEN)
pygame.display.set_caption('Snake By Ghost', 'ME')
window.fill([255,255,255])
pygame.mixer.music.load('snake_beat.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 50)
score_font = pygame.font.SysFont('arial', 15)
game_over = font.render('Game Over', True, [0, 0, 0])
snake = pygame.sprite.Group()
rect_obj = pygame.Rect(120, 40, 400, 400)
rect_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
is_over = False
score = 0
pieces = []
direction = 'right'
snake_length = 6
apple = Apple()
#rect_obj = pygame.Rect(170, 90, 300, 300)

for i in range(snake_length):
		x = 250 - (width + margin) * i
		y = 240
		segment = Segment(x, y)
		snake.add(segment)
		pieces.append(segment)
apple_list = pygame.sprite.Group()
apple_list.add(apple)
running = True
while running:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
						running = False
				elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
								running = False
						elif event.key == pygame.K_d:
								if direction == 'up' or direction == 'down':
										x_speed = width + margin 
										y_speed = 0
										direction = 'right'
						elif event.key == pygame.K_a:
								if direction == 'up' or direction == 'down':
										x_speed = (width + margin) * -1
										y_speed = 0
										direction = 'left'
						elif event.key == pygame.K_w:
								if direction == 'left' or direction == 'right':
										x_speed = 0
										y_speed = (height + margin) * -1
										direction = 'up'
						elif event.key == pygame.K_s:
								if direction == 'left' or direction == 'right':
										x_speed = 0
										y_speed = height + margin
										direction = 'down'
		window.fill([255,255,255])
		last = pieces.pop()
		snake.remove(last)
		x = pieces[0].rect.x + x_speed
		y = pieces[0].rect.y + y_speed
		new_piece = Segment(x, y)
		pieces.insert(0, new_piece)
		snake.add(new_piece)
		if pygame.sprite.spritecollide(pieces[0], apple_list, False):
				score += 1
				apple.locate()
				new_x = pieces[len(pieces)-1].rect.x + x_speed
				new_y = pieces[len(pieces)-1].rect.y + y_speed
				new = Segment(x, y)
				pieces.append(new)
				snake.add(new)
				new.image.fill([randint(0, 255),randint(0, 255),randint(0, 255)])
				rect_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
		if pieces[0].rect.x <= 120 or pieces[0].rect.x >= 517:
        #print 'You are dead'
				is_over = True
		if pieces[0].rect.y <= 40 or pieces[0].rect.y >= 440:
        #print 'You are dead'
				is_over = True
    #if pygame.sprite.spritecollide(pieces[0], snake, False):
    #    print 'You are dead'
		window.blit(score_font.render('Score:' + str(score), True, [0, 0, 0]), [10, 10])
		pygame.draw.rect(window, rect_color, rect_obj, 3)
		apple.paste()
		snake.draw(window)
		if is_over:
				for s in snake:
						s.kill()
				window.fill([255,255,255])
				window.blit(game_over, [320 - game_over.get_size()[0]/2, 240 - game_over.get_size()[1]/2])
		pygame.display.update()
		clock.tick(7)
pygame.quit()

  
