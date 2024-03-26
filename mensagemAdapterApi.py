from abc import ABC, abstractmethod
import pathlib
import textwrap
import os 
import dotenv
from IPython.display import display
from IPython.display import Markdown
import openai 
from load_creds import load_creds

from abc import ABC, abstractmethod
dotenv.load_dotenv()

class IAAdapter(ABC):
    @abstractmethod
    def gerar_texto(self, prompt: str) -> str:
        pass

class GeminiAdapter(IAAdapter):

    def __init__(self):
        model='gemini-pro'
        import google.generativeai as genai
        creds = load_creds()
        #na credencial simplificada, sem o cloud
        #GOOGLE_API_KEY=os.getenv("GEMINI_API_KEY")
        #genai.configure(api_key=GOOGLE_API_KEY)
        genai.configure(credentials=creds)
        self.api = genai.GenerativeModel(model)

        #for i, m in zip(range(5), genai.list_tuned_models()):
        #    print(m.name)

    def gerar_texto(self, prompt: str) -> str:
        resposta = self.api.generate_content(prompt)
        return resposta.text

class OpenAIAdaper(IAAdapter):

    def __init__(self):

        self.modelo = 'gpt-3.5-turbo' 

    def gerar_texto(self, prompt: str) -> str:

        resposta =  response = openai.chat.completions(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                stream = True,
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                model = self.modelo)
        
        return resposta.choices[0]["text"]

class IAGenerativa:
    def __init__(self):
        self.ia_adapter = GeminiAdapter()
    
    def gerar_texto_personalizado(self, prompt: str) -> str:
        # Geração de texto usando a API de IA
        texto_gerado = self.ia_adapter.gerar_texto(prompt)

        return texto_gerado



# Exemplo de uso

#IAGenerativa = IAGenerativa()
# componente_ia = IAGenerativa(api_adapter)

#prompt = "teste do gemini"
#texto_gerado = IAGenerativa.gerar_texto_personalizado(prompt)

# print(f"\nPrompt: {prompt}")
#print(f"\nTexto Gerado: {texto_gerado}")
    
