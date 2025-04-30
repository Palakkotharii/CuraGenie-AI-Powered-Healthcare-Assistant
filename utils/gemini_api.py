
# utils/gemini_api.py

import google.generativeai as genai

# Configure your API key
genai.configure(api_key="AIzaSyCY919J6cBAhRxsz4p_s1oX74cC5ah0k28")

# Initialize the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def gemini_ask(prompt):
    """
    Sends a prompt to the Gemini model and returns the response.

    Args:
        prompt (str): The input prompt for the model.

    Returns:
        str: The response from the model.
    """
    response = model.generate_content(prompt)
    return response.text

