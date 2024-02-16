import uuid
import google.generativeai as genai
import os 


class GeminiAI:
    def __init__(self):
        genai.configure(api_key=os.getenv("GENAI_API_KEY"))
        self.session_id = str(uuid.uuid4())
        # Set up the model
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
        ]   
        self.model = genai.GenerativeModel(
            model_name="gemini-1.0-pro", 
            generation_config=generation_config,
            safety_settings=safety_settings)

    def start_chat(self, history: list):
        self.convo=self.model.start_chat(history=history)

    def send_message(self, message: str):
         self.convo.send_message(message)
         return self.convo.history