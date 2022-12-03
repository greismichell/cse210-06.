import pathlib
from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Elude"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "mush/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "mush/assets/sounds/boing.wav"
WELCOME_SOUND = "mush/assets/sounds/start.wav"
OVER_SOUND = "mush/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "mush/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# MUSH
MUSH_GROUP = "balls"
MUSH_IMAGES = [f"mush/assets/images/{n:03}.png" for n in range(301,342)]
MUSH_WIDTH = 20
MUSH_HEIGHT = 80
MUSH_RATE = 7
MUSH_VELOCITY = 8

# GRASS
GRASS_GROUP = "rackets"
GRASS_IMAGE = "mush/assets/images/000.png"
GRASS_WIDTH = 200
GRASS_HEIGHT = 28
GRASS_VELOCITY = 7

# FOOD
FOOD_GROUP = "foods"
FOOD_IMAGES = {
    "b": [f"mush/assets/images/{i:03}.png" for i in range(10,14)],
    "g": [f"mush/assets/images/{i:03}.png" for i in range(20,24)],
    "p": [f"mush/assets/images/{i:03}.png" for i in range(30,34)],
    "y": [f"mush/assets/images/{i:03}.png" for i in range(40,44)]
}
FOOD_WIDTH = 78
FOOD_HEIGHT = 50
FOOD_DELAY = 0.5
FOOD_RATE = 4
FOOD_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"

