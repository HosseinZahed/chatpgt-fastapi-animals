from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    # Get a list of image files in the 'images' folder
    image_folder = "images"
    image_files = [f for f in os.listdir(image_folder) if f.endswith(".jpg") or f.endswith(".png")]

    # Select a random image from the list
    import random
    selected_image = random.choice(image_files)

    # Get the title of the image (the file name without the extension)
    title = os.path.splitext(selected_image)[0].title()

    # Create the jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Render the template
    template = env.get_template('index.html')
    html_content = template.render(title=title, image_folder=image_folder, selected_image=selected_image)

    # Return the HTML content
    return HTMLResponse(html_content)
