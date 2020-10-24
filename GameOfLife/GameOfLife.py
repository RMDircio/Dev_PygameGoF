
import sys, pygame
import random

# Customizable items
grid_size = width, height = 800, 600
cell_size = 10 # radius
# cell colors
dead_black = 0, 0, 0
alive_coral = 255, 102, 102

# Class for whole game
class GameOfLife:

    # initialize pygame
    def __init__(self):
        pygame.init()
        # set up screen window
        self.screen = pygame.display.set_mode(grid_size)
        self.clear_screen()
        self.init_grids()
        # push drawing to memory with flip
        pygame.display.flip()

    def init_grids(self):
        self.num_of_columns = int(width / cell_size)
        self.num_of_rows = int(height / cell_size)
        print('columns: %d\nRows: %d' % (self.num_of_columns, self.num_of_rows))
        # set up game grid
        self.grids = []

        rows = []
        for num_of_rows in range(self.num_of_rows):
            list_of_columns = [0] * self.num_of_columns
            rows.append(list_of_columns)
        
        self.grids.append(rows)
        self.game_grid_active = 0
        self.game_grid_inactive = []
        self.set_grid()
        print(self.grids[0])

    
    def set_grid(self, value=None):
    # can either zero out the grid or randomize it via value param
    # (1) --> all alive
    # (0) --> all dead
    # ()  --> randomize
    # (None) --> randomize
        for r in range(self.num_of_rows):
            for c in range(self.num_of_columns):
                if value is None:
                    cell_value = random.randint(0,1)
                else:
                    cell_value = value
                # set to value from 0 -1 
                self.grids[self.game_grid_active][r][c] = cell_value


    # clear the screen
    def clear_screen(self):
        # default screen is dead/black
        self.screen.fill(dead_black)

    # update the instances
    def update_generation(self):
        # look at current generation
        # update inactive gride to store next generation
        # change out active grid
        self.set_grid(None)
        

    def draw_grid(self):
        # clear screen first
        self.clear_screen()
        # draw circles on grid
        #(surface, color, center(x,y), radius, width)
        # circle = pygame.draw.circle(self.screen, alive_coral, (50,50), 5, 0) 
        for c in range(self.num_of_columns):
            for r in range(self.num_of_rows):
                # set up colors
                if self.grids[self.game_grid_active][r][c] == 1:
                    color = alive_coral
                else:
                    color = dead_black
                #(surface, color, center(x,y), radius, width)
                pygame.draw.circle(self.screen,
                                            color,
                                            (int(c * cell_size + (cell_size /2)),
                                            int(r * cell_size + (cell_size/2))),
                                            int(cell_size/2),
                                            0) 
        pygame.display.flip()
    
    def handle_events(self):
        for event in pygame.event.get():
            # if 's' key is pressed --> toggle game pause
            # if 'r' key is pressed --> randomize gride
            # if 'q' key is pressed --> quit game
            if event.type == pygame.QUIT: sys.exit()

 
    # game loop
    def run_game(self):
    
    
        while True:
            self.handle_events()
            self.update_generation()
            self.draw_grid()
            # pygame.time.wait(1)

        



if __name__ == "__main__":
    game = GameOfLife()
    game.run_game()