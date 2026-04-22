import pygame

# Инициализация цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    # Основной холст, где мы рисуем
    base_layer = pygame.Surface((800, 600))
    base_layer.fill(BLACK)
    
    clock = pygame.time.Clock()
    
    radius = 15
    drawing = False
    mode = 'brush' # Текущий инструмент: brush, rectangle, circle, eraser
    color = BLUE
    
    # Координаты начала рисования фигуры
    start_pos = None

    while True:
        # Текущий слой для отображения (предпросмотр фигуры)
        draw_layer = base_layer.copy()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            # ГОРЯЧИЕ КЛАВИШИ
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                # Выбор цвета
                if event.key == pygame.K_r: color = RED
                if event.key == pygame.K_g: color = GREEN
                if event.key == pygame.K_b: color = BLUE
                # Выбор инструмента
                if event.key == pygame.K_1: mode = 'brush'
                if event.key == pygame.K_2: mode = 'rectangle'
                if event.key == pygame.K_3: mode = 'circle'
                if event.key == pygame.K_4: mode = 'eraser'

            # ЛОГИКА МЫШКИ
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos # Запоминаем точку нажатия
                
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                # Когда отпускаем мышь, рисуем финальную фигуру на основной слой
                if mode in ['rectangle', 'circle']:
                    draw_shape(base_layer, start_pos, event.pos, radius, color, mode)
                start_pos = None

            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if mode == 'brush':
                        # Рисуем линию из кругов сразу на основной слой
                        draw_line(base_layer, event.pos, radius, color)
                    elif mode == 'eraser':
                        # Ластик — это просто черная кисть
                        draw_line(base_layer, event.pos, radius, BLACK)

        # Отрисовка предпросмотра (только для фигур)
        if drawing and mode in ['rectangle', 'circle'] and start_pos:
            current_pos = pygame.mouse.get_pos()
            draw_shape(draw_layer, start_pos, current_pos, radius, color, mode)

        # Вывод на экран
        screen.blit(draw_layer, (0, 0))
        
        # Информационная панель
        draw_ui(screen, mode, color, radius)
        
        pygame.display.flip()
        clock.tick(60)

def draw_line(surf, pos, radius, color):
    """Рисование кистью/ластиком"""
    pygame.draw.circle(surf, color, pos, radius)

def draw_shape(surf, start, end, radius, color, mode):
    """Рисование прямоугольника или круга"""
    x1, y1 = start
    x2, y2 = end
    
    width = abs(x1 - x2)
    height = abs(y1 - y2)
    top_left = (min(x1, x2), min(y1, y2))

    if mode == 'rectangle':
        pygame.draw.rect(surf, color, (top_left[0], top_left[1], width, height), 2)
    elif mode == 'circle':
        center = start
        # Радиус круга равен расстоянию от начала до текущей позиции мыши
        r = int(((x1 - x2)**2 + (y1 - y2)**2)**0.5)
        pygame.draw.circle(surf, color, center, r, 2)

def draw_ui(screen, mode, color, radius):
    """Отрисовка текста с подсказками"""
    font = pygame.font.SysFont("Arial", 18)
    text = f"Mode: {mode} | Color: {color} | Radius: {radius}"
    hint = "Keys: 1:Brush, 2:Rect, 3:Circle, 4:Eraser | R,G,B: Colors"
    
    img = font.render(text, True, WHITE)
    img_hint = font.render(hint, True, WHITE)
    
    screen.blit(img, (10, 10))
    screen.blit(img_hint, (10, 35))

# Функция рисования линии из старого примера (упрощенная)
def drawLineBetween(screen, start, end, width, color):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

if __name__ == "__main__":
    main()