import os
from dotenv import load_dotenv
from typing import Literal, List

import openai
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


def convert_to_png(image_path):
    # Open the image file
    image = img.open(image_path)

    # Convert to RGBA if the image has no alpha channel
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Create the output file path
    output_path = os.path.splitext(image_path)[0] + ".png"

    # Save the image as PNG
    image.save(output_path, "PNG")

    # Close the image
    image.close()

    return output_path


def create_image_variation(
    img_path: str,
    num_of_images: int = 1,
    image_size: Literal["256x256", "512x512", "1024x1024"] = "256x256",
):
    # convert to png 
    if os.path.splitext(img_path)[-1] != '.png' | '.PNG':
        img_path = convert_to_png(img_path)
        
    response = openai.Image.create_variation(
        image=open(img_path, "rb"), n=num_of_images, size=image_size
    )
    urls = [res["url"] for res in response["data"]]
    images = [img.open(requests.get(url, stream=True).raw) for url in urls]

    return images
