
import pygame
import math

running = True  
screen = pygame.display.set_mode((1820, 980))
pygame.display.set_caption("Robot Simulator")
clock = pygame.time.Clock()
robot = pygame.Rect(240, 250, 50, 50)


# Liste des murs
walls = [pygame.Rect(200, 200, 800, 10),
         pygame.Rect(1000, 200, 10, 600),
         pygame.Rect(200, 800, 810, 10),
         pygame.Rect(200, 200, 10, 600)]

pygame.font.init()
text_font = pygame.font.SysFont("Arial", 30)

def draw_text_distance(text, font, text_col, x, y):
    
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def get_distance_to_wall(robot, walls, angle):
    # Définir la position initiale du rayon
    x, y = robot.center

    # Paramètre du pas pour avancer le long du rayon
    step = 5

    # Convertir la rotation du robot en radians
    angle = math.radians(angle)
    # Avancer le long du rayon jusqu'à ce qu'il atteigne un mur
    while True:
        
        x += step * math.cos(angle)
        y += step * math.sin(angle)

        # Vérifier s'il y a une collision avec un mur
        # Pouvoir choisir quel mur detecter (Droite, gauche,)
        for wall in walls:
            if wall.colliderect(pygame.Rect(x - 1, y - 1, 2, 2)):  # Collision détectée
                return math.sqrt((x - robot.centerx)**2 + (y - robot.centery)**2)



def getDistanceRight():
    return get_distance_to_wall(robot, walls, 0)

def getDistanceLeft():
    return get_distance_to_wall(robot, walls, 180)

def getDistanceUp():
    return get_distance_to_wall(robot, walls, 90)

def getDistanceDown():
    return get_distance_to_wall(robot, walls, 270)


def update_screen():
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), robot)
    for wall in walls:
        pygame.draw.rect(screen, (0, 255, 0), wall)  # Couleur des murs

    distanceRight = get_distance_to_wall(robot, walls, 0)
    distanceLeft = get_distance_to_wall(robot, walls, 180)
    distanceUp = get_distance_to_wall(robot, walls, 90)
    distanceDown = get_distance_to_wall(robot, walls, 270)

    draw_text_distance(f"Distance Droite : {distanceRight}", text_font, (255, 255, 255), 10, 10)
    draw_text_distance(f"Distance Gauche : {distanceLeft} ", text_font, (255, 255, 255), 10, 40)
    draw_text_distance(f"Distance Haut : {distanceUp} ", text_font, (255, 255, 255), 10, 70)
    draw_text_distance(f"Distance Bas : {distanceDown}", text_font, (255, 255, 255), 10, 100    )

    pygame.display.update()


def move_robot_keyboard():

    # Récupérer les touches pressées
    pressed_keys = pygame.key.get_pressed()
    # Déplacer le robot
    if pressed_keys[pygame.K_UP]:
        move_robot(0, -5)
    elif pressed_keys[pygame.K_DOWN]:
        move_robot(0, 5)
    elif pressed_keys[pygame.K_LEFT]:
        move_robot(-5, 0)
    elif pressed_keys[pygame.K_RIGHT]:
        move_robot(5, 0)


def move_robot(x, y):
    # Nouvelles coordonnées du robot
    new_x = robot.x + x
    new_y = robot.y + y
    
    # Vérifier les collisions avec les murs
    for wall in walls:
        if wall.colliderect(pygame.Rect(new_x, new_y, robot.width, robot.height)):
            return False  # Collision détectée, ne pas déplacer le robot

    # Déplacer le robot
    robot.x = new_x
    robot.y = new_y
    return True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    move_robot_keyboard()
    clock.tick(60)
    update_screen()

pygame.quit()

