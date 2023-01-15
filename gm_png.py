from PIL import Image, ImageDraw, ImageFont
import random

def create_image(filename, fontType, fontSize):
    # create a new 16:9 transparent image
    width, height = (640, 360)
    img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

    # create a draw object
    draw = ImageDraw.Draw(img)

    # select a font
    font = ImageFont.truetype(fontType, fontSize)

    # draw the text
    draw.text((300, 100), "GM", fill=(0,0,0, 255), font=font)

    # save the image
    img.save(filename)

theFonts = ["RubikVinyl.ttf", "BlackOpsOne.ttf", "FrederickatheGreat.ttf", "LuckiestGuy.ttf", "Monoton.ttf", "RubikSprayPaint.ttf", "RubikVinyl.ttf", "Rye.ttf", "Tangerine.ttf", "TitanOne.ttf", "YesevaOne.ttf"]
fontSize = 100
filename = "Examples\\gm3.png"

create_image(filename, ("Fonts\\" + random.choice(theFonts)), fontSize)
