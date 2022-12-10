> cse210-06.
# Elude Game: 
 - [Porpuse](http://github.com/greismichell/cse210-04/blob/main/README.md#Porpuse)
 - [Game Specificatiom](https://github.com/greismichell/cse210-04/blob/main/README.md#Game-Specification)
 - [Game Design](https://github.com/greismichell/cse210-04/blob/main/README.md#Game-Design)
 - [Project Structure](https://github.com/greismichell/cse210-04/blob/main/README.md#Project-Structure)
 - [Getting Started](https://github.com/greismichell/cse210-04/blob/main/README.md#Getting-Started)
 - [Required Technologies](https://github.com/greismichell/cse210-04/blob/main/README.md#Required-Technologies)
 - [Autors](https://github.com/greismichell/cse210-04/blob/main/README.md#Autors)

## Porpuse
---
- Design software using the principles of programming with classes.
   - Design a program that is easily maintained.

## Game Specification
---
Elude is a game where the player try to avoid any collision with the elements that are falling from the top of the screen and trying to catch the gems that are falling too.

 ### Elude Rules
 
   "Elude" game is played according to the following rules:

   * Several blocks(image) and extra are randomly positioned and falling on the screen.
   * The player start with 3 lives. The player needs to elude all the blocks and catch the gems.
   * The Player can move left and right, to avoid any collision with the blocks.
       * The player moves with the keypath.
   * When the player crush any block lost a live.
   * If the player catch a gem erans points.
   * Each 100 points is a level up.
   *  "Game Over" message is displayed on the middle of the scren, when the player lost his lives.

## Game Design
---
```
* Object: Director:  "A person who directs the game."
    Responsibility:
    - Control the sequence of play.
    Behaviors:
    - Create a new match game using the keyboard and video services, and optain the score.
    State: 
    - on_next(): Overriden ActionCallback method transitions to next scene.
    - Start_game():  Starts the game using the given cast. Runs the main game loop.
    - execute_actions(): Calls execute for each action in the given group.


* Object: Scene Manager: "The person in charge of setting up the cast and script for each scene."
    Responsibility: Prepare scene.
    States: 
    "scene methods"
    - prepare_scene(): prepare the right scene.
    - prepare_new_game(): prepare a new game.
    - prepare_next_level(): Prepare a next level.
    - Prepare_try_again(): next oportunuty.
    - prepare_in_play(): comtinue game.
    - prepare_game_over(): prepare game over.
    "Casting methods"
    - add_gem()
    - add_blocks()
    - add_dialog()
    - add_level()
    - add_lives()
    - add_stats()
    - add_vehicle()
    "Scripting methods"
    - add_inialize_script()
    - add_load_script()
    - add_output_script()
    - add_realese_script()
    - add_unload_script()
    - add_update_script()





* Object: Actor:  "A thing that participates in the game."
    Responsibility:  
    - Constructs a new Actor using the given group and id.
    State: 
   - is_debug(): Whether or not the actor is being debugged.


* Object: Animation:  " An animation "
    Responsability: 
    -  Constructs a new Animation..
    States:
    - get_delay(): Gets the delay between animation cycles. 
    - get_images(): Gets the images that make up the animation.
    - get_ rate(): Gets the rate of animation in frames.
    - next_image(): Gets the next image to display.
   

* Object: Block(Actor): "A solid obstacle, shaped object that is falling from the top of the screen."
    Responsability: 
    -  The responsibility of the block is to move itself.
    States:
    - get_animation(): Gets the block's image.
    - get_body(): Gets the block's body.
    - move_next(): Moves the block's body using its velocity
    - get_points(): Gets the element value
   

* Object: gem(Actor): " A movible thing that participates in the game"
    Responsability: 
     -  The responsibility of the gem is to move itself.
 States:
    - get_animation(): Gets the gem's image.
    - get_body(): Gets the gem's body.
    - move_next(): Moves the gem's body using its velocity
    - get_points(): Gets the element value


* Object: Cast: "A collection of artifacts."
    Responsibility:
    - keep track of a collection of artifacts. It has methods for adding, removing and getting them by a group name.
    States:
    - Add_actor: Adds an actor to the given group.
    - clear_actors(): Clears actors from the given group.
    - clear_all_actors(): Clears all actors.
    - get_actors(): Gets the actors in the given group.
    -  get_all_actors(): Gets all of the actors in the cast.
    - get_first_actor(): Gets the first actor in the given group.
    - remove_actor(): Removes an actor from the given group.


* Object: Color:  "A color"
    Responsibility:
    - Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
    value is the color's opacity.
    State:
    - to_tuple(): Gets the color as a tuple of four values (red, green, blue, alpha).


* Object: Image:  "An image"
    Responsibility:
    - Constructs a new Image.
    States:
    - get_filename(): Gets the name of the image file.
    - get_rotation(): Gets the degrees the image should be rotation.
    - get_scale(): Gets the scaling factor for the image.
    - set_rotation(): Sets the image's rotation to the given value.
    - set_scale(): Sets the image's scale to the given value.
    

* Object: Label(Actor): "A label to be displayed."
    Responsibility:
    - Constructs a new Label.
    States:
    - get_ position(): Gets the label's position.
    - get_text(): Gets the label's text.
   

* Object: Point: "A distance from a relative origin (0, 0)."
    Responsibility:
    - The responsibility is to get the direction and move the player's head
    States:
    - add(): Gets a new point that is the sum of this and the given one.
    - equals(): Whether or not this Point is equal to the given one.
    - get_x(): Gets the horizontal distance.
    - get_y(): Gets the vertical distance.
    - multiply():  Multiplies the point by the provided factor.
    - reverse(): Reverses the point by inverting both x and y values.


*  Object: Vehicle(Actor):  "A solid object that participates in the game and try to elude the blocks and shoot the aliens"
    Responsability: 
    - Constructs a new vihicle.
    States:
    - Executes the debbug actors action by applaying polymorphism.
    - get_animation(): Gets the vehicle's animation.
    - get_body(): Gets the vehicle's body.
    - move_next(): Moves the bat using its velocity.
    - swing_left(): Steers the vehicle to the left.
    - swing_right(): Steers the vehicle to the right.
    - stop_moving(): Stops the vehicle from moving.


* Object: Rectangle: "A 4-sided flat shape with straight sides."
    Responsibility: Constructs a new Rectangle.
    States:
    - get_position(): Gets the top left point of the rectangle.
    - get_size(): Gets the size of the rectangle.


* Object: Sound: "A sound that can be heard."
    Responsibility: Constructs a new Sound.
    States:
    - get_filename(): Gets the filename for the sound.
    - get_volume(): Gets the volume the sound should be played at.
    - is_repeated(): Whether or not the sound should be repeatedly played.


* Object: States: "The game stats."
    Responsability: Constructs a new Stats.
    States:
    - add_life(): Adds one life.
    - add_points(): Adds the given points to the score.
    - get_level(): Gets the level.
    - get_lives(): Gets the lives. 
    - get_score(): Gets the score.
    - lose_life(): Removes one life.
    - next_level(): Adds one level.
    - reset(): Resets the stats back to their default values.


* Object: Text: "A text message."
    Responsibility: Constructs a new Text.
    States: 
    - get_aligment(): Gets the alignment for the text.
    - get_fontfile(): Gets the font file for the text.
    - get_size(): Gets the font size of the text.
    - get_value(): Gets the text's value.
    - set_value(): Sets the text's value.





* Object: Action Callback: "A callback that can be used to trigger scene changes." 
   Responsibility: Changes scenes 
   States: 
   - on_next(): Called when we need to transition from one scene to the next.


* Object: Action: "A thing that is done."
    Responsability: The responsibility of action is to do something that is important in the game. Thus, it has one method, execute(), which should be overridden by derived classes.
    States: 
    - execute(): Executes something that is important in the game. This method should be overriden by derived classes.


* Object: Change Scene Action(Action): "control the change scene"
    States:
    - execute(): using polymorphism from action class.


* Object: Check Over Action(Action): "revise the action"
    States:
    - execute(): using polymorphism from action class.


* Object: Collide Borders Action(): "revise the collide borders"
    States:
    - execute(): using polymorphism from action class.


* Object: Collide Block Action(Action): "revise the collide block action"
    States: 
    - execute(): using polymorphism from action class.


* Object: Collide Vehicle Action(Action): "revise the collide vehicle action"
    States: 
    - execute(): using polymorphism from action class.


* Object: Control Vehicle Action(Action): "move vehicle action"
    States: 
    - execute(): using polymorphism from action class.


* Object: Draw Gem Action(Action): "the gem action"
    States: 
    - execute(): using polymorphism from action class.


* Object: Draw Block Action(Action): "draw block action"
    States: 
    - execute(): using polymorphism from action class.

* Object: Draw Dialog Action(Action): "Do the draw"
    States: 
    - execute(): using polymorphism from action class.


* Object: Draw Hud Action(Action): "Do the draw"
    States: 
    - execute(): using polymorphism from action class.


* Object: Draw Vehicle Action(Action): "Do the draw"
    States: 
    - execute(): using polymorphism from action class.


* Object: End Drawing Action(Action): "Do the draw"
    States: 
    - execute(): using polymorphism from action class.


* Object: Initialize Devices Action(Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Load Assets Action (Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Move Vehicle Action (Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Play Sound Action (Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Realease Devices Action (Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Script: "A collection of actions."
    Responsibily:
    States: 
    - add_action(): Adds an action to the given group.
    - clear_actions(): Clears actions from the given group.
    - clear_all_actions(): Clears all actions.
    - get_actions(): Gets the actions in the given group.
    - remove_action(): Removes an action from the given group.


* Object: Start Drawing Action(Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Timed Change Scene Action(Action):
    States: 
    - execute(): using polymorphism from action class.


* Object: Unload Assets Action (Action):
    States: 
    - execute(): using polymorphism from action class.





* Object: RaylibAudioService(AudioService): "A Raylib implementation of AudioService."
    States: 
    - Execute the methods from AudioService class through polymorphism.
    - get_filepaths(): Gets the file paths.


* Object: RaylibAudioService(AudioService): "A Raylib implementation of KeyboardService"
    States: 
    - Execute the methods from KeyboardService class through polymorphism.
   

* Object: Raylib Mouse Service(MouseService): " A Raylib implementation of MouseService."
    States:
    - Execute the methods from MouseService class through polymorphism.


* Object: Raylib Physics Service(PhysicsService): " A Raylib implementation of PhysicsServic."
    States: 
    - Execute the methods from PhysicsService class through polymorphism.
    - get_rectangle: Gest the dimension and parts of the rectangle.


* Object: Raylib Video Service(VideoService): " A Raylib implementation of VideoService."
    States:
    - Execute the methods from VideoService class through polymorphism.
    - get_filepaths(): Gets file paths.
    - to_raylib_color(): Gets the colors.


* Object: AudioService: "An audio service inteface."
    Responsibility: "The responsibility of AudioService is to handle the audio assets for a game."
    States:
    - initialize(): "Initializes underlying audio device"
    - load_sounds(): "Loads all the sounds in the given directory and sub-directories."
    - play_sound(): "Plays the given sound."
    - release(): "Releases the underlying audio device."
    - unload_sounds(): "Unloads all the sounds that were previously loaded."


* Object: KeyboardService:
    "Detects player input."
   
    Responsibility:
    - Dectect player key presses and translate them into a point representing a direction.

    Behavior:
    - Scalling directional intput to a grip.
   States:
    - Get_ direction: gets the slected direction based on the currently pressed keys.
                  

* Object: Video Service:
    "Outputs the game state"

    Responsibility: 
    - The responsibility of the class of objects is to draw the game state on the screen.

    Behaviors:
    - Debug (bool): wheter or not to draw in debug mode.

    States:

    - Clase_window: Closes the window and releases all computing resources.
    - Clear_buffer: Clears the buffer in preparation for the next rendering. This method   should be called at the beginning of the game's output phase.
    - Draw_artifact: Draws the given artifact's text on the screen.
    - Draw_artifacs: Draws the text for the given list of artifacts on the screen.
    - Flush_buffer: Copies the buffer contents to the screen. This method should be called at the end of  the game's output phase.
    - Get_cell_size: Gets the video screen's cell size.
    - Get_height: Gets the video screen's height.
    - Get_width: Gets the video screen's width.
    - Is_window_open: Whether or not the window was closed by the user.
    - Open_window: Opens a new window with the provided title.
    - Draw_grid: Draws a grid on the screen.


* Object: Mouse Service: "A mouse service inteface."
    State:
    - get_coordinates(): Gets the current mouse coordinates as a Point.
    - has_mouse_moved(): Whether or not the mouse has moved since the last frame.
    - is_button_down(): Detects if the given button is pressed.
    - is_button_pressed(): Detects if the given button was pressed once.
    - is_button_released(): Detects if the given button was released once.
    - is_button_up(): Detects if the given button is released.


* Object: Physics Service: "A physics service inteface."
    States: 
    - has_collided(): Whether or not the given subject has collided with the given agent.
    - is_above(): Whether or not the given subject is above the given agent.
    - is_below(): Whether or not the given subject is below the given agent.
    - is_left_of(): Whether or not the given subject is to the left of the given agent.
    - is_right_of(): Whether or not the given subject is to the right of the given agent.


## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- elude             (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)

```

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 elude
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Autors
---
- Greis Michell Garcia Villanueva - greis.tolosa@gmail.com
