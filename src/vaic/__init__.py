from vertexai.preview.vision_models import ImageGenerationModel
from vertexai.preview.generative_models import (
    GenerativeModel,
    HarmCategory,
    HarmBlockThreshold,
)

# Initialize models
gen_model = GenerativeModel("gemini-pro")
image_model = ImageGenerationModel.from_pretrained("imagegeneration")

# Specify default safety and generation parameters
safety_settings = {
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
}
parameters = {"temperature": 0.9, "max_output_tokens": 1024, "top_p": 0.95, "top_k": 5}


def text_response(text_prompt):
    context = gen_model.generate_content(
        text_prompt, generation_config=parameters, safety_settings=safety_settings
    )
    return context.text


def image_response(image_prompt):
    image = image_model.generate_images(
        prompt=image_prompt,
        seed=0,
        number_of_images=1,
    )
    return image[0]._image_bytes
