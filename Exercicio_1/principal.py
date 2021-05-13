import analisa_ficheiro
import json

pessoa_dict = {
    "nome": "Pedro",
    "linguas": ["Portugues", "Espanhol"],
    "casado": True,
    "esposa": "Ines",
    "idade": 32,
    "filhos": {
        "Afonso":12,
        "Beatriz":10,
        "Joao":7,
        "Diniz":4
    }
}

with open('pessoa.json', 'w') as json_file:
    json.dump(pessoa_dict, json_file, indent = 4)


def main():
    analisa_ficheiro.pede_nome("pessoa.json")
    analisa_ficheiro.gera_nome("pessoa.json")
    analisa_ficheiro.calcula_linhas("pessoa.json")
    analisa_ficheiro.calcula_carateres("pessoa.json")
    analisa_ficheiro.calcula_palavra_comprida("pessoa.json")
    analisa.ficheiro.calcula_ocorrencia_de_letras("pessoa.json")

if __name__  == "__main__":
    main()

