from google import genai
from decouple import config

client = genai.Client(api_key=config("GEMINI_API_KEY"))
def get_car_ia_bio(model, brand, year):
    prompt= f"""
          Crie uma descrição de venda para o carro {brand} {model} {year}.

    Regras:
    - Máximo 250 caracteres
    - Não faça correções
    - Não adicione observações
    - Não explique nada
    - Retorne apenas a descrição 
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    
    return response.text