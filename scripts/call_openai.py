import os
import sys

# Make sure TD has the right path for our modules
#myPath = "c://users//dunca//appdata//local//packages//pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0//localcache//local-packages//python310//site-packages"
#myPath = "C:/Users/dunca/AppData/Local/Programs/Python/Python39"
#sys.path.append(myPath)

import openai
import requests
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY_TD")

# Generate a variant and save it
response = openai.Image.create_variation(
  image=open('scripts/original.png', "rb"),
  n=1,
  size="512x512"
)

image_url = response['data'][0]['url']
image = requests.get(image_url)
with open("scripts/variant.png", "wb+") as f:
    f.write(image.content)

print('Done')