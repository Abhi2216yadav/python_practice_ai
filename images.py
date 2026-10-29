import sys

from PIL import Image as PILImage

images = [PILImage.open(arg) for arg in sys.argv[1:]]

images[0].save(
    "images1.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0,
)