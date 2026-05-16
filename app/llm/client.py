from google import genai
from google.genai import types

from pydantic import BaseModel

from app.core.config import settings


class GeminiClient:

    def __init__(self):

        self.client = genai.Client(api_key=settings.gemini_api_key)

    async def generate_text(
        self,
        prompt: str,
        model: str = "gemini-2.5-flash",
    ) -> str:

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
        )

        return response.text

    async def generate_structured(
        self,
        prompt: str,
        schema: type[BaseModel],
        model: str = "gemini-2.5-flash",
    ):

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=schema,
            ),
        )

        return schema.model_validate_json(response.text)
