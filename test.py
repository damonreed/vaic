from src.vaic import text_response

# Test the text response
text_prompt = """
Develop a gritty fantasy plot outline for a graphic novel.  There is a slight steampunk aspect to the world.
The protagonist is a sly rogue who is a master of disguise.  He is a bit of a loner and has a dark past.
His love interest is a upright paladin who is a bit naive.  She is a bit of a zealot and has a strong sense of justice.
"""
print(text_response(text_prompt))
