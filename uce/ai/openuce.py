import openai
from pydantic import BaseModel

openai.organization = 'org-iWJNxFXvNTTeP5rwz0VYDvEy'
openai.api_key = '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'


class Document(BaseModel):
    item: str = 'Pizza'


def process_inference(user_prompt) -> str:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un chef que lista los ingredientes de los platillos que se te proporcionan.
        E.G
        Pan
        Ingredientes:
        Harina
        Huevos
        Agua
        Azucar
        ...
        """},
            {"role": "user", "content": user_prompt}
        ]
    )
    response = completion.choices[0].message.content
    return response
