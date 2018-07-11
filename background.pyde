def setup():
    size(1000, 1000)
    background(255,0 , 0)
    noStroke()
    img = loadImage("Game.png")
    img1 = loadImage("game.jpg")
    
    x = 0
    b = 500
    
    while x < 500:
        y = 0
        while y >= 0 and y <= 1000:
            if y % 200 == 0:
                image (img1, x, y, 100, 100)
            else:
                image(img, x, y, 100, 100)
            y = y + 100
        x = x + 100
        
    while b >= 500 and b< 1000:
        y = 0
        while y >= 0 and y <= 1000:
            if y % 200 == 0:
                image(img, b, y, 100, 100)
            else:
                image (img1, b, y, 100, 100)
            y = y + 100
        b = b + 100
    
