@namespace
class SpriteKind:
    logo = SpriteKind.create()
    Créditos = SpriteKind.create()

def on_on_score():
    music.play(music.create_song(hex("""
            0096000408020400001c00010a006400f401640000040000000000000000000000000005000004060004000800012707001c00020a006400f401640000040000000000000000000000000000000003180008000c00012710001400012414001800012518001c00012708001c000e050046006603320000040a002d0000006400140001320002010002180008000c00012010001400012214001800012418001c00012509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80018000800090001061400150001041800190001041c001d000104
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    effects.confetti.start_screen_effect(2000)
info.on_score(250, on_on_score)

def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        tiro
    """), SpacePlane, 200, 0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_score2():
    effects.confetti.start_screen_effect(2000)
info.on_score(30, on_on_score2)

def on_on_score3():
    music.play(music.create_song(hex("""
            0096000408020400001c00010a006400f401640000040000000000000000000000000005000004060004000800012707001c00020a006400f401640000040000000000000000000000000000000003180008000c00012710001400012414001800012518001c00012708001c000e050046006603320000040a002d0000006400140001320002010002180008000c00012010001400012214001800012418001c00012509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80018000800090001061400150001041800190001041c001d000104
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    effects.confetti.start_screen_effect(2000)
info.on_score(100, on_on_score3)

def on_on_score4():
    effects.confetti.start_screen_effect(2000)
info.on_score(150, on_on_score4)

def on_life_zero():
    music.stop_all_sounds()
    music.play(music.create_song(hex("""
            0078000408020400001c00010a006400f401640000040000000000000000000000000005000004060004000c00012702001c000c960064006d019001000478002c010000640032000000000a06000506000c001000012408001c000e050046006603320000040a002d0000006400140001320002010002120004000800012510001400012418001c00012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80018000400050001040c000d0001041400150001041c001d000104
        """)),
        music.PlaybackMode.IN_BACKGROUND)
    game.splash("Sua pontuação", info.score())
    game.splash("Fim de Jogo!", "Clique no A/Espaço pra ir ao menu")
    game.reset()
info.on_life_zero(on_life_zero)

def on_on_score5():
    effects.confetti.start_screen_effect(2000)
info.on_score(50, on_on_score5)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.fire, 500)
    scene.camera_shake(3, 500)
    info.change_score_by(1)
    music.play(music.create_song(hex("""
            0078000408020208001c000e050046006603320000040a002d0000006400140001320002010002070008000c0002202509010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8000800080009000305080a
        """)),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy()
    scene.camera_shake(4, 500)
    info.change_life_by(-1)
    animation.run_image_animation(SpacePlane,
        assets.animation("""
            Lili e Lilão recebendo ataque
        """),
        100,
        False)
    music.play(music.create_song(hex("""
            0078000408020204001c00100500640000041e000004000000000000000000000000000a040004060008000c00012407001c00020a006400f401640000040000000000000000000000000000000003060008000c000124
        """)),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

Metoro: Sprite = None
Alien: Sprite = None
Inimigo: Sprite = None
projectile: Sprite = None
SpacePlane: Sprite = None
scene.set_background_image(assets.image("""
    Fundo de espaço
"""))
logo2 = sprites.create(assets.image("""
        Logo - Lili e Lilão em Nave Espacial
    """),
    SpriteKind.logo)
Créditoss = sprites.create(img("""
        .................................................................................................................................................
            .................................................................................................................................................
            .................................................................................................................................................
            ...................................................................................7....11...6...................................................
            .....................................111.1.1..1..1..1...111..1..1...1..11..........7...1..1..6...................................................
            .....................................1.1.1.1.1.1.11.1...1.1.1.1.1...1.1..1.........7...1..1..6...................................................
            .....................................11..1.1.1.1.1.11...111.1.1.111.1.11111...111..7....11...6...................................................
            .....................................1.1.1.1.111.1.11...1...111.1.1.1.1..1.........7...1..11.6...................................................
            .....................................1.1..1..1.1.1..1...1...1.1.111.1..11..........777..11.1.666.................................................
            .................................................................................................................................................
    """),
    SpriteKind.Créditos)
logo2.change_scale(0.8, ScaleAnchor.BOTTOM)
logo2.set_position(80, 25)
Créditoss.set_position(87, 70)
Créditoss.change_scale(0.08, ScaleAnchor.RIGHT)
music.play(music.create_song(hex("""
        008c000408020401001c000f05001202c102c20100040500280000006400280003140006020004060010001800012405001c000f0a006400f4010a0000040000000000000000000000000000000002060008000c00012207001c00020a006400f401640000040000000000000000000000000000000003060004000800012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c80006000c000d000106
    """)),
    music.PlaybackMode.IN_BACKGROUND)
game.set_dialog_frame(img("""
    ..bbabbaabbaabbaabbbbb..
        .bddbaddbaddbaddbabbddb.
        addddbaddbaddbaddbadddda
        addddbbaabbaabbaabbdddda
        abddb11111111111111bddba
        bbab1111111111111111bbab
        babb1111111111111111badb
        abda1111111111111111adda
        adda1111111111111111adba
        bdab1111111111111111bbab
        babb1111111111111111badb
        abda1111111111111111adda
        adda1111111111111111adba
        bdab1111111111111111bbab
        babb1111111111111111badb
        abda1111111111111111adda
        adda1111111111111111adba
        bdab1111111111111111bbab
        babb1111111111111111babb
        abddb11111111111111bddba
        addddbbaabbaabbaabbdddda
        addddabddabddabddabdddda
        .addbbabddabddabddabdda.
        ..aaabbaabbaabbaabbaaa..
"""))
game.show_long_text("Clique no A/Espaço pra iniciar", DialogLayout.BOTTOM)
sprites.destroy(logo2)
sprites.destroy(Créditoss)
music.play(music.create_song(hex("""
        0078000408020500001c00010a006400f4016400000400000000000000000000000000050000040c0010001400012414001800012201001c000f05001202c102c2010004050028000000640028000314000602000406001c002000012503001c0001dc00690000045e010004000000000000000000000564000104000306001c002000012205001c000f0a006400f4010a000004000000000000000000000000000000000206001c002000012508001c000e050046006603320000040a002d0000006400140001320002010002120010001400012414001800012218001c000120
    """)),
    music.PlaybackMode.IN_BACKGROUND)
SpacePlane = sprites.create(assets.image("""
    Lili e Lilão
"""), SpriteKind.player)
SpacePlane.set_position(23, 61)
controller.move_sprite(SpacePlane, 80, 80)
SpacePlane.set_stay_in_screen(True)
info.set_life(5)

def on_update_interval():
    global Inimigo
    Inimigo = sprites.create(img("""
            ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ....................
                    ........ffffff..f...
                    ......ff222222ff2f..
                    ....ff112222222f22f.
                    ...f11112222222222f.
                    ...f2222222222222ff.
                    ....ffff22222fffff..
                    ........f22222f.....
                    .........f22222f....
                    ..........fffff.....
                    ....................
                    ....................
                    ....................
                    ....................
        """),
        SpriteKind.enemy)
    Inimigo.set_velocity(-100, 0)
    Inimigo.set_position(160, randint(5, 115))
    Inimigo.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(1000, on_update_interval)

def on_update_interval2():
    global Alien
    Alien = sprites.create(assets.image("""
        Alien
    """), SpriteKind.enemy)
    animation.run_image_animation(Alien,
        assets.animation("""
            Alien Animate
        """),
        1000,
        True)
    Alien.set_velocity(-140, 0)
    Alien.set_position(160, randint(5, 115))
    Alien.set_flag(SpriteFlag.AUTO_DESTROY, True)
    Alien.start_effect(effects.rings)
game.on_update_interval(6000, on_update_interval2)

def on_update_interval3():
    global Metoro
    Metoro = sprites.create(assets.image("""
        Meteoro
    """), SpriteKind.enemy)
    animation.run_image_animation(Metoro,
        assets.animation("""
            Meteoro Animate
        """),
        100,
        True)
    Metoro.set_velocity(-120, 0)
    Metoro.set_position(160, randint(5, 115))
    Metoro.set_flag(SpriteFlag.AUTO_DESTROY, True)
    Metoro.start_effect(effects.fire)
game.on_update_interval(3500, on_update_interval3)