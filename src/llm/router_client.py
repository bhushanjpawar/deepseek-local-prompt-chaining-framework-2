import httpx
import json
from typing import Dict, Any
from src.config.settings import ollama_config

class LLMRouter:
    def __init__(self, config):
        self.config = config
        
    async def generate(self, prompt: str) -> Dict[str, Any]:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.config.base_url}/api/generate",
                    json={
                        "model": self.config.model,
                        "prompt": prompt,
                        "stream": False,
                        "options": {
                            "num_predict": 2048,
                            "temperature": 0.7,
                            "top_p": 0.9
                        }
                    },
                    timeout=120.0
                )
                
                if response.status_code != 200:
                    print(f"Error response: {response.text}")
                    response.raise_for_status()
                    
                result = response.json()
                content = result.get('response', '')
                
                # Clean up response content
                if '<think>' in content:
                    content = content.split('</think>')[-1].strip()
                
                # Format markdown content
                content = self._format_markdown(content)
                
                return {"message": {"content": content}}
                
        except httpx.HTTPError as e:
            print(f"HTTP Error details: {str(e)}")
            print(f"Response content: {e.response.text if hasattr(e, 'response') else 'No response'}")
            raise
        except Exception as e:
            print(f"Unexpected error in generate: {str(e)}")
            raise

    def _format_markdown(self, content: str) -> str:
        """Format markdown content for better readability"""
        # Remove multiple spaces
        content = ' '.join(content.split())
        
        # Fix markdown headers spacing
        lines = content.split('\n')
        formatted_lines = []
        for line in lines:
            if line.startswith('#'):
                formatted_lines.append('\n' + line)
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)