"""
Platformer Game
"""
import arcade
import pygame
from pygame import mixer



# Constants

SCREEN_WIDTH = 510
SCREEN_HEIGHT = 510
SCREEN_TITLE = "Maze"

MOVEMENT_SPEED = 50


class Player(arcade.Sprite):

    def update(self):

        print("hello")
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyGame(arcade.Window):
    # avatar_x = 30
    # avatar_y = 30

    def __init__(self, width, height, name):

        super().__init__(width, height, name)

        arcade.set_background_color(arcade.color.WHITE)

        self.player_sprite = None

    def setup(self):

        mixer.init()
        mixer.music.load('celebrate.mp3')

        self.player_sprite = Player(":resources:images/animated_characters/female_person/"
                                    "femalePerson_idle.png", scale=.3)
        self.player_sprite.center_x = 32

        self.player_sprite.center_y = 32

    def on_draw(self):

        self.clear()

        self.player_sprite.draw()

        # Circle

        # arcade.draw_circle_filled(self.avatar_x, self.avatar_y, 10, arcade.color.YELLOW)

        # Grid

        # for x in range(0, 601, 10):
        #     arcade.draw_line(x, 0, x, 600, arcade.color.BLACK, 1)
        #
        # for y in range(0, 601, 10):
        #     arcade.draw_line(0, y, 800, y, arcade.color.BLACK, 1)

        # Outside lines

        for y in range(0, 550):
            arcade.draw_point(y, 505, arcade.color.BLACK, 10)

        for y in range(560):
            arcade.draw_point(y, 555, arcade.color.BLACK, 10)

        for y in range(55, 560):
            arcade.draw_point(5, y, arcade.color.BLACK, 10)

        for y in range(0, 450):
            arcade.draw_point(505, y, arcade.color.BLACK, 10)

        # First row vertical

        for y in range(560):
            arcade.draw_point(y, 5, arcade.color.BLACK, 10)

        for y in range(55, 105):
            arcade.draw_point(55, y, arcade.color.BLACK, 10)

        for y in range(205, 305):
            arcade.draw_point(55, y, arcade.color.BLACK, 10)

        for y in range(355, 455):
            arcade.draw_point(55, y, arcade.color.BLACK, 10)

        # 0 row horizontal

        for y in range(0, 55):
            arcade.draw_point(y, 455, arcade.color.BLACK, 10)

        for y in range(0, 105):
            arcade.draw_point(y, 155, arcade.color.BLACK, 10)

        #         First Row Horizontal

        for y in range(55, 105):
            arcade.draw_point(y, 355, arcade.color.BLACK, 10)

        for y in range(55, 155):
            arcade.draw_point(y, 305, arcade.color.BLACK, 10)

        for y in range(55, 105):
            arcade.draw_point(y, 205, arcade.color.BLACK, 10)

        for y in range(55, 105):
            arcade.draw_point(y, 105, arcade.color.BLACK, 10)

        for y in range(55, 155):
            arcade.draw_point(y, 55, arcade.color.BLACK, 10)

        # Second row vertical

        for y in range(405, 455):
            arcade.draw_point(105, y, arcade.color.BLACK, 10)

        for y in range(305, 355):
            arcade.draw_point(105, y, arcade.color.BLACK, 10)

        #        Second Row Horizontal

        for y in range(105, 155):
            arcade.draw_point(y, 405, arcade.color.BLACK, 10)

        for y in range(105, 205):
            arcade.draw_point(y, 255, arcade.color.BLACK, 10)

            # Third row vertical

        for y in range(355, 405):
            arcade.draw_point(155, y, arcade.color.BLACK, 10)

        for y in range(205, 255):
            arcade.draw_point(155, y, arcade.color.BLACK, 10)

        for y in range(105, 155):
            arcade.draw_point(155, y, arcade.color.BLACK, 10)

        for y in range(455, 505):
            arcade.draw_point(155, y, arcade.color.BLACK, 10)

        for y in range(355, 405):
            arcade.draw_point(155, y, arcade.color.BLACK, 10)

            #        Third Row Horizontal

        for y in range(155, 255):
            arcade.draw_point(y, 355, arcade.color.BLACK, 10)

        for y in range(155, 205):
            arcade.draw_point(y, 455, arcade.color.BLACK, 10)

            # Fourth row vertical

        for y in range(405, 455):
            arcade.draw_point(205, y, arcade.color.BLACK, 10)

        for y in range(205, 305):
            arcade.draw_point(205, y, arcade.color.BLACK, 10)

        for y in range(55, 155):
            arcade.draw_point(205, y, arcade.color.BLACK, 10)

            # Fourth row h

        for y in range(205, 255):
            arcade.draw_point(y, 305, arcade.color.BLACK, 10)

        for y in range(205, 255):
            arcade.draw_point(y, 205, arcade.color.BLACK, 10)

        for y in range(205, 255):
            arcade.draw_point(y, 155, arcade.color.BLACK, 10)

            # Fourth row vertical

        for y in range(455, 505):
            arcade.draw_point(255, y, arcade.color.BLACK, 10)

        for y in range(305, 405):
            arcade.draw_point(255, y, arcade.color.BLACK, 10)

        for y in range(105, 155):
            arcade.draw_point(255, y, arcade.color.BLACK, 10)

            # Fifth row h

        for y in range(255, 405):
            arcade.draw_point(y, 405, arcade.color.BLACK, 10)

        for y in range(255, 305):
            arcade.draw_point(y, 255, arcade.color.BLACK, 10)

        for y in range(255, 305):
            arcade.draw_point(y, 55, arcade.color.BLACK, 10)

            # Fifth row vertical

        for y in range(405, 455):
            arcade.draw_point(305, y, arcade.color.BLACK, 10)

        for y in range(255, 355):
            arcade.draw_point(305, y, arcade.color.BLACK, 10)

        for y in range(105, 155):
            arcade.draw_point(305, y, arcade.color.BLACK, 10)

        for y in range(0, 55):
            arcade.draw_point(305, y, arcade.color.BLACK, 10)

            # 6th row h

        for y in range(305, 455):
            arcade.draw_point(y, 355, arcade.color.BLACK, 10)

        for y in range(305, 355):
            arcade.draw_point(y, 205, arcade.color.BLACK, 10)

        for y in range(305, 405):
            arcade.draw_point(y, 155, arcade.color.BLACK, 10)

            # Fifth row vertical

        for y in range(455, 505):
            arcade.draw_point(355, y, arcade.color.BLACK, 10)

        for y in range(355, 405):
            arcade.draw_point(355, y, arcade.color.BLACK, 10)

        for y in range(205, 305):
            arcade.draw_point(355, y, arcade.color.BLACK, 10)

        for y in range(55, 105):
            arcade.draw_point(355, y, arcade.color.BLACK, 10)

        # 7th row h

        for y in range(355, 455):
            arcade.draw_point(y, 455, arcade.color.BLACK, 10)

        for y in range(355, 405):
            arcade.draw_point(y, 55, arcade.color.BLACK, 10)

        # 7th row vertical

        for y in range(305, 355):
            arcade.draw_point(405, y, arcade.color.BLACK, 10)

        for y in range(155, 255):
            arcade.draw_point(405, y, arcade.color.BLACK, 10)

        for y in range(55, 105):
            arcade.draw_point(405, y, arcade.color.BLACK, 10)

            # 7th row h

        for y in range(405, 455):
            arcade.draw_point(y, 305, arcade.color.BLACK, 10)

        for y in range(405, 505):
            arcade.draw_point(y, 105, arcade.color.BLACK, 10)

            # 7th row vertical

        for y in range(355, 405):
            arcade.draw_point(455, y, arcade.color.BLACK, 10)

        for y in range(155, 255):
            arcade.draw_point(455, y, arcade.color.BLACK, 10)

        for y in range(0, 55):
            arcade.draw_point(455, y, arcade.color.BLACK, 10)

        # 8th row h

        for y in range(455, 505):
            arcade.draw_point(y, 355, arcade.color.BLACK, 10)

        for y in range(455, 505):
            arcade.draw_point(y, 255, arcade.color.BLACK, 10)

    def on_key_press(self, symbol: int, modifiers: int):

        # arcade.play_sound('celebrate.mp3')
        if symbol == arcade.key.UP:
            self.player_sprite.center_y += MOVEMENT_SPEED
        if symbol == arcade.key.DOWN:
            self.player_sprite.center_y -= MOVEMENT_SPEED
        if symbol == arcade.key.RIGHT:
            self.player_sprite.center_x += MOVEMENT_SPEED
        if symbol == arcade.key.LEFT:
            self.player_sprite.center_x -= MOVEMENT_SPEED
            print(self.player_sprite.center_x)
            print(self.player_sprite.center_y)

        if self.player_sprite.center_x == 482 and self.player_sprite.center_y == 482:
            mixer.music.play()

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
