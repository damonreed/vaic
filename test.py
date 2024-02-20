from src.vaic import text_response, image_response
from PIL import Image
import io


# Test the text response
text_prompt = """
Develop a gritty fantasy plot outline for a graphic novel.  There is a slight steampunk aspect to the world.
The protagonist is a sly rogue who is a master of disguise.  He is a bit of a loner and has a dark past.
His love interest is a upright paladin who is a bit naive.  She is a bit of a zealot and has a strong sense of justice.
One antagonist is a former lover of the protagonist who is a rival rogue.  She is a bit of a femme fatale and has a very dark past.
The protagonist has pledged his loyalty to a powerful firemage who runs a cirle of adventurers.  
The mage is supported by a priest of the light who struggles with her own inner darkness.
"""
print(text_response(text_prompt))

image_bytes = image_response(f"Draw a graphic novel cover for {text_prompt}")
image = Image.open(io.BytesIO(image_bytes))
image.show()
