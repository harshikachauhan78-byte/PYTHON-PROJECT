import pygame

pygame.init()

# Screen
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddles
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
left_paddle = pygame.Rect(30, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH-40, HEIGHT//2 - 50, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
ball_dx, ball_dy = 5, 5

# Score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 50)

clock = pygame.time.Clock()
running = True

def reset_ball():
    global ball_dx, ball_dy
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_dx *= -1

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()

    # Left paddle (W/S)
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 6
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += 6

    # Right paddle (UP/DOWN)
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 6
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += 6

    # Ball movement
    ball.x += ball_dx
    ball.y += ball_dy

    # Top/bottom collision
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    # Paddle collision
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx *= -1

    # Scoring
    if ball.left <= 0:
        right_score += 1
        reset_ball()

    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

    # Draw everything
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH//4, 20))
    screen.blit(right_text, (WIDTH*3//4, 20))

    pygame.display.flip()

pygame.quit()