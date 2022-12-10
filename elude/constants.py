import pathlib
import random
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
DEFAULT_DROPS = 5

# FIELD
FIELD_TOP = 0
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "elude/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "elude/assets/sounds/boing.wav"
WELCOME_SOUND = "elude/assets/sounds/start.wav"
OVER_SOUND = "elude/assets/sounds/over.wav"

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
LEVEL_FILE = "elude/assets/data/level-{:03}.txt"
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

# DROP
DROP_GROUP = "drops"
DROP_IMAGE = "elude/assets/images/020.png"
DROP_WIDTH = 70
DROP_HEIGHT = 100
DROP_VELOCITY = 6

# CAT
CAT_GROUP = "cats"
SITTING_CAT_IMAGES = [f"elude/assets/images/{n:03}.png" for n in range(103, 105)]
CAT_IMAGES = [f"elude/assets/images/{n:03}.png" for n in range(100, 103)]
CAT_WIDTH = 100
CAT_HEIGHT = 80
CAT_RATE = 10
CAT_VELOCITY = 7

# FISH
FISH_GROUP = "fishes"
FISH1_IMAGE = "elude/assets/images/000.png"
FISH2_IMAGE = "elude/assets/images/001.png"
FISH3_IMAGE = "elude/assets/images/002.png"
FISH4_IMAGE = "elude/assets/images/003.png"
FISH5_IMAGE = "elude/assets/images/004.png"
FISH6_IMAGE = "elude/assets/images/005.png"
FISH7_IMAGE = "elude/assets/images/006.png"

FISH_WIDTH = 70
FISH_HEIGHT = 50
FISH_VELOCITY = 7
FISH_POINTS = 20



# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING"
WAS_GOOD_GAME = "GAME OVER"