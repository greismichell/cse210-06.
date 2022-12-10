import csv
from constants import *
import random
from game.casting.animation import Animation
from game.casting.drop import Drop
from game.casting.body import Body
from game.casting.fish import Fish
from game.casting.fish2 import Fish2
from game.casting.fish3 import Fish3
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.cat import Cat
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.drop_collide_borders_action import CollideBordersAction
from game.scripting.drop2_collide_borders_action import CollideBordersAction2
from game.scripting.fish_collide_borders_action import FishCollideBordersAction
from game.scripting.collide_fish_action import CollideFishAction
from game.scripting.collide_cat_action import CollideCatAction
from game.scripting.control_cat_action import ControlCatAction
from game.scripting.draw_drop_action import DrawDropAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_cat_action import DrawCatAction
from game.scripting.draw_fish_action import DrawFishAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_drop_action import MoveDropAction
from game.scripting.move_cat_action import MoveCatAction
from game.scripting.move_fish_action import MoveFishAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    DROP_COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    DROP2_COLLIDE_BORDERS_ACTION = CollideBordersAction2(PHYSICS_SERVICE, AUDIO_SERVICE)
    FISH_COLLIDE_BORDERS_ACTION = FishCollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_FISH_ACTION = CollideFishAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_CAT_ACTION = CollideCatAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_CAT_ACTION = ControlCatAction(KEYBOARD_SERVICE)
    DRAW_DROP_ACTION = DrawDropAction(VIDEO_SERVICE)
    DRAW_FISH_ACTION = DrawFishAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_CAT_ACTION= DrawCatAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_DROP_ACTION = MoveDropAction()
    MOVE_CAT_ACTION = MoveCatAction()
    MOVE_FISH_ACTION = MoveFishAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_drop(cast)
        self._add_fish(cast)
        self._add_cat(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_drop(cast)
        self._add_fish(cast)
        self._add_cat(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_drop(cast)
        self._add_cat(cast)
        self._add_fish(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_release(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_CAT_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_drop(cast)
        self._add_fish(cast)
        self._add_cat(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_release(self, cast):
        drop = cast.get_first_actor(DROP_GROUP)
        fish = cast.get_first_actor(FISH_GROUP)
        fish.release()
        drop.release()
    
    def _add_drop(self, cast):
        cast.clear_actors(DROP_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        rx = random.randint(0,SCREEN_WIDTH - DROP_WIDTH)
        ry = random.randint(0,SCREEN_HEIGHT - DROP_HEIGHT)
        position = Point(rx, ry)
        size = Point(DROP_WIDTH, DROP_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(DROP_IMAGE)
        drop = Drop(body, image, True)
        cast.add_actor(DROP_GROUP, drop)
        
        #change velocity constant
        if level == 2:
            DROP_VELOCITY + 1
        if level == 3:
            DROP_VELOCITY + 2



    #def _add_drop2(self, cast):
    #    cast.clear_actors(DROP_GROUP)
    #    stats = cast.get_first_actor(STATS_GROUP)
    #    level = stats.get_level() % BASE_LEVELS
    #    
    #    if level == 3:
    #        rx = random.randint(0,SCREEN_WIDTH - DROP_WIDTH)
    #        ry = random.randint(0,SCREEN_HEIGHT - DROP_HEIGHT)
    #        position = Point(rx, ry)
    #        size = Point(DROP_WIDTH, DROP_HEIGHT)
    #        velocity = Point(0, 0)
    #        body = Body(position, size, velocity)
    #        image = Image(DROP_IMAGE)
    #        drop = Drop(body, image, True)
    #        cast.add_actor(DROP_GROUP, drop)
    #        
    #        #change velocity constant
    #        DROP_VELOCITY + 1

    def _add_fish(self, cast):
        cast.clear_actors(FISH_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level() % BASE_LEVELS
        
        points = FISH_POINTS
        rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
        ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
        position = Point(rx, ry)
        size = Point(FISH_WIDTH, FISH_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(FISH1_IMAGE)
        fish = Fish(body, image, points)
        cast.add_actor(FISH_GROUP, fish)
        COUNT = 0

        if level == 2:
            cast.clear_actors(FISH_GROUP)
            points = FISH_POINTS * 2
            FISH_VELOCITY + 1
            rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
            ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
            position = Point(rx, ry)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FISH2_IMAGE)
            fish = Fish(body, image, points)
            cast.add_actor(FISH_GROUP, fish)

        if level == 3:
            cast.clear_actors(FISH_GROUP)
            points = FISH_POINTS * 3
            FISH_VELOCITY + 2
            rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
            ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
            position = Point(rx, ry)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FISH3_IMAGE)
            fish = Fish(body, image, points)
            cast.add_actor(FISH_GROUP, fish)

        if level == 4:
            cast.clear_actors(FISH_GROUP)
            points = FISH_POINTS * 3
            FISH_VELOCITY + 3
            rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
            ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
            position = Point(rx, ry)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FISH4_IMAGE)
            fish = Fish(body, image, points)
            cast.add_actor(FISH_GROUP, fish)

        if level == 5:
            cast.clear_actors(FISH_GROUP)
            points = FISH_POINTS * 4
            FISH_VELOCITY + 4
            rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
            ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
            position = Point(rx, ry)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FISH5_IMAGE)
            fish = Fish(body, image, points)
            cast.add_actor(FISH_GROUP, fish)
        
        if level == 5:
            cast.clear_actors(FISH_GROUP)
            points = FISH_POINTS * 5
            FISH_VELOCITY + 5
            rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
            ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
            position = Point(rx, ry)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FISH6_IMAGE)
            fish = Fish(body, image, points)
            cast.add_actor(FISH_GROUP, fish)

        if level == 6:
            cast.clear_actors(FISH_GROUP)
            points = FISH_POINTS * 6
            FISH_VELOCITY + 6
            rx = random.randint(0,SCREEN_WIDTH - FISH_WIDTH)
            ry = random.randint(0,SCREEN_HEIGHT - FISH_HEIGHT)
            position = Point(rx, ry)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(0, 0)
            body = Body(position, size, velocity)
            image = Image(FISH7_IMAGE)
            fish = Fish(body, image, points)
            cast.add_actor(FISH_GROUP, fish)

        if level  > 6:
            COUNT += 1
            FISH_VELOCITY + COUNT





    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_cat(self, cast):
        cast.clear_actors(CAT_GROUP)
        x = CENTER_X - CAT_WIDTH / 2
        y = SCREEN_HEIGHT - CAT_HEIGHT
        position = Point(x, y)
        size = Point(CAT_WIDTH, CAT_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        #animation1 = Animation(SITTING_CAT_IMAGES, CAT_RATE)
        animation2 = Animation(CAT_IMAGES, CAT_RATE)
        #cat = Cat(body, animation1)
        cat = Cat(body, animation2)

        cast.add_actor(CAT_GROUP, cat)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_DROP_ACTION)
        script.add_action(OUTPUT, self.DRAW_FISH_ACTION)
        script.add_action(OUTPUT, self.DRAW_CAT_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_DROP_ACTION)
        script.add_action(UPDATE, self.MOVE_CAT_ACTION)
        script.add_action(UPDATE, self.MOVE_FISH_ACTION)
        script.add_action(UPDATE, self.DROP_COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.FISH_COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_FISH_ACTION)
        script.add_action(UPDATE, self.COLLIDE_CAT_ACTION)
        script.add_action(UPDATE, self.MOVE_CAT_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)