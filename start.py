from dotenv import load_dotenv
from slugify import slugify
from colorama import init
from termcolor import cprint, colored
from comunicacao import comunica
import os

if __name__ == "__main__":
    arquivos = os.listdir()
    init()

    if "input" not in arquivos:
        cprint("Criando pasta de input", "blue", attrs=["bold"])
        os.mkdir("input")

    if "output" not in arquivos:
        cprint("Criando pasta de output", "blue", attrs=["bold"])
        os.mkdir("output")
    
    
    if ".env" not in arquivos:
        raise Exception(colored("Arquivo de OPEN_AI_KEY não existe!!", "red", attrs=["bold"]))

    load_dotenv()

    while True:
        ok_file = input("Configurou os arquivos (y/n) ?: ")
        print()
        if ok_file.lower() in ["y", "n"]:
            if ok_file == "y":
                while True:
                    titulo = input("Digite um título para essa requisição: ")
                    if titulo == "":
                        cprint("Titulo não pode ser vazio!", "red", attrs=["bold"])
                        continue
                    else:
                        titulo = slugify(titulo)
                        if titulo in os.listdir("output"):
                            cprint("Essa saída já existe!", "red", attrs=["bold"])
                            continue

                    print(colored("Contexto é como o chat deve se comporta para responder sua pergunta, como ao pedir uma questão de matemática setar um contexto como um professor de tal matéria e enfim", "white", attrs=["bold"]))
                    while True:
                        contexto = input("Deseja adicionar um contexto (y/n):")
                        if contexto == "":
                            cprint("Responda a pergunta", "red", attrs=["bold"])
                        elif contexto == "y":
                            contexto = input("Digite o contexto: ")
                            break
                        elif contexto == "n":
                            contexto = ""
                            break
                        else:
                            cprint("Resposta inválida", "red") 
                    comando = input("Digite a mensagem que será enviada junto aos arquivos para o ChatGPT: ")
                    if comando == "":
                        cprint("Comando inválido! Tente novamente", "red", attrs=["bold"])
                    else:
                        cprint("Mensagem será enviada! Aguarde a confirmação de resposta", "green", attrs=["bold",])
                        comunica(titulo, comando, contexto)
                        break
                cprint("Processo finalizado!", "blue", attrs=["bold", ])
                break
            else:
                cprint("Coloque os arquivos no local adequado dentro da pasta de input de confirme!", "red", attrs=["bold"])
        cprint("Resposta inválida! Tente novamente", "red", attrs=["bold"])

