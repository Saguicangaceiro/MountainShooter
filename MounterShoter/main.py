import pygame

pygame.init()
print("Setup start")
window = pygame.display.set_mode(size=(600, 480))
print("Setup ending")

print("Setup Start")
while True:
    # Check for all events (check todos os eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window (fecha a janela)
            quit()  # end pygame (finaliza o pygame)
