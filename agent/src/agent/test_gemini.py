import os
import google.genai as genai


class AgentClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key = self.api_key)
        self.model_name = "gemini-2.0-flash"


