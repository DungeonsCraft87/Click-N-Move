def on_player4_button_up_pressed():
    statusbar.value += 0.05
controller.player4.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player4_button_up_pressed)

def on_player4_connected():
    global mySprite4, statusbar4
    mySprite4 = sprites.create(assets.image("""
        myImage1
    """), SpriteKind.player)
    mySprite4 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.FOUR),
        sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player))
    animation.run_image_animation(mySprite4,
        [img("""
                ....ffffff.........ccc..
                        ....ff22ccf.......cc4f..
                        .....ffccccfff...cc44f..
                        ....cc24442222cccc442f..
                        ...c9b4422222222cc422f..
                        ..c999b2222222222222fc..
                        .c2b99111b222222222c22c.
                        c222b111992222ccccccc22f
                        f222222222222c222ccfffff
                        .f2222222222442222f.....
                        ..ff2222222cf442222f....
                        ....ffffffffff442222c...
                        .........f2cfffc2222c...
                        .........fcc2ffffffff...
                        ..........fc2ffff.......
                        ...........fffff........
            """),
            img("""
                ....ffffff.........ccc..
                        ....ff22ccf.......cc4f..
                        .....ffccccfff...cc44f..
                        ....cc24442222cccc442f..
                        ...c9b4422222222cc422f..
                        ..c9999b222222222222fc..
                        .c2b991119222222222c22c.
                        c2222b11992222ccccccc22f
                        f222222222222c222ccfffff
                        .f2222222222444222f.....
                        ..ff2222222cf444222f....
                        ....ffffffffff444222c...
                        .........f2cfffc2222c...
                        .........fcc2ffffffff...
                        ..........fc2ffff.......
                        ...........fffff........
            """),
            img("""
                ...ffffff..........ccc..
                        ...ff22ccff.......c44f..
                        ....fffccccfff...c442f..
                        ....cc24442222ccc4422f..
                        ...c99b222222222cc22fc..
                        ..c999111b222222222222c.
                        .c2bb11199222ccccccc222f
                        c22222222222c222cccfffff
                        f22222222222442222ccc...
                        .f222222222224442222c...
                        ..ff2222222cffc44222c...
                        ....fffffffcffffcccc....
                        .........f2c2ffff.......
                        .........fcc2ffff.......
                        ..........ffffff........
                        ........................
            """),
            img("""
                ...fffffff.........ccc..
                        ...ff22ccff.......cc4f..
                        ....fffccccfff...cc44f..
                        ....cc24442222cccc442f..
                        ...c9b4422222222cc422f..
                        ..c999b2222222222222fc..
                        .c2b99111b222222222c22c.
                        c222b111992222ccccccc22f
                        f222222222222c222ccfffff
                        .f2222222222442222f.....
                        ..ff2222222cf442222f....
                        ....ffffffffff442222c...
                        .........f2cfffc2222c...
                        .........fcc2ffffffff...
                        ..........fc2ffff.......
                        ...........fffff........
            """),
            img("""
                ....ffffff..............
                        ....ff22ccf.........cf..
                        .....ffccccfff.....c4f..
                        ....cc22222222ccccc44f..
                        ...c9b244422222ccc442f..
                        ..c99944222222222242fc..
                        .c2b9992222222222222fcc.
                        c222b1111b22222222cc22cf
                        f2222211992222ccccccc22f
                        .f22222222222c222cffffff
                        ..ff2222222c442222ff....
                        ....fffffffff442222fc...
                        .........f2cff442222c...
                        .........fccfffc2222c...
                        ..........fc2ffffffff...
                        ...........c2fff........
            """),
            img("""
                ....ffffff..............
                        ....ff2cccf.........cf..
                        .....ff2cccfff.....c4f..
                        ....cc22222222ccccc44f..
                        ...c9b244422222ccc442f..
                        ..c99944222222222242fc..
                        .c2b9912222222222222fcc.
                        c222b1111b22222222cc22cf
                        f2222221992222ccccccc22f
                        .f22222222222c222cffffff
                        ..ff2222222c442222ff....
                        ....fffffffff442222fc...
                        .........f2cff442222c...
                        .........fccfffc2222c...
                        ..........fc2ffffffff...
                        ...........c2fff........
            """)],
        200,
        True)
    controller.player4.move_sprite(mySprite4)
    statusbar4 = statusbars.create(100, 4, StatusBarKind.enemy_health)
    statusbar4.attach_to_sprite(mySprite4)
    statusbar4.value = 0
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.FOUR))
controller.player4.on_event(ControllerEvent.CONNECTED, on_player4_connected)

def on_player2_button_b_pressed():
    statusbar2.value += 0.05
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_player1_button_up_pressed():
    statusbar.value += 0.05
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def on_status_reached_comparison_gt_type_percentage(status):
    game.set_game_over_message(True, "P3 Wins")
    game.game_over(True)
statusbars.on_status_reached(StatusBarKind.energy,
    statusbars.StatusComparison.GT,
    statusbars.ComparisonType.PERCENTAGE,
    100,
    on_status_reached_comparison_gt_type_percentage)

def on_player2_button_a_pressed():
    statusbar2.value += 0.05
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_button_down_pressed():
    statusbar.value += 0.05
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def on_player4_button_down_pressed():
    statusbar.value += 0.05
controller.player4.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player4_button_down_pressed)

