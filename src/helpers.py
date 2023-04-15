"""
### This module contains helper functions for the project.
"""

import string
import os

from PIL import Image


def to_kebab_case(s: str) -> str:
    """
    Convert a string to kebab case, removing all punctuation.
    """
    # Remove all punctuation from the string
    s = s.translate(str.maketrans("", "", string.punctuation))

    # Split the string into words, convert to lowercase, and join with hyphens
    words = s.split()
    return "-".join(word.lower() for word in words)


def check_for_output_dir() -> None:
    """
    Check if the outputs directory exists, and if not, create it.
    """
    if not os.path.exists("outputs"):
        os.mkdir("outputs")


def create_image_grid(prompt: str, images: list[str]) -> None:
    """
    Create a 2x2 grid of images and save it as a png file.

    Args:
        prompt (str): _description_
        images (list[str]): _description_
    """

    collage = Image.new("RGBA", (1024 * 2, 1024 * 2))

    for i in range(0, len(images)):
        img = Image.open(images[i])
        img = img.resize((1024, 1024))
        collage.paste(img, (1024 * (i % 2), 1024 * (i // 2)))

    collage.save("outputs/" + prompt + ".png")
    collage.show()
