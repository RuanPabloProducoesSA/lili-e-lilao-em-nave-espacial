namespace SpriteKind {
    export const logo = SpriteKind.create()
    export const Créditos = SpriteKind.create()
    export const Ready = SpriteKind.create()
    export const Bubble = SpriteKind.create()
    export const logointro = SpriteKind.create()
}
info.onScore(250, function () {
    music.play(music.createSong(assets.song`Parabéns`), music.PlaybackMode.InBackground)
    info.changeLifeBy(2)
    effects.confetti.startScreenEffect(2000)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    projectile = sprites.createProjectileFromSprite(assets.image`tiro`, SpacePlane, 200, 0)
    animation.runImageAnimation(
    projectile,
    assets.animation`tiro animation`,
    500,
    true
    )
    projectile.startEffect(effects.fire)
})
info.onScore(30, function () {
    effects.confetti.startScreenEffect(2000)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, otherSprite2) {
    otherSprite2.destroy()
    scene.cameraShake(4, 500)
    info.changeLifeBy(-1)
    animation.runImageAnimation(
    SpacePlane,
    assets.animation`lili e lilão recebendo dano`,
    100,
    false
    )
    music.play(music.createSong(assets.song`dano`), music.PlaybackMode.UntilDone)
})
info.onScore(100, function () {
    music.play(music.createSong(assets.song`Parabéns`), music.PlaybackMode.InBackground)
    effects.confetti.startScreenEffect(2000)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite2, otherSprite2) {
    otherSprite2.destroy()
    info.changeLifeBy(1)
    animation.runImageAnimation(
    SpacePlane,
    assets.animation`Lili e Lilão recebendo mais uma vida`,
    100,
    false
    )
    music.play(music.createSong(assets.song`vida sound`), music.PlaybackMode.UntilDone)
})
info.onScore(150, function () {
    effects.confetti.startScreenEffect(2000)
    info.changeLifeBy(2)
    music.play(music.createSong(assets.song`Upgrade`), music.PlaybackMode.InBackground)
})
info.onLifeZero(function () {
    music.stopAllSounds()
    music.play(music.createSong(assets.song`Game over music`), music.PlaybackMode.InBackground)
    game.splash("Sua pontuação", info.score())
    game.splash("Fim de Jogo!", "Clique no A/Espaço pra ir ao menu")
    game.reset()
})
info.onScore(50, function () {
    effects.confetti.startScreenEffect(2000)
    info.changeLifeBy(1)
    music.play(music.createSong(assets.song`Upgrade`), music.PlaybackMode.InBackground)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.fire, 500)
    scene.cameraShake(3, 500)
    info.changeScoreBy(1)
    music.play(music.createSong(assets.song`Ataque`), music.PlaybackMode.UntilDone)
})
let Metoro: Sprite = null
let Alien: Sprite = null
let Inimigo: Sprite = null
let life: Sprite = null
let projectile: Sprite = null
let SpacePlane: Sprite = null
let intro = sprites.create(assets.image`logo ntro`, SpriteKind.logointro)
intro.changeScale(0.8, ScaleAnchor.Middle)
music.play(music.createSong(assets.song`intro music`), music.PlaybackMode.UntilDone)
sprites.destroy(intro)
scene.setBackgroundImage(assets.image`Fundo de espaço`)
let logo2 = sprites.create(assets.image`Logo - Lili e Lilão em Nave Espacial`, SpriteKind.logo)
let Créditoss = sprites.create(img`
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
    `, SpriteKind.Créditos)
logo2.changeScale(0.8, ScaleAnchor.Bottom)
logo2.setPosition(80, 25)
Créditoss.setPosition(87, 70)
Créditoss.changeScale(0.08, ScaleAnchor.Right)
music.play(music.createSong(assets.song`Menu`), music.PlaybackMode.InBackground)
game.setDialogFrame(img`
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
    `)
game.showLongText("Clique no A/Espaço pra iniciar", DialogLayout.Bottom)
sprites.destroy(logo2)
sprites.destroy(Créditoss)
music.play(music.createSong(assets.song`Comecou`), music.PlaybackMode.InBackground)
effects.starField.startScreenEffect()
SpacePlane = sprites.create(assets.image`Lili e Lilão`, SpriteKind.Player)
SpacePlane.setPosition(23, 61)
controller.moveSprite(SpacePlane, 80, 80)
SpacePlane.setStayInScreen(true)
info.setLife(5)
game.onUpdateInterval(7500, function () {
    life = sprites.create(assets.image`vida`, SpriteKind.Food)
    animation.runImageAnimation(
    life,
    assets.animation`vida animation`,
    500,
    true
    )
    life.setVelocity(-140, 0)
    life.setPosition(160, randint(5, 115))
    life.setFlag(SpriteFlag.AutoDestroy, true)
    life.startEffect(effects.confetti)
})
game.onUpdateInterval(1000, function () {
    Inimigo = sprites.create(img`
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
        `, SpriteKind.Enemy)
    Inimigo.setVelocity(-100, 0)
    Inimigo.setPosition(160, randint(5, 115))
    Inimigo.setFlag(SpriteFlag.AutoDestroy, true)
})
game.onUpdateInterval(6000, function () {
    Alien = sprites.create(assets.image`Alien`, SpriteKind.Enemy)
    animation.runImageAnimation(
    Alien,
    assets.animation`Alien Animate`,
    1000,
    true
    )
    Alien.setVelocity(-140, 0)
    Alien.setPosition(160, randint(5, 115))
    Alien.setFlag(SpriteFlag.AutoDestroy, true)
    Alien.startEffect(effects.rings)
})
game.onUpdateInterval(3500, function () {
    Metoro = sprites.create(assets.image`Meteoro`, SpriteKind.Enemy)
    animation.runImageAnimation(
    Metoro,
    assets.animation`Meteoro Animate`,
    100,
    true
    )
    Metoro.setVelocity(-120, 0)
    Metoro.setPosition(160, randint(5, 115))
    Metoro.setFlag(SpriteFlag.AutoDestroy, true)
    Metoro.startEffect(effects.fire)
})
