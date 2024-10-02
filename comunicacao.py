from dotenv import load_dotenv
from openai import OpenAI
import os
import pdfplumber

def pdf_to_text(pdf_path):
  text = ''
  with pdfplumber.open(pdf_path) as pdf:
      for page in pdf.pages:
          text += page.extract_text()
  return text


def comunica(titulo, comando, contexto):

  os.mkdir(f"output/{titulo}")

  dados = []
  for arquivo in os.listdir("input"):
    if arquivo.split(".")[-1] == "pdf":
      dados.append("--- Início do Arquivo ---")
      dados.append(pdf_to_text(f"input/{arquivo}"))
      dados.append("--- Fim do Arquivo ---")

  dados = "\n".join(dados)
  content = [
    {
      "type": "text",
      "text": comando
    }
  ]


  client = OpenAI()
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {
        "role" : "system",
        "content" : contexto
      },
      {
        "role": "user",
        "content": content
      },
      {
         "role" : "user",
         "content" : [
            {
               "type" : "text",
               "text" : dados
            }
         ]
      }
    ],
  )

  for arquivo in os.listdir("input"):
    os.rename(f"input/{arquivo}", f"output/{titulo}/{arquivo}")

  with open(f"output/{titulo}/resposta_chat.txt", "w+") as resposta:
    resposta.write(str(response.choices[0].message.content))