def pede_nome(nomeFicheiro) :
    verificacao = False
    while verificacao :
        if not (nomeFicheiro is None):
            print(f"{nomeFicheiro}")
            verificacao = True



def gera_nome(nomeFicheiro):
    jsonFileName = ""
    if not (nomeFicheiro is None):
        jsonFileName = nomeFicheiro.split(".")[0] + ".json"
        return jsonFileName



def ler_linhas(nomeFicheiro):
    f = open(nomeFicheiro, encoding = "utf-8")
    lista = f.readlines()
    f.close
    return lista

def ler_texto(nomeFichero):
    f = open(nomeFicheiro, encoding = "utf-8")
    texto = f.read()
    f.close
    return texto