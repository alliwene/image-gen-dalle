import os
from dotenv import load_dotenv
from typing import Literal, List

import openai
from openai import InvalidRequestError
import requests
from PIL.Image import Image
from PIL import Image as img

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def get_images(
    prompt: str,
    num_of_images: int = 1,
    image_size: Literal["256x256", "512x512", "1024x1024"] = "256x256",
) -> List[Image]:
    response = openai.Image.create(prompt=prompt, n=num_of_images, size=image_size)
    urls = [res["url"] for res in response["data"]]
    images = [img.open(requests.get(url, stream=True).raw) for url in urls]

    return images


def create_image_variation(
    img_path: str,
    num_of_images: int = 1,
    image_size: Literal["256x256", "512x512", "1024x1024"] = "256x256",
):
    img_mode = img.open(img_path).mode
    if img_mode not in ["RGB", "RGBA"]:
        raise InvalidRequestError(
            f"Invalid input image - format must be RGB or RGBA not {img_mode}"
        )

    response = openai.Image.create_variation(
        image=open(img_path, "rb"), n=num_of_images, size=image_size
    )
    urls = [res["url"] for res in response["data"]]
    images = [img.open(requests.get(url, stream=True).raw) for url in urls]

    return images
