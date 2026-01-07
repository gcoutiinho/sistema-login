import json

def salvar_usuarios (usuarios):
    with open("usuarios.json", "w", encoding="utf-8") as lista_usuarios:
        json.dump(usuarios, lista_usuarios, ensure_ascii=False, indent=4)

def carregar_usuarios():
    try:
        with open("usuarios.json", "r", encoding="utf-8") as lista_usuarios:
            return json.load(lista_usuarios)
    except FileNotFoundError:
        return {}