def on_player3_connected():
    global mySprite3, statusbar3
    mySprite3 = sprites.create(assets.image("""
        myImage1
    """), SpriteKind.player)
    mySprite3 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.THREE))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.THREE),
        sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player))
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . b 5 5 b . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . b b b b b 5 5 5 5 5 5 5 b . . 
                        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                        . . b d 5 5 b 1 f f 5 4 4 c . . 
                        b b d b 5 5 5 d f b 4 4 4 4 b . 
                        b d d c d 5 5 b 5 4 4 4 4 4 4 b 
                        c d d d c c b 5 5 5 5 5 5 5 b . 
                        c b d d d d d 5 5 5 5 5 5 5 b . 
                        . c d d d d d d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . b b b b b 5 5 5 5 5 5 5 b . . 
                        . b d 5 b 5 5 5 5 5 5 5 5 b . . 
                        . . b 5 5 b 5 d 1 f 5 d 4 f . . 
                        . . b d 5 5 b 1 f f 5 4 4 c . . 
                        b b d b 5 5 5 d f b 4 4 4 4 4 b 
                        b d d c d 5 5 b 5 4 4 4 4 4 b . 
                        c d d d c c b 5 5 5 5 5 5 5 b . 
                        c b d d d d d 5 5 5 5 5 5 5 b . 
                        . c d d d d d d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . . . . b c . . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 5 d f . . 
                        . . . . b 5 5 1 f f 5 d 4 c . . 
                        . . . . b 5 5 d f b d d 4 4 . . 
                        b d d d b b d 5 5 5 4 4 4 4 4 b 
                        b b d 5 5 5 b 5 5 4 4 4 4 4 b . 
                        b d c 5 5 5 5 d 5 5 5 5 5 b . . 
                        c d d c d 5 5 b 5 5 5 5 5 5 b . 
                        c b d d c c b 5 5 5 5 5 5 5 b . 
                        . c d d d d d d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 d 4 c . . 
                        . . . . b 5 5 1 f f d d 4 4 4 b 
                        . . . . b 5 5 d f b 4 4 4 4 b . 
                        . . . b d 5 5 5 5 4 4 4 4 b . . 
                        . . b d d 5 5 5 5 5 5 5 5 b . . 
                        . b d d d d 5 5 5 5 5 5 5 5 b . 
                        b d d d b b b 5 5 5 5 5 5 5 b . 
                        c d d b 5 5 d c 5 5 5 5 5 5 b . 
                        c b b d 5 d c d 5 5 5 5 5 5 b . 
                        . b 5 5 b c d d 5 5 5 5 5 d b . 
                        b b c c c d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 d 4 c . . 
                        . . . . b 5 5 1 f f d d 4 4 4 b 
                        . . . . b 5 5 d f b 4 4 4 4 b . 
                        . . . b d 5 5 5 5 4 4 4 4 b . . 
                        . b b d d d 5 5 5 5 5 5 5 b . . 
                        b d d d b b b 5 5 5 5 5 5 5 b . 
                        c d d b 5 5 d c 5 5 5 5 5 5 b . 
                        c b b d 5 d c d 5 5 5 5 5 5 b . 
                        c b 5 5 b c d d 5 5 5 5 5 5 b . 
                        b b c c c d d d 5 5 5 5 5 d b . 
                        . . . . c c d d d 5 5 5 b b . . 
                        . . . . . . c c c c c b b . . .
            """),
            img("""
                . . . . . . . . . . b 5 b . . . 
                        . . . . . . . . . b 5 b . . . . 
                        . . . . . . b b b b b b . . . . 
                        . . . . . b b 5 5 5 5 5 b . . . 
                        . . . . b b 5 d 1 f 5 5 d f . . 
                        . . . . b 5 5 1 f f 5 d 4 c . . 
                        . . . . b 5 5 d f b d d 4 4 . . 
                        . b b b d 5 5 5 5 5 4 4 4 4 4 b 
                        b d d d b b d 5 5 4 4 4 4 4 b . 
                        b b d 5 5 5 b 5 5 5 5 5 5 b . . 
                        c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
                        c b d c d 5 5 b 5 5 5 5 5 5 b . 
                        . c d d c c b d 5 5 5 5 5 d b . 
                        . . c b d d d d d 5 5 5 b b . . 
                        . . . c c c c c c c c b b . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        200,
        True)
    controller.player3.move_sprite(mySprite3)
    statusbar3 = statusbars.create(100, 4, StatusBarKind.energy)
    statusbar3.attach_to_sprite(mySprite3)
    statusbar3.value = 0
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.THREE))
controller.player3.on_event(ControllerEvent.CONNECTED, on_player3_connected)

def on_player3_button_right_pressed():
    statusbar.value += 0.05
controller.player3.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_right_pressed)

def on_player2_button_up_pressed():
    statusbar.value += 0.05
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_player2_button_right_pressed():
    statusbar.value += 0.05
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_player2_button_left_pressed():
    statusbar.value += 0.05
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player3_button_down_pressed():
    statusbar.value += 0.05
controller.player3.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player3_button_down_pressed)

def on_player1_button_right_pressed():
    statusbar.value += 0.05
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player1_button_a_pressed():
    statusbar.value += 0.05
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player4_button_left_pressed():
    statusbar.value += 0.05
controller.player4.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_left_pressed)

def on_player2_connected():
    global mySprite2, statusbar2
    mySprite2 = sprites.create(assets.image("""
        myImage1
    """), SpriteKind.player)
    mySprite2 = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.TWO))
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.TWO),
        sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player))
    animation.run_image_animation(mySprite2, assets.animation("""
        myAnim0
    """), 200, True)
    controller.player2.move_sprite(mySprite2)
    statusbar2 = statusbars.create(100, 4, StatusBarKind.magic)
    statusbar2.attach_to_sprite(mySprite2)
    statusbar2.value = 0
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.TWO))
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def on_player1_button_b_pressed():
    statusbar.value += 0.05
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_status_reached_comparison_gt_type_percentage2(status2):
    game.set_game_over_message(True, "P4 wins")
    game.game_over(True)
statusbars.on_status_reached(StatusBarKind.enemy_health,
    statusbars.StatusComparison.GT,
    statusbars.ComparisonType.PERCENTAGE,
    100,
    on_status_reached_comparison_gt_type_percentage2)

def on_player1_connected():
    global mySprite, statusbar
    mySprite = mp.get_player_sprite(mp.player_selector(mp.PlayerNumber.ONE))
    mySprite = sprites.create(img("""
            . . f f f . . . . . . . . f f f 
                    . f f c c . . . . . . f c b b c 
                    f f c c . . . . . . f c b b c . 
                    f c f c . . . . . . f b c c c . 
                    f f f c c . c c . f c b b c c . 
                    f f c 3 c c 3 c c f b c b b c . 
                    f f b 3 b c 3 b c f b c c b c . 
                    . c 1 b b b 1 b c b b c c c . . 
                    . c 1 b b b 1 b b c c c c . . . 
                    c b b b b b b b b b c c . . . . 
                    c b 1 f f 1 c b b b b f . . . . 
                    f f 1 f f 1 f b b b b f c . . . 
                    f f 2 2 2 2 f b b b b f c c . . 
                    . f 2 2 2 2 b b b b c f . . . . 
                    . . f b b b b b b c f . . . . . 
                    . . . f f f f f f f . . . . . .
        """),
        SpriteKind.player)
    mp.set_player_sprite(mp.player_selector(mp.PlayerNumber.ONE),
        sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            SpriteKind.player))
    animation.run_image_animation(mySprite,
        [img("""
                f f f . . . . . . . . f f f . . 
                        c b b c f . . . . . . c c f f . 
                        . c b b c f . . . . . . c c f f 
                        . c c c b f . . . . . . c f c f 
                        . c c b b c f . c c . c c f f f 
                        . c b b c b f c c 3 c c 3 c f f 
                        . c b c c b f c b 3 c b 3 b f f 
                        . . c c c b b c b 1 b b b 1 c . 
                        . . . c c c c b b 1 b b b 1 c . 
                        . . . . c c b b b b b b b b b c 
                        . . . . f b b b b c 1 f f 1 b c 
                        . . . c f b b b b f 1 f f 1 f f 
                        . . c c f b b b b f 2 2 2 2 f f 
                        . . . . f c b b b b 2 2 2 2 f . 
                        . . . . . f c b b b b b b f . . 
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . . . . . f f f . . 
                        f f f . . . . . . . . c c f f f 
                        c b b c f . . . c c . c c c f f 
                        . c b b b f f c c 3 c c 3 c f f 
                        . c c c b b f c b 3 c b 3 c f f 
                        . c c b c b f c b b b b b b c f 
                        . c b b c b b c b 1 b b b 1 c c 
                        . c b c c c b b b b b b b b b c 
                        . . c c c c c b b c 1 f f 1 b c 
                        . . . c f b b b b f 1 f f 1 f c 
                        . . . c f b b b b f f f f f f f 
                        . . c c f b b b b f 2 2 2 2 f f 
                        . . . . f c b b b 2 2 2 2 2 f . 
                        . . . . . f c b b b 2 2 2 f . . 
                        . . . . . . f f f f f f f . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . c c . c c . . . 
                        . . . . . . c c c 3 c c 3 f . . 
                        . . . . . c c c b 3 c b 3 c f . 
                        . . . . f f b b b b b b b b c f 
                        . . . . f f b b b 1 b b b 1 c c 
                        . . . f f f c b b b b b b b b c 
                        . . . f f f f b b c 1 f f 1 b c 
                        . . . b b b c c b f 1 f f 1 f f 
                        . . . c c c c f b f f f f f f f 
                        . . c c c b b f b f 2 2 2 2 f f 
                        . . . c b b c c b 2 2 2 2 2 f . 
                        . . c b b c c f f b 2 2 2 f . . 
                        . c c c c c f f f f f f f . . . 
                        c c c c . . . . . . . . . . . .
            """),
            img("""
                . f f f . . . . . . . . f f f . 
                        . c b b c f . . . . . . . c f f 
                        . . c b b c f . . . . . . c c f 
                        . . c c c b f . . . . . . . f c 
                        . . c c b b f f . . . . . f f c 
                        . . c b b c b f c c . c c f f f 
                        . . c b c c b f c c c c c f f f 
                        . . . c c c b c b 3 c c 3 c f . 
                        . . . c c c c b b 3 c b 3 b c . 
                        . . . . c c b b b b b b b b c c 
                        . . . c f b b b 1 1 b b b 1 1 c 
                        . . c c f b b b b b b b b b b f 
                        . . . . f b b b b c b b b c b f 
                        . . . . f c b b b 1 f f f 1 f . 
                        . . . . . f c b b b b b b f . . 
                        . . . . . . f f f f f f f . . .
            """)],
        200,
        True)
    controller.player1.move_sprite(mySprite)
    statusbar = statusbars.create(100, 4, StatusBarKind.health)
    statusbar.value = 0
    statusbar.attach_to_sprite(mySprite)
    mp.move_with_buttons(mp.player_selector(mp.PlayerNumber.ONE))
controller.player1.on_event(ControllerEvent.CONNECTED, on_player1_connected)

def on_player4_button_right_pressed():
    statusbar.value += 0.05
controller.player4.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player4_button_right_pressed)

def on_player3_button_left_pressed():
    statusbar.value += 0.05
controller.player3.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player3_button_left_pressed)

def on_status_reached_comparison_gt_type_percentage3(status3):
    game.set_game_over_message(True, "P2 Wins")
    game.game_over(True)
statusbars.on_status_reached(StatusBarKind.magic,
    statusbars.StatusComparison.GT,
    statusbars.ComparisonType.PERCENTAGE,
    100,
    on_status_reached_comparison_gt_type_percentage3)

def on_player3_button_up_pressed():
    statusbar.value += 0.05
controller.player3.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player3_button_up_pressed)

def on_status_reached_comparison_gt_type_percentage4(status4):
    game.set_game_over_message(True, "P1 Wins")
    game.game_over(True)
statusbars.on_status_reached(StatusBarKind.health,
    statusbars.StatusComparison.GT,
    statusbars.ComparisonType.PERCENTAGE,
    100,
    on_status_reached_comparison_gt_type_percentage4)

def on_player1_button_left_pressed():
    statusbar.value += 0.05
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

def on_player1_button_down_pressed():
    statusbar.value += 0.05
controller.player1.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player1_button_down_pressed)

