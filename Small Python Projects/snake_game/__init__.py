from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from announcer import ModeAnnouncer
from scoreboard import Scoreboard

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
GRID = 20
WALL = 250

AI_STEAL = "steal"
AI_HUNT = "hunt"
AI_SHRINK = "shrink"

def in_bounds(cell):
    x, y = cell
    return -WALL <= x <= WALL and -WALL <= y <= WALL

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def legal_headings(ai_snake, forbidden_cells):
    options = [UP, DOWN, LEFT, RIGHT]
    legal = []

    for h in options:
        if (ai_snake.head.heading() == UP and h == DOWN) or \
           (ai_snake.head.heading() == DOWN and h == UP) or \
           (ai_snake.head.heading() == LEFT and h == RIGHT) or \
           (ai_snake.head.heading() == RIGHT and h == LEFT):
            continue

        nxt = ai_snake.next_cell(h)
        if in_bounds(nxt) and (nxt not in forbidden_cells):
            legal.append(h)

    return legal

def pick_heading_towards(ai_snake, target_cell, forbidden_cells):
    legal = legal_headings(ai_snake, forbidden_cells)
    if len(legal) == 0:
        return ai_snake.head.heading()
    
    best = legal[0]
    best_dist = manhattan(ai_snake.next_cell(best), target_cell)

    for h in legal[1:]:
        d = manhattan(ai_snake.next_cell(h), target_cell)
        if d < best_dist:
            best = h
            best_dist = d

    return best

def hide_snake(snake):
    for seg in snake.segments:
        seg.hideturtle()
    snake.segments.clear()

def run_episode(screen, scoreboard):
    replay_requested = False

    def request_replay():
        nonlocal replay_requested
        replay_requested = True
        announcer.clear()

    # create fresh game objects
    player = Snake(color="white", starting_positions=[(0, 0), (-20, 0), (-40, 0)])
    ai = Snake(color="red", starting_positions=[(200, 200), (180, 200), (160, 200)])
    food = Food()
    announcer = ModeAnnouncer(pos=(0, 220), color="white")

    scoreboard.reset()
    screen.listen()
    screen.onkey(player.up, "Up")
    screen.onkey(player.down, "Down")
    screen.onkey(player.left, "Left")
    screen.onkey(player.right, "Right")

    ai_mode = AI_STEAL
    hunt_ticks_left = 0

    HUNT_TIME_LIMIT_TICKS = 50
    SHRINK_EVERY_TICKS = 10
    shrink_counter = 0

    # main episode loop
    game_is_on = True
    while game_is_on and (not replay_requested):
        screen.update()
        announcer.update()
        time.sleep(0.1)

        forbidden_for_ai = player.positions_set().union(ai.positions_set())
        forbidden_for_ai.discard((int(ai.head.xcor()), int(ai.head.ycor())))

        prev_ai_mode = ai_mode

        if ai_mode == AI_STEAL:
            if ai.length() >= 3 * player.length():
                ai_mode = AI_HUNT
                hunt_ticks_left = HUNT_TIME_LIMIT_TICKS
                shrink_counter = 0

        elif ai_mode == AI_HUNT:
            hunt_ticks_left -= 1
            if hunt_ticks_left <= 0:
                ai_mode = AI_SHRINK
                shrink_counter = 0

        elif ai_mode == AI_SHRINK:
            shrink_counter += 1
            if shrink_counter >= SHRINK_EVERY_TICKS:
                ai.shrink()
                shrink_counter = 0

            if ai.length() <= player.length():
                ai_mode = AI_STEAL

        if prev_ai_mode != ai_mode:
            if prev_ai_mode == AI_STEAL and ai_mode == AI_HUNT:
                announcer.pop("RED SNAKE IS HUNTING YOU! AVOID HIM!", ticks=55)
            if prev_ai_mode == AI_SHRINK and ai_mode == AI_STEAL:
                announcer.pop("Hunt failed...\nHis big back is going to eat your food instead")

        if ai_mode == AI_STEAL:
            target = (int(food.xcor()), int(food.ycor()))
        else:
            target = (int(player.head.xcor()), int(player.head.ycor()))

        ai_heading = pick_heading_towards(ai, target, forbidden_for_ai)
        ai.head.setheading(ai_heading)
        player.move()
        ai.move()

        # player eats food
        if player.head.distance(food) < 15:
            food.refresh()
            player.extend()
            scoreboard.update_score()

        # AI eats food only in STEAL
        if ai_mode == AI_STEAL and ai.head.distance(food) < 15:
            food.refresh()
            ai.extend()

        # lose conditions
        def end_game():
            nonlocal game_is_on
            game_is_on = False
            scoreboard.game_over(request_replay)

        # AI catches player
        if ai_mode in [AI_HUNT, AI_SHRINK] and ai.head.distance(player.head) < 10:
            end_game()

        # wall collision
        if (player.head.xcor() > 290 or player.head.xcor() < -290 or
                player.head.ycor() > 290 or player.head.ycor() < -290):
            end_game()

        # player hits self
        if game_is_on:
            for segment in player.segments[1:]:
                if player.head.distance(segment) < 10:
                    end_game()
                    break

        # player hits AI body
        if game_is_on:
            for segment in ai.segments:
                if player.head.distance(segment) < 10:
                    end_game()
                    break

    # If game ended normally (not already replay requested), wait for replay click
    if not replay_requested:
        while not replay_requested:
            screen.update()
            announcer.update()
            time.sleep(0.05)

    # cleanup episode objects
    hide_snake(player)
    hide_snake(ai)
    food.hideturtle()
    announcer.clear()


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    scoreboard = Scoreboard()

    while True:
        run_episode(screen, scoreboard)


main()