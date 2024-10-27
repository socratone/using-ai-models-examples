from transformers import pipeline
import os

def image_to_text(url):
    local_model_path = os.path.expanduser("/app/model")

    img_to_text = pipeline("image-to-text", model=local_model_path, device_map="cpu")

    text = img_to_text(url)

    print(text)
    return text

image_to_text("dog.jpg")
 