mySprite: Sprite = None
mySprite2: Sprite = None
statusbar3: StatusBarSprite = None
mySprite3: Sprite = None
statusbar2: StatusBarSprite = None
statusbar4: StatusBarSprite = None
mySprite4: Sprite = None
statusbar: StatusBarSprite = None
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1f11fffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111ffff1fff1fffffffe55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffff11111fffffffff455fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff1111111fffffffffffffffff1fffffff1ffff1ffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff1ffffffff1ffffffffffffff1fffffff1ffff1ffffffff5ee5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff1ffffffff1ffffffff1fffff1fffffff1ffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff1ffffffff1ffffffff1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff1ffffffff1ffffffff1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff1ffffffff1ffffffff1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff111111fff1ffffffff1fffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff1f1111fff1fffff1111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffff1111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff11ffffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffff111111111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffffffffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111111fffffff1ffffff1ffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1111f1111ffff1fffff1fffffff1ffffff1ffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffff1fffff1fffffff1ffffff1ffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffff1fffff1fffffff1ffffff1ffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffff1fffff1fffffff1ffffff1ffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffff1fffff1fffffff1ffffff1ffff11111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffff1fffff1fffffff1ffffff1ffff1ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffff1111111fffffff11111111ffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1ff1ffff1ffffffffffffffffffffffffffffff111111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff1fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5cfffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5557cccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5555cccccfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffff5fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5557cccccffffcfffffffffffffffffffffffffffffffffffffffffffffff5ffffffffffffffffffff
        fffffffff55feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff557cccccccffcccffffffffffffffffffffffffffffffffffffffffffffff45ffffffffffffffffffff
        fffffff555555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff55ccccccccfffffffffffffffffffffffffffffffffffffffffffffffff5555554fffffffffffffffff
        fffffff55555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff5ccccccccffffccfffffffffffffffffffffffffffffffffffffffffff555554ffffffffffffffffff
        fffffffff5555ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccfffccfffffffffffffffffffffffffffffffffffffffffffff555fffffffffffffffffff
        fffffffff55555fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcccccccccccfffffffffffffffffffffffffffffffffffffffffffffffff55555efffffffffffffffff
        ffffffff55ff5efffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffccccccccccccccfffffffffffffffffffffffffffffffffffffffffffffff555ff55fffffffffffffffff
        ffffffff5ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe444eccccccceccecccffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffeee444444eeee4cceceeceeec4efeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe5554444eeee444ee44eee4eee44444eefffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff444ee4eeeeee4444ee4444ee44eee44444eeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffe444444eeeeee44444eee4444eee444ee44444ee4ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff44444444eeeeeee4444ee444444ee444eeee44eee4444fffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffff444444444eee444eee44ee4444444ee4444eeeeeee4444444fffffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffff444444444eee444444eeeee4444eeeeeeeee4eeee44444444444fffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffff444444444eee44444444eeeeeeeeeee4eeeeeeeeee444444444444ffffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffff444444444ee44444444444eeeeeee44444ee44444eee444444444444fffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffff444444444ee44444444444ee44444444444ee444444ee4444444444444ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff444444444ee444444444444ee444444444444ee444444ee444444444444ffffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffff44444444ee444444444444ee4444444444444ee4444444ee444444444444fffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffff44444444ee4444444444444ee4444444444444ee4444444ee444444444444effffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffe4444444eee444444444444eee44444444444444ee4444444ee444444444444ffffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffff44444444ee44444444444411d44444444444444d1d4444444ee444444444444efffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff44444444ee444444444444111dd444444444444d11ddb444444ee444444444444fffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffff44444444ee44444444444d115ddd444444444441155ddb44444ee4444444444444ffffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff44444444ee44444444444411555dd4444444444115555dd444444ee444444444444efffffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff44444444ee444444444441155555dd4444444431555555dd44444ee4444444444444effffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff4444444ee4444444444445555555dd4444444445554e45dd444444ee444444444444effffffffffffffffffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffff4444444ee44444444444555ee455dd4444444455554ee55dd44444ee444444444444effffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff4444444ee444444444444454ee44ddd44444444545544eeddb44444ee444444444444effffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff4444444ee44444444444444ee44444444444444444444ee444444444ee44444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff4444444ee44444444444444ee44444444444444444444ee444444444ee44444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff444444ee444444444444444ee44444444444444444444ee4444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff444444ee44444444444444ee444444444411d444444444e4444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff444444ee44444444444444ee444444444111dd44444444ee444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee444444444444444ee444444444115dd44444444ee444444444ee4444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee444444444444444e44444444411555dd4444444ee4444444444ee444444444eefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee44444444444444ee4444444441d555dd4444444ee4444444444ee44444444eeefffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffff44444ee44444444444444ee444444445dddddddd444444eed444444444ee44444444eeecccccccccccccc88888888888888888888888888888
        888888888888888888888888888888888888888888888844444e444444444444444e51d4444445dddddddd444444edd4444444444e4444444eeee8888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888c444ee444444444444444e511144444444444444444444ddd4444444444e4444444eeec8888888888888888888888888888888888888888888
        888888866b9999999999999999999999999999999988888444ee44444444444444ee55111d444444444444444454dd44444444444ee444444eee88888888888888888888888888888888888888888888
        99999999999999999999999999999999999999999968888444ee44444444444444ee4555111d444444444444455ddb44444444444ee44444eeee88888888888888888888888888888888888888888888
        99996666688888888888888888888888888888888888888844ee44444444444444ee4455551144444444444445ddde44444444444ee44444eeec88888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888844ee44444444444444ee4445555544455551114445ddee44444444444ee4444eeee888888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888884ee44444444444444ee444555555555555555555dddee44444444444ee4444eeec888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888844ee4444444444444e4444455555555555555555dd4ee44444444444ee444eee88888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888884ee4444444444444e444444555555511115555dd44ee44444444444ee44eeeffff88888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888ee4444444444444ee44444455dddd511dddddd444ee4444444444ee4eeeeffffffffc8888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888ce4444444444444ee44444445dd444ddddbdd4444ee4444444444eeeeeeffffffffff8888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888ee444444444444ee44444444bd44455444db4444ee4444444444eeeecfffffffffffff88888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888e444444444444ee444444444444444444444444ee444444444eeeefffffffffffffffc8888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888888884444444444ee444444444444444444444444ee4444444eeeeeffffffffffffffffff888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888884444444444ee44444444444444444444444ee44444eeeeefffffffffffffffffff8888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888e4444444ee4444444444444444444444ee444eeeeeefffffffffffffffffffff8888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888e4444ee4444444444444444444444eeeeeeeefffffffffffffffffffffff88888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888feeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffffffffffffffffffffffc888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888fffffffffeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffff8888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888ffffffffffffffffffffffffffffffffffffffffffffffffffff8888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888888cffffffffffffffffffffffffffffffffffffffffffc888888888888888888888888888888888888888888888888
        888888888888888888888888888888888888888888888888888888888888888888888888cffcffffffffffffffffffffcc88888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
        88888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888886866666666666b9999888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888886999999999999999999999999999999999999999999888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888889999999999999999999999966666666666666688888888
        8888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888
