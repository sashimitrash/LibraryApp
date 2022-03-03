from tkinter import Label, Frame
from PIL import Image, ImageTk

from apps.resources.variables import *


class Container:
    def __init__(self, root, title):
        self.root = root
        root.title(title)

        # container window, everything will be added to this container
        self.container = Frame(root, bg='black', width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.container.grid()

    # reason for this init image fn is because Tk will automatically destroy all variables after a fn is called
    # initialize background image again when we enter a new frame
    def init_image(self):
        # background image, DOES NOT CHANGE DYNAMICALLY, so we do not allow prof to expand the window
        self.image = self.open_image('apps/resources/library_wallpaper.png', CANVAS_WIDTH, CANVAS_HEIGHT)
        self.background_image = Label(self.container, image=self.image)
        self.background_image.grid()
        self.background_image.image = self.image

    def open_image(self, image_path, resized_width, resized_height):
        path = image_path
        image = Image.open(path)
        resized_image = image.resize((resized_width, resized_height), Image.ANTIALIAS)
        resized_image = ImageTk.PhotoImage(resized_image)
        return resized_image