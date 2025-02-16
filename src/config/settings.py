from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class OllamaConfig(BaseModel):
    model: str = os.getenv('DEFAULT_MODEL', 'deepseek-r1:7b')
    base_url: str = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')

ollama_config = OllamaConfig()