"""))
music.play(music.create_song(hex("""
        0078000408040105001c000f0a006400f4010a00000400000000000000000000000000000000028a0000000400012708000c00012010001400012918001c0001271c002000012920002400012a24002800012928002c00012a2c003000012930003400012738003c0001273c004000012940004400012a44004800012948004c00012a4c005000012950005400012758005c00012560006400012768006c00012970007400012478007c0001257c0080000122
    """)),
    music.PlaybackMode.UNTIL_DONE)
scene.set_background_image(img("""
    fffffffcbccffffffffffcfbddddddddddd111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbffcddffffffcfcfffff
        fffffffccffffcffffffbfddddddddd11111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfccdbffffffffffffff
        fffffffcffffffbffffffddddddddd1111111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcffcbfffffffffffcdcf
        ffffffcffffffffbdffffddddddd11111111111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccffffffdfbfffffff
        fcfffffffcdcdffdffdccdddddd11111111111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbbffffffdffffffff
        fffffffffdbddcfffffcddddd1111111111111111111111111111111111111111111dddd1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfcfffffcfffbfff
        fcffffbffbffffffffbbddddd111111111111111111111111111111111111111111d11dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbdcfffffffffbffff
        fcbffffffcfffffffcdddd1111111111111111111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccffffffffffffff
        fdcccffffdbffcffccdddd111111111111111111cc1111111111111111111111111d111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfffffffffffffff
        fffffffffffffffcdddd1111111111111111111cccc111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddfcfffffffffffff
        ffffffffffffffcbddd11111111111111111111cccc11111111111111111111111111111dddd1ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcffffffffffffff
        fffffffddcfffdddddd11111111111111111111ccccc11111111111111111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffffffffffff
        fffffffdddbffbddd111111111111111111111cccccc111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfffcffffffffff
        ffffffcbfcccddddd111111111111111111111ccccccc11111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccfffffffffffff
        fffffffffcfddddd1111111111111111111111ccccccc11111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcffffffffffff
        ffffffffdfcdddd1111111d11111d111111111cccccccc11111111111111111111111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfbfffcfffffff
        ffffffffcfbddd11111111111111111111111ccccccccc1111111111111111111111111111111111d1dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfffdffffffff
        fffffffcdcdddd11111111111111111111111cccccccccc1111111ccc111111111ccc111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddffffffffffff
        fffffbfffcddd11111111111111111111111ccccccccccc1111111cccc111c1111ccc11111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffffffff
        fccffdcbfbddd11111111111111111111111cccccccccccc111111cccc11ccc111ccc1111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffffffff
        fffcffcdfbdd11111111111111111111111ccccccccccccccc1111cc1c11ccc11cccc111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffffffff
        ffddfffbbbdd1111111111111111111111cccccccccccccccc1111cc1c11ccc11c11c111111111111111dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddcfccfffffffff
        cfdffffbcdd11111111111111111111111cccccccccccccccc1111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbfcdfffffffff
        ffffffccdd111111111111111111111111cccccccccccccccc1111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddccfbfffffffff
        ffcfffbdb111111111111111111111111111cccccccccccc111111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbbdddddddddddddddcfdbffffffff
        fffffcddddd1111111111111111111111111cc1cc1ccd1cc111111ccccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddbfcfffffffff
        fffffbdddd11111111111111111111111111cc1cc1ccc1cc1111111ccccccccccccc1111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbbddddddddddddddddcfcfffffffff
        ffffcbddddd1111111111111111111111111cccccccccccc11111111ccccccccccc11111111111111111d1ddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddbcfffffffffff
        fffccddddd11111111111111111111111111cccccccccccc111111111cccccccccc11111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbdddddddddddddddbbffffffffffff
        ffdcbddddd11111111111111111111111111cccccccccccc111111111ccccccccc111111111111111111ddddddddddddddddddddddddddddddddddddddddddddddbddddddddddddddddbffffffffffcf
        ffccddddddd11111111111111111111111111cccccccccc1111111111ccccccccc1111111111111111111dddddddddddddddddddddddddddddddddddddddddddddbddddddbbdddddddbcffffffffffff
        ffcbdddddd1111111111111111111111111111cccccccc11b11111111ccccccccc111111111111bb1111ddddddddddddddddddddddddddddddddddddddddddbbddbbdddddbbdddddddbccfffffffffff
        ffcbddddd111111111111111111111111111111cccccccbccccccc111ccccccccc1111111111111b1111dddddddddddddddddddddddddddddddddddddddddddbbddbddddddbddddddddfffffffffffff
        fcbbdddddd1111111111cccb1ccc1111cccc111ccccccccccccccccc1ccccccccc1111111111111b1111dddddddddddddddddddddddddddddddddddddddddddbbbdbbdddddbdbddddbbbcfffffffffff
        fcddddddd1111111111ccccb1cccc11ccccc111cccccccccbbccbbbccccccccccc1111111111111b111ddddddddddddddddddddddddddbdddddddddddddddddddbddbbddddbbbddbbbcfffffffffffff
        ccddddddd1111111111cccccbcccc11ccccc111cccccccccbbcccbbccccccccccc111111111111111111dddddddddddddddddddddddddbbdddddddddddddddddddbddbddddbbddbbbbffffffffffffff
        ddddddddd1111111111ccc1ccccccccc1ccc111ccccccccccccccccccccccccccc1111111111111b111bdddddddddddddddddddddddddbbdddddddddddddddddddbbbbddddbddbbbbccfffffffffffff
        dddddddd11111111111cc11ccc11cccc1ccc111ccccccccc1111cccccccccccccc1111111111111b111bddd1dddddddddddddddddddddbdddbdddddddddddddddddbbbddddbbbbbbbccfffffffffffff
        dddddddd11111111111cccccccbcccccccccc11cccccccc1111111cccccccccccc1111111111111b111bddd1dddddddddddddddddddddbddbbdddddddddddddddddbbbdddbbbbbbbbccfffffffffffff
        dddddddd11111111111ccccccccccccccccc111ccccccc1111b1111ccccccccccc1111111111111b1dbb1ddddddddddddddbbbbddddddbddbdddddddddddddddddddbbdddbbbbbbbccffffffffffffff
        dddddddddd111111111cccccccccccccccc1bb1ccccccc1111bb111ccccccccccc11111b1111111b1dbbdddddddddddddddbddbbbddddbdbddddddddddddddddddddbbddbbbbbbbbcbffffffffffffff
        dddddddddd1111111111cccccccccccccccccccccccccc111111111cccccccccccbb11111111111b1db1dddddddddddddddbdddbbddddbbdddddddddddddddddddddbbdbbbbbbbbccfffffffffffffff
        dddddddddd11111111111cccccccccccccbccbbccccccc1111111b1cccccccccccbbbb111111111b1db1ddd1ddddddddddbbdddbbbddbbdddddddddddbbddddddddbbbbbbbbbbbcbbcffffffffffffff
        ddddddddd1d11111111111ccccccccccccbbcbbccccccc1111111b1cccccccccccc1b1111111111bbbddddd1dddddddddbbdddddbbdbbddddddddddddbdddddddddbbbbbbbbbbccbcfffffffffffffff
        ddddddddd1d11b11111111ccccccccccccbccbcccccccc111111bb1cccccccccccc111111111111bbbdddddddddddddddbbdddddbbbbbddddddddddddbdddddddddbbbbbbbbbbbbcffffffffffffffff
        ddddddddd1d11b11111111cccccccccccccccccccccccc1111111bbcccccccccccc11111111111bbbdddddddddddddddddddddddbbbbddddddddddddbbdddddbddbbbbbbbbbbbccfffffffffffffffff
        dddddddddddddbbd1bb111cccccccccccc111d1cccccccd1d1111bbcccccccccccc11111111111bbb1ddddddddddddddddddddddbbbbddddddddddddbbdddddbddbbbbbbbbbbbbccffffffffffffffff
        dddddddddddddbbd1b1111ccccccccccccddbccccccccccc1ddddbccccccccccccc11111111bb1bb11dddbddddddddddddddddddbbbbddddddddddddbbdddddbdbbbbbbbbbbbbcffffffffffffffffff
        ddddddddddddddbd1b11bbccccccccccccccccccccccccccbcccccccccccccccccb1d111111bbbbbdddddbbdddddddddddddddddbbbbddddddddddddbbdddddbdbbbbbbbbbbbbcffffffffffffffffff
        ddddddddddddddbb1b11bbccccccccccccccccccccccccccccccccccccccccccccd1111b1111bbb11ddddbbdddddddddddddddddbbbbddddddddddddbbdddddbbbbbbbbbbbbbbcffffffffffffffffff
        dddddddddddddddb1b1db1ccccccccccccccccccccccccccccccccccccccccccccc1111d1111bbb11dddddbbddddddddddddddddbbbbbddddddddddddbdddddbbbbbbbbbbbbbbbcfffffffffffffffff
        ddddddddddddddddbb1bbdccccccccccccccccccccccccccccccccccccccccccccb1111d1111bbbddddddddbddddddddddddddddbbbbbddddddddddddbbdddbbbbbbbbbbbbbbbcffffffffffffffffff
        ddddddddddddddddbb1bbdccccccccccccccccccccccccccccccccccccccccccccb1b11d1111bbbddddddddbbdbbddddddddddddbbbbbddddddddddddbbddbbbbbbbbbbbbbbbcfcffffffffffffffcff
        ddddddddddddddddbb1b11cccccccccccccccccccccccccccccccccccccccccccccbbb111111bbbddddddddbbdbdddddddbbddddbbbbbdddddddddddbbbbbbbbbbbbbbbbbbbccfffffffffffffffffff
        ddddddddddddddddbddbd1ccccccccccccccccccccccccccccccccccccccccccccbbb111d111bbbb1dddddddbbbdddddddbbddddbbbbbddddddddbdbbbbbbbbbbbbbbbbbbbbcfcffffffffffffffffff
        ddddddddddddddddbbb111cccccccccccccccccccccccccccccccccccccccccccc1bb1111111bbbbddddddddbbbdddddddbdddddbbbbbddddbdddbdbbbbbbbbbbbbbbbbbbbbffffffffffffffffffcff
        ddddddddddddddddbbd111ccccccccccccccccccccccccccccccccccccccccccccd1bbb11111bbbbdddddddddbbddddddbbdddddbbbbbdddbbdddbbbbbbbbdbbbbbbbbbbbbcfffffffffffffffffffff
        ddddddddddddddddbbdd1dcccccccccccccccccccccccccccccccccccccccccccc111bb11111bbbbdddd1ddddbbddddddbbdddddbbbbbdddbbddddddbdddddddddbbbbbbbbcfffffffcfffffffffffff
        dddddddbbdddddbbbbddddcccccccccccccccccccccccccccccccccccccccccccc111bb1111bbbbbdddddddddbbbdddddbbdddddbbbbbddddbdbdddddddddddddddddddddddfffffffffffffffffffff
        dbddddddddbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccbcccccb11bb1111bbbbbdddddddddbbbdddddbbdddddbbbbbbdddddddddddddddbddddddddddbbcfffffffffffffffffffff
        ddbddbddbbbbbbbbbbbbbbcccccccccccccccccccccccccccccbccccccccccccccd11b11111bbbbbbddddddddbbbdddddbbddddbbbbbbdddddddddddddddddddddddddddbcffffffffffffffffffffff
        dbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccc111bb111bbbbbbbbdddddddbbbbddddbbdddbbbbbbddddddddddddddddddddddddddbbbcdfffffffffffffffffffff
        bbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccbb1bb1bbbbbbbbbbbbdddddbbbbddddbbddbbbbddbbdddddddddddddddddddbddddbccfddfffffffffffffffffffff
        dbbbbbbbbbbbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbdddddddddddddbdddddddddddddbcffffffffffffffffffffffffff
        bbbbbbbbbbbbbbbbbbbbbbccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbbbbbdbbbdbddddbdddddddddddddddddddddddddddccffffffffffffffffffffffffff
        bbbbbbbbddbbbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbbbddddddddddbddddddddddddddddddddddbdddddbbbffbdfffffffffffffffffffffff
        bbbbbbbdddddbbbbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbbbbbbbbbbbddddbddddddddbdddddddddddddddddddddddddddbddfcbfdffffffffffffffffffffff
        bbbbddddddddddddddbbbbcccccccccccccccccccccccccccccccccccccccccccccccbbbbbbbbbbbbdddddddddddddddddddddddddddddddddddddddddddddddddbdffdffbcfffffffffffffffffffff
        bbbddddddddddddbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccccccbbbdbbdbdddddddbddddbddddddddddddddddddddddddddddddddddddddcffcdfffffffffffffffffcfffffff
        bbdddddddddddddbbbbbbbcccccccccccccccccccccccccccccccccccccccccccccbcccbbbbbddbdddddddddddddddddddddddddddddddddddddddddddddddddbcdffdfcdfffffffffffffffffffffff
        bddddddddddddddbdbbbbccccccccccccccccccccccccccccccccccccccccccbcbbbcbddddddddddddbddddddddddddddddddddddddddddddddddbddddddddddbfcffffcffffffffffffffffffffffff
        ddddddddddddddddbdbbbcccccccccccccccccccccccccccccccccccccccccbbcddddcdbddddbbddddbbdddddddddddbdddddddddddddddddddbddddddddddddcbdffffffffffbfffffcffffffffcbff
        dbdbddddddddbdbdbbbbccccccccccccccccccccccccccccccccccbcccbcbbdbcddddddddddddddddddddddddbddddddddddddddddddddddddddddddddddddddcffffffffffffffffffffffffcfffddf
        ddddddbddddddddbbbbbcccccccccccccccccccccccccccccccbbcbccbbbbdbdddddddddddbbbddddddddddddddddddddddddddddddddddddddddddddddddddbffffffffffffffffffffffffcdfffcff
        ddddddddddddbdbbbbbbccccccccccccccccccccccccccccccbbbbbbdddddddbddddddddddddbddddddddddddddddddddddddddddddddddddddddddddddddddcfffffffffffffffffffffffffffdffff
        dddddddddddddbbbbbbcccccccccccccccccccccccccccccbbbcddddbdbcdddcddddddddddddddddbdddbddddddddddbdddddddddddddddddddddddddddddddccfffffffffffffffffffffffffffffff
        ddddddddddddbbbbbbbcccccccccccccccccccccccccccbbddddddddbdbddddbdddddddddddddddddddddddddbbbddddddddddddddddddddddddddddddddddcfcffffffffffffffffcffffffffffffff
        bdbddddddbddbbbbbbccccccccccccccccccccccccccbddddbbdddddddddddddddddddbddddddddddddddddddddddddddddbdbdddddddddddddddddddddddbffffffffcffffffffffffffffcfcffffff
        dbddbdddddddbbbbcccccccccccccccccccccccccccdbdbdddddddddddddddddddddddbddddddddbdcbddddddddddddddddddddddddddddddddddddddddddcfffffffffffffffffffffffffffcffffff
        dddddddddddddddddbcbcccccccccccccccccccccbddcbbcdddbddddddddddddcdbddddddddddddddddddddbdddddddddddddddddddddddddddddddddddddfffbffffffffffffffffffffffffffcffff
        ddddddddddddcddddddbbccccccccccccccccbcbcbddddddbdbcddddddddddddddddddddddddddcbddddddddddddbdddddddddddddddddddddddddddddddcfffdfffffffffffffffffffffffffffffff
        dddddddddddbcdddddbddcbbcccccccbcccbbbbbccddbddddbdbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbbddddddddddddddbffffcfffffffffffffffffffffffffffffff
        bdddddddddcdddddddddbcbbbcbbbcbbbdddbddddbddddddddddddddddbddddddddddddddddbcdddcddddddddddddddddddddddddddccddddddddddddddbddfffffffffffcffffffffffffffffcccfff
        ddddddddddddbddddbdddbbdbcbddbdbddddddddddbdddddddbdddddcddddddddddddbddddddddddddddddbddddddddbdddddddddddddddddddddddddddcdfffffffffffffffffffffffffffffccfffc
        dddcdddddddddddddddddcdddddddbdbbbdddbddddddddddddccdddddbddddddddcddddddddcddddddddddddddddddddddddddddddddddddddddcddddddcffffffffffffffffffffffffffffffffffff
        dddbdddddddddddddddddcdddddddcbddddbbddddddcdbddbdddddddddddbcbbbdcbddddddcbddddddddddddddddddddddddddddbddddddddddddddddddcfffffffffffffffcffffffffffffffffffff
        bdddddddddddddddddddddddddddbddbdbcbdbbddddbdddddddddddddbbbbbbcbbbbcdbbddddbddbcddddddddddddddddbdddddddddddddddddddddddddcffffbdcffffffffcffffffffffcfffffffff
        dddddddddddddddddddddddddddbbdddddbcdddddddbddddcdbbdbbbbcccbbccccbcbcbbbbbbbbccbcbbbdbbbbddddddddddddddddddddddddddbbbbdddcffffcfbfffffffffffffffffffffffffffff
        dddddddddddddddddddbdddddcbbddddddbbdddddddbbddddbbbbbccccccccccccccccccccccccccccbccbcbbccbdbbdddddddddddddddddddbbbbbbddbccfddfffffffffffbbfffffffffffffffffff
        bbbdddddddbddddddddddddbddcddbdddddbbddbccbcccbbcbbbcbccccccccccccccccccccccccccbcccccccccccccbbbdddddddddddddbbbbccccbbddccfffffcffffffffffffffffffffffffffffff
        cccbddddddddddddddddddddddbdddddbbbcbcccccbcccccccccccccccccccccccccccccccccccccccccccccccccccbccccbdbdddbdbbbcccbccbbbdddbfffffdfffffffffffffffffffffffffffffff
        ccccddbdddddddddddcddddccbbbccbbcbbccccccbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccbdddddfffffffffffffffcfffffffffffffffffffff
        ccbbbbbddddddddddbcdddcccccccccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccccccccccccccccbbddddddbfffffffffffffffffffffffffffffffffffff
        ccccccbcbbbdddddbcccbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbddddddddbfffffffffffffffffffffffffffffffffffff
        cccccccbccbbbcbccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcbdddddddddbcffffffffffffffffcbfffffffffffffffffff
        cccccccccccbcbcccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbccccccccccccccccbbdddddbdddbcfffffffffffffffffffffffffffffffffffff
        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcbbcccccccccccccbbbbddddddddddbcffcffffffffffffffffffffffffffffffffff
        ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcccbbcccccbbcccccccbbbbdddddddddddbccffffffffffffffffffffffffffffffffffff
        cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccbcbddddddbbcbbbdbccccbbdddddbdddddddddcffdffdffffffffffffffffffffffffffffffff
        cccccccccccccccccccccccccccccccbbccccccccccccccccccccccccccccccccccccccccbcccbbbbbbddddddddddddddbbbbbbdddddcdddddddddddbcfffffffffffffffffffffffffffffffffffffc
        cccccccccccccccccccccccccccccbbddcbccccbccccccccccccccccccccccccccccccbdbbbbddddbdddddbddddddddddddddddddddddccdddddddddcfffffffffffffffffffffffffffffffffffffff
        cccccccccccccccccccccccccccbbbcddbbcbbbbbccbbcccccccccccccccccccccbbbddddbbdddddbdccddbdddddddddddddddddddddddddddddddbcffffffffffffffffffffcfffffffffffffffffff
        ccccccccccccccccccccccccccbddddddbbbbddbbbbdbccccccccccccccccccbcddddddddddbddcbdccbddddddddddddddddddddddddddddddddcbfdffffffffffffffffffffffffffffffffffffffff
        cccccccccccccccbccccccccbcdddddddddbddddddbbbddbbbbccccccccccccdbdddddddddddbddddddddddddddddddddddddddddddddddddddcfcfffffffffffffffffcbffffffffffffffcffffffff
        cccccccccccccccccccccfccccbddddddddddddddbcbcdddddbbbcccccbbbcdddddddbdddddddddddddddddddddddddddddddddddddddddddcdffbffffffffffffffffffbffffffffffffcbcffffffff
        ccccccccccccccccccfccffffccbdddddddddddddddbdbddddddcdbcbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfffdffcfffffbfffffffffdccfffffffffffffffffffff
        cccccccccccccccffcffcccffffccdddddddddddddcccdddddbdbddbdddddddddddddddddddddddddddddddddddddddddddddddddddddddbcffffffddfffffffffffffffddffffffffffffffffffffff
        cccccccfccffffcffffffcdfffffcfddddddddddddbccbddddbddddddddddddddddddddddddddddddddddddddddddddddddddddddddddbcfffffffffdfffffffffcffffffffffffffbffffffffffffff
        ccfcccfffffffffffffffffffffcfccddddddddddbdcdddddddddddddddddddddddddddddddddddddddddddddbccbbccbcbbbdbbbdbfffdffffffffffffffffcfffffffffffffddfffffffffffffffff
        cffcccffffffffffffffffffffffbcfcdddddddddccbdbdddddddddddddddddddddddddddddddddddddddbddfccccbfcfffffcbcfffcffcffffffffffccfffcffffffffffffffdbfffffffffffffffff
        fcfffffffffffffffffffffffffffffbcbbdddddbcbcdbbbcbdbddddddddddddddddddddddddddddddbbccffffffffffffffffcbfffffffffffdffffcfffffffffffffffffffccffffffffffffffffff
        fffffffffffffffffffffffffffffffcfffcdcfffcbcfcbccfccbddddddddddddddddddddddddddddbbbcfffffffffffffffffffcdbffffffffffffcdfdfffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffcffffffdffdfcffffccddddddddddddddddddddddddbdccfffffffffffffffffffffcffffcffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffdfffffbfbfffffbcfbffffffcccbcbcbdddddddddddddccccffffffffffffffffffffffffffffffffffffffffffcfffffffccfffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffccffffffffffffffdfdcfffffddffcffccccffbdbbbdddcfdfffffffffffffffffffffffffffffffffffffffffffffffffffffffffbfffffffffffffffffffffffff
        fffffffffffffffffffcffffffffffffffffffffffffffffffffddfcfbfffffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffcfffffdcfffddffffffffffffffffbffffcbffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffffffffcffcfffff
        ffffffffffffffffffffffdfffffffffcfffffffbffffffffffdffffffffffffffffffcfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbdffffffffffffffffffffffffffff
        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffbffffbffffdfffcddcfffffffffffffffff
        fffffffffffffffffffffffffffffffffbffffffbffffffffffffffffffffffbfcffffcfffffffffffffffcffffffffffffffffffffffffffffffffffffffffffffffffffffdddffffffffffccffffff
"""))