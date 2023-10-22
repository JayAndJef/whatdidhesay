from PIL import Image, ImageDraw

with Image.open("goofyparrot.jpeg").convert("RGBA") as base:
    img_width, img_height = base.size
    canvas = ImageDraw.Draw(base)

    canvas.ellipse(
        [(0, -(img_height / 5)), (img_width, img_height / 5)], fill=(255, 255, 255, 0)
    )
    canvas.polygon([(img_width, 0), (4/5 * img_width, 0), (img_width/2, 2/5 *img_height)], fill=(255, 255, 255, 0))

    base.show()
