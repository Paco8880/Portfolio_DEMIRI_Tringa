 #Tetris        DYOA Assignment 2 WS 2024
# Name:         TRINGA_DEMIRI
# Student ID:   11845777


import pygame, sys, time, random
from pygame.locals import *
from framework import BaseGame

# You should only modify this file and only in the TODO sections.
# If you have any questions or find any bugs feel free to let us know 
# on discord in the forum: https://discord.gg/gpNN2U9wtx
# Familiarize yourself with the framework, take a look at the different
# functions and attributes available.
# We provide more information about each function to implement in the README file


class Block:
    def __init__(self, game, block_name):
        self.name = block_name  # Store the block's name (e.g., 'hero', 'orangeRicky').

        # Assign the block's color based on its name using the framework's block_colors dictionary.
        self.color = game.block_colors[self.name]

        # Randomly select one of the possible rotations for this block.
        # Each block has multiple rotations defined in game.block_list.
        self.rotation = random.randrange(len(game.block_list[self.name]))

        # Set the block's shape based on the randomly chosen rotation.
        # This will also calculate the block's width and height.
        self.set_shape(game.block_list[self.name][self.rotation])

        # Position the block horizontally at the center of the board.
        # Subtract half the block's width to ensure proper centering.
        self.x = int(game.board_width / 2) - int(self.width / 2)

        # Set the block's initial vertical position at the top of the board.
        self.y = 0


        

    # Input: shape as array of strings
    # This function sets the height and width of a block. Do not change this.
    def set_shape(self, shape):
        self.shape = shape
        self.width = len(shape[0])
        self.height = len(shape)
        

    # =========================================
    # TODO START
    # Step 2 Rotation
    # Input: rotation_options is a list of possible rotations a block can have. 
    # Each block has different rotation options. I.e. the block 'hero' has 2 options, 
    # whereas 'orangeRicky' has 4 options.
    # rotate block once clockwise. You might want to take another look at the framework for this.
    # Again check how blocks are defined and how you could change the shape such that
    #  the block is rotated once. All the necessary shapes are provided in the framework.
    # Pay attention to potential out of bounds errors!
    # Hint: you will need to use set_shape() to "apply" the rotation


    def right_rotation(self, rotation_options):
        pass
    

    def left_rotation(self, rotation_options):
        pass


class Game(BaseGame):
    def run_game(self):
        self.gameboard = self.get_empty_board()  # Initializing the game board
        current_block = self.get_new_block()
        next_block = self.get_new_block()
        
        # dictionary for score
        self.score_dictionary = {0: 0, 1: 40, 2: 100, 3: 300, 4: 1200}

        while True:
            self.test_quit_game()

            if current_block is None:
                current_block = next_block
                next_block = self.get_new_block()

            if not self.is_block_on_valid_position(current_block):
                return

            for event in pygame.event.get():
                if event.type == KEYUP and event.key == K_p:
                    self.show_text("Paused")
                elif event.type == KEYDOWN:
                    if event.key in [K_LEFT, K_a]:
                        if self.is_block_on_valid_position(current_block, x_change=-1):
                            current_block.x -= 1
                    elif event.key in [K_RIGHT, K_d]:
                        if self.is_block_on_valid_position(current_block, x_change=1):
                            current_block.x += 1
                    elif event.key in [K_DOWN, K_s]:
                        if self.is_block_on_valid_position(current_block, y_change=1):
                            current_block.y += 1
                    elif event.key == K_q:
                        current_block.rotation = (current_block.rotation - 1) % len(self.block_list[current_block.name])
                        current_block.set_shape(self.block_list[current_block.name][current_block.rotation])
                    elif event.key == K_e:
                        current_block.rotation = (current_block.rotation + 1) % len(self.block_list[current_block.name])
                        current_block.set_shape(self.block_list[current_block.name][current_block.rotation])

            if self.is_block_on_valid_position(current_block, y_change=1):
                current_block.y += 1
            else:
                # Block cannot move; add it to the gameboard
                self.add_block_to_board(current_block)

                # Removing completed rows and update score and level
                lines_removed = self.remove_complete_row()
                self.calculate_new_score(lines_removed, self.level)
                self.calculate_new_level(self.score)

                # Getting a new block
                current_block = next_block
                next_block = self.get_new_block()

                # Checking if the new block is in a valid position; if not, end the game
                if not self.is_block_on_valid_position(current_block):
                    self.show_text("Game Over")
                    return

            self.display.fill(self.background)
            self.draw_game_board()  # Draw the updated game board
            self.draw_score()
            self.draw_level()
            self.draw_next_block(next_block)
            if current_block:
                self.draw_block(current_block)
            pygame.display.update()
            self.clock.tick(self.speed)


    def is_coordinate_on_board(self, x, y):
        # Check if x and y are within the boundaries of the board
        return 0 <= x < self.board_width and 0 <= y < self.board_height
    
    def is_block_on_valid_position(self, block, x_change=0, y_change=0):
        for row in range(block.height):
            for col in range(block.width):
                if block.shape[row][col] != self.blank_color:
                    new_x = block.x + col + x_change
                    new_y = block.y + row + y_change

                    # Logging the new position being checked
                    print(f"Checking position ({new_x}, {new_y})")

                    if not self.is_coordinate_on_board(new_x, new_y):
                        print(f"Out of bounds: ({new_x}, {new_y})")
                        return False
                    if self.gameboard[new_y][new_x] != self.blank_color:
                        print(f"Collision detected at ({new_x}, {new_y})")
                        return False
        return True



    def add_block_to_board(self, block):
        for row in range(block.height):
            for col in range(block.width):
                if block.shape[row][col] != self.blank_color:
                    self.gameboard[block.y + row][block.x + col] = block.color 
        print("Block added to board")


    def check_row_complete(self, y_coord):
        for x in range(self.board_width):
            if self.gameboard[y_coord][x] == self.blank_color:
                return False
        return True

    def remove_complete_row(self):
        lines_removed = 0
        y = self.board_height - 1
        while y >= 0:
            if self.check_row_complete(y):
                del self.gameboard[y]
                self.gameboard.insert(0, [self.blank_color] * self.board_width)
                lines_removed += 1
            else:
                y -= 1
        return lines_removed

    def calculate_new_score(self, lines_removed, level):
        if lines_removed > 0:
            base_points = self.score_dictionary[lines_removed]
            self.score += base_points * (level + 1)

    def set_game_speed(self, speed):
        self.speed = speed

    def calculate_new_level(self, score):
        new_level = score // 300
        if new_level > self.level:
            self.set_game_speed(self.speed + (new_level - self.level))
            self.level = new_level

    def get_new_block(self):
        blockname = random.choice(list(self.block_list.keys()))
        return Block(self, blockname)



    # Should you want to add custom functions add them below.
    # Make sure the other functions above work as they are described!


#-------------------------------------------------------------------------------------
# Do not modify the code below, your implementation should be done above
#-------------------------------------------------------------------------------------
def main():
    pygame.init()
    game = Game()

    game.display = pygame.display.set_mode((game.window_width, game.window_height))
    game.clock = pygame.time.Clock()
    pygame.display.set_caption('Tetris')

    game.show_text('Tetris')

    game.run_game()
    game.show_text('Game Over')


if __name__ == '__main__':
    main()

#This initializes the game, sets up the display, 
# starts the game loop, and shows "Game Over" when the